# Phase 1 audit

Phase 1 goal: working trading infrastructure, real market data and a simulated
account, with the risk rules enforced in code. Strategy quality is Phase 2.

Verified on 2026-11-27 in the cloud sandbox (synthetic data, CI) and end to end on
the Mac (real Binance data, Freqtrade 2026.10, Python 3.14).

| Area | Status | Evidence |
| --- | --- | --- |
| Engine | Freqtrade 2026.10 pinned (`requirements.txt` and Docker image) | `make setup`, CI |
| Mac setup | One command, no Docker needed, picks Python 3.12+ automatically | `make setup` on the Mac |
| Market data | BTC/ETH/SOL-USDT 1h, 2024-11-27 to 2026-11-27, 17,532 candles per pair, no gaps reported | `make data-check` |
| Simulated account | 7 dry-run bots, 266.67 USDT (= SAR 1,000) each, own database each | 4-minute paper smoke test: all running, heartbeats every minute, no errors |
| Safety gate | Refuses dry_run off, API keys, futures, env overrides, public dashboards | `make test` (5 refusal cases) |
| Risk engine | 1% risk per trade; 5% hard halt in paper/live, latched; peak equity persisted across restarts; corrupt state blocks trading | 4 unit tests, sizing check (max 1.01%), halt probe |
| Backtest honesty | No lookahead bias in any strategy; startup candles raised so indicators are stable; OBV level bug fixed | `make analyze` |
| Measurement | SAR scorecard with a pass/fail gate (≥1,100, no 5% breach, beats benchmark, ≥30 trades, p < 0.05) for backtests and paper bots | `make backtest`, `make paper-scorecard` |
| Monitoring | FreqUI dashboard per bot on 127.0.0.1:8081-8087, generated logins never committed | 7/7 dashboards answered |
| Version control and CI | GitHub repo, every push and PR runs the full offline suite | GitHub Actions `checks` |
| Docs | README, Mac setup, risk policy with change log, exchange eligibility note | `docs/` |

## Known limits (by design, not defects)

- **No strategy passes the gate yet.** All five lose after fees over Jan 2025 to Nov 2026, and all cross the 5% line in their first month. That is the Phase 2 starting point.
- **Machine learning slot is a placeholder** and never trades until Phase 2 adds a FreqAI model.
- **Paper bots run only while the Mac is awake.** A VPS for 24/7 running comes later; `docker-*` targets are ready for it.
- **The 5% halt acts on the next check** (30 s in paper/live, next candle in backtests), so a fast move can overshoot it slightly.
- **Exchange eligibility in Saudi Arabia is unverified.** Phase 1 needs no account.
- **No phone alerts yet** (Telegram is wired in Freqtrade but disabled; needs a bot token from you).
