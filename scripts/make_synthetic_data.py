#!/usr/bin/env python3
"""
SYNTHETIC test candles - for checking the plumbing only, never for judging a strategy.

Generates 1h BTC/ETH/SOL candles (regime-switching random walk, including one
sharp crash) in Freqtrade's feather format, so backtests and the drawdown
guard can be exercised without exchange access.

usage: make_synthetic_data.py <datadir> [days]
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

out = Path(sys.argv[1]) / "binance"
days = int(sys.argv[2]) if len(sys.argv) > 2 else 730
out.mkdir(parents=True, exist_ok=True)
n = days * 24
dates = pd.date_range(end=pd.Timestamp("2026-11-01", tz="UTC"), periods=n, freq="1h")

for i, (pair, start, vol) in enumerate([("BTC_USDT", 60000, 0.006), ("ETH_USDT", 3000, 0.008),
                                        ("SOL_USDT", 150, 0.011)]):
    rng = np.random.default_rng(42 + i)
    regime = np.repeat(rng.choice([-1, 0, 1], size=n // 500 + 1, p=[0.3, 0.3, 0.4]), 500)[:n]
    drift = regime * vol * 0.06
    rets = drift + rng.standard_normal(n) * vol
    crash = int(n * 0.6)
    rets[crash:crash + 12] -= vol * 2.5  # ~12h selloff to exercise the drawdown halt
    close = start * np.exp(np.cumsum(rets))
    open_ = np.concatenate([[start], close[:-1]])
    wick = np.abs(rng.standard_normal(n)) * vol * 0.5
    high = np.maximum(open_, close) * (1 + wick)
    low = np.minimum(open_, close) * (1 - wick)
    volume = rng.lognormal(10, 0.4, n) * (1 + 3 * np.abs(rets) / vol / 10)
    df = pd.DataFrame({"date": dates, "open": open_, "high": high, "low": low,
                       "close": close, "volume": volume})
    df.to_feather(out / f"{pair}-1h.feather")
    print(f"wrote {pair}: {close[0]:.2f} -> {close[-1]:.2f}")
