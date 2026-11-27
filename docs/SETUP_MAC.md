# Running Trading Lab on a Mac

Works on Apple silicon and Intel. Needs Python 3.11+ (`python3 --version`), `make`
(`xcode-select --install` if missing) and about 3 GB of free disk. Docker is optional.

## 1. Install

```bash
cd ~/Developer/trading-lab        # or wherever you cloned github.com/rayan2099/TradingLab
make setup
```

This creates `.venv` with the pinned Freqtrade, installs the FreqUI dashboard, and writes
your local dashboard login to `user_data/config/local/CREDENTIALS.txt` (never committed).

## 2. Data, checks and backtest

```bash
make download     # 2 years of 1h candles for BTC, ETH, SOL (public data, no account)
make data-check   # confirm the date range per pair
make test         # offline test suite, should end with ALL CHECKS PASSED
make analyze      # lookahead-bias and recursive-indicator checks on real data
make backtest     # STRATEGY SUMMARY + SAR scorecard (copy in user_data/reports/)
```

Change the window with `make backtest TIMERANGE=20240101-20250101`, or get more history
with `make download DAYS=1095`.

If `make download` fails with a connection or "restricted location" error, set
`exchange.name` in `user_data/config/base.json` to another spot exchange Freqtrade supports
(for example `okx`) and run it again. Only public candles are affected; no account is used.

## 3. Paper trading

```bash
make paper-start      # 7 bots, each with a virtual 266.67 USDT (SAR 1,000)
make paper-status     # running / stopped / HALTED
make paper-scorecard  # progress in SAR towards 1,100
make paper-stop
```

Dashboards: open the addresses in `CREDENTIALS.txt` (http://127.0.0.1:8081 to 8087) and log in.
They only listen on this Mac. Bots run while the Mac is awake; logs are in `user_data/logs/`.

If a bot hits the 5% drawdown halt it sells everything and stops. `make paper-status` shows
HALTED and a file appears in `user_data/risk_state/`. Review what happened before deleting
that file; deleting it resumes trading. Deleting `<bot>.state.json` resets the drawdown peak,
which is a risk-limit change and needs a human decision.

## Docker (optional, for an always-on server later)

`make docker-pull`, `make docker-download`, `make docker-backtest`, `make docker-up`,
`make docker-down`. Same configs and safety gate; no dashboards in this mode.
