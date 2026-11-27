"""Phase 2: VolumeAnalysisV1 unchanged, plus the shared uptrend filter (lab_regime.py).

Only new entries are filtered; exits are the V1 exits. See docs/PHASE2_RESEARCH.md.
"""
from lab_regime import add_regime, startup_candles
from lab_risk import RiskGuardedStrategy
from VolumeAnalysisV1 import VolumeAnalysisV1


class VolumeAnalysisR(VolumeAnalysisV1, RiskGuardedStrategy):
    startup_candle_count = startup_candles("1h")
    stoploss = -0.04  # same as V1 (restated for the safety gate)

    def populate_indicators(self, df, metadata):
        return add_regime(super().populate_indicators(df, metadata))

    def populate_entry_trend(self, df, metadata):
        df = super().populate_entry_trend(df, metadata)
        df.loc[~df["uptrend"], ["enter_long", "enter_tag"]] = (0, None)
        return df
