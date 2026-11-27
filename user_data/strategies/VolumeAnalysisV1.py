"""Slot 05 - Volume analysis: Chaikin money flow + OBV trend confirm buying pressure."""
import talib.abstract as ta
from lab_risk import RiskGuardedStrategy


class VolumeAnalysisV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = 200  # EMA50 settles by ~200 candles (recursive-analysis)
    minimal_roi = {"0": 0.05, "480": 0.025, "1440": 0}
    stoploss = -0.04

    def populate_indicators(self, df, metadata):
        mfm = ((df["close"] - df["low"]) - (df["high"] - df["close"])) / (
            (df["high"] - df["low"]).replace(0, 1e-9))
        df["cmf"] = (mfm * df["volume"]).rolling(20).sum() / df["volume"].rolling(20).sum()
        df["obv"] = ta.OBV(df)
        # OBV is cumulative, so its level depends on where the data starts. Only the
        # gap to its own EMA is used, which is independent of that starting point.
        df["obv_gap"] = df["obv"] - df["obv"].ewm(span=20, adjust=False).mean()
        df["ema50"] = ta.EMA(df, timeperiod=50)
        return df

    def populate_entry_trend(self, df, metadata):
        df.loc[
            (df["cmf"] > 0.10)
            & (df["cmf"].shift(1) <= 0.10)
            & (df["obv_gap"] > 0)
            & (df["close"] > df["ema50"]),
            ["enter_long", "enter_tag"],
        ] = (1, "cmf_obv_accumulation")
        return df

    def populate_exit_trend(self, df, metadata):
        df.loc[(df["cmf"] < -0.05) | (df["obv_gap"] < 0), ["exit_long", "exit_tag"]] = (
            1, "distribution")
        return df
