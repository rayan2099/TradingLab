#!/usr/bin/env python3
"""
Trading Lab safety gate. Runs before every bot, backtest and data download.
Exits non-zero (and the container refuses to start) if any Phase 1 rule is broken:

  * dry_run must be true
  * no exchange API key, secret, password or uid anywhere
  * spot only, no margin mode, no leverage
  * no FREQTRADE__* environment overrides (they could flip dry_run off)
  * strategies may not short, and guarded strategies may not set a stoploss
    looser than the hard limit in lab_risk.py

Standard library only, so it also runs on a Mac without Freqtrade installed.
"""
from __future__ import annotations

import ast
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UD = ROOT / "user_data"
if not UD.exists():  # inside the container scripts/ and user_data/ are siblings under /freqtrade
    UD = Path("/freqtrade/user_data")
CONFIG_DIR = UD / "config"
STRAT_DIR = UD / "strategies"

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def load(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        fail(f"{path.name}: cannot parse JSON ({exc})")
        return {}


def check_config(name: str, cfg: dict) -> None:
    if cfg.get("dry_run") is not True:
        fail(f"{name}: dry_run must be true")
    if cfg.get("trading_mode", "spot") != "spot":
        fail(f"{name}: trading_mode must be spot")
    if cfg.get("margin_mode"):
        fail(f"{name}: margin_mode must be empty")
    if "leverage" in json.dumps(cfg).lower():
        fail(f"{name}: leverage settings are not allowed")
    ex = cfg.get("exchange", {})
    for field in ("key", "secret", "password", "uid", "walletAddress", "privateKey"):
        if ex.get(field):
            fail(f"{name}: exchange.{field} must be empty (no API keys in Phase 1)")
    for field in ("apiKey", "secret", "password", "uid"):
        for ccxt_key in ("ccxt_config", "ccxt_async_config", "ccxt_sync_config"):
            if ex.get(ccxt_key, {}).get(field):
                fail(f"{name}: exchange.{ccxt_key}.{field} must be empty")


def merged(*cfgs: dict) -> dict:
    out: dict = {}
    for c in cfgs:
        for k, v in c.items():
            if isinstance(v, dict) and isinstance(out.get(k), dict):
                out[k] = {**out[k], **v}
            else:
                out[k] = v
    return out


def hard_stoploss_limit() -> float:
    tree = ast.parse((STRAT_DIR / "lab_risk.py").read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "MAX_TRADE_STOPLOSS" for t in node.targets
        ):
            return float(ast.literal_eval(node.value))
    fail("lab_risk.py: MAX_TRADE_STOPLOSS not found")
    return 0.0


def check_strategies() -> None:
    limit = hard_stoploss_limit()
    for path in sorted(STRAT_DIR.glob("*.py")):
        if path.name == "lab_risk.py":
            continue
        tree = ast.parse(path.read_text())
        for cls in [n for n in tree.body if isinstance(n, ast.ClassDef)]:
            attrs = {}
            for node in cls.body:
                if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
                    try:
                        attrs[node.targets[0].id] = ast.literal_eval(node.value)
                    except ValueError:
                        pass
            bases = [getattr(b, "id", "") for b in cls.bases]
            if attrs.get("can_short"):
                fail(f"{path.name}:{cls.name}: can_short must be False")
            if "RiskGuardedStrategy" in bases:
                sl = attrs.get("stoploss")
                if sl is None or sl < -limit:
                    fail(f"{path.name}:{cls.name}: stoploss {sl} looser than -{limit}")
            elif attrs.get("risk_guarded") is not False:
                fail(f"{path.name}:{cls.name}: must inherit RiskGuardedStrategy "
                     "(only the benchmark may opt out with risk_guarded = False)")


def main() -> int:
    for var in os.environ:
        if var.upper().startswith("FREQTRADE__"):
            fail(f"environment override {var} is not allowed in Phase 1")

    base = load(CONFIG_DIR / "base.json")
    check_config("base.json", base)
    for bot in sorted((CONFIG_DIR / "bots").glob("*.json")):
        check_config(f"bots/{bot.name}", merged(base, load(bot)))
    check_strategies()

    if errors:
        print("SAFETY CHECK FAILED - refusing to start:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("Safety check passed: dry-run, spot, no keys, no leverage, no shorts, stops within limit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
