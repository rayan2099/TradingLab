"""Slot 01 - Trend following: EMA alignment with a fast/slow crossover."""
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from lab_risk import RiskGuardedStrategy


class TrendFollowingV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = 210
    minimal_roi = {"0": 100}  # exits come from signals / stops, not ROI
    stoploss = -0.04
    trailing_stop = True
    trailing_stop_positive = 0.02
    trailing_stop_positive_offset = 0.04
    trailing_only_offset_is_reached = True

    def populate_indicators(self, df, metadata):
        df["ema20"] = ta.EMA(df, timeperiod=20)
        df["ema50"] = ta.EMA(df, timeperiod=50)
        df["ema200"] = ta.EMA(df, timeperiod=200)
        df["adx"] = ta.ADX(df)
        return df

    def populate_entry_trend(self, df, metadata):
        df.loc[
            qtpylib.crossed_above(df["ema20"], df["ema50"])
            & (df["close"] > df["ema200"])
            & (df["adx"] > 20)
            & (df["volume"] > 0),
            ["enter_long", "enter_tag"],
        ] = (1, "ema_cross_up")
        return df

    def populate_exit_trend(self, df, metadata):
        df.loc[qtpylib.crossed_below(df["ema20"], df["ema50"]), ["exit_long", "exit_tag"]] = (
            1, "ema_cross_down")
        return df
