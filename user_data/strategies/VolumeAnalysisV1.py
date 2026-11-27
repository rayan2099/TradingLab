"""Slot 05 - Volume analysis: Chaikin money flow + OBV trend confirm buying pressure."""
import talib.abstract as ta
from lab_risk import RiskGuardedStrategy


class VolumeAnalysisV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = 60
    minimal_roi = {"0": 0.05, "480": 0.025, "1440": 0}
    stoploss = -0.04

    def populate_indicators(self, df, metadata):
        mfm = ((df["close"] - df["low"]) - (df["high"] - df["close"])) / (
            (df["high"] - df["low"]).replace(0, 1e-9))
        df["cmf"] = (mfm * df["volume"]).rolling(20).sum() / df["volume"].rolling(20).sum()
        df["obv"] = ta.OBV(df)
        df["obv_ema"] = df["obv"].ewm(span=20).mean()
        df["ema50"] = ta.EMA(df, timeperiod=50)
        return df

    def populate_entry_trend(self, df, metadata):
        df.loc[
            (df["cmf"] > 0.10)
            & (df["cmf"].shift(1) <= 0.10)
            & (df["obv"] > df["obv_ema"])
            & (df["close"] > df["ema50"]),
            ["enter_long", "enter_tag"],
        ] = (1, "cmf_obv_accumulation")
        return df

    def populate_exit_trend(self, df, metadata):
        df.loc[(df["cmf"] < -0.05) | (df["obv"] < df["obv_ema"] * 0.98), [
            "exit_long", "exit_tag"]] = (1, "distribution")
        return df
