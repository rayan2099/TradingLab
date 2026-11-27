#!/usr/bin/env bash
# Offline test suite: safety gate (pass + must-fail cases), and backtests on
# synthetic candles proving the strategies load and the 5% halt fires.
# usage: tests/run_checks.sh   (needs a Python env with freqtrade installed)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="${PYTHON:-python3}"
WORK="$(mktemp -d)"
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

echo "== synthetic data"; mkdir -p "$WORK/results"
"$PY" "$ROOT/scripts/make_synthetic_data.py" "$WORK/data" 730 >/dev/null
FT=("$PY" "$ROOT/tests/offline_freqtrade.py" backtesting --userdir "$ROOT/user_data"
    --datadir "$WORK/data/binance" --config "$ROOT/user_data/config/base.json"
    --export trades --backtest-directory "$WORK/results/")

echo "== all slots + benchmark load and backtest"
"${FT[@]}" --strategy-list TrendFollowingV1 MeanReversionV1 MomentumV1 BreakoutV1 \
  VolumeAnalysisV1 MachineLearningV1 BuyAndHoldBenchmark > "$WORK/all.log" 2>&1
sed -n '/STRATEGY SUMMARY/,$p' "$WORK/all.log"

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
