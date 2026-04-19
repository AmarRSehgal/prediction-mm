# weather_rain

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **13** (13 with open markets)
- Open markets: **72** (20 contested)
- Total 24h volume: **$51,594**
- Total open interest: **316,960**
- Top-OI mean spread (median across series): **4.5 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **29**
- Median spread: **4.0c**
- Median TOB bid / ask size: **32 / 41** contracts
- Median cumulative depth within 5c of mid — bid: **416** / ask: **433** contracts
- Median cumulative depth within 10c of mid — bid: **631** / ask: **554** contracts
- Mean trades per market (last 3000): **311**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 15m-1h | 10 | 0.00 | 0.000 | 0.00 | 0.0 |
| 1-6h | 87 | 0.00 | 0.000 | 0.00 | 0.0 |
| 6-12h | 31 | 0.00 | 0.000 | 0.00 | 0.0 |
| 12-24h | 50 | 0.00 | 0.000 | 0.00 | 0.0 |
| 1-3d | 34 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 8993 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 26 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXRAINSFOM-26APR-3 | Above 3 inches | 88c | 5.0c | 16 | 58 | 416 | 578 | 14302 | $4872 | 7-30d |
| KXRAINCHIM-26APR-7 | Above 7 inches | 11c | 2.0c | 2 | 247 | 1202 | 3578 | 9318 | $2699 | 7-30d |
| KXRAINCHIM-26APR-6 | Above 6 inches | 30c | 2.0c | 42 | 14 | 905 | 2219 | 8516 | $3632 | 7-30d |
| KXRAINDENM-26APR-1 | Above 1 inch | 31c | 8.0c | 400 | 400 | 400 | 400 | 8148 | $960 | 7-30d |
| KXRAINDENM-26APR-3 | Above 3 inches | 5c | 5.0c | 430 | 401 | 1764 | 1457 | 8016 | $106 | 7-30d |
| KXRAINSFOM-26APR-4 | Above 4 inches | 9c | 4.0c | 25 | 23 | 426 | 464 | 6171 | $2837 | 7-30d |
| KXRAINNYCM-26APR-2 | 2 inches | 32c | 1.0c | 6 | 1 | 285 | 433 | 5723 | $637 | 7-30d |
| KXRAINCHIM-26APR-5 | Above 5 inches | 80c | 3.0c | 6 | 19 | 473 | 455 | 5592 | $1687 | 7-30d |
| KXRAINSEAM-26APR-3 | Above 3 inches | 27c | 2.0c | 32 | 32 | 448 | 327 | 5398 | $514 | 7-30d |
| KXRAINNYCM-26APR-4 | 4 inches | 5c | 5.0c | 200 | 429 | 631 | 479 | 5064 | $109 | 7-30d |
| KXRAINNYCM-26APR-3 | 3 inches | 12c | 3.0c | 32 | 41 | 528 | 446 | 4902 | $752 | 7-30d |
| KXRAINNYCM-26APR-1 | 1 inches | 82c | 1.0c | 1157 | 18 | 1602 | 483 | 4705 | $238 | 7-30d |
| KXRAINHOUM-26APR-6 | Above 6 inches | 40c | 10.0c | 9 | 3 | 9 | 3 | 4508 | $3119 | 7-30d |
| KXRAINHOUM-26APR-5 | Above 5 inches | 66c | 23.0c | 12 | 17 | 0 | 0 | 4424 | $3909 | 7-30d |
| KXRAINHOUM-26APR-4 | Above 4 inches | 67c | 48.0c | 1 | 1 | 0 | 0 | 4171 | $3738 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXRAINSFOM | RAIN SAN FRANCISCO | custom | 7 | 1 | $8,634 | 75,872 | 4.0c |
| KXRAINCHIM | Rain Chicago | monthly | 7 | 3 | $9,354 | 35,081 | 2.3c |
| KXRAINDENM | RAIN DENVER | monthly | 7 | 1 | $2,946 | 35,076 | 8.0c |
| KXRAINLAXM | Rain Los Angeles | custom | 7 | 0 | $2,612 | 33,588 | nanc |
| KXRAINHOUM | Rain Houston | custom | 7 | 3 | $12,332 | 30,763 | 8.3c |
| KXRAINSEAM | RAIN SEATTLE | custom | 7 | 1 | $1,709 | 22,101 | 4.0c |
| KXRAINNYCM | Monthly rain in New York | monthly | 4 | 3 | $1,485 | 19,988 | 1.7c |
| KXRAINMIAM | Rain Miami | custom | 7 | 2 | $2,148 | 16,185 | 3.5c |
| KXRAINDALM | Rain Dallas | custom | 7 | 3 | $2,530 | 16,117 | 5.0c |
| KXRAINAUSM | RAIN AUSTIN | custom | 7 | 2 | $1,517 | 15,752 | 7.0c |

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
