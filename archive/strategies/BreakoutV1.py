"""Slot 04 - Breakout: close above the 20-candle Donchian high on above-average volume."""
from lab_risk import RiskGuardedStrategy


class BreakoutV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = 50
    minimal_roi = {"0": 100}
    stoploss = -0.04

    def populate_indicators(self, df, metadata):
        df["dc_high20"] = df["high"].rolling(20).max().shift(1)
        df["dc_low10"] = df["low"].rolling(10).min().shift(1)
        df["vol_avg"] = df["volume"].rolling(20).mean()
        return df

    def populate_entry_trend(self, df, metadata):
        df.loc[
            (df["close"] > df["dc_high20"])
            & (df["volume"] > 1.5 * df["vol_avg"]),
            ["enter_long", "enter_tag"],
        ] = (1, "donchian_breakout")
        return df

    def populate_exit_trend(self, df, metadata):
        df.loc[df["close"] < df["dc_low10"], ["exit_long", "exit_tag"]] = (1, "donchian_exit")
        return df
