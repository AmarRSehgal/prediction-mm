# comm_gold

_Auto-generated from sector scan. Curated notes in the KEEP block below are preserved across regenerations._

## Live stats

_Will be populated on next regeneration. See `INDEX.md` for latest snapshot._

## Curated notes

<!-- KEEP-START -->

### Market structure
- Series: KXGOLDD (daily), KXGOLDW (weekly), KXGOLDMON (monthly), KXGOLDPRICE (one-off), GOLD (aggregate).
- Resolution: COMEX GC settlement (or equivalent spot fix for some variants).
- Frequency: daily primary.
- Structure: strike ladder — "Gold above $X" for X in a grid around current spot.
- Close time: 21:00 UTC daily.

### Informed flow profile
- **Mostly retail gold-bugs + some institutional hedgers.**
- **HFT presence: light to moderate.** Observed 20-35c spreads on shoulder strikes
  even at OI 1000+. Nearest-the-money strike can tighten to 2-3c.
- Informed flow sources:
  - Fed-day repositioning (rate decisions move gold hard via USD).
  - Geopolitical spikes (gold is a safe-haven bid on news).
  - Central bank buying rumors.

### Time windows (UTC)
- **SAFE**: 00:00 - 08:00 UTC (Asian gold session quiet; US / London closed).
- **QUIET**: 08:00 - 12:00 UTC (London pre-open and open; moderate flow).
- **QUIET/DANGEROUS**: 12:00 - 14:00 UTC (US pre-open; CPI / PPI / jobs release times).
- **DANGEROUS**: 14:00 - 16:00 UTC (US cash open and volatility window).
- **VERY DANGEROUS**:
  - Scheduled data releases: CPI (monthly, Wed 13:30 UTC), NFP (Fri 13:30 UTC),
    PPI (monthly, 13:30 UTC), FOMC (18:00-19:30 UTC on scheduled Wednesdays).
  - Geopolitical breaking news (Middle East, Russia-Ukraine).
- **DANGEROUS**: 20:00 - 21:00 UTC (close-hour convergence).

### Correlation / basket structure
- Monotone strike ladder — same arb / CDF-fitting opportunity as oil.
- Gold correlates:
  - Negatively with USD (real rates).
  - Positively with silver (~0.80).
  - Positively with safe-haven assets (Swiss franc, JPY).
- Cross-commodity hedge: long Kalshi gold strike can be offset with short silver strike
  on days when the ratio is stable.

### Verdict
- **v0 target: YES — secondary to oil.**
- Why: wide shoulder spreads, clean resolution, predictable dangerous windows.
- Caveats:
  - News-driven jump risk is higher than oil (geopolitics).
  - Correlation with silver makes family-level inventory cap important.
- Path: include in commodity strike-ladder paper trade, but weight smaller than oil
  given jump risk.

<!-- KEEP-END -->
