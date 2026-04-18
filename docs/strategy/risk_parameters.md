# Risk Parameters

## Thesis

Risk parameters must be **derived from the data** for each market, not pulled from theory defaults or copied across markets. A parameter set that is safe for Kalshi weather is probably suicidal for niche political contracts, and vice versa.

This doc defines *what* parameters we need and *how* they should be calibrated. Actual values get filled in during Phase 2 after data collection.

## Parameter list

### Capital-level
- **Total capital at risk (`C_total`)**: hard dollar cap. Everything below is a fraction of this.
- **Per-venue cap (`C_venue`)**: e.g. Kalshi total <= X% of `C_total`.
- **Per-market-category cap (`C_cat`)**: weather, economic, political separately limited.
- **Per-family cap (`C_fam`)**: one strike ladder or exclusive basket counts as one family.
- **Per-contract cap (`C_ctr`)**: absolute floor on single-contract exposure.

Rule: `C_ctr <= C_fam <= C_cat <= C_venue <= C_total` with strict inequalities to leave headroom.

### Inventory-level (per contract)
- **`q_max`**: max absolute inventory per contract. Expressed in contracts AND in dollars (whichever binds first).
- **`q_soft`**: soft inventory limit (e.g. 0.7 * `q_max`) beyond which quote skew intensifies aggressively.
- **`q_hard`**: hard limit (e.g. `q_max`) at which the far-side quote is pulled entirely.

### AS quoter parameters (per market)
- **`gamma`**: risk aversion. Main tuning knob. Start high, tune down on validation.
- **`sigma`**: realized vol estimate. Rolling window (e.g. 30-60 min), market-specific.
- **`A`**: base arrival rate. Fit from trade data: `A = (trades/second) * calibration_factor`.
- **`k`**: price sensitivity of arrivals. Fit from orderbook + trade data: regress `log(fill_rate)` on `distance_from_mid`.
- **`T`**: horizon = time to resolution (natural).

### Quoting-level
- **Minimum spread (`s_min`)**: never quote tighter than this, even if AS suggests it. Covers latency, fees, and adverse-selection floor.
- **Maximum spread (`s_max`)**: above this, no one trades; do not bother. Signal that we should not be in the market.
- **Quote size**: constant per contract initially; later scale with book depth.
- **Price bands**: `[p_low, p_high]` where quoting is allowed. Default `[0.05, 0.95]`; refine per category.

### Time-based
- **Safe window states**: `SAFE / QUIET / DANGEROUS / POST_EVENT_COOLDOWN`.
- **Cooldown duration**: minutes to wait after dangerous window ends before resuming normal quoting.
- **End-of-life unwind time**: seconds before resolution at which to force-flatten inventory.

### Kill switches
- **Max realized daily loss**: hit it => stop all quoting for the day.
- **Max unrealized MTM drawdown**: hit it => pull quotes, unwind.
- **Max consecutive adverse fills**: fills where price moves wrong within N seconds => indication of being picked off; widen and investigate.
- **API error rate**: above threshold => pull quotes, alert.
- **Staleness**: if market data is older than X ms, pull quotes.

## Calibration methodology

Each parameter falls into one of three categories:

### Directly fittable from data
- `A`, `k`, `sigma`: fit from orderbook + trade history. Re-estimate nightly; use rolling window intraday.
- Safe-window classifications: fit from realized vol heatmap + event calendar.
- Price-band edges: fit from simulated-MM PnL by price decile.

### Set by capital / risk policy
- `C_total`, `C_venue`, `C_cat`, `C_fam`, `C_ctr`: set manually based on capital, risk tolerance, diversification goals.
- `q_max` per contract: derived as `C_ctr / max_contract_value`.

### Empirical, iterative
- `gamma`: start high (e.g. 10-50 for prices in [0,1]), observe fill rate and inventory dynamics, tune.
- `s_min`, `s_max`: start conservative (wide `s_min`), tighten as confidence grows.
- Kill-switch thresholds: start very tight, relax only after extended stable operation.

## Guardrails that never move

- No single contract > 10% of category capital.
- No single family > 40% of category capital.
- Price bands never extend past `[0.02, 0.98]` regardless of calibration output.
- Kill switches must trip on 5% daily drawdown minimum; can be tighter.
- All parameter changes logged with timestamp and rationale.

## Phase 1 / Phase 2 deliverable

Fill in the actual numerical values for every parameter above, per market category, grounded in the data collected in Phase 1. A parameter file per category. The MM runner reads this at startup; there should be no magic numbers in code.
