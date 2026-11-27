#!/usr/bin/env python3
"""
Independent mark-to-market drawdown check for a backtest result.

Rebuilds hourly equity (cash + open positions at each 1h close, exit fee
included) from the exported trades, so the 5% line can be verified without
trusting the strategy's own bookkeeping.

usage: mtm_drawdown.py STRATEGY [results.zip]
"""
import glob
import json
import sys
import zipfile

import pandas as pd

strategy = sys.argv[1]
path = sys.argv[2] if len(sys.argv) > 2 else sorted(glob.glob("user_data/backtest_results/*.zip"))[-1]
with zipfile.ZipFile(path) as f:
    name = next(n for n in f.namelist() if n.endswith(".json") and not n.endswith("_config.json"))
    r = json.loads(f.read(name))["strategy"][strategy]
trades = pd.DataFrame(r["trades"])
idx = pd.date_range(r["backtest_start"], r["backtest_end"], freq="1h", tz="UTC")
equity = pd.Series(float(r["starting_balance"]), index=idx)
if not trades.empty:
    closes = {p: pd.read_feather(f"user_data/data/binance/{p.replace('/', '_')}-1h.feather")
              .set_index("date")["close"] for p in trades["pair"].unique()}
    for _, t in trades.iterrows():
        opened, closed = pd.Timestamp(t["open_date"]), pd.Timestamp(t["close_date"])
        equity[idx >= closed] += t["profit_abs"]
        held = (idx >= opened) & (idx < closed)
        px = closes[t["pair"]].reindex(idx[held], method="ffill").to_numpy()
        equity[held] += t["amount"] * px * (1 - t["fee_close"]) - t["stake_amount"] * (1 + t["fee_open"])
dd = 1 - equity / equity.cummax()
print(f"{strategy}: end equity {equity.iloc[-1]:.2f}, worst mark-to-market drawdown "
      f"{dd.max():.2%} on {dd.idxmax():%Y-%m-%d %H:%M}, hours beyond 5%: {(dd > 0.05).sum()}")
