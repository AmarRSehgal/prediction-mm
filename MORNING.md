# Morning report

**Last updated:** 2026-04-19T13:14 UTC (~5h into overnight run)

## Headline

**First complete round-trip cycle fired.** Paper trader opened 9 fills across
4 PSL markets for today's games, and auto-flattened when the 13:00 UTC
exit-window triggered. **Net realized PnL: -$0.04 on $2+$2 of exposure
round-tripped.**

## Per-market result (all PSL games closing ~15:00 UTC today)

| Market | Inv flow | Realized |
|---|---|---:|
| MUSKKI-MUS | bought 2@$0.59, flatten-sold 2@$0.60 | **+$0.02** |
| MUSKKI-KKI | bought 4@$0.37 avg, flatten-sold 4@$0.35 | -$0.08 |
| QGLPZA-PZA | shorted 2@$0.63, flatten-covered 2@$0.56 | **+$0.14** |
| QGLPZA-QGL | shorted 2@$0.46, flatten-covered 2@$0.52 | -$0.12 |
| **Total** | 9 fills + 4 flattens | **-$0.04** |

**Observation:** MUSKKI pair -$0.06 (adverse move on KKI), QGLPZA pair +$0.02
(short-both-sides basket captured $0.09 over-round). Noise-dominant outcome at
this sample size. Key is **the mechanism works end-to-end**.

## Bugs found and fixed tonight

1. **Runner order of ops** — Fill-check ran after cancel+repost, so trades in
   the 15s inter-cycle gap got skipped (`ts < placed_ts`). **Moved fill-check
   before cancel.** This unlocked all 5 organic fills we got.

2. **Wrapper restart logic** — Trader clean exit (rc=0) misinterpreted as
   "done". **Wrapper now restarts on any exit until deadline.**

3. **Paper flatten was no-op** — At EXIT window, flatten just logged without
   simulating. **Now simulates taking the current bid/ask.** This let us see
   the round-trip PnL through settlement.

4. **Position PnL sign-flip on shorts** — Realized PnL formula had an extra
   `(-1 if delta > 0 else 1)` factor that inverted the sign for short closes.
   **Removed the factor.** Corrected the 4 existing position realizations in
   state file.

## Current state

- **Paper trader**: running (PID 3525, restart #2 of 20, wrapper deadline
  ~18:34 UTC)
- **PnL tracker**: running (PID 87230)
- **Realized PnL (corrected)**: -$0.04
- **Open positions**: 0 (all flattened)
- **Active universe**: PSL games for Apr 22-27, NPB/KBO for Apr 21-22 — no
  exit for these in the next few hours

## What's still queued

The universe now contains mostly 2-3-day-out games with lower flow. More
fills expected through the morning as:
- NPB/KBO games closing tomorrow enter their active-pricing window
- Retail flow picks up as US morning approaches

## Observations for post-mortem

- **One-sided flow** in the QUIET window. MUSKKI got only BUY fills (NO
  takers crossing our bid); QGLPZA got only SELL fills (YES takers crossing
  our ask). Same game, opposite flow pattern — likely an artifact of where
  each market's mid sat.
- **Adverse selection cost roughly matched spread capture**. Gross captured:
  +$0.16 (MUS, PZA wins). Gross lost: -$0.20 (KKI, QGL moved against us).
  Net -$0.04. Suggests the "lean into flow / quote both sides" strategy is
  net approximately fair in these markets — needs tighter spread or better
  flow-prediction to turn profit.
- **Sample size is tiny** (4 round-trips). Treat as sanity-check, not signal.

## How to inspect

```bash
cd ~/personal/prediction-mm
cat MORNING.md
tail -100 logs/overnight_trader.log
grep "PAPER FILL\|PAPER FLATTEN" logs/overnight_trader.log
cat research/data/trader_state/pnl_timeseries.csv | tail -30
```

## Stop

```bash
pkill -f overnight_runner; pkill -f run_trader; pkill -f pnl_tracker
```
