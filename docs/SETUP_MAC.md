# Running Trading Lab on a Mac

Works on Apple silicon and Intel Macs (the Freqtrade image is multi-arch).

## 1. Docker Desktop

```bash
docker --version
docker compose version
```

If either fails, install Docker Desktop from https://www.docker.com/products/docker-desktop/
and open it once so the engine is running (whale icon in the menu bar).
Recommended in Docker Desktop → Settings → Resources: 4 CPUs, 4 GB memory.

## 2. Get the repo

Clone it (once it is on GitHub) or copy the `trading-lab` folder, then:

```bash
cd trading-lab
make check
```

You should see `Safety check passed: dry-run, spot, no keys, no leverage, no shorts, stops within limit.`

`make` ships with the Xcode command line tools. If it is missing: `xcode-select --install`.

## 3. Historical data and first backtest

```bash
make pull         # ~1 GB image, first time only
make download     # 2 years of 1h candles for BTC, ETH, SOL (public data, no account)
make backtest     # prints a STRATEGY SUMMARY table; compare every slot with BuyAndHoldBenchmark
```

Change the window with `make backtest TIMERANGE=20240101-20250101` or
download more history with `make download DAYS=1095`.

Results are saved in `user_data/backtest_results/`.

If `make download` fails with a connection or "restricted location" error, Binance's
public API is not reachable from your network. Switch `exchange.name` in
`user_data/config/base.json` to another exchange Freqtrade supports for spot data
(for example `okx` or `bybit`) and run it again. This only affects where public
candles come from; no account is used.

## 4. Paper trading

```bash
make up       # starts 7 bots, each with a virtual 266.67 USDT (SAR 1,000)
make status   # all 7 should be "running"
make logs     # follow what they do (Ctrl+C to stop following)
make down     # stop everything
```

Each bot keeps its trades in `user_data/db/<bot>.sqlite` and logs in `user_data/logs/`.
Bots only run while the Mac is awake and Docker is open. A VPS for 24/7 running is a later step.

If a bot hits the 5% drawdown halt, it closes its positions and stops trading. A file appears
in `user_data/risk_state/`. Review what happened before deleting it; deleting it resumes trading.
