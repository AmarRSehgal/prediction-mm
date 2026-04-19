# Sunday paper test — live status

**Last updated:** 2026-04-19T19:00 UTC (~minutes into Sunday test)

## Experiment setup

- **Mode:** paper / Tier-2 (virtual orders matched against real Kalshi trades)
- **Capital:** $1,000 nominal (per-market cap is the binding constraint)
- **Per-market cap:** $5
- **Subsectors targeted:** 36 (sports niches, commodities, economics, entertainment, politics, companies, tech, geopolitics)
- **Per-subsector tuning:** custom gamma (10-35) and max_markets (15-40) and UTC-hour blackouts per subsector — see `src/pmm/trader/subsector_tuning.py`
- **Active series in universe:** ~399 (filtered from 1971 by sector_scan known-open-markets)
- **Duration:** 24h wrapper, auto-restart on any crash
- **Overnight test archived:** `portfolio_paper_overnight_20260419_1853.json` and `pnl_timeseries_overnight_20260419_1853.csv`

## Per-subsector gamma overrides

| Subsector | gamma | why |
|---|---:|---|
| baseball_kbo, npb | 10 | lowest toxicity, wide spreads; quote tighter for more fills |
| cricket_psl, tennis_challenger | 12 | low toxicity |
| baseball_us, cricket_ipl, soccer_mls, golf, esports_valorant/cs2 | 20 | default |
| cricket_t20_misc, basketball_cba/acb, golf, esports_dota | 18 | moderate |
| combat (UFC) | 35 | high abs-move toxicity; wide safe quotes |
| eco_jobs, eco_fed | 30 | scheduled release blowouts |
| eco_cpi, ppi, gdp | 22-25 | smaller releases but still dangerous |

## UTC-hour blackouts (active per subsector)

| Subsector | Blackout hours UTC | Reason |
|---|---|---|
| comm_energy | 13, 14, 20 | US open, EIA 14:30 Wed, close hour |
| comm_gold | 13, 14, 18, 19, 20 | data releases, FOMC, close |
| comm_precious_other | 13, 14, 20 | mirror gold |
| comm_metals_industrial | 1, 2, 13, 14 | SHFE + US open |
| comm_agri | 12, 13 | USDA reports |
| eco_cpi/ppi/gdp | 13, 14, 15 | release + cooldown |
| eco_jobs | 12, 13, 14, 15 | NFP + ADP |
| eco_fed | 17, 18, 19, 20 | FOMC windows |
| companies_earnings, tech_ev_tesla | 20, 21, 22 | after-hours earnings |

## Processes

- **Trader**: PID 24814, launched 18:59 UTC with universe caching fix
- **PnL tracker**: PID 24281 (writing `pnl_timeseries.csv` + `pnl_by_subsector.csv` every 60s)
- **Wrapper**: PID 24280, 24h deadline, up to 50 auto-restarts

## What the PnL tracker records

- `pnl_timeseries.csv`: ts_utc, realized_pnl, **deployed_capital**, n_open, n_tracked, n_fills
- `pnl_by_subsector.csv`: ts_utc, subsector, realized_pnl, deployed_capital, n_open, n_tracked, n_fills
- Per-market PnL is in `portfolio_paper.json` (one entry per ticker)

## Debugging done just now

1. **Capital config**: CLI --capital default was 100, overriding the config's 1000. Fixed: default None, only override if explicitly passed.
2. **Universe pre-filter**: 1971 series was too many list_markets calls per cycle. Added filter to only scan series with known open markets (from sector_scan) → 399.
3. **Kill-restart loop**: My repeated `pkill -9` kept triggering wrapper restarts. Wrapper correctly interprets SIGKILL (rc=137) as crash and restarts. Self-inflicted, paused once trader stabilized.
4. **Universe caching**: Even 399 list_markets per cycle serialized cycles to 3+ min. Added cache (refresh every 300s). First cycle still slow; subsequent cycles only do orderbook+trades, much faster.

## Inspect while I'm away

```bash
cd ~/personal/prediction-mm
cat MORNING.md                                              # this doc
tail -30 logs/overnight_trader.log                           # live trader
cat research/data/trader_state/pnl_timeseries.csv | tail -10 # portfolio PnL
cat research/data/trader_state/pnl_by_subsector.csv | tail -40 # per-subsector
.venv/bin/python -c "
import json
p = json.load(open('research/data/trader_state/portfolio_paper.json'))
fills = sum(len(pos['fills']) for pos in p['positions'].values())
tr = sum(pos['realized_pnl'] for pos in p['positions'].values())
print(f'tracked: {len(p[\"positions\"])} fills: {fills} realized: \${tr:+.4f}')
for t, pos in p['positions'].items():
    if pos['fills']: print(f'  {t[:55]}: inv={pos[\"yes_contracts\"]:+d} realized=\${pos[\"realized_pnl\"]:+.4f} fills={len(pos[\"fills\"])}')
"
```

## Stop everything

```bash
pkill -f overnight_runner; pkill -f run_trader; pkill -f pnl_tracker
```
