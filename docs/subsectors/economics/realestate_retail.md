# eco_realestate_retail

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **16** (5 contested)
- Total 24h volume: **$706**
- Total open interest: **52,511**
- Top-OI mean spread (median across series): **4.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **8**
- Median spread: **6.0c**
- Median TOB bid / ask size: **140 / 262** contracts
- Median cumulative depth within 5c of mid — bid: **250** / ask: **420** contracts
- Median cumulative depth within 10c of mid — bid: **269** / ask: **437** contracts
- Mean trades per market (last 3000): **258**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 831 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 1233 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXHFHOUSING-27 | Before Jan 1, 2027 | 64c | 1.0c | 5976 | 388 | 5976 | 1138 | 29442 | $84 | 30d+ |
| KXHOUSINGSTART-26APR17-T1.325 | Above 1.325M | 70c | 9.0c | 259 | 272 | 259 | 272 | 10173 | $507 | 7-30d |
| KXBUILDPERMS-26APR17-T1.400 | Above 1.400M | 7c | 5.0c | 1 | 167 | 1 | 417 | 2924 | $38 | 7-30d |
| KXBUILDPERMS-26APR17-T1.350 | Above 1.350M | 37c | 4.0c | 29 | 24 | 279 | 452 | 2683 | $3 | 7-30d |
| KXHOUSINGSTART-26APR17-T1.375 | Above 1.375M | 14c | 7.0c | 1 | 265 | 1 | 423 | 2606 | $59 | 7-30d |
| KXBUILDPERMS-26APR17-T1.300 | Above 1.300M | 90c | 9.0c | 250 | 250 | 250 | 250 | 1279 | $73 | 7-30d |
| KXHOUSINGSTART-26APR17-T1.350 | Above 1.350M | 34c | 5.0c | 22 | 259 | 22 | 259 | 738 | $0 | 7-30d |
| KXHOUSINGSTART-26APR17-T1.400 | Above 1.400M | 6c | 9.0c | 250 | 451 | 250 | 451 | 618 | $62 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXHFHOUSING | Bill taxing/banning hedge funds owning s | custom | 1 | 1 | $84 | 29,442 | 1.0c |
| KXHOUSINGSTART | Monthly housing starts | custom | 8 | 3 | $508 | 15,363 | 6.7c |
| KXBUILDPERMS | Building permits for month | custom | 7 | 1 | $114 | 7,706 | 4.0c |

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
