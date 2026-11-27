# Trading Lab Phase 1 - paper / historical only.
#
# Two ways to run, same configs and strategies:
#   local (default) : Python virtualenv, no Docker needed  -> make setup / backtest / paper-start
#   docker          : docker compose (for a VPS later)      -> make docker-backtest / docker-up
#
# Every target runs the safety gate first.

# Freqtrade 2026.10 needs Python 3.12+; pick the newest one installed.
PY        ?= $(shell for p in python3.14 python3.13 python3.12 python3; do command -v $$p >/dev/null 2>&1 && $$p -c 'import sys; sys.exit(sys.version_info < (3, 12))' 2>/dev/null && { echo $$p; break; }; done)
VENV      := .venv
FT        := $(VENV)/bin/freqtrade
CFG       := --userdir user_data --config user_data/config/base.json
TIMERANGE ?= 20250101-
DAYS      ?= 730
STRATS    := TrendFollowingV1 MeanReversionV1 MomentumV1 BreakoutV1 VolumeAnalysisV1 MachineLearningV1 BuyAndHoldBenchmark
SIGNAL_STRATS := TrendFollowingV1 MeanReversionV1 MomentumV1 BreakoutV1 VolumeAnalysisV1

.PHONY: help check setup download data-check backtest analyze scorecard test \
        paper-start paper-stop paper-status paper-scorecard \
        docker-pull docker-download docker-backtest docker-up docker-down docker-logs

help:            ## list targets
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*##/ -/'

check:           ## safety gate: dry-run, no keys, spot, no leverage/shorts, stops within limit
	python3 scripts/safety_check.py

setup: check     ## create .venv with the pinned Freqtrade, FreqUI and local dashboard logins
	@test -n "$(PY)" || { echo "Python 3.12+ is required (brew install python@3.13)"; exit 1; }
	$(PY) -m venv $(VENV)
	$(VENV)/bin/pip install -q --upgrade pip
	$(VENV)/bin/pip install -q -r requirements.txt
	$(FT) install-ui
	$(VENV)/bin/python scripts/setup_local.py

download: check  ## download 1h candles for BTC/ETH/SOL (public data, no account)
	$(FT) download-data $(CFG) --timeframes 1h --days $(DAYS)

data-check:      ## show the downloaded date range per pair
	$(FT) list-data $(CFG) --show-timerange

backtest: check  ## backtest all slots + benchmark, then print the SAR scorecard
	rm -f user_data/backtest_results/risk_breaches_*.json
	$(FT) backtesting $(CFG) --strategy-list $(STRATS) --timerange $(TIMERANGE) --export trades --breakdown month
	$(VENV)/bin/python scripts/scorecard.py bind
	$(VENV)/bin/python scripts/scorecard.py backtest

analyze: check   ## lookahead-bias and recursive-indicator checks for every signal strategy
	$(FT) lookahead-analysis $(CFG) --strategy-list $(SIGNAL_STRATS) --timerange $(TIMERANGE)
	for s in $(SIGNAL_STRATS); do $(FT) recursive-analysis $(CFG) --strategy $$s --timerange $(TIMERANGE) || exit 1; done

scorecard:       ## scorecard for the latest backtest
	$(VENV)/bin/python scripts/scorecard.py backtest

test:            ## offline test suite (synthetic data, no network)
	PYTHON=$(VENV)/bin/python bash tests/run_checks.sh

paper-start: check  ## start the 7 paper bots locally (dashboards on 127.0.0.1:8081-8087)
	bash scripts/paper.sh start

paper-stop:      ## stop the local paper bots
	bash scripts/paper.sh stop

paper-status:    ## are the paper bots alive?
	bash scripts/paper.sh status

paper-scorecard: ## SAR scorecard from the paper bots' trade databases
	$(VENV)/bin/python scripts/scorecard.py paper

# ---- Docker (same configs; for an always-on server later) -------------------
docker-pull:
	docker compose pull tools

docker-download: check
	docker compose run --rm tools "python /freqtrade/scripts/safety_check.py && freqtrade download-data --config /freqtrade/user_data/config/base.json --timeframes 1h --days $(DAYS)"

docker-backtest: check
	rm -f user_data/backtest_results/risk_breaches_*.json
	docker compose run --rm tools "python /freqtrade/scripts/safety_check.py && freqtrade backtesting --config /freqtrade/user_data/config/base.json --strategy-list $(STRATS) --timerange $(TIMERANGE) --export trades --breakdown month"
	python3 scripts/scorecard.py bind
	python3 scripts/scorecard.py backtest

docker-up: check
	mkdir -p user_data/db user_data/logs
	docker compose up -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f --tail 50
