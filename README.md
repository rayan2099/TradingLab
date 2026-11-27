# Trading Lab — الشموع والكميات (الملخص ٩)

A paper-trading lab for **one method**: the candles and volume method (الشموع والكميات) taught in
the Telegram channel **«الملخص ٩»** and practised in the group **«احتراف المضاربات اللحظية ٩»**.
The lab turns the course rules into code, backtests them honestly, and paper-trades them with a
simulated SAR 1,000, to find out whether the method makes money and whether the result repeats.

مختبر تداول ورقي لطريقة واحدة: **الشموع والكميات** كما شُرحت في قناة «الملخص ٩» وطُبّقت في مجموعة
«احتراف المضاربات اللحظية ٩». نحوّل قواعد الدورة إلى كود، ونختبرها على البيانات التاريخية بأمانة،
ثم نتداولها ورقيًا بمبلغ افتراضي ١٬٠٠٠ ريال.

**No real money. No exchange API keys. Spot only. No leverage. No shorts.**

## The method in one line — الفكرة باختصار

Find a market-maker zone on the higher timeframe (daily/weekly), wait for price to come back into
it, and enter only when a bullish intraday pattern (15 m / 5 m, or 1 h) forms inside the zone,
with a stop of at most 3 %.

حدد منطقة صناع السوق على الفاصل الأكبر، انتظر عودة السعر لها، ثم ادخل فقط عند ظهور نموذج لحظي
داعم للصعود داخل المنطقة، بوقف خسارة لا يزيد عن ٣٪.

## Start here

| Document | What it is |
| --- | --- |
| [`docs/CANDLES_VOLUME_RULES.md`](docs/CANDLES_VOLUME_RULES.md) | **The rules**, extracted from the course lessons and the practice group, with message references. Candle definitions, the 7 buyer zones, the 12 intraday patterns, volume, stops, targets, and the teacher's and Mod's answers. |
| [`docs/COURSE_TO_CODE.md`](docs/COURSE_TO_CODE.md) | Which rules are coded, in which strategy, what is still missing, and how the lab differs from the course (crypto instead of Tadawul). |
| [`docs/RISK_POLICY.md`](docs/RISK_POLICY.md) | The lab's hard risk limits and who may change them. |
| [`docs/SETUP_MAC.md`](docs/SETUP_MAC.md) | Running everything on the Mac. |

## Strategies

| Strategy | Status |
| --- | --- |
| `CandlesVolumeCourseV1` | The course method coded from the rules (daily zones, 15 m entries, stop ≤ 3 %). Being written; lands in `user_data/strategies/` when committed. |
| `CandleVolumeV1` | A rough first proxy (TA-Lib reversal candles on high volume in an uptrend). Runs as paper bot `course_candle_volume`. No edge so far. |
| `BuyAndHoldBenchmark` | Equal-weight buy-and-hold of BTC/ETH/SOL. Every course strategy must beat it. |

The generic Phase 1/2 strategies that were not from the course (trend following, mean reversion,
momentum, breakout, volume analysis, ML placeholder, TrendRider) are in [`archive/`](archive/README.md)
and no longer run.

## What is here

| Path | What it does |
| --- | --- |
| `docs/` | Course rules, rules-to-code map, risk policy, setup; `docs/history/` holds the Phase 1 audit and Phase 2 research log |
| `user_data/strategies/` | Course strategies, the benchmark, and the shared code: `lab_risk.py` (hard risk limits) and `lab_regime.py` (daily uptrend filter) |
| `user_data/config/base.json` | Shared config: `dry_run: true`, Binance public data, BTC/ETH/SOL vs USDT, 266.67 USDT (= SAR 1,000) per bot |
| `user_data/config/bots/*.json` | One file per paper bot: `course_*` plus the benchmark |
| `scripts/safety_check.py` | Safety gate run before every command and container start |
| `scripts/scorecard.py` | SAR scorecard and pass/fail gate |
| `scripts/fetch_binance_archive.py` | Years of public candles from Binance's archive (no account) |
| `scripts/paper.sh` | Start / stop / status for the local paper bots |
| `tests/` | Offline test suite: safety gate, risk unit tests, sizing, lookahead bias, uptrend filter, 5% halt |
| `archive/` | Generic strategies from earlier phases, kept for reference only |
| `Makefile` | Every command (`make help`) |

## Risk limits (enforced in code)

Every course strategy inherits `RiskGuardedStrategy` from `lab_risk.py`:

1. **Spot, long only, 1× leverage.** The course is buy-only too (Saudi market).
2. **Per-trade stop no looser than 5%** in code. The course itself asks for **≤ 3 %**, and course strategies should use that.
3. **1% of equity risked per trade.**
4. **Hard 5% drawdown halt for paper bots**, marked to market, latched across restarts. Only a human deleting the halt file resumes trading.
5. **Backtests measure the 5% line** instead of enforcing it, and log every breach.

The safety gate refuses to start if `dry_run` is not true, any API key is set, the mode is not
spot, any leverage setting exists, or any `FREQTRADE__*` override is present. Changing any risk
number needs human approval (`docs/RISK_POLICY.md`).

## Commands

```bash
make setup            # .venv with pinned Freqtrade 2026.10 + dashboard UI + local logins
make archive-data     # BTC/ETH/SOL candles since 2020 (public, no account)
make test             # offline test suite
make course-insample  # course strategies on the 2021-2024 design window
make backtest         # course strategies + benchmark on 2025 onward, then the SAR scorecard
make analyze          # lookahead-bias + recursive-indicator checks on real data
make paper-start      # course paper bots + benchmark; dashboards from http://127.0.0.1:8081
make paper-status     # running / stopped / HALTED
make paper-scorecard  # progress towards SAR 1,100
make paper-stop
```

## The gate

A course strategy has earned real attention only if `scripts/scorecard.py` passes it: SAR 1,100
or more, never 5% below peak, beats buy-and-hold, at least 30 trades, p-value under 0.05.
Design on 2021-2024; the 2025-2026 window is the test and is used once per frozen version.
**No strategy passes yet.**

## Notes

- The course trades **Saudi stocks (Tadawul)**. The lab tests the same rules on **crypto**, because
  that history is free and public. Whether the method carries over is part of what is being tested.
- Exchange eligibility in Saudi Arabia is **unverified** (`docs/EXCHANGE_ELIGIBILITY.md`). Public
  market data needs no account; live trading would.
