# health_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **31** (27 contested)
- Total 24h volume: **$2,719**
- Total open interest: **11,848**
- Top-OI mean spread (median across series): **7.8 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **30**
- Median spread: **9.0c**
- Median TOB bid / ask size: **250 / 312** contracts
- Median cumulative depth within 5c of mid — bid: **250** / ask: **438** contracts
- Median cumulative depth within 10c of mid — bid: **412** / ask: **438** contracts
- Mean trades per market (last 3000): **9**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 259 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXFDAAPPROVALDATECMPS-360-27JUL01 | Before July 2027 | 46c | 8.0c | 53 | 216 | 124 | 216 | 1904 | $1087 | 30d+ |
| KXVACCINEREC-27-C19 | COVID-19 | 16c | 6.0c | 100 | 500 | 300 | 500 | 1732 | $0 | 30d+ |
| KXFDAAPPROVALDATENTLA-LONV-27JUL01 | Before July 2027 | 32c | 9.0c | 37 | 505 | 37 | 505 | 1094 | $8 | 30d+ |
| KXVACCINEREC-27-HEPB | Hepatitis B | 14c | 8.0c | 32 | 500 | 32 | 532 | 956 | $0 | 30d+ |
| KXNEWDRUGAPPNTLA-LONV-26NOV01 | before November | 57c | 10.0c | 250 | 250 | 250 | 250 | 898 | $0 | 30d+ |
| KXFDAAPPROVALDATECMPS-360-27OCT01 | Before October 2027 | 64c | 2.0c | 5 | 200 | 5 | 200 | 812 | $343 | 30d+ |
| KXNEWDRUGAPPLICATIONCMPS-360-26SEP01 | before September | 25c | 10.0c | 250 | 250 | 250 | 0 | 723 | $723 | 30d+ |
| KXNEWDRUGAPPNTLA-LONV-26DEC01 | before December | 60c | 10.0c | 250 | 250 | 250 | 250 | 511 | $0 | 30d+ |
| KXNEWDRUGAPPBEAM-RIST-27APR01 | before April 2027 | 74c | 8.0c | 1 | 500 | 501 | 500 | 501 | $0 | 30d+ |
| KXNEWDRUGAPPLICATIONCMPS-360-26OCT01 | before October | 36c | 8.0c | 4 | 375 | 36 | 375 | 412 | $416 | 30d+ |
| KXVACCINEREC-27-FLU | Influenza | 12c | 5.0c | 200 | 500 | 200 | 500 | 374 | $0 | 30d+ |
| KXNEWDRUGAPPLICATIONCMPS-360-26NOV01 | before November | 51c | 8.0c | 32 | 250 | 282 | 250 | 326 | $136 | 30d+ |
| KXVACCINEREC-27-ROT | Rotavirus | 7c | 3.4c | 500 | 500 | 500 | 500 | 232 | $0 | 30d+ |
| KXNEWDRUGAPPNTLA-LONV-26OCT01 | before October | 48c | 9.0c | 32 | 250 | 32 | 250 | 210 | $0 | 30d+ |
| KXNEWDRUGAPPNTLA-LONV-26SEP01 | before September | 41c | 10.0c | 250 | 250 | 250 | 250 | 202 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXVACCINEREC | Vaccine rec ended | custom | 6 | 3 | $0 | 3,396 | 6.3c |
| KXFDAAPPROVALDATECMPS | Compass Pathways Drug Approval | one_off | 3 | 3 | $1,430 | 2,807 | 5.3c |
| KXNEWDRUGAPPNTLA | Intellia Therapeutics Drug Application | one_off | 6 | 6 | $0 | 1,896 | 9.7c |
| KXNEWDRUGAPPLICATIONCMPS | Compass Pathways Drug Application | one_off | 6 | 6 | $1,275 | 1,533 | 7.7c |
| KXFDAAPPROVALDATENTLA | Intellia Therapeutics drug approval date | one_off | 3 | 3 | $8 | 1,132 | 8.7c |
| KXNEWDRUGAPPBEAM | Beam Therapeutics Drug Application | one_off | 6 | 6 | $0 | 695 | 8.0c |
| KXNEWOUTBREAK-P | New pandemic | custom | 1 | 0 | $6 | 388 | nanc |

## Curated notes

<!-- KEEP-START -->
<!-- Add market structure, resolution mechanics, time-of-day / TTE patterns, informed-flow analysis, verdict here -->

### Market structure
- Resolution mechanism:
- Frequency:
- Typical close time:

### Informed flow profile
- Retail vs pro:
- HFT presence:
- Known asymmetries:

### Time windows (UTC) / TTE behavior
- Safe:
- Quiet:
- Dangerous:
- Key events:
- TTE pattern: when does informed_signal_c spike?

### Verdict
- v0 target?
- Notes:
<!-- KEEP-END -->
