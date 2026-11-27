# Phase 2 research log: can any strategy pass the scorecard?

**Answer so far: no.** No strategy passes the gate on the scorecard period
(1 Jan 2025 to 26 Nov 2026). The uptrend filter cut losses in all five
existing slots, and a new strategy, TrendRider, made a small profit with very low
drawdown. Neither result reaches SAR 1,100, and neither has enough trades to
show statistically that the edge is real.

## Method (set before testing)

- **Data**: Binance spot 1h candles for BTC/ETH/SOL-USDT, Jan 2020 to 26 Nov 2026,
  taken from Binance's public archive (`make archive-data`). The candles are the same
  ones `make download` gets. This setup reproduces the Phase 1 Mac result
  (BreakoutV1 907 SAR, VolumeAnalysisV1 667 SAR, buy and hold 508 SAR).
- **Design window**: 2021-2024. It includes the 2021 bull market, the 2022 crash,
  the 2023 recovery and the 2024 bull market. Every design choice used this window only.
- **Test window**: 2025-01-01 to 2026-11-26, the scorecard period. Strategies were frozen
  first, and each frozen candidate was run on this window once. Everything was then
  committed as it stood, with no further changes after seeing the results.
- **No optimiser.** I did not use hyperopt. Parameters are textbook values
  (50/200-day averages, 20-day breakout, 5-day exit). A small set of variants was
  compared by hand, and all of them are listed below, because picking the best of
  many variants is itself a form of overfitting.
- **Costs**: 0.1% fee per side (Binance's lowest tier), the lab's 1%-per-trade risk
  sizing, a 5% stop, and at most 3 open trades. Risk constants are unchanged.
- **Drawdown**: the lab's mark-to-market 5% line, checked independently with
  `scripts/mtm_drawdown.py` (equity rebuilt hourly from the trade list).
- **Lookahead**: Freqtrade `lookahead-analysis` reports no bias for any new strategy.
  This now runs in `make test`/CI.

## Idea 1: "only buy in an uptrend" on the five existing slots

`lab_regime.py`: the uptrend is on when the pair's last completed daily close is above
its 50-day average and the 50-day average is above the 200-day average. The value for
a day is only used from the next day on. The `*R` strategies are the V1 strategies
unchanged, except that new entries are blocked outside an uptrend.

| Slot | V1, test window | **R, test window** | R, design window 2021-24 |
|---|---:|---:|---:|
| Breakout | 907 SAR, DD 21% | **1,044 SAR**, DD 7.5% (8.9% marked to market) | 1,354 |
| Trend following | 814, DD 19% | **910**, DD 9.0% | 935 |
| Volume analysis | 667, DD 35% | **920**, DD 8.2% | 985 |
| Momentum | 503, DD 53% | **919**, DD 11.8% | 844 |
| Mean reversion | 739, DD 26% | **888**, DD 11.5% | 857 |
| Buy and hold | 508, DD 49% | 508 | 6,926 |

The filter does what it should and keeps the bots out of the 2022 and 2025-26 sell-offs.
Underneath it, though, four of the five 1h signals lose money even in good years. They
trade too often (130 to 1,100 trades), and with stakes of about 23% of equity, the
0.2% round-trip fee costs about 0.05% of equity per trade.

## Idea 2: TrendRider (new, `TrendRiderV1`, 4h candles)

Fewer and larger trades. It enters on a 20-day breakout while the uptrend is on. It exits
on a 5-day low, when the uptrend ends, or at the 5% stop. It uses half of the lab's 1%
risk budget per trade.

| Window | End SAR | Trades | Win % | PF | p | Max DD (closed / marked to market) |
|---|---:|---:|---:|---:|---:|---|
| 2021 | 1,304 | 27 | 44% | 4.6 | 0.04 | 2.2% / **7.3%** |
| 2022 | 1,000 | 0 | – | – | – | 0% (stood aside all year) |
| 2023 | 1,022 | 23 | 26% | 1.3 | 0.70 | 3.9% / 4.4% |
| 2024 | 1,087 | 24 | 33% | 2.2 | 0.26 | 3.0% / 4.7% |
| 2021-2024 continuous | 1,431 | 74 | 38% | 2.6 | 0.023 | 4.0% / **8.9%** |
| **Test: 2025-01 to 2026-11** | **1,013** | **15** | 47% | 1.4 | 0.72 | 2.1% / **3.9%, never crossed** |

On the test window it stays safe, but it has almost nothing to trade. BTC, ETH and SOL
were in a 50/200 uptrend for only a few months of 2025.

## Every variant tried (design window only, unless marked)

| # | Variant | 2021-24 result | Kept? |
|---|---|---|---|
| 1-5 | V1 slot + uptrend filter (the `*R` strategies) | see table above | kept for comparison |
| 6 | DipBuyer: RSI(2) < 10 pullback in an uptrend, 4h, exit above SMA5 | 733 SAR, PF 0.81 | dropped |
| 7 | TrendRider, full risk, 10-day-low exit | 2,609 SAR, DD 11.5% | dropped (drawdown) |
| 8 | ... 5-day-low exit | per year: +667 / 0 / +41 / +174 | dropped (drawdown) |
| 9 | ... chandelier (3×ATR) exit | per year: +369 / 0 / -22 / +82 | dropped |
| 10 | half risk, 10-day-low exit | 1,669, marked-to-market DD over 5% | dropped |
| **11** | **half risk, 5-day-low exit = TrendRiderV1** | 1,431, 74 trades, p 0.023 | **candidate** |
| 12 | half risk, chandelier exit | per year: +174 / 0 / -10 / +42 | dropped |
| 13 | half risk, 10-day breakout | 1,445, 88 trades, p 0.029 | candidate |
| 14 | #13 + 12% take-profit | 1,134, p 0.22 | dropped |
| 15 | #11 at 40% risk | 1,336, marked-to-market DD 7.3% | candidate |
| 16 | #11 + profit lock (trail 10% after +10%) | 1,090, p 0.38 | dropped |

On the test window, candidates 10, 11, 13 and 15 scored 991, 1,013, 997 and 1,010 SAR,
on 15 to 25 trades each. None passes. Only #11 is kept in the repo.

## Idea 3: candles + volume (`CandleVolumeV1`, requested 2026-11-27)

Bullish reversal candles (hammer, bullish engulfing, morning star, piercing line), on
volume of at least 2x the 20-candle average, at a fresh 10-candle low, during an uptrend.
Exit at +6%, at the 4% stop, or after 3 days. All rules were fixed before testing.

| Version | 2021-24 | Test window 2025-26 |
|---|---|---|
| 1h, uptrend filter (kept) | 1,038 SAR, 81 trades, PF 1.09, DD 12.5% | 1,012 SAR, 29 trades, marked-to-market DD 6.0% |
| 1h, no filter | 835, 270 trades | 981, DD 15.9% |
| 4h, uptrend filter | 998, 13 trades | 1,006, 8 trades, DD 2.3% |
| 4h, no filter | 1,096, 46 trades, DD 5.6% | 987, DD 8.6% |

None of these shows an edge (PF close to 1 everywhere). Rules taken from your own
material can be tested the same way.

## Why the gate is so hard as it is set up now

To pass, a strategy needs all of the following at once over 23 months, long-only,
trading only BTC/ETH/SOL:

1. **+10% while a falling market lost 49%.** Long-only spot can only earn in the
   up-legs, and there were few of them.
2. **Never 5% below peak, marked to market.** Even at 0.5% risk per trade, a trend
   system gives back open profit on its winners. On 2021-24, TrendRider's worst
   point was 8.9% below peak.
3. **30+ trades with p < 0.05.** The strategies that trade often enough lose to fees
   on 1h candles. The strategies that beat fees trade only 15-25 times in this
   window, and with winners that vary that much, the t-test needs well over 50 trades.

Points 2 and 3 pull against each other. I don't think more tuning on these three coins
will fix that without fitting the strategy to the past. Real options:

- **Paper-trade TrendRiderV1 (and BreakoutR) forward.** New, unseen data is the only
  clean test left now that the test window has been used once. The bot config needs
  `"timeframe": "4h"` for TrendRider.
- **More pairs** (for example the 10 most liquid USDT pairs). This gives more independent
  trades for the significance test and more up-legs to trade. It changes a risk-policy
  item, so it needs your approval.
- **Judge the gate over a full cycle** (for example 2021 to 2026, with the 5% line per
  calendar year) instead of a single 23-month window that happens to be a bear market.
  This is your decision.
- **Machine-learning slot (FreqAI)**: still a placeholder. This would be the next build.
- **Community strategies** (for example freqtrade/freqtrade-strategies) can be dropped in
  and run through `make phase2`. This session can only reach this repository on GitHub,
  so I have not imported any of them yet.

## Reproduce

```bash
make archive-data      # ~10 MB, Binance public archive, no account
make phase2            # test window: *R strategies + TrendRiderV1, scorecards, drawdown checks
make phase2-insample   # the same on 2021-2024
```

Where the exchange API is unreachable (the cloud sandbox), add
`FTRUN=".venv/bin/python tests/offline_freqtrade.py"`.
