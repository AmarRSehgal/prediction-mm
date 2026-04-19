# eco_ppi

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **12** (8 contested)
- Total 24h volume: **$31**
- Total open interest: **32**
- Top-OI mean spread (median across series): **51.7 cents**
- **MM profile: Wide but dead**

## Book depth (from comprehensive scan)

- Markets sampled: **8**
- Median spread: **67.0c**
- Median TOB bid / ask size: **8 / 8** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **0**
- Mean informed-signal proxy: **nan** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **nanc**

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXUSPPIYOY-26MAY13-T5.2 | Above 5.2% | 16c | 5.0c | 10 | 331 | 10 | 331 | 10 | $10 | 7-30d |
| KXUSPPIYOY-26MAY13-T5.0 | Above 5.0% | 50c | 75.0c | 8 | 8 | 0 | 0 | 0 | $0 | 7-30d |
| KXUSPPIYOY-26MAY13-T4.8 | Above 4.8% | 50c | 75.0c | 8 | 8 | 0 | 0 | 0 | $0 | 7-30d |
| KXUSPPIYOY-26MAY13-T4.6 | Above 4.6% | 50c | 75.0c | 8 | 8 | 0 | 0 | 0 | $0 | 7-30d |
| KXUSPPIYOY-26MAY13-T4.4 | Above 4.4% | 51c | 72.0c | 8 | 8 | 0 | 0 | 0 | $0 | 7-30d |
| KXUSPPIYOY-26MAY13-T4.2 | Above 4.2% | 54c | 61.0c | 7 | 6 | 0 | 0 | 0 | $0 | 7-30d |
| KXUSPPIYOY-26MAY13-T4.0 | Above 4.0% | 54c | 61.0c | 7 | 6 | 0 | 0 | 0 | $0 | 7-30d |
| KXUSPPIYOY-26MAY13-T3.8 | Above 3.8% | 56c | 62.0c | 7 | 8 | 0 | 0 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXUSPPIYOY | US PPI YoY in [month] | monthly | 12 | 8 | $31 | 32 | 51.7c |

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
