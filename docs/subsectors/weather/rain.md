# weather_rain

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **13** (13 with open markets)
- Open markets: **71** (19 contested)
- Total 24h volume: **$38,763**
- Total open interest: **316,189**
- Top-OI mean spread (median across series): **4.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **26**
- Median spread: **4.0c**
- Median TOB bid / ask size: **88 / 253** contracts
- Median depth within 5c of best bid / ask — **482 / 460** contracts
- Median depth within 10c of best bid / ask — **734 / 882** contracts
- Median depth within 5c of midpoint — bid: **400** / ask: **426** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **327**
- Mean informed-signal proxy: **-0.499** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.43c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 8474 | 2.13 | -0.424 | 8.00 | 35.3 |
| 30d+ | 26 | 3.68 | -1.227 | 9.00 | 46.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXRAINHOUM-26APR-3 | Above 3 inches | 98c | 1.0c | 200 | 121 | 200 | 121 | 200 | 121 | 12161 | $142 | 7-30d |
| KXRAINCHIM-26APR-7 | Above 7 inches | 11c | 2.0c | 2 | 223 | 1860 | 3553 | 2703 | 4449 | 9318 | $1291 | 7-30d |
| KXRAINCHIM-26APR-6 | Above 6 inches | 31c | 4.0c | 56 | 284 | 1126 | 2205 | 1626 | 2264 | 8806 | $1912 | 7-30d |
| KXRAINDENM-26APR-1 | Above 1 inch | 31c | 8.0c | 400 | 400 | 400 | 400 | 800 | 1108 | 8148 | $947 | 7-30d |
| KXRAINDENM-26APR-3 | Above 3 inches | 5c | 5.0c | 473 | 401 | 1823 | 1457 | 1823 | 2346 | 8016 | $106 | 7-30d |
| KXRAINNYCM-26APR-2 | 2 inches | 34c | 3.0c | 6 | 432 | 685 | 445 | 685 | 884 | 5743 | $657 | 7-30d |
| KXRAINCHIM-26APR-5 | Above 5 inches | 80c | 2.0c | 12 | 419 | 121 | 492 | 521 | 961 | 5592 | $864 | 7-30d |
| KXRAINSEAM-26APR-3 | Above 3 inches | 31c | 3.0c | 56 | 410 | 628 | 410 | 628 | 1049 | 5558 | $669 | 7-30d |
| KXRAINNYCM-26APR-4 | 4 inches | 5c | 5.0c | 200 | 429 | 631 | 529 | 631 | 959 | 5064 | $109 | 7-30d |
| KXRAINNYCM-26APR-3 | 3 inches | 12c | 5.0c | 496 | 400 | 897 | 487 | 3413 | 887 | 4902 | $747 | 7-30d |
| KXRAINNYCM-26APR-1 | 1 inches | 82c | 1.0c | 1157 | 18 | 1602 | 526 | 1638 | 892 | 4705 | $238 | 7-30d |
| KXRAINHOUM-26APR-6 | Above 6 inches | 40c | 10.0c | 9 | 2 | 309 | 52 | 327 | 96 | 4508 | $3119 | 7-30d |
| KXRAINHOUM-26APR-5 | Above 5 inches | 87c | 12.0c | 99 | 15 | 550 | 73 | 550 | 324 | 4441 | $3698 | 7-30d |
| KXRAINHOUM-26APR-4 | Above 4 inches | 92c | 13.0c | 100 | 2 | 692 | 65 | 692 | 65 | 4226 | $3419 | 7-30d |
| KXRAINMIAM-26APR-5 | Above 5 inches | 5c | 3.0c | 400 | 108 | 698 | 305 | 698 | 705 | 3881 | $716 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXRAINSFOM | RAIN SAN FRANCISCO | custom | 7 | 0 | $7,384 | 76,163 | nanc |
| KXRAINCHIM | Rain Chicago | monthly | 7 | 3 | $4,167 | 35,371 | 2.3c |
| KXRAINDENM | RAIN DENVER | monthly | 7 | 1 | $1,348 | 35,076 | 8.0c |
| KXRAINLAXM | Rain Los Angeles | custom | 7 | 0 | $1,089 | 33,613 | nanc |
| KXRAINHOUM | Rain Houston | custom | 7 | 4 | $12,121 | 30,849 | 19.7c |
| KXRAINSEAM | RAIN SEATTLE | custom | 7 | 1 | $1,551 | 22,261 | 3.0c |
| KXRAINNYCM | Monthly rain in New York | monthly | 4 | 3 | $1,750 | 20,413 | 1.7c |
| KXRAINMIAM | Rain Miami | custom | 7 | 2 | $2,109 | 16,185 | 2.5c |
| KXRAINDALM | Rain Dallas | custom | 7 | 3 | $2,533 | 16,141 | 5.0c |
| KXRAINAUSM | RAIN AUSTIN | custom | 7 | 2 | $1,344 | 15,821 | 5.0c |

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
