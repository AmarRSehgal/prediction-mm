# Extreme Probability Avoidance

## Thesis

There is little to no market-making value in contracts trading near the [0, 1] boundary. Avoid quoting outside roughly `[0.05, 0.95]` (band to be tuned with data).

## Why MM breaks down near the boundary

### 1. Tick size dominates spread
Kalshi tick is $0.01. At a mid of 0.50, a 1-cent spread is 2% of price. At a mid of 0.02, a 1-cent spread is **50% of price**. You cannot quote a reasonably-sized spread because the minimum tick is already huge relative to the price level. Either you quote a spread that is massive in relative terms (nobody trades) or tight in absolute terms (you lose to adverse selection).

### 2. Asymmetric payoff structure
At mid = 0.99 YES:
- Your bid fills: you paid 0.99, max loss = 0.99, max gain = 0.01.
- Risk / reward is 99:1 against you on any single contract.
A single wrong resolution wipes out ~100 "correct" round trips. The expected-value math can be positive on paper, but the variance is ruinous at any realistic size.

### 3. Fat-tail resolution risk
Near-boundary contracts are "mostly decided already". The market has priced them that way for a reason. The remaining probability mass is on tail outcomes that, when they hit, hit hard. You are short the tail at bad odds.

### 4. Informed-flow concentration
Near-boundary contracts are where insiders with last-mile information operate. If someone knows a weather observation is about to come in exactly wrong, they will hit your stale quote at 0.98. You are the sucker by construction.

### 5. Liquidity is unreliable exactly when you need it
Near resolution, bid-ask spreads on near-boundary contracts often widen as other MMers pull (they know what is coming). You may not be able to unwind inventory at a reasonable price.

## Where to draw the line

The right band is empirical, not theoretical. First-pass heuristic: `[0.05, 0.95]`. Tune per market from data by computing, at each price level:

- Realized PnL of a simulated constant-spread MM.
- Frequency of adverse resolution (losses > some threshold).
- Mean tick-size-relative spread available.
- Historical fill rates at that level.

Tighten the band to where MM is actually profitable in simulation.

## Handling a market that moves into the band

Contracts do not stay at 0.5 forever; many drift to the boundary over their life. Policy:

1. **Reduce size** as price approaches the band edges (taper, do not cliff).
2. **Stop quoting** the far side (the one pushing away from 0.5) entirely once near the edge — you cannot win there.
3. **Keep quoting the near side only while you have inventory to unwind**; otherwise step away.
4. **Unwind existing inventory** before price crosses the band, even at a small loss, to avoid resolution risk.

## Phase 1 deliverable

Per market category, produce a table of:
- Distribution of time spent at each price decile.
- Realized per-contract MM PnL by price decile (from simulation over historical data).
- Estimated adverse-selection cost by decile.

Use this to set the actual band per category, not a hardcoded default.
