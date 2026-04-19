# eco_ppi

_Auto-generated from sector scan. Curated notes in the KEEP block below are preserved across regenerations._

## Live stats

_Will be populated on next regeneration._

## Curated notes

<!-- KEEP-START -->

### Market structure
- Series: KXUSPPIYOY (US PPI YoY monthly), KXPPI* variants.
- Resolution: official BLS Producer Price Index release.
- Frequency: monthly, typically mid-month, Tue-Thu 13:30 UTC (8:30 ET).
- Structure: strike ladder — "Above 5.0%", "Above 5.2%", "Above 4.8%".
- Close time: ~13:30 UTC on release day (= release time).

### Informed flow profile
- **Macro traders + informed institutions around release, retail elsewhere.**
- **HFT presence: near zero** between releases. Observed 50-70c median spreads.
- Informed flow pattern:
  - Pre-release (days 1-28 of month): very thin, retail only, no informed edge.
  - Release morning (hours before): positioning by macro desks; informed flow spikes.
  - Release moment (13:30 UTC): massive jump, spreads blow out, pull quotes entirely.
  - Post-release: fresh equilibrium within ~30 minutes.

### Time windows (UTC)
- **SAFE**: 23 days of the month (any day not in the 7-day release window).
- **QUIET**: release week before release day.
- **DANGEROUS**: release day, 08:00-13:00 UTC (pre-release positioning).
- **VERY DANGEROUS**: 13:25-14:30 UTC on release day. Pull quotes entirely.
- **DANGEROUS**: 14:30-16:00 UTC post-release. Wait for new equilibrium.

### Correlation / basket structure
- Strike ladder monotone.
- PPI correlates with CPI (~0.7 monthly changes); releases are 1-2 weeks apart so
  CPI-surprise repositions PPI expectations.
- PPI also correlates with oil / commodity prices (input costs).

### Verdict
- **v0 target: EXPERIMENTAL.**
- Why consider:
  - 50-70c spreads are enormous. Any fill at all pays massively.
  - Release calendar is public; dangerous window is exactly one day per month.
  - 23+ safe days per month.
- Why hesitate:
  - **Volume is near zero** — even wide spreads produce no PnL if nobody trades.
  - At tiny size, fill rate could be one contract per week; unclear if economic.
- Path:
  - Passive quote with very wide spreads (25c+) during the 23 safe days.
  - Pull quotes entirely starting 24h before release.
  - Measure fill rate for 2 months before deciding whether it's worth the operational overhead.

<!-- KEEP-END -->
