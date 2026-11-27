#!/usr/bin/env python3
"""
Trading Lab scorecard, in SAR, against the mission:
turn SAR 1,000 into SAR 1,100 without breaking the 5% drawdown limit.

  scorecard.py backtest [results.zip]   latest (or given) backtest result
  scorecard.py paper                    the running / stopped paper bots

A strategy PASSES the Phase 1 gate only if ALL of these hold:
  * ends at or above SAR 1,100 (net +100)
  * never crossed the 5% drawdown line
  * beats the buy-and-hold benchmark
  * at least 30 closed trades (backtest) so the result is not a handful of lucky trades
  * p-value < 0.05 on average trade profit (backtest), i.e. not plausibly zero edge

Writes a Markdown copy to user_data/reports/. Standard library only.
"""
from __future__ import annotations

import base64
import json
import sqlite3
import sys
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UD = ROOT / "user_data"
SAR_PER_USDT = 3.75  # SAR is pegged to USD; USDT treated as USD
START_SAR = 1000.0
TARGET_SAR = 1100.0
MAX_DD = 0.05
MIN_TRADES = 30
BENCHMARK = "BuyAndHoldBenchmark"


def sar(usdt: float) -> float:
    return usdt * SAR_PER_USDT


def latest_zip() -> Path:
    zips = sorted((UD / "backtest_results").glob("*.zip"), key=lambda p: p.stat().st_mtime)
    if not zips:
        sys.exit("No backtest results found. Run `make backtest` first.")
    return zips[-1]


def breaches(strategy: str) -> list[dict]:
    f = UD / "backtest_results" / f"risk_breaches_{strategy}.json"
    return json.loads(f.read_text())["breaches"] if f.exists() else []


def backtest_rows(path: Path) -> tuple[list[dict], str]:
    with zipfile.ZipFile(path) as z:
        name = next(n for n in z.namelist()
                    if n.endswith(".json") and not n.endswith("_config.json"))
        data = json.loads(z.read(name))["strategy"]
    rows = []
    for strat, r in data.items():
        b = breaches(strat)
        rows.append({
            "strategy": strat,
            "trades": r["total_trades"],
            "final_sar": sar(r["final_balance"]),
            "max_dd": r["max_drawdown_account"],
            "profit_factor": r.get("profit_factor"),
            "p_value": r.get("p_value"),
            "breaches": len(b),
            "first_breach": b[0]["at"][:10] if b else "",
            "is_benchmark": strat == BENCHMARK,
        })
    any_r = next(iter(data.values()))
    period = f"{any_r['backtest_start'][:10]} to {any_r['backtest_end'][:10]}"
    return rows, period


def api_balance(local_cfg: Path) -> float | None:
    try:
        api = json.loads(local_cfg.read_text())["api_server"]
        req = urllib.request.Request(f"http://127.0.0.1:{api['listen_port']}/api/v1/balance")
        token = base64.b64encode(f"{api['username']}:{api['password']}".encode()).decode()
        req.add_header("Authorization", f"Basic {token}")
        with urllib.request.urlopen(req, timeout=3) as resp:
            return float(json.loads(resp.read())["total"])
    except Exception:  # noqa: BLE001 - bot not running
        return None


def paper_rows() -> tuple[list[dict], str]:
    base = json.loads((UD / "config" / "base.json").read_text())
    start = float(base["dry_run_wallet"])
    rows = []
    for bot_cfg in sorted((UD / "config" / "bots").glob("*.json")):
        bot = bot_cfg.stem
        strategy = json.loads(bot_cfg.read_text())["strategy"]
        db = UD / "db" / f"{bot}.sqlite"
        closed = n_closed = n_open = 0
        if db.exists():
            con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
            closed, n_closed = con.execute(
                "select coalesce(sum(close_profit_abs),0), count(*) from trades where is_open=0"
            ).fetchone()
            n_open = con.execute("select count(*) from trades where is_open=1").fetchone()[0]
            con.close()
        live_total = api_balance(UD / "config" / "local" / f"{bot}.json")
        equity = live_total if live_total is not None else start + closed
        state = json.loads((UD / "risk_state" / f"{bot}.state.json").read_text()) \
            if (UD / "risk_state" / f"{bot}.state.json").exists() else {}
        peak = max(state.get("peak_equity", start), equity)
        halted = (UD / "risk_state" / f"{bot}.halted.json").exists()
        rows.append({
            "strategy": strategy, "trades": n_closed, "open": n_open,
            "final_sar": sar(equity), "max_dd": 1 - equity / peak if peak else 0,
            "profit_factor": None, "p_value": None,
            "breaches": int(halted), "first_breach": "HALTED" if halted else "",
            "is_benchmark": strategy == BENCHMARK,
            "marked": "live" if live_total is not None else "closed trades only",
        })
    return rows, "paper trading so far"


def verdicts(rows: list[dict], mode: str) -> None:
    bench = next((r for r in rows if r["is_benchmark"]), None)
    for r in rows:
        if r["is_benchmark"]:
            r["verdict"] = "benchmark"
            continue
        why = []
        if r["final_sar"] < TARGET_SAR:
            why.append("below 1,100")
        if r["breaches"]:
            why.append("hit 5% line")
        if bench and r["final_sar"] <= bench["final_sar"]:
            why.append("does not beat benchmark")
        if mode == "backtest":
            if r["trades"] < MIN_TRADES:
                why.append(f"<{MIN_TRADES} trades")
            if r["p_value"] is None or r["p_value"] >= 0.05:
                why.append("not significant")
        r["verdict"] = "PASS" if not why else "FAIL: " + ", ".join(why)


def render(rows: list[dict], period: str, mode: str, source: str) -> str:
    rows = sorted(rows, key=lambda r: (r["is_benchmark"], -r["final_sar"]))
    out = [f"# Trading Lab scorecard ({mode})", "",
           f"Period: {period}. Source: {source}. Start SAR {START_SAR:,.0f} per strategy, "
           f"target SAR {TARGET_SAR:,.0f}, max drawdown {MAX_DD:.0%}.", "",
           "| Strategy | Trades | End SAR | Net SAR | Max DD | 5% line | PF | p | Verdict |",
           "|---|---:|---:|---:|---:|---|---:|---:|---|"]
    for r in rows:
        line = "first " + r["first_breach"] if r["breaches"] and r["first_breach"] != "HALTED" \
            else ("HALTED" if r["first_breach"] == "HALTED" else "never")
        pf = f"{r['profit_factor']:.2f}" if r["profit_factor"] is not None else "-"
        pv = f"{r['p_value']:.3f}" if r["p_value"] is not None else "-"
        out.append(f"| {r['strategy']} | {r['trades']} | {r['final_sar']:,.0f} | "
                   f"{r['final_sar'] - START_SAR:+,.0f} | {r['max_dd']:.1%} | {line} | "
                   f"{pf} | {pv} | {r['verdict']} |")
    passed = [r["strategy"] for r in rows if r["verdict"] == "PASS"]
    out += ["", f"**Passing the gate: {', '.join(passed) if passed else 'none'}.**"]
    return "\n".join(out) + "\n"


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "backtest"
    if mode == "backtest":
        path = Path(sys.argv[2]) if len(sys.argv) > 2 else latest_zip()
        rows, period = backtest_rows(path)
        source = path.name
    elif mode == "paper":
        rows, period = paper_rows()
        source = "bot databases / local dashboards"
    else:
        sys.exit(__doc__)
    verdicts(rows, mode)
    text = render(rows, period, mode, source)
    print(text)
    reports = UD / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    (reports / f"scorecard_{mode}_{stamp}.md").write_text(text)


if __name__ == "__main__":
    main()
