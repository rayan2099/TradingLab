"""
Trading Lab hard risk limits.

Every lab strategy inherits from RiskGuardedStrategy. The limits below are
enforced in code, not left to any agent or config file:

  * spot only, long only, leverage fixed at 1x
  * per-trade stoploss may not be looser than MAX_TRADE_STOPLOSS
  * position sizing: each trade risks RISK_PER_TRADE of current equity if its
    stoploss is hit (plus fees), capped at the normal equal-split stake
  * paper / live bots: at HARD_DRAWDOWN_LIMIT below peak equity (marked to
    market), every open trade is exited and the bot stays halted (latched)
    until a human clears the halt file
  * backtests: the same 5% line is measured but NOT enforced, so a strategy's
    full history can be judged. Every breach is logged and written to
    user_data/backtest_results/risk_breaches_<Strategy>.json

Changing any number in this file is a "risk-limit modification" and needs
human approval (see docs/RISK_POLICY.md).
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path

from freqtrade.enums import RunMode
from freqtrade.persistence import LocalTrade, Trade
from freqtrade.strategy import IStrategy

logger = logging.getLogger(__name__)

# ---- Hard limits (human approval required to change) -----------------------
HARD_DRAWDOWN_LIMIT = 0.05  # 5% below peak equity -> exit everything, halt
RISK_PER_TRADE = 0.01  # a stopped-out trade costs at most ~1% of equity
FEE_BUFFER = 0.003  # round-trip fees + slippage assumed per trade
MAX_TRADE_STOPLOSS = 0.05  # no single trade may risk more than 5% of its stake
MAX_LEVERAGE = 1.0
# -----------------------------------------------------------------------------

HALT_EXIT_TAG = "risk_halt_max_drawdown"


class RiskGuardedStrategy(IStrategy):
    """Base class: subclasses implement indicators / entry / exit signals only."""

    INTERFACE_VERSION = 3
    can_short = False  # spot, long only
    risk_guarded = True
    enforce_halt_in_backtest = False  # only test probes set this

    def bot_start(self, **kwargs) -> None:
        if self.can_short:
            raise RuntimeError(f"{self.__class__.__name__}: shorting is not allowed")
        if self.stoploss < -MAX_TRADE_STOPLOSS:
            raise RuntimeError(
                f"{self.__class__.__name__}: stoploss {self.stoploss} is looser than "
                f"the hard limit -{MAX_TRADE_STOPLOSS}"
            )
        if self.config.get("trading_mode", "spot") != "spot":
            raise RuntimeError("Trading Lab Phase 1 is spot only")
        self._peak_equity = self._starting_capital()
        self._halted = False
        self._halt_file = self._halt_path()
        self._breaches: list[dict] = []
        self._in_breach = False
        if self._halt_file and self._halt_file.exists():
            self._halted = True
            logger.warning("Risk halt file present (%s): bot stays halted.", self._halt_file)

    # ---- equity tracking ----------------------------------------------------

    def _is_backtest(self) -> bool:
        return self.dp.runmode not in (RunMode.DRY_RUN, RunMode.LIVE)

    def _starting_capital(self) -> float:
        wallet = self.config.get("dry_run_wallet", 0)
        if isinstance(wallet, dict):
            wallet = wallet.get(self.config["stake_currency"], 0)
        return float(wallet)

    def _halt_path(self) -> Path | None:
        if self._is_backtest():
            return None
        name = self.config.get("bot_name", self.__class__.__name__)
        return Path(self.config["user_data_dir"]) / "risk_state" / f"{name}.halted.json"

    def _last_close(self, pair: str) -> float | None:
        df, _ = self.dp.get_analyzed_dataframe(pair, self.timeframe)
        if df is None or df.empty:
            return None
        return float(df["close"].iloc[-1])

    def _equity(self) -> float:
        start = self._starting_capital()
        if self._is_backtest():
            closed = LocalTrade.bt_total_profit
        else:
            closed = Trade.get_total_closed_profit()
        unrealized = 0.0
        for trade in Trade.get_trades_proxy(is_open=True):
            rate = self._last_close(trade.pair) or trade.open_rate
            unrealized += trade.calc_profit(rate) + trade.realized_profit
        return start + closed + unrealized

    def current_drawdown(self) -> float:
        equity = self._equity()
        self._peak_equity = max(getattr(self, "_peak_equity", equity), equity)
        if self._peak_equity <= 0:
            return 0.0
        return 1 - equity / self._peak_equity

    def _trip_halt(self, drawdown: float, when: datetime) -> None:
        self._halted = True
        logger.warning("HARD DRAWDOWN LIMIT HIT: %.2f%% at %s. Exiting and halting.",
                       drawdown * 100, when)
        if self._halt_file:
            self._halt_file.parent.mkdir(parents=True, exist_ok=True)
            self._halt_file.write_text(json.dumps({
                "halted_at": when.isoformat(),
                "drawdown": round(drawdown, 5),
                "peak_equity": round(self._peak_equity, 4),
                "note": "Delete this file only after a human review.",
            }, indent=2))

    # ---- hooks --------------------------------------------------------------

    def _enforcing(self) -> bool:
        return not self._is_backtest() or self.enforce_halt_in_backtest

    def _record_breach(self, dd: float, when: datetime) -> None:
        self._breaches.append({"at": when.isoformat(), "drawdown": round(dd, 5),
                               "peak_equity": round(self._peak_equity, 4)})
        logger.warning("Backtest: 5%% drawdown line crossed (%.2f%%) at %s - a paper/live "
                       "bot would have halted here.", dd * 100, when)
        out = Path(self.config["user_data_dir"]) / "backtest_results"
        out.mkdir(parents=True, exist_ok=True)
        (out / f"risk_breaches_{self.__class__.__name__}.json").write_text(json.dumps({
            "strategy": self.__class__.__name__,
            "hard_drawdown_limit": HARD_DRAWDOWN_LIMIT,
            "first_breach": self._breaches[0],
            "breaches": self._breaches,
        }, indent=2))

    def bot_loop_start(self, current_time: datetime, **kwargs) -> None:
        if self._halted:
            return
        dd = self.current_drawdown()
        if dd < HARD_DRAWDOWN_LIMIT:
            self._in_breach = False
            return
        if self._enforcing():
            self._trip_halt(dd, current_time)
        elif not self._in_breach:
            self._in_breach = True
            self._record_breach(dd, current_time)

    def confirm_trade_entry(self, pair, order_type, amount, rate, time_in_force,
                            current_time, entry_tag, side, **kwargs) -> bool:
        if side != "long" or self._halted:
            return False
        return True

    def custom_stake_amount(self, pair, current_time, current_rate, proposed_stake,
                            min_stake, max_stake, leverage, entry_tag, side, **kwargs) -> float:
        if self._halted:
            return 0
        equity = self._equity()
        per_unit_risk = abs(self.stoploss) + FEE_BUFFER
        max_by_risk = equity * RISK_PER_TRADE / per_unit_risk
        stake = min(proposed_stake, max_by_risk, max_stake)
        if min_stake and stake < min_stake:
            return 0
        return stake

    def custom_exit(self, pair, trade, current_time, current_rate, current_profit, **kwargs):
        if self._halted:
            return HALT_EXIT_TAG
        return None

    def leverage(self, pair, current_time, current_rate, proposed_leverage,
                 max_leverage, entry_tag, side, **kwargs) -> float:
        return MAX_LEVERAGE
