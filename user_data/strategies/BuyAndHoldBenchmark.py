"""
Benchmark - buy and hold BTC/ETH/SOL in equal parts from the first candle.

Deliberately NOT risk guarded: it is the yardstick every strategy must beat
after fees. It is still spot, long only, dry-run and 1x.
"""
from freqtrade.strategy import IStrategy


class BuyAndHoldBenchmark(IStrategy):
    INTERFACE_VERSION = 3
    can_short = False
    risk_guarded = False
    timeframe = "1h"
    startup_candle_count = 0
    minimal_roi = {"0": 100}
    stoploss = -0.99
    use_exit_signal = False

    def populate_indicators(self, df, metadata):
        return df

    def populate_entry_trend(self, df, metadata):
        df["enter_long"] = 1
        return df

    def populate_exit_trend(self, df, metadata):
        df["exit_long"] = 0
        return df
