# Morning report — check-in

**Last updated:** 2026-04-19T15:20 UTC (~7h into overnight run)

## TL;DR

- Paper trader ran overnight across KBO / NPB / PSL cricket subsectors
- **9 total fills** (5 organic + 4 auto-flattens at game exit)
- **Net realized PnL: -$0.04** across ~$4 exposure round-tripped
- Zero errors, zero crashes, 3 processes still healthy
- Found and fixed **4 real bugs** during the run — see details below

## Fill timeline

All fills happened in the **first 1.5 hours** of the run (09:35 - 11:17 UTC),
then the flatten window fired at 13:00 UTC for today's PSL games.
Since then, zero new fills — quiet markets globally (Sunday morning, no
KBO/NPB games live, PSL 2-7 days out).

## Realized PnL per round-trip

| Market | Entry | Exit | Realized |
|---|---|---|---:|
| MUSKKI-MUS | bought 2 @ $0.59 | sold 2 @ $0.60 | **+$0.02** |
| MUSKKI-KKI | bought 4 @ $0.37 avg | sold 4 @ $0.35 | -$0.08 |
| QGLPZA-PZA | shorted 2 @ $0.63 | covered 2 @ $0.56 | **+$0.14** |
| QGLPZA-QGL | shorted 2 @ $0.46 | covered 2 @ $0.52 | -$0.12 |
| **Total** | | | **-$0.04** |

**Per-pair breakdown:**
- MUSKKI (Multan vs Karachi) pair: -$0.06 net. Flow was one-sided buy; we
  accumulated long on KKI as price drifted against us.
- QGLPZA (Quetta vs Peshawar) pair: +$0.02 net. Short-both-sides basket
  collected $1.09 in premium vs $1.00 payout liability — the $0.09 over-round
  was captured.

**Verdict at this sample size:** noise-dominant. 4 round-trips can't
distinguish profit from zero. But the mechanism is working end-to-end.

## Bugs found and fixed tonight

### 1. Runner order of operations
Fill-check ran AFTER cancel+repost. Any trade in the 15s inter-cycle gap
got skipped because new orders had `ts > trade.ts`. **Fix: moved fill-check
before cancel.** This single fix unlocked all 5 organic fills.

### 2. Wrapper restart logic
Trader clean exit (rc=0) was misinterpreted as "done". **Fix: wrapper now
restarts on any exit until deadline**, up to max-restarts count.

### 3. Paper flatten was no-op
At EXIT window, `flatten_market` just logged without updating state. **Fix:
now simulates taking the current bid/ask** (conservative: we receive
prevailing bid if long, pay prevailing ask if short). PnL now tracks through
settlement.

### 4. Position PnL sign-flip on short closes
Realized PnL formula had an extra `(-1 if delta > 0 else 1)` factor that
inverted the sign when closing a short. **Fix: removed the factor.** Now
`realized = direction * (price - cost)` which is correct for both long and
short. Backfilled existing state.

### 5. Race condition during fix application
Wrapper auto-restarts a killed trader in seconds. If I correct the state
file during that window, the new trader loads the corrected state and
then saves its (still wrong) in-memory copy on top. **Fix: kill wrapper AND
trader before applying state corrections.** No code change; process
discipline.

## Current state

- **Paper trader**: PID 6710 (running since 14:01 UTC, wrapper restart #0)
- **PnL tracker**: PID 87230 (continuous since 09:01 UTC)
- **Overnight wrapper**: PID 6703 (7h remaining on deadline)
- **Realized PnL**: -$0.04 (persisted correctly, sticking across restarts)
- **Open positions**: 0
- **Active universe**: 30 markets across KBO/NPB/PSL closing in next 7 days
- **Current quotes**: placed on every cycle (15s), no errors

## What to look at when you're up

1. `MORNING.md` (this file) — overall summary
2. `research/data/trader_state/pnl_timeseries.csv` — minute-by-minute PnL
3. `logs/overnight_trader.log` — every fill, quote, cycle
4. `research/data/trader_state/portfolio_paper.json` — position-level state

## Known limitations observed overnight

- **Quote staleness**: we cancel-then-repost every cycle even if the quote
  hasn't changed. Fine for paper; wasteful for live. Future: smart-cancel
  only when price moves.
- **Flow concentration**: 55% of fills happened in a 10-minute window,
  suggesting our paper fill-match model is event-clustered rather than
  Poisson. Might need a per-subsector arrival-rate estimate.
- **Adverse selection on MUSKKI**: bought at 0.37, settled at 0.35. Spread
  captured was +$0.00; adverse move was -$0.02 per contract. **For a
  ~4c TOB-relative spread, we lost to a ~2c adverse drift.** Spread-per-fill
  must exceed drift-per-fill for MM to be profitable. Current net is noise;
  watch over more samples.

## Next natural steps (for daytime)

- Let it run until wrapper deadline (~18:34 UTC) or stop now.
- Review the 9 fills in detail — compute effective spread capture vs
  drift cost per market.
- Consider tighter or different target subsectors based on tonight's
  findings (e.g., drop MUSKKI-style single-sided flow; keep QGLPZA-style
  short-basket setups).

## To stop everything

```bash
pkill -f overnight_runner; pkill -f run_trader; pkill -f pnl_tracker
```

To keep running, do nothing. Wrapper has 3h left before natural stop.
