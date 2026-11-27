"""
Test-only strategy: always long, wide stops and NO budget sizing, so a crash
pushes it past the 5% line and the hard drawdown halt must fire. It imitates
the case the budget cannot prevent (a price gap through the stoploss).
Never copy this into user_data/strategies.
"""
from lab_risk import RiskGuardedStrategy


class HaltProbe(RiskGuardedStrategy):
    timeframe = "1h"
    minimal_roi = {"0": 100}
    stoploss = -0.04
    enforce_halt_in_backtest = True

    def bot_start(self, **kwargs) -> None:
        super().bot_start(**kwargs)
        self.stoploss = -0.5  # simulate a gap: stops are not hit, only the halt can act

    def custom_stake_amount(self, pair, current_time, current_rate, proposed_stake, *a, **k):
        return proposed_stake if not self._halted else 0

    def populate_indicators(self, df, metadata):
        return df

    def populate_entry_trend(self, df, metadata):
        df["enter_long"] = 1
        return df

    def populate_exit_trend(self, df, metadata):
        df["exit_long"] = 0
        return df
