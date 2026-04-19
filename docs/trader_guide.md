# Trader guide

Minimal MM bot targeting 3 subsectors chosen for wide spreads + low toxicity:
`sports_baseball_kbo`, `sports_baseball_npb`, `sports_cricket_psl`.

## Defaults (for $100 capital)

- Per-market cap: $5 (5%)
- Per-subsector cap: $20 (20%)
- Total exposure cap: $50 (50%)
- Default order size: 2 contracts
- Max inventory per market: ±5 contracts
- Min spread: 3 cents
- Quote refresh: 15 seconds
- Daily stop-loss: $10
- Exit any market when inside 2 hours of game start (sports) or 30 hours of close (fallback)

Change via `--capital`, `--subsectors`, or edit `src/pmm/trader/config.py`.

## Paper (Tier 2) — trade-match fills

```bash
cd ~/personal/prediction-mm
.venv/bin/python scripts/run_trader.py                  # forever
.venv/bin/python scripts/run_trader.py --duration 3600  # one hour
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
- The daily_stop_loss kill switch (default $10) halts new quoting for the
  session when realized PnL crosses the threshold.

## Not yet implemented

- Smart-cancel-on-move (the runner currently cancels + reposts every cycle).
- Per-subsector parameter tuning via YAML.
- True queue-position FIFO modeling.
- News-event pull (e.g. injury scratches causing jumps in KBO/NPB).

These are Phase 3 work.
