# From the course to code — من الدورة إلى الكود

This lab exists to test one method: **candles and volume (الشموع والكميات)** as taught in the
Telegram channel **«الملخص ٩»** and practised in the group **«احتراف المضاربات اللحظية ٩»**.

- **The rules** (what the course says, with message references): [`CANDLES_VOLUME_RULES.md`](CANDLES_VOLUME_RULES.md)
- **This file**: which of those rules are coded, in which strategy, and what is still missing.

The method in one line: *find a market-maker zone on the higher timeframe (daily/weekly), wait for
price to come back into it, enter only on a bullish intraday pattern (15 m / 5 m, or 1 h if you can't
watch the screen) inside the zone, with a stop of at most 3 %.*

## Strategies

| Strategy | Status | What it covers |
| --- | --- | --- |
| `CandlesVolumeCourseV1` | **Being written** (in the "Find a strategy that passes the scorecard" work, not committed yet) | Daily demand zones, 15 m entries inside the zone, stop ≤ 3 %, previous top as target. Early results: 1,047 SAR on 2021-24, 969 SAR on 2025-26 (does not pass). |
| `CandleVolumeV1` | In the repo, paper bot `course_candle_volume` | A **rough first proxy**, written before the rules were extracted: TA-Lib reversal candles (hammer, engulfing, morning star, piercing) on ≥ 2× average volume at a fresh 10-candle low, in a daily uptrend. Exit +6 % / 4 % stop / 3 days. 1,012 SAR on 2025-26, 29 trades: no edge. |
| `BuyAndHoldBenchmark` | Kept | The yardstick every course strategy must beat. |

When a new course strategy lands: put it in `user_data/strategies/`, inherit `RiskGuardedStrategy`,
add it to `COURSE_STRATS` in the `Makefile` and `tests/run_checks.sh`, add a `course_*.json` bot
config, and update the coverage table below.

## Rule coverage

Section numbers refer to `CANDLES_VOLUME_RULES.md`. ✓ coded · ◐ partly / approximated · ✗ not yet · — not applicable to crypto.

| Rule | Section | `CandleVolumeV1` | Notes |
| --- | --- | --- | --- |
| Change % is close-to-close, not open-to-close | 1 | ✗ | uses TA-Lib shapes instead |
| Buying candle ≥ +1 % (15 m) / +3 % (1 h, 1 d) / +10 % (1 w) | 1.1 P1 | ✗ | |
| Bullish engulfing (ideal and non-ideal) | 1.1 P3, 3.1 #7 | ◐ | TA-Lib `CDLENGULFING`, not the course's wick rules |
| Volume candle = highest volume vs the candles before it | 4 | ◐ | approximated as ≥ 2× the 20-candle average |
| Close above a volume candle | 1.1 P4, 3.1 #4, 4 | ✗ | the volume-candle entry the teacher uses most |
| Close above a selling candle / price trap | 2.1a #6, 3.1 #3, 8.1 | ✗ | |
| Higher-TF zones: the 7 buyer zones (uptrend, prior low, volume candle, buying candle, broken high, broken selling candle, Fib 50/61.8) | 2.1a | ◐ | only zone 1 (uptrend), as daily close > SMA50 > SMA200 |
| Zone drawing and grading (2× exit, fresh, < 6 candles) | 2.3, 2.4 | ✗ | |
| Two timeframes: zone on HTF, pattern on LTF | 3 | ◐ | daily regime + 1 h pattern |
| The 12 intraday buy patterns | 3.1 | ◐ | only engulfing (and hammer ≈ pin bar) |
| False break, fakey, failed bearish engulfing, broken-then-recovered buying candle | 3.1 #2, #8, #10, #11 | ✗ | |
| Positive RSI divergence (quality filter) | 3.1 #12, 8.1 | ✗ | |
| **Stop ≤ 3 %** | 3, 5 | ✗ | uses a 4 % stop: **breaks the course rule** |
| Stop on a 15 m **close** below the pattern low, not a wick | 6, 8.2 | ✗ | Freqtrade stops on price touch by default |
| Trail the stop under each new bullish pattern / volume candle | 8.2, 8.4 | ✗ | |
| Exit on a bearish engulfing at the highs, or a shooting star + close below | 8.1 | ✗ | |
| Target: next HTF supply zone / previous top; take 1-3 % if resistance is near | 5, 8.2 | ✗ | fixed +6 % instead |
| Mod's momentum-pullback strategy (≥ 12 % rise in 3-7 candles, volume > MA50, M-shaped pullback) | 8.3 | ✗ | a separate strategy candidate |
| Ignore closing-auction volume bars | 8.1 | — | crypto trades 24/7, no auction |
| Market filter: TASI not negative | 8.2 | — | no TASI; BTC's own trend could stand in |
| Avoid 10:00-15:00 distractions (Saudi session) | 3 | — | |

## How the lab differs from the course

- **Market.** Every example in the course is a **Saudi stock (Tadawul)** on TickerChart. The lab
  tests on **crypto (BTC/ETH/SOL vs USDT)** because that history is free and public. The teacher
  says candles and volume "work in every market and every timeframe" (`g#25221`), but that is the
  claim being tested, not a given.
- **Risk.** The lab's own limits apply on top of the course's 3 % stop: 1 % of equity risked per
  trade, and a hard halt at 5 % below peak equity (`RISK_POLICY.md`). Those numbers only change
  with a human decision.
- **Honesty rules for testing.** Design on 2021-2024 (`make course-insample`). The 2025-2026
  window is the scorecard test and is used once per frozen version; tuning on it is overfitting.
  A strategy passes only if `scripts/scorecard.py` says so: SAR 1,100 or more, never 5 % below
  peak, beats buy-and-hold, 30+ trades, p < 0.05.
