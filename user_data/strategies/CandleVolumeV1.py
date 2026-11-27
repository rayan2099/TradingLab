"""Candles + volume (استراتيجية الشموع والكميات): bullish reversal candles on heavy volume.

Rules fixed before any backtest (textbook values, not tuned):
  pattern : hammer, bullish engulfing, morning star or piercing line (TA-Lib)
  volume  : the signal candle's volume is at least 2x its 20-candle average
  location: the candle makes a fresh 10-candle low (a reversal at a pullback)
  regime  : lab_regime uptrend (daily close > SMA50 > SMA200)
  exit    : +6% take profit, 4% stop, or flat after 3 days
"""
import talib.abstract as ta
from lab_regime import add_regime, startup_candles
from lab_risk import RiskGuardedStrategy

PATTERNS = ("CDLHAMMER", "CDLENGULFING", "CDLMORNINGSTAR", "CDLPIERCING")


class CandleVolumeV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = startup_candles("1h")
    minimal_roi = {"0": 0.06, "4320": 0}
    stoploss = -0.04
    use_regime = True

    def populate_indicators(self, df, metadata):
        bullish = False
        for name in PATTERNS:
            bullish = bullish | (getattr(ta, name)(df) > 0)
        df["bull_candle"] = bullish
        df["vol_avg20"] = df["volume"].rolling(20).mean().shift(1)
        df["low10"] = df["low"].rolling(10).min().shift(1)
        return add_regime(df)

    def populate_entry_trend(self, df, metadata):
        cond = (df["bull_candle"]
                & (df["volume"] >= 2 * df["vol_avg20"])
                & (df["low"].rolling(3).min() <= df["low10"]))  # pattern formed at a fresh low
        if self.use_regime:
            cond &= df["uptrend"]
        df.loc[cond, ["enter_long", "enter_tag"]] = (1, "bull_candle_high_volume")
        return df

    def populate_exit_trend(self, df, metadata):
        return df
