#!/usr/bin/env python3
"""
Unit tests for user_data/strategies/lab_risk.py in paper-trading mode (no network).
usage: python tests/test_risk_unit.py   (needs freqtrade installed)
"""
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "user_data" / "strategies"))

from freqtrade.enums import RunMode  # noqa: E402

import lab_risk  # noqa: E402
from TrendFollowingV1 import TrendFollowingV1  # noqa: E402

START = 266.67
T0 = datetime(2026, 1, 1, tzinfo=timezone.utc)


class World:
    """Fake account: closed profit, open trades and a ticker price."""

    def __init__(self):
        self.closed = 0.0
        self.open_trades = []
        self.price = 100.0


def make_bot(world: World, userdir: Path):
    cfg = {"dry_run_wallet": START, "stake_currency": "USDT", "user_data_dir": userdir,
           "bot_name": "unit_bot", "trading_mode": "spot", "timeframe": "1h"}
    bot = TrendFollowingV1(cfg)
    bot.dp = SimpleNamespace(runmode=RunMode.DRY_RUN,
                             ticker=lambda pair: {"last": world.price},
                             get_analyzed_dataframe=lambda *a: (None, None))
    patches = [
        mock.patch.object(lab_risk.Trade, "get_total_closed_profit", lambda: world.closed),
        mock.patch.object(lab_risk.Trade, "get_trades_proxy", lambda **k: world.open_trades),
    ]
    for p in patches:
        p.start()
    bot.bot_start()
    return bot, patches


def open_trade(amount, open_rate):
    return SimpleNamespace(pair="BTC/USDT", amount=amount, open_rate=open_rate, realized_profit=0.0,
                           calc_profit=lambda rate: amount * (rate - open_rate))


def stop(patches):
    for p in patches:
        p.stop()


def tick(bot, minutes):
    bot.bot_loop_start(current_time=T0 + timedelta(minutes=minutes))


def test_sizing(tmp):
    w = World()
    bot, p = make_bot(w, tmp)
    stake = bot.custom_stake_amount("BTC/USDT", T0, 100, 88.0, 5, 1000, 1, None, "long")
    expected = START * lab_risk.RISK_PER_TRADE / (abs(bot.stoploss) + lab_risk.FEE_BUFFER)
    assert abs(stake - expected) < 1e-6, (stake, expected)
    assert bot.custom_stake_amount("BTC/USDT", T0, 100, 3.0, 5, 1000, 1, None, "long") == 0
    assert bot.leverage("BTC/USDT", T0, 100, 3, 10, None, "long") == 1.0
    assert bot.confirm_trade_entry("BTC/USDT", "limit", 1, 100, "GTC", T0, None, "short") is False
    stop(p)


def test_peak_survives_restart_and_halt_latches(tmp):
    w = World()
    bot, p = make_bot(w, tmp)
    w.closed = 20.0  # equity 286.67 -> new peak, saved to disk
    tick(bot, 0)
    assert (tmp / "risk_state" / "unit_bot.state.json").exists()
    stop(p)

    w.closed = 0.0  # restart after losing it back: equity 266.67, peak must still be 286.67
    bot, p = make_bot(w, tmp)
    assert abs(bot._peak_equity - 286.67) < 1e-6, bot._peak_equity
    w.open_trades = [open_trade(1.0, 100.0)]
    w.price = 95.0  # equity 261.67 -> 8.7% below peak
    tick(bot, 0)
    assert bot._halted, "halt did not trip"
    assert (tmp / "risk_state" / "unit_bot.halted.json").exists()
    assert bot.custom_exit("BTC/USDT", w.open_trades[0], T0, 95, -0.05) == lab_risk.HALT_EXIT_TAG
    assert bot.confirm_trade_entry("BTC/USDT", "limit", 1, 100, "GTC", T0, None, "long") is False
    stop(p)

    w.open_trades, w.price = [], 100.0  # restart: the halt must still hold
    bot, p = make_bot(w, tmp)
    assert bot._halted, "halt was not latched across restart"
    assert bot.custom_stake_amount("BTC/USDT", T0, 100, 88.0, 5, 1000, 1, None, "long") == 0
    stop(p)


def test_live_check_throttle(tmp):
    w = World()
    bot, p = make_bot(w, tmp)
    tick(bot, 0)
    w.closed = -50.0  # big loss, but within the 30 s throttle window -> not yet checked
    bot.bot_loop_start(current_time=T0 + timedelta(seconds=10))
    assert not bot._halted
    bot.bot_loop_start(current_time=T0 + timedelta(seconds=40))
    assert bot._halted
    stop(p)


def test_corrupt_state_refuses_to_trade(tmp):
    (tmp / "risk_state").mkdir(parents=True)
    (tmp / "risk_state" / "unit_bot.state.json").write_text("{not json")
    w = World()
    bot, p = make_bot(w, tmp)
    assert bot._halted
    stop(p)


if __name__ == "__main__":
    tests = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    for t in tests:
        with tempfile.TemporaryDirectory() as d:
            t(Path(d))
        print(f"   PASS {t.__name__}")
    print(f"   {len(tests)} risk unit tests passed")
