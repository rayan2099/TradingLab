"""
Market-regime filter shared by the Phase 2 strategies ("only buy in an uptrend").

Built from the strategy's own candles, so it needs no extra data download:
completed daily closes are resampled from the strategy timeframe, and a day's
value is only used from the next day on (no lookahead).

uptrend = the pair's last completed daily close is above its 50-day SMA, and
          that SMA is above the 200-day SMA ("golden-cross" regime).

The 50/200 pair is the textbook definition and was fixed before any backtest;
it is deliberately not tuned.
"""
from __future__ import annotations

import pandas as pd

FAST_DAYS = 50
SLOW_DAYS = 200
_PER_DAY = {"1h": 24, "4h": 6, "1d": 1}


def startup_candles(timeframe: str) -> int:
    return (SLOW_DAYS + 2) * _PER_DAY[timeframe]


def add_regime(df: pd.DataFrame) -> pd.DataFrame:
    daily = df.set_index("date")["close"].resample("1D").last()
    sma_fast = daily.rolling(FAST_DAYS).mean()
    sma_slow = daily.rolling(SLOW_DAYS).mean()
    up = (daily > sma_fast) & (sma_fast > sma_slow)
    # the value for day D becomes usable at D+1 00:00, after D's last candle has closed
    up = up.shift(1, freq="1D")
    df["uptrend"] = up.reindex(df["date"], method="ffill").fillna(False).astype(bool).values
    return df
