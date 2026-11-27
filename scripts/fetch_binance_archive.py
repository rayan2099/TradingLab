#!/usr/bin/env python3
"""
Download BTC/ETH/SOL-USDT 1h candles from Binance's public archive
(data.binance.vision: free, no account, no API keys) and write them in
Freqtrade's feather format, plus 4h and 1d candles resampled from them.

Used where the exchange API is unreachable (e.g. the cloud sandbox) and for
long histories. Same candles as `make download`, which uses the live API.

usage: fetch_binance_archive.py [--start 2020-01] [--datadir user_data/data/binance]
"""
from __future__ import annotations

import argparse
import io
import time
import urllib.error
import urllib.request
import zipfile
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

BASE = "https://data.binance.vision/data/spot"
PAIRS = {"BTCUSDT": "BTC_USDT", "ETHUSDT": "ETH_USDT", "SOLUSDT": "SOL_USDT"}
COLS = ["ts", "open", "high", "low", "close", "volume"]


def fetch(url: str, attempts: int = 4) -> pd.DataFrame | None:
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                raw = resp.read()
            break
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None  # not listed yet / not published yet
            raise
        except (urllib.error.URLError, ConnectionError, TimeoutError):
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        df = pd.read_csv(z.open(z.namelist()[0]), header=None)
    if not str(df.iloc[0, 0]).isdigit():  # some files carry a header row
        df = df.iloc[1:]
    df = df.iloc[:, :6].astype(float)
    df.columns = COLS
    ts = df["ts"].astype("int64")
    ts = ts.where(ts < 1e14, ts // 1000)  # files from 2025 on use microseconds
    df["date"] = pd.to_datetime(ts, unit="ms", utc=True)
    return df[["date", *COLS[1:]]]


def months(start: str, today: date):
    y, m = map(int, start.split("-"))
    while (y, m) < (today.year, today.month):
        yield f"{y}-{m:02d}"
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2020-01")
    ap.add_argument("--datadir", default="user_data/data/binance")
    args = ap.parse_args()
    out = Path(args.datadir)
    out.mkdir(parents=True, exist_ok=True)
    today = date.today()
    for sym, pair in PAIRS.items():
        parts = [fetch(f"{BASE}/monthly/klines/{sym}/1h/{sym}-1h-{m}.zip")
                 for m in months(args.start, today)]
        day = today.replace(day=1)
        while day < today:  # current month: daily files
            parts.append(fetch(f"{BASE}/daily/klines/{sym}/1h/{sym}-1h-{day}.zip"))
            day += timedelta(days=1)
        df = (pd.concat([p for p in parts if p is not None])
              .drop_duplicates("date").sort_values("date").reset_index(drop=True))
        df.to_feather(out / f"{pair}-1h.feather")
        h = df.set_index("date")
        for tf, rule in (("4h", "4h"), ("1d", "1D")):
            r = h.resample(rule).agg({"open": "first", "high": "max", "low": "min",
                                      "close": "last", "volume": "sum"}).dropna()
            r.reset_index().to_feather(out / f"{pair}-{tf}.feather")
        print(f"{pair}: {df['date'].iloc[0]:%Y-%m-%d} to {df['date'].iloc[-1]:%Y-%m-%d %H:%M}, "
              f"{len(df)} hourly candles")


if __name__ == "__main__":
    main()
