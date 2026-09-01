# Trader guide

MM bot over `TraderConfig.target_subsectors`. The live defaults are whatever is
in `src/pmm/trader/config.py` -- read it rather than this file for exact
numbers; the values below are the shape, not the source of truth.

## Defaults

- Capital: `RiskLimits.capital_dollars`
- Caps: `per_market_frac` / `per_subsector_frac` / `total_exposure_frac` of it
- Default order size: 2 contracts, max inventory +/-5 per market
- Min spread: 3 cents -- and it is now enforced on the POSTED quote, so a book
  narrower than 3c is sat out entirely rather than quoted at 1c
- Quote refresh: 15 seconds
- Exit inside 2h of game start (sports) or 30h of close (fallback)

Change via `--capital`, `--subsectors`, or edit `src/pmm/trader/config.py`.

## How the quoter decides

Per market it computes an AS reservation price `r` (mid, skewed against
inventory) and a desired spread `gamma*sigma^2*T + (2/gamma)*ln(1+gamma/k)`,
then posts inside the admissible passive band:

    bid in [tob_bid, tob_ask - min_spread]   posted only if AS bid >= tob_bid
    ask in [tob_bid + min_spread, tob_ask]   posted only if AS ask <= tob_ask

Consequences worth knowing at the console:

- **A one-sided quote is normal and correct.** Holding inventory pushes the AS
  bid below the top-of-book bid, so the bid stands down and the ask keeps
  working the position off. It is not a bug and it does not need a forced exit.
- **No quote at all is also normal.** If the book is tighter than min_spread,
  or tighter than the desired AS spread, there is no admissible quote. On a
  369-market sample of the target universe, 55% of the markets carrying any
  volume had a 1c book -- expect to sit out a lot of them.
- `ASParams.k_order_arrival` (default 40) contributes ~4c of the desired
  spread on its own and is uncalibrated. If fill rate is far off, that is the
  first knob, not gamma.

## Fees

`pmm.trader.fees` implements Kalshi's schedule off the per-series `fee_type` /
`fee_multiplier` fields. Two numbers to keep in your head:

- **A passive round trip is free** on a standard series. Fees are not the
  reason to want a wide spread; adverse selection is.
- **A crossed exit costs ~2c per contract** in the 0.15-0.85 band at our order
  sizes, because the round-up is per order and P*(1-P) peaks mid-book. That is
  on top of the spread you pay to cross.

`realized_pnl` in the state file and in both tracker scripts is NET of fees.
`scripts/fee_report.py` prints the fee table and re-prices the recorded
sessions; `scripts/quoter_counterfactual.py` scores the quoter against them.

## Paper (Tier 2) — trade-match fills

```bash
cd ~/personal/prediction-mm
.venv/bin/python scripts/run_trader.py                  # forever
.venv/bin/python scripts/run_trader.py --duration 3600  # one hour

# Anything exploratory: send state somewhere else. Without --state-path the
# run appends to the canonical paper record that every PnL report reads.
.venv/bin/python scripts/run_trader.py --duration 300 --state-path /tmp/smoke.json
```

Default is paper. Virtual orders; every cycle we pull real trades and check
whether a trade would have crossed our virtual price with enough size to sweep
past the book-ahead estimate. Realistic-ish fill rate.

**Caveats:**
- Queue-ahead estimate is a snapshot at place time, not per-level FIFO.
- No simulated order-add/cancel dynamics.
- Fills never move the market (correct for tiny sizes; wrong at scale).

Verdict: good enough to validate strategy logic, generate fills/PnL for 1-2
weeks of data, and identify subsectors where fills actually happen.

## Live (Tier 3) — real orders with your key

```bash
.venv/bin/python scripts/run_trader.py --live
# Type "GO" at the confirmation prompt
```

Requires your API key to have **trade** scope on Kalshi. The current key
(`51b80757-...`) is read-only; going live needs a new key created in the Kalshi
dashboard with trade permission.

Recommended first live run:
- `--capital 20` (limits per-market cap to $1)
- Run during a known SAFE window (e.g., 00:00-08:00 UTC for KBO, before lineup releases)
- Watch for an hour. Kill with Ctrl-C.
- Examine `research/data/trader_state/portfolio_live.json` for fills + PnL.

## What to watch for

1. **Fill rate** — if no fills in an hour of SAFE window, spreads are too wide.
   Widen criterion or move to less-competitive markets.
2. **Post-fill drift** — if your fills consistently move against you by >3c in
   5 min, you're taking toxic flow. Widen spreads or pull the subsector.
3. **End-of-game inventory** — the system force-flattens at EXIT window. If you
   consistently carry inventory into the game, check the game-start-time parser.
4. **Daily PnL** — should be slightly positive per day if MM is working. If
   flat, spreads aren't wide enough vs. realized vol. If negative, toxicity.

## State files

- Paper: `research/data/trader_state/portfolio_paper.json`
- Live:  `research/data/trader_state/portfolio_live.json`

Each contains cash, all positions, and complete fill log (timestamps, prices).
Safe to restart — state loads on startup.

## Kill / intervention

- Ctrl-C: cancels all active orders, saves state, exits.
- The `daily_stop_loss_dollars` kill switch halts new quoting for the session
  when realized PnL crosses the threshold. It reads realized only and ignores
  mark-to-market, so an unrealized hole does not trip it.

## Not yet implemented

- `sigma_cents` is a 4-entry lookup table defaulting to 5.0c, while the runner
  already measures realised vol per market for the price-discovery gate and
  then discards it. Feeding that measurement into the quoter is the highest
  value open item now that the AS spread actually reaches the book.
- Per-underlying net delta accounting (see `docs/strategy/commodity_ladders.md`).
- Smart-cancel-on-move (the runner cancels + reposts every cycle).
- True queue-position FIFO modeling.
- News-event pull (e.g. injury scratches causing jumps in KBO/NPB).
