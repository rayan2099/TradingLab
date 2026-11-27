"""Slot 03 - Momentum: rising MACD histogram with positive rate of change."""
import talib.abstract as ta
from lab_risk import RiskGuardedStrategy


class MomentumV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = 200  # MACD settles by ~200 candles (recursive-analysis)
    minimal_roi = {"0": 0.06, "360": 0.03, "1440": 0}
    stoploss = -0.035

    def populate_indicators(self, df, metadata):
        macd = ta.MACD(df)
        df["macdhist"] = macd["macdhist"]
        df["roc"] = ta.ROC(df, timeperiod=12)
        df["rsi"] = ta.RSI(df, timeperiod=14)
        return df

    def populate_entry_trend(self, df, metadata):
        df.loc[
            (df["macdhist"] > 0)
            & (df["macdhist"] > df["macdhist"].shift(1))
            & (df["macdhist"].shift(1) > df["macdhist"].shift(2))
            & (df["roc"] > 1.0)
            & (df["rsi"].between(55, 75))
            & (df["volume"] > 0),
            ["enter_long", "enter_tag"],
        ] = (1, "macd_momentum")
        return df

    def populate_exit_trend(self, df, metadata):
        df.loc[(df["macdhist"] < 0) | (df["rsi"] > 80), ["exit_long", "exit_tag"]] = (
            1, "momentum_fade")
        return df
