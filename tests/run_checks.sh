#!/usr/bin/env bash
# Offline test suite: safety gate (pass + must-fail cases), and backtests on
# synthetic candles proving the course strategies load and the 5% halt fires.
# usage: tests/run_checks.sh   (needs a Python env with freqtrade installed)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="${PYTHON:-python3}"
WORK="$(mktemp -d)"
# Strategies coded from the course (docs/CANDLES_VOLUME_RULES.md). Add new ones here.
COURSE_STRATS="${COURSE_STRATS:-CandleVolumeV1}"
echo "== safety gate (expect pass)"; "$PY" "$ROOT/scripts/safety_check.py"

echo "== safety gate must refuse bad configs"
for mutation in 'c["dry_run"]=False' 'c["exchange"]["key"]="abc"' 'c["trading_mode"]="futures"'; do
  cp -r "$ROOT" "$WORK/bad"
  "$PY" - "$WORK/bad/user_data/config/base.json" "$mutation" <<'PYEOF'
import json, sys
p, m = sys.argv[1], sys.argv[2]; c = json.load(open(p)); exec(m); json.dump(c, open(p, "w"))
PYEOF
  if "$PY" "$WORK/bad/scripts/safety_check.py" >/dev/null 2>&1; then echo "FAIL: accepted $mutation"; exit 1; fi
  echo "   refused: $mutation"; rm -rf "$WORK/bad"
done
if FREQTRADE__DRY_RUN=false "$PY" "$ROOT/scripts/safety_check.py" >/dev/null 2>&1; then
  echo "FAIL: accepted env override"; exit 1; fi
echo "   refused: FREQTRADE__DRY_RUN env override"
cp -r "$ROOT" "$WORK/bad"; mkdir -p "$WORK/bad/user_data/config/local"
echo '{"api_server":{"enabled":true,"listen_ip_address":"0.0.0.0","listen_port":8081}}' \
  > "$WORK/bad/user_data/config/local/course_candle_volume.json"
if "$PY" "$WORK/bad/scripts/safety_check.py" >/dev/null 2>&1; then echo "FAIL: accepted public dashboard"; exit 1; fi
echo "   refused: dashboard listening beyond 127.0.0.1"; rm -rf "$WORK/bad"

echo "== risk engine unit tests (paper mode: sizing, persisted peak, latched halt, throttle)"
"$PY" "$ROOT/tests/test_risk_unit.py" 2>/dev/null | grep -E "PASS|passed"

echo "== synthetic data"; mkdir -p "$WORK/results" "$WORK/la"
"$PY" "$ROOT/scripts/make_synthetic_data.py" "$WORK/data" 730 >/dev/null
FT=("$PY" "$ROOT/tests/offline_freqtrade.py" backtesting --userdir "$ROOT/user_data"
    --datadir "$WORK/data/binance" --config "$ROOT/user_data/config/base.json"
    --export trades --backtest-directory "$WORK/results/")

echo "== course strategies + benchmark load and backtest"
"${FT[@]}" --strategy-list $COURSE_STRATS BuyAndHoldBenchmark > "$WORK/all.log" 2>&1 \
  || { tail -20 "$WORK/all.log"; exit 1; }
sed -n '/STRATEGY SUMMARY/,$p' "$WORK/all.log"

echo "== every trade sized to ~1% equity risk"
"$PY" - "$WORK/results" "$ROOT" <<'PYEOF'
import glob, json, sys, zipfile
sys.path.insert(0, sys.argv[2] + "/user_data/strategies")
z = sorted(glob.glob(sys.argv[1] + "/*.zip"))[-1]
with zipfile.ZipFile(z) as f:
    name = next(n for n in f.namelist() if n.endswith(".json") and not n.endswith("_config.json"))
    data = json.loads(f.read(name))["strategy"]
worst = 0.0
for strat, r in data.items():
    if strat == "BuyAndHoldBenchmark":
        continue
    equity = r["starting_balance"]
    for t in sorted(r["trades"], key=lambda t: t["open_timestamp"]):
        risk = t["stake_amount"] * (abs(t["initial_stop_loss_ratio"]) + 0.003) / equity
        worst = max(worst, risk)
        equity += t["profit_abs"]
assert worst <= 0.0125, f"a trade risked {worst:.2%} of equity"
print(f"   PASS: largest planned risk on any trade {worst:.2%} of equity (limit ~1%)")
PYEOF

echo "== scorecard renders"
cp "$WORK"/results/*.zip "$WORK/latest.zip"
"$PY" "$ROOT/scripts/scorecard.py" backtest "$WORK/latest.zip" | tail -3

echo "== no lookahead bias in any course strategy"
"$PY" "$ROOT/tests/offline_freqtrade.py" lookahead-analysis --userdir "$ROOT/user_data" \
  --datadir "$WORK/data/binance" --config "$ROOT/user_data/config/base.json" \
  --backtest-directory "$WORK/la/" --timerange 20260101- \
  --strategy-list $COURSE_STRATS > "$WORK/la.log" 2>&1
grep -E "\.py " "$WORK/la.log" | grep -q " Yes " && { grep -E "\.py " "$WORK/la.log"; echo "FAIL: lookahead bias"; exit 1; }
echo "   PASS: $COURSE_STRATS has_bias = No"

echo "== uptrend filter (lab_regime) behaves"
"$PY" - "$ROOT" <<'PYEOF'
import sys
import pandas as pd
sys.path.insert(0, sys.argv[1] + "/user_data/strategies")
from lab_regime import add_regime
# 300 days falling then 300 days rising: no uptrend while falling, uptrend late in the rise,
# and a day's regime may only change at midnight from the previous day's close
d = pd.date_range("2024-01-01", periods=600 * 24, freq="1h", tz="UTC")
px = [100 - i / 24 * 0.1 if i < 300 * 24 else 70 + (i - 300 * 24) / 24 * 0.3 for i in range(len(d))]
df = add_regime(pd.DataFrame({"date": d, "close": px}))
assert not df["uptrend"].iloc[: 300 * 24].any(), "uptrend during a fall"
assert df["uptrend"].iloc[-24:].all(), "no uptrend at the end of a long rise"
assert df.groupby(df["date"].dt.date)["uptrend"].nunique().max() == 1, "regime changed intraday"
print("   PASS: uptrend filter (off in a fall, on in a rise, changes only at day close)")
PYEOF

echo "== hard 5% halt fires"
cp "$ROOT/tests/strategies/HaltProbe.py" "$WORK/HaltProbe.py"
cp "$ROOT/user_data/strategies/lab_risk.py" "$WORK/lab_risk.py"
rm -f "$WORK"/results/*
"${FT[@]}" --strategy HaltProbe --strategy-path "$WORK" > "$WORK/halt.log" 2>&1 || { tail -20 "$WORK/halt.log"; exit 1; }
"$PY" - "$WORK/results" <<'PYEOF'
import json, sys, zipfile, glob
z = sorted(glob.glob(sys.argv[1] + "/*.zip"))[-1]
with zipfile.ZipFile(z) as f:
    name = [n for n in f.namelist() if n.endswith(".json") and "config" not in n and "_" in n][0]
    res = json.loads(f.read(name))["strategy"]["HaltProbe"]
trades = res["trades"]
halts = [t for t in trades if t["exit_reason"] == "risk_halt_max_drawdown"]
last_halt = max(t["close_date"] for t in halts) if halts else None
after = [t for t in trades if last_halt and t["open_date"] > last_halt]
print(f"   trades={len(trades)} halted_exits={len(halts)} opened_after_halt={len(after)} "
      f"max_drawdown_account={res['max_drawdown_account']:.2%}")
assert halts, "halt never fired"
assert not after, "trades opened after the halt"
print("   PASS: halt fired, every position closed, no trades afterwards")
PYEOF
rm -rf "$WORK"
echo "ALL CHECKS PASSED"
