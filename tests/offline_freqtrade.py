#!/usr/bin/env python3
"""
Test harness: run the Freqtrade CLI with NO network access to the exchange.

Exchange market metadata for BTC/ETH/SOL-USDT is stubbed in, so backtests can
run on local candle files (e.g. the synthetic set from make_synthetic_data.py)
in CI or sandboxes. Not used for real research - real backtests go through
`make backtest`, which talks to the exchange's public API normally.

usage: offline_freqtrade.py backtesting --config ... --datadir ... --strategy ...
"""
import sys

from freqtrade.exchange import exchange as ft_exchange


def _market(base: str, quote: str = "USDT") -> dict:
    return {
        "id": f"{base}{quote}", "symbol": f"{base}/{quote}", "base": base, "quote": quote,
        "baseId": base, "quoteId": quote, "settle": None, "settleId": None,
        "type": "spot", "spot": True, "margin": False, "swap": False, "future": False,
        "option": False, "active": True, "contract": False, "linear": None, "inverse": None,
        "contractSize": None, "taker": 0.001, "maker": 0.001,
        "precision": {"amount": 1e-5, "price": 0.01},
        "limits": {"amount": {"min": 1e-5, "max": 9000}, "price": {"min": 0.01, "max": 1e7},
                   "cost": {"min": 5, "max": 9e6}, "leverage": {"min": None, "max": None}},
        "info": {},
    }


MARKETS = {m["symbol"]: m for m in (_market(b) for b in ("BTC", "ETH", "SOL"))}


async def _offline_reload(self, reload: bool = False) -> None:
    self._api_async.set_markets(MARKETS)


ft_exchange.Exchange._api_reload_markets = _offline_reload
ft_exchange.Exchange.fetch_trading_fees = lambda self: {}

if __name__ == "__main__":
    from freqtrade.main import main

    main(sys.argv[1:])
