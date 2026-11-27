# Trading Lab — Phase 1

Paper-trading research platform built on [Freqtrade](https://www.freqtrade.io).
Mission: turn a **simulated** SAR 1,000 into SAR 1,100 within strict risk limits,
then find out whether the result repeats.

**No real money. No exchange API keys. Spot only. No leverage. No shorts.**

## What is here

| Path | What it does |
| --- | --- |
| `Makefile` | Every command (`make help`). Local virtualenv by default, `docker-*` targets for a server later |
| `requirements.txt` | Pinned `freqtrade==2026.10`, same version as the Docker image |
| `user_data/config/base.json` | Shared config: `dry_run: true`, Binance public data, BTC/ETH/SOL vs USDT, 266.67 USDT (= SAR 1,000) per bot, max 3 open trades |
| `user_data/config/bots/*.json` | One file per bot: name, strategy, its own trade database |
| `user_data/config/local/` | Per-machine dashboard logins, created by `make setup`, never committed |
| `user_data/strategies/lab_risk.py` | **Hard risk limits in code** (see below) |
| `user_data/strategies/*V1.py` | Strategy slots 01–06 |
| `user_data/strategies/BuyAndHoldBenchmark.py` | Equal-weight buy-and-hold yardstick |
| `scripts/safety_check.py` | Safety gate run before every command and container start |
| `scripts/paper.sh` | Start / stop / status for the 7 local paper bots |
| `scripts/scorecard.py` | SAR scorecard and pass/fail gate for backtests and paper trading |
| `scripts/setup_local.py` | Creates the local dashboard settings and login |
| `scripts/make_synthetic_data.py` | Fake candles for testing the plumbing only |
| `tests/` | Offline test suite: safety gate, risk unit tests, sizing, lookahead bias, 5% halt |
| `.github/workflows/checks.yml` | Runs the full test suite on every push and pull request |
| `docker-compose.yml` | Same 7 bots on the pinned Docker image, for an always-on server later |
| `docs/` | Mac setup, risk policy, exchange eligibility, Phase 1 audit |

## Strategy slots

| Slot | Strategy | Idea | Per-trade stop |
| --- | --- | --- | --- |
| 01 | `TrendFollowingV1` | EMA20/50 cross above EMA200 with ADX > 20, trailing stop | 4% |
| 02 | `MeanReversionV1` | Close under lower Bollinger band with RSI < 30, exit at the mid band | 4% |
| 03 | `MomentumV1` | Rising positive MACD histogram, ROC > 1%, RSI 55–75 | 3.5% |
| 04 | `BreakoutV1` | Close above the 20-candle Donchian high on 1.5× volume | 4% |
| 05 | `VolumeAnalysisV1` | Chaikin money flow crosses 0.10 with OBV above its average | 4% |
| 06 | `MachineLearningV1` | **Placeholder**, never trades. FreqAI model comes in Phase 2 | – |
| – | `BuyAndHoldBenchmark` | Buy BTC/ETH/SOL equally on the first candle, hold | none |

All are simple, textbook starting points on 1h candles. They are slots to be
replaced and compared in Phase 2, not recommendations.

## Risk limits (enforced in code)

Every strategy except the benchmark inherits `RiskGuardedStrategy`:

1. **Spot, long only, 1× leverage.** `can_short = False`; `leverage()` always returns 1; the bot refuses to start in any other trading mode.
2. **Per-trade stoploss no looser than 5%.** Checked at start-up and by the safety gate.
3. **1% risk per trade.** Each trade is sized so that hitting its stoploss (plus 0.3% fees) costs about 1% of current equity, capped at the normal one-third split.
4. **Hard 5% drawdown halt for paper and live bots.** Equity is marked to market every candle. At 5% below peak equity every open trade is exited (`risk_halt_max_drawdown`) and the bot stays halted. Peak equity is saved to `user_data/risk_state/<bot>.state.json`, so a restart can never reset the drawdown. The halt is written to `user_data/risk_state/<bot>.halted.json` and survives restarts; only a human deleting that file resumes trading. Paper bots mark equity to the live price every 30 seconds.
5. **Backtests measure the 5% line instead of enforcing it**, so each strategy is judged over the full period. Every time a strategy crosses it, the time is logged and saved to `user_data/backtest_results/risk_breaches_<Strategy>.json`. A strategy with breaches would have been halted in paper trading at the first one.

The safety gate (`scripts/safety_check.py`) also refuses to start if `dry_run` is not true, any API key/secret is set, `trading_mode` is not spot, any leverage setting exists, or any `FREQTRADE__*` environment override is present.

Limits of the guarantee: the halt acts on the next candle, so a fast move or price gap can overshoot the 5% line before positions are closed.

Changing any number in `lab_risk.py` is a risk-limit modification and needs human approval (`docs/RISK_POLICY.md`).

## Quick start (Mac, no Docker needed)

See `docs/SETUP_MAC.md`. In short:

```bash
make setup            # .venv with pinned Freqtrade + dashboard UI + local logins
make download         # ~2 years of 1h BTC/ETH/SOL candles (public data, no account)
make test             # offline test suite
make analyze          # lookahead-bias + recursive-indicator checks on real data
make backtest         # all slots + benchmark, then the SAR scorecard
make paper-start      # 7 paper bots; dashboards on http://127.0.0.1:8081-8087
make paper-status     # running / stopped / HALTED
make paper-scorecard  # progress towards SAR 1,100
make paper-stop
```

## The gate

`scripts/scorecard.py` decides whether a strategy has earned a place in the next phase.
It must end at or above SAR 1,100, never cross the 5% drawdown line, beat buy-and-hold,
make at least 30 trades and have a p-value under 0.05. On the first real backtest
(Jan 2025 to Nov 2026) **no strategy passes**, which is the honest starting point for Phase 2.

## Status

See `docs/PHASE1_AUDIT.md`.
- Exchange eligibility in Saudi Arabia: **unverified**, see `docs/EXCHANGE_ELIGIBILITY.md`. Public market data needs no account; live trading does.
