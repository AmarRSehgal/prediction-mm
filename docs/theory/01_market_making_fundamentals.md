# Market Making Fundamentals

## What market making actually is

MM is not prediction. It is **risk transformation**: absorb the imbalance between buyers and sellers who do not show up at the same instant, and charge for it (the spread).

## The three sources of PnL

1. **Spread capture** — sell at ask, buy at bid, pocket the difference averaged over round trips.
2. **Maker rebates** — some venues pay you for providing liquidity (negative fees). Kalshi: implicit. Polymarket: none currently.
3. **Avoiding toxic flow** — not losing to informed traders. This is "PnL" in the sense of losses avoided.

## The three sources of loss

1. **Adverse selection** — your bid gets hit right before price drops; your ask gets lifted right before price rises. Someone knew something. This is the dominant cost in toxic markets.
2. **Inventory risk** — you accumulate one side, market moves against you before you unwind.
3. **Operational** — latency, bugs, API failures, rate limits.

## The core tension

Tighter spread =>  more fills =>  more adverse selection AND more inventory accumulation.

Every MM model is a principled solution to this tradeoff. Avellaneda-Stoikov (see `03_avellaneda_stoikov.md`) is the canonical academic answer; Glosten-Milgrom addresses adverse selection explicitly; Kyle treats informed vs uninformed flow as a signal extraction problem.

## What this means for a prediction-market MM

- Accept that raw spread capture in liquid, competitive markets is hard. Edge comes from being selective about *which* markets to quote.
- Toxic flow is the biggest enemy. Venue, market category, and time-of-day selection are all ways to reduce exposure to it before strategy math even runs.
- The spread has to pay for adverse selection, not just volatility. Vanilla AS under-prices this.
