# Trading Lab Phase 1. All targets are paper / historical only.
COMPOSE   = docker compose
RUN       = $(COMPOSE) run --rm tools
GATE      = python /freqtrade/scripts/safety_check.py &&
CFG       = --config /freqtrade/user_data/config/base.json
TIMERANGE ?= 20250101-
DAYS      ?= 730
STRATS    = TrendFollowingV1 MeanReversionV1 MomentumV1 BreakoutV1 VolumeAnalysisV1 MachineLearningV1 BuyAndHoldBenchmark

.PHONY: check pull download backtest up down status logs report

check:            ## run the safety gate locally (needs only python3)
	python3 scripts/safety_check.py

pull:             ## fetch the pinned Freqtrade image
	$(COMPOSE) pull tools

download: check   ## download ~2 years of 1h candles for BTC/ETH/SOL (public data)
	$(RUN) "$(GATE) freqtrade download-data $(CFG) --timeframes 1h --days $(DAYS)"

backtest: check   ## backtest every slot + benchmark on the same data
	$(RUN) "$(GATE) freqtrade backtesting $(CFG) --strategy-list $(STRATS) --timerange $(TIMERANGE) --export trades --breakdown month"

up: check         ## start all 7 paper-trading bots
	mkdir -p user_data/db user_data/logs
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

status:
	$(COMPOSE) ps

logs:
	$(COMPOSE) logs -f --tail 50
