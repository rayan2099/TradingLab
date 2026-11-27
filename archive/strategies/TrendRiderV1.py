"""Phase 2 candidate: TrendRider - 20-day breakout, only in an uptrend, 4h candles.

  regime : lab_regime uptrend (daily close > SMA50 > SMA200)
  entry  : 4h close above the highest high of the previous 20 days (120 candles)
  exit   : 4h close below the lowest low of the previous 5 days (30 candles),
           or the uptrend ends, or the 5% stop
  sizing : half of the lab's 1%-per-trade risk budget (0.5% of equity per stop-out);
           this only makes positions smaller, never larger than lab_risk allows

Run it on 4h candles: freqtrade ... --timeframe 4h (base.json says 1h and the
config wins over the strategy). Designed on 2021-2024 only; see docs/history/PHASE2_RESEARCH.md.
"""
from lab_regime import add_regime, startup_candles
from lab_risk import RiskGuardedStrategy


class TrendRiderV1(RiskGuardedStrategy):
    timeframe = "4h"
    startup_candle_count = startup_candles("4h")
    minimal_roi = {"0": 100}  # exits come from signals / stops, not ROI
    stoploss = -0.05
    risk_scale = 0.5

    def populate_indicators(self, df, metadata):
        df["hh20d"] = df["high"].rolling(120).max().shift(1)
        df["ll5d"] = df["low"].rolling(30).min().shift(1)
        return add_regime(df)

    def populate_entry_trend(self, df, metadata):
        df.loc[df["uptrend"] & (df["close"] > df["hh20d"]) & (df["volume"] > 0),
               ["enter_long", "enter_tag"]] = (1, "breakout_20d_in_uptrend")
        return df

    def populate_exit_trend(self, df, metadata):
        df.loc[(df["close"] < df["ll5d"]) | ~df["uptrend"], ["exit_long", "exit_tag"]] = (
            1, "low_5d_or_regime_off")
        return df

    def custom_stake_amount(self, *args, **kwargs):
        return super().custom_stake_amount(*args, **kwargs) * self.risk_scale
