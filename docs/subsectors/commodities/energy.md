# comm_energy

_Auto-generated from sector scan. Curated notes in the KEEP block below are preserved across regenerations._

## Live stats

_Will be populated on next regeneration. See `INDEX.md` for latest snapshot._

## Curated notes

<!-- KEEP-START -->

### Market structure
- Series covered: KXBRENTD (Brent daily), KXWTID (WTI daily; currently 0 open), KXWTIH (WTI hourly), KXNATGASW (Nat gas weekly), KXNATGASMON (Nat gas monthly).
- Resolution mechanism: official futures settlement price (ICE Brent, NYMEX WTI/NG).
- Frequency: daily (Brent), hourly (WTI-H), weekly/monthly (nat gas).
- Structure: **strike ladder** — for each day, multiple strikes like "$93 or above",
  "$95 or above", "$100 or above". Each strike is a separate binary market.
- Typical close time: 21:00 UTC (= 17:00 ET, roughly US cash close).

### Informed flow profile
- **Retail + professional mix.** Real hedgers and speculators trade these.
- **HFT presence: moderate.** Top-2 strikes near spot often 1-3c spread; shoulder
  strikes (10-30% OTM or ITM) stay 15-40c wide. This is our zone.
- Informed-flow sources:
  - Physical-traders (refiners, producers) on Brent especially.
  - CL/BZ futures arbers: will eat any mispricing > fees + gas vs the futures curve.
  - News traders around EIA inventory (US oil), OPEC, geopolitical shocks.

### Time windows (UTC)
- **SAFE**: 00:00 - 11:00 UTC (Asian session, US/EU oil markets quiet or closed).
- **QUIET**: 11:00 - 13:30 UTC (EU oil pickup, not yet chaotic).
- **DANGEROUS**: 13:30 - 14:00 UTC (US cash equities open; cross-flow into commodities).
- **VERY DANGEROUS**:
  - **Wed 14:30 UTC**: EIA Weekly Petroleum Status Report — crude/gasoline/distillate
    inventory data. Biggest single scheduled mover for oil.
  - **OPEC / OPEC+ announcements**: ad hoc but pre-scheduled meeting dates.
  - **FOMC days, 18:00-19:30 UTC**: USD moves drag on commodities.
- **DANGEROUS**: 20:00 - 21:00 UTC — close-hour convergence; informed flow spikes.

### Correlation / basket structure
- Strike ladder = monotone CDF per underlying. P(>$95) >= P(>$96) >= P(>$97)...
  Violations = direct arb. Fit a smooth CDF to all strikes; outliers are relative
  value. See `correlation_structure.md`.
- Brent and WTI correlate ~0.95 daily. If both markets are open we can cross-hedge.
- Natural gas decoupled from crude most of the time.

### Verdict
- **v0 target: YES — primary commodity target.**
- Why:
  - 15-40c spreads on shoulder strikes give real MM edge.
  - Strike-ladder structure = correlation opportunities (adjacent-strike arb, CDF fitting).
  - Well-defined dangerous windows (EIA, FOMC, US cash open).
- Caveats:
  - Underlying-arb risk: if someone hedges on futures, we could be picked off when
    Brent moves intraday without Kalshi-market liquidity catching up.
  - Position sizing must respect strike-ladder correlation (one "oil up" view
    positions us across many adjacent strikes).
- Path: paper trade the shoulder strikes for a week. Skip Wed 14:30 UTC entirely.

<!-- KEEP-END -->
