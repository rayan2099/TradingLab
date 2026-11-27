# Archive: generic strategies from Phases 1 and 2

These strategies are **not from the الملخص 9 course**. They were textbook starting points
(Phase 1 slots 01–06) and their uptrend-filtered variants (Phase 2). None of them passed the
scorecard; the results are kept in `docs/history/PHASE1_AUDIT.md` and
`docs/history/PHASE2_RESEARCH.md`.

They live outside `user_data/` on purpose, so Freqtrade, the paper bots, the safety gate and the
test suite no longer load them. Nothing here runs.

| File | What it was |
| --- | --- |
| `strategies/TrendFollowingV1.py` | Slot 01: EMA20/50 cross above EMA200, ADX > 20 |
| `strategies/MeanReversionV1.py` | Slot 02: lower Bollinger band + RSI < 30 |
| `strategies/MomentumV1.py` | Slot 03: MACD histogram, ROC, RSI 55–75 |
| `strategies/BreakoutV1.py` | Slot 04: 20-candle Donchian breakout on 1.5× volume |
| `strategies/VolumeAnalysisV1.py` | Slot 05: Chaikin money flow + OBV |
| `strategies/MachineLearningV1.py` | Slot 06: placeholder, never traded |
| `strategies/*R.py` | Phase 2: the five slots above with the daily uptrend filter |
| `strategies/TrendRiderV1.py` | Phase 2: 4h, 20-day breakout in an uptrend |
| `bots/slot0*.json` | Their paper-bot configs |

To re-run one for comparison, copy it (and, for an `R` variant, its `V1` parent) back into
`user_data/strategies/`, then backtest it with `--strategy`. Don't add it back to the Makefile,
the paper bots or the docs: the lab is about the course method now.
