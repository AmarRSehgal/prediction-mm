# Morning report (auto-updated overnight)

**Last updated:** initializing...

_This file is overwritten by the autonomous runner every check-in. If you see this text unchanged, something went wrong — see `logs/overnight_wrapper.log` and `logs/overnight_trader.log`._

## Quick glance

- Paper trader status: launching...
- Tracking started at: 2026-04-19T02:01 UTC
- Configured duration: 10 hours
- Target subsectors: KBO / NPB / PSL cricket
- Capital: $100 (paper)

## How to inspect after waking

```bash
cd ~/personal/prediction-mm
tail -100 logs/overnight_trader.log
cat research/data/trader_state/portfolio_paper.json | python3 -m json.tool | head -40
cat research/data/trader_state/pnl_timeseries.csv | tail -20
```

## How to stop everything

```bash
pkill -f overnight_runner.sh
pkill -f run_trader.py
pkill -f pnl_tracker.py
```
