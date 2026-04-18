# prediction-mm

Research notes and (eventually) implementation for a small market-making bot targeting prediction markets.

## Status

**Phase 0 — Ideation & theory.** No code yet. Collecting theory, defining thesis, planning data collection.

Next step: obtain read-only API key(s) for a target venue (Kalshi first), pull sample orderbook + trade data, validate that the edge exists before writing any quoting logic.

## Thesis (v0)

1. **Target illiquid / inefficient prediction markets** where informed flow is minimal. Avoid headline political markets, sports, anything with a public model (538, Metaculus).
2. **Be time-aware**: every market has safe windows (low info-release probability) and dangerous windows (scheduled releases, news events). Quote in safe windows, pull in dangerous ones.
3. **Avoid extreme probabilities** (roughly outside [0.05, 0.95]): tick size dominates, payoff is asymmetric, resolution risk fat-tails.
4. **Derive risk parameters from the data**, not from theory defaults. Calibrate per market.
5. **Exploit correlation structure** between related contracts (adjacent temperature strikes, CPI headline vs core, candidate win vs vote-share). No-arb bounds give both hedging and opportunistic edge.

## Repository layout

```
docs/
  theory/
    01_market_making_fundamentals.md     # PnL sources, losses, core tension
    02_orderbook_reading.md              # Book shapes and what they imply
    03_avellaneda_stoikov.md             # Deep dive on the AS model
  strategy/
    target_markets.md                    # Which market categories fit the thesis
    safe_windows.md                      # Time-of-day / event-driven risk windows
    extreme_probability_avoidance.md     # Why not to quote near 0 or 1
    correlation_structure.md             # Adjacent-strike and cross-market correlations
    risk_parameters.md                   # Inventory, spread, capital limits — data-driven
  venues/
    venue_comparison.md                  # Kalshi vs Polymarket vs Manifold

research/                                # (future) notebooks, data pulls, analysis
```

## Roadmap

- **Phase 0** (now): ideation, theory docs, strategy framing.
- **Phase 1**: venue pick, read-only API key, data collection harness. Per-market stats: spread, depth, trade frequency, informed-flow proxies, time-of-day profiles.
- **Phase 2**: go/no-go per market category from Phase 1 stats. Fit `A`, `k`, `sigma` for survivors.
- **Phase 3**: paper-trading quoter. AS core + safe-window overlay + extreme-probability clamps + inventory caps.
- **Phase 4**: live with tiny size on one contract. Measure vs paper. Iterate.
- **Phase 5**: multi-contract, correlation hedging.

## Ground rules

- No API keys in the repo. Ever. `.gitignore` is strict.
- No trading until data inspection says the edge exists. Do not skip Phase 1.
- Paper before live. Small before big.
