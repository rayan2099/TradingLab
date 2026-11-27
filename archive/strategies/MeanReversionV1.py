"""Slot 02 - Mean reversion: oversold dips below the lower Bollinger band in an uptrend."""
import talib.abstract as ta
from technical import qtpylib
from lab_risk import RiskGuardedStrategy


class MeanReversionV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = 600  # EMA200 needs ~3x its period to settle (recursive-analysis)
    minimal_roi = {"0": 0.04, "240": 0.02, "720": 0}
    stoploss = -0.04

    def populate_indicators(self, df, metadata):
        bb = qtpylib.bollinger_bands(qtpylib.typical_price(df), window=20, stds=2)
        df["bb_lower"], df["bb_mid"] = bb["lower"], bb["mid"]
        df["rsi"] = ta.RSI(df, timeperiod=14)
        df["ema200"] = ta.EMA(df, timeperiod=200)
        return df

    def populate_entry_trend(self, df, metadata):
        df.loc[
            (df["close"] < df["bb_lower"])
            & (df["rsi"] < 30)
            & (df["close"] > df["ema200"] * 0.95)
            & (df["volume"] > 0),
            ["enter_long", "enter_tag"],
        ] = (1, "bb_oversold")
        return df

    def populate_exit_trend(self, df, metadata):
        df.loc[df["close"] > df["bb_mid"], ["exit_long", "exit_tag"]] = (1, "back_to_mean")
        return df
