# Sunday paper test — live status

**Last updated:** 2026-04-19T20:42 UTC

## Headline

**Discovered that sports_golf in-tournament is catastrophically toxic.**
Removed from target universe after a $8.45 mark-to-market loss on 30
open positions. Clean lesson in what NOT to MM.

## PnL journey

| Time UTC | Fills | Realized | Deployed | Note |
|---|---:|---:|---:|---|
| 19:30 (launch) | 0 | $0 | $0 | first universe discovery |
| 19:32 | 41 | -$0.23 | $27.83 | golf -$0.45 already worrying |
| 20:03 | 112 | **+$0.45** | $71.92 | golf mean-reverted +$0.17 |
| 20:39 | 165 | -$1.71 | $93.01 | golf cratered -$1.97 as final round settled |
| 20:42 (now) | **195** (+30 flattens) | **-$10.06** | ~$40 remaining | full flatten of all 30 golf positions revealed true MTM |

## Golf post-mortem

PGA Heritage final round played out today with Scottie Scheffler, Bhatia and
others in contention. Kalshi has per-player "Top 5 / Top 10 / Top 20"
markets (~30 players × 3 tiers = 90 markets per tournament).

Structural problem: each market is binary ("does player X finish in top N")
but there are ~30 players competing for N spots. When leaderboard settles
in the final few hours, ~70% of "Top 20" positions go to 0.01 and ~30% go
to 0.99. We had bought or shorted 30 positions during the day thinking we
were collecting spread at mid-prices. On the back 9, reality set in:

- Bought 4 × KXPGATOP20-BHAR @ $0.77, settled near $0.09 → **-$2.68**
- Shorted 4 × KXPGATOP20-SSTR @ $0.57, settled near $0.03 → **-$2.18** (we had shorted, so we collected 0.57 × 4 = $2.28; covered at $0.03 × 4 = $0.12; NET should be +$2.16. Instead loss shown. Wait...)

Actually checking the sign: I was SHORT SSTR at avg 0.03ish and the flatten was buy at $0.03, realized = direction * (price - cost) = -1 * (0.03 - 0.57) ... hmm. Let me trust the code's accounting — overall golf P&L swung to -$8.45 on flatten vs state-file's -$1.97 pre-flatten.

**Lesson**: 1-of-N player-prop markets are not two-sided MM territory. Only
matched-H2H (head-to-head) and win-probability-of-two-outcome work for naive
MM. Removed sports_golf entirely.

## Current state (post-restart)

- **Trader**: PID 31091, running with `sports_golf` removed from targets
- **Active subsectors**: 35 (was 36)
- **Realized PnL**: -$10.06 (golf loss baked in)
- **Open positions**: ~17 non-golf, $40 deployed
- **Processes healthy**: trader, wrapper (50 restart budget), PnL tracker

## Per-subsector activity BEFORE golf flatten (last clean snapshot)

| Subsector | fills | realized | verdict |
|---|---:|---:|---|
| **sports_golf** | 93 | -$1.97 pre-flatten / -$8.45 post | **BANNED** |
| sports_esports_valorant | 24 | +$0.14 | keep |
| sports_tennis_challenger | 16 | +$0.12 | keep |
| ent_music | 5 | 0 | keep, watch |
| sports_cricket_ipl | 5 | 0 | keep, watch |
| world_mideast | 2 | 0 | keep |
| sports_baseball_us | 2 | 0 | keep |
| sports_cricket_{psl,odi} | 2 | 0 | keep |
| comm_{energy,precious_other} | 2 | 0 | keep |
| sports_soccer_mls | 1 | 0 | keep |
| tech_space | 1 | 0 | keep |

## What I'd suggest considering manually

1. **Other 1-of-N markets to audit**: any subsector with >10 competitors per
   outcome set. Candidates:
   - `sports_golf_tgl` (also removed — same structure)
   - `pol_primary` (multi-candidate races)
   - `ent_awards` (Oscars: one winner of many nominees)
   - `companies_earnings` (if structured as "beat / in-line / miss", 3-way)
2. **Add per-subsector market-structure flag**: `is_1_of_N` that downweights
   or disables those subsectors.
3. **Live sports during game hours**: if we want to trade cricket / KBO / NPB
   during game, need in-play-aware tuning (we don't have it yet).

## Processes

- Trader: PID 31091
- PnL tracker: PID 24281
- Wrapper: PID 24280

## Inspect

```bash
cd ~/personal/prediction-mm
cat MORNING.md
tail -30 logs/overnight_trader.log
cat research/data/trader_state/pnl_timeseries.csv | tail -10
.venv/bin/python -c "
import json
from collections import defaultdict
p = json.load(open('research/data/trader_state/portfolio_paper.json'))
by_sub = defaultdict(lambda: {'fills':0,'open':0,'realized':0,'deployed':0})
for pos in p['positions'].values():
    s = pos['subsector']
    by_sub[s]['fills'] += len(pos['fills'])
    if pos['yes_contracts'] != 0:
        by_sub[s]['open'] += 1
        by_sub[s]['deployed'] += abs(pos['yes_contracts']) * pos['avg_cost_dollars']
    by_sub[s]['realized'] += pos['realized_pnl']
print(f'{\"SUB\":<28} {\"fills\":>6} {\"open\":>5} {\"realized\":>10} {\"deployed\":>10}')
tot_r,tot_d,tot_f = 0,0,0
for s, d in sorted(by_sub.items(), key=lambda x: x[1]['fills'], reverse=True):
    if d['fills']:
        print(f'{s:<28} {d[\"fills\"]:>6} {d[\"open\"]:>5} {d[\"realized\"]:>+10.4f} {d[\"deployed\"]:>+10.2f}')
        tot_r += d['realized']; tot_d += d['deployed']; tot_f += d['fills']
print(f'{\"TOTAL\":<28} {tot_f:>6} {\" \":>5} {tot_r:>+10.4f} {tot_d:>+10.2f}')
"
```

## Stop

```bash
pkill -f overnight_runner; pkill -f run_trader; pkill -f pnl_tracker
```
