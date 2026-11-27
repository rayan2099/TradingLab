#!/usr/bin/env bash
# Run the 7 paper (dry-run) bots locally with the project virtualenv.
# usage: scripts/paper.sh start|stop|status
set -euo pipefail
cd "$(dirname "$0")/.."
FT=.venv/bin/freqtrade
RUN=user_data/run
mkdir -p "$RUN" user_data/logs user_data/db

bots() { for f in user_data/config/bots/*.json; do basename "$f" .json; done; }
alive() { [ -f "$RUN/$1.pid" ] && kill -0 "$(cat "$RUN/$1.pid")" 2>/dev/null; }

case "${1:-status}" in
  start)
    python3 scripts/safety_check.py
    [ -x "$FT" ] || { echo "Run 'make setup' first."; exit 1; }
    for b in $(bots); do
      [ -f "user_data/config/local/$b.json" ] || { echo "Run 'make setup' first (missing local config for $b)."; exit 1; }
      if alive "$b"; then echo "$b already running"; continue; fi
      nohup "$FT" trade --userdir user_data \
        --config user_data/config/base.json \
        --config "user_data/config/bots/$b.json" \
        --config "user_data/config/local/$b.json" \
        --logfile "user_data/logs/$b.log" > "$RUN/$b.out" 2>&1 &
      echo $! > "$RUN/$b.pid"
      echo "started $b (pid $!)"
    done
    echo "Dashboards and login: user_data/config/local/CREDENTIALS.txt"
    ;;
  stop)
    for b in $(bots); do
      if alive "$b"; then kill "$(cat "$RUN/$b.pid")" && echo "stopped $b"; fi
      rm -f "$RUN/$b.pid"
    done
    ;;
  status)
    for b in $(bots); do
      if alive "$b"; then state=running; else state=stopped; fi
      halt=""; [ -f "user_data/risk_state/$b.halted.json" ] && halt="  HALTED (5% drawdown) - see user_data/risk_state/"
      printf "%-28s %s%s\n" "$b" "$state" "$halt"
    done
    ;;
  *) echo "usage: $0 start|stop|status"; exit 2 ;;
esac
