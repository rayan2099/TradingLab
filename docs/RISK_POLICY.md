# Risk policy

| Parameter | Value | Where enforced |
| --- | --- | --- |
| Mode | Paper trading (`dry_run: true`) | `scripts/safety_check.py` (blocks start) |
| API keys | None | `scripts/safety_check.py` |
| Market | Crypto spot, BTC/ETH/SOL vs USDT | `base.json`, `lab_risk.py` |
| Leverage | 1× | `lab_risk.py` (`leverage()`), safety gate |
| Short selling | Disabled | `can_short = False`, safety gate |
| Capital per strategy | 266.67 USDT (= SAR 1,000 at 3.75 SAR/USD) | `base.json` `dry_run_wallet` |
| Profit objective | +SAR 100 net (= 293.33 USDT equity) | reporting only |
| Max drawdown | 5% from peak equity, marked to market: hard halt in paper/live, measured and reported in backtests | `lab_risk.py` |
| Risk per trade | ~1% of equity if the stop is hit | `lab_risk.py` sizing |
| Per-trade stop | no looser than 5% | `lab_risk.py`, safety gate |

## Who may change what

- **Strategy logic** (indicators, entries, exits, tighter stops): research agents may propose; changes go through backtest and review.
- **Risk limits** (any constant in `lab_risk.py`, the safety gate, `dry_run`, pairs, capital): **human approval only.**
- **Real-money deployment**: human approval only, Phase 4, after independent tests and exchange eligibility is confirmed.

No AI agent receives exchange credentials or the ability to move funds.

## Change log

- 2026-11-27: approved by rayan. Replaced drawdown-budget sizing (which froze bots near 4%) with 1% risk per trade; 5% halt kept for paper/live, measured-only in backtests.
