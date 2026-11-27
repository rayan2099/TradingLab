"""
Slot 06 - Machine learning (reserved for Phase 2).

Placeholder only: it loads, passes the safety checks and never trades, so the
slot exists in every report. Phase 2 will replace it with a FreqAI model,
which needs the freqtrade "freqai" Docker image and its own validation.
"""
from lab_risk import RiskGuardedStrategy


class MachineLearningV1(RiskGuardedStrategy):
    timeframe = "1h"
    startup_candle_count = 0
    minimal_roi = {"0": 100}
    stoploss = -0.04

    def populate_indicators(self, df, metadata):
        return df

    def populate_entry_trend(self, df, metadata):
        df["enter_long"] = 0
        return df

    def populate_exit_trend(self, df, metadata):
        df["exit_long"] = 0
        return df
