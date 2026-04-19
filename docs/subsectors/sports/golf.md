# sports_golf

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **32** (32 with open markets)
- Open markets: **1375** (307 contested)
- Total 24h volume: **$13,794,187**
- Total open interest: **52,140,054**
- Top-OI mean spread (median across series): **2.2 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **199**
- Median spread: **3.0c**
- Median TOB bid / ask size: **111 / 344** contracts
- Median depth within 5c of best bid / ask — **2466 / 6290** contracts
- Median depth within 10c of best bid / ask — **3901 / 10718** contracts
- Median depth within 5c of midpoint — bid: **1598** / ask: **4677** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **163**
- Mean informed-signal proxy: **-0.818** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.71c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 2000 | 0.30 | -0.286 | 1.00 | 214.0 |
| 7-30d | 13013 | 3.00 | -1.032 | 13.00 | 58.9 |
| 30d+ | 17435 | 1.54 | -0.448 | 7.00 | 93.6 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPGATOUR-RBH26-SSCH | Scottie Scheffler | 26c | 1.0c | 28958 | 636993 | 125948 | 2147115 | 188740 | 2148358 | 4498942 | $3110840 | 1-3d |
| KXPGATOUR-RBH26-MFIT | Matt Fitzpatrick | 54c | 1.0c | 4 | 390606 | 283726 | 1222350 | 293928 | 1222537 | 1450066 | $1081967 | 1-3d |
| KXPGATOUR-PGC26-SSCH | Scottie Scheffler | 19c | 1.0c | 1123 | 2236 | 21717 | 72984 | 21977 | 72984 | 116050 | $18171 | 30d+ |
| KXPGATOP20-RBH26-JSPI | Jordan Spieth | 8c | 3.0c | 2970 | 344 | 4605 | 6116 | 7537 | 17366 | 111523 | $4299 | 7-30d |
| KXPGATOUR-PGC26-RMCI | Rory McIlroy | 9c | 1.0c | 3842 | 521 | 13129 | 177561 | 24169 | 190111 | 108245 | $9602 | 30d+ |
| KXPGATOP5-RBH26-SSCH | Scottie Scheffler | 78c | 1.0c | 65 | 8 | 1863 | 69 | 8559 | 24570 | 104367 | $35756 | 7-30d |
| KXPGATOP10-RBH26-SSCH | Scottie Scheffler | 94c | 2.0c | 12 | 52 | 5553 | 46508 | 11803 | 46508 | 62546 | $20342 | 7-30d |
| KXPGATOP20-RBH26-PCAN | Patrick Cantlay | 90c | 3.0c | 65 | 7 | 4780 | 28088 | 10335 | 28395 | 56343 | $2962 | 7-30d |
| KXPGAMAJORWIN-26-SSCH | Scottie Scheffler | 46c | 3.0c | 32 | 5704 | 1343 | 22422 | 1907 | 22422 | 45299 | $552 | 30d+ |
| KXPGATOP20-RBH26-BHAR | Brian Harman | 86c | 2.0c | 6609 | 200 | 12717 | 671 | 17478 | 48880 | 40599 | $4132 | 7-30d |
| KXPGATOP20-RBH26-CAME | Cameron Young | 52c | 2.0c | 47 | 3493 | 1158 | 4611 | 2912 | 13750 | 36218 | $3991 | 7-30d |
| KXPGATOP20-RBH26-LABE | Ludvig Aberg | 88c | 3.0c | 350 | 177 | 1349 | 13540 | 10515 | 24508 | 34441 | $3648 | 7-30d |
| KXPGATOP20-RBH26-JBRI | Jacob Bridgeman | 30c | 1.0c | 7 | 2090 | 1538 | 3169 | 2803 | 5733 | 30733 | $2307 | 7-30d |
| KXPGAMAJORWIN-26-CYOU | Cameron Young | 19c | 2.0c | 33 | 1746 | 3346 | 5646 | 9635 | 5947 | 28826 | $292 | 30d+ |
| KXPGATOP20-RBH26-SBUR | Sam Burns | 54c | 8.0c | 98 | 3450 | 2034 | 22634 | 5728 | 26126 | 27269 | $633 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPGATOUR | PGA Tour | custom | 148 | 3 | $13,394,898 | 49,128,753 | 1.0c |
| KXPGATOP20 | PGA Top 20 Finisher | custom | 147 | 41 | $107,153 | 1,362,738 | 1.3c |
| KXPGATOP10 | PGA Top 10 Finisher | custom | 147 | 31 | $86,426 | 528,864 | 3.3c |
| KXPGATOP5 | PGA Top 5 Finisher | custom | 147 | 18 | $81,648 | 445,565 | 1.3c |
| KXPGAMAJORWIN | PGA Major Winner | custom | 52 | 9 | $1,484 | 285,349 | 3.7c |
| KXLPGATOUR | PGA Tour | custom | 65 | 5 | $54,731 | 118,420 | 14.3c |
| KXPGAMAJORTOP10 | PGA Top 10 for All 4 Majors | annual | 11 | 7 | $562 | 60,677 | 1.7c |
| KXPGAHOLEINONE | PGA Hole in One | custom | 3 | 1 | $25,602 | 42,300 | 1.0c |
| KXGOLFMAJORS | Golf Majors Won | custom | 3 | 2 | $447 | 32,099 | 1.0c |
| KXPGAPLAYOFF | Golf Playoff | custom | 1 | 1 | $16,111 | 26,860 | 2.0c |

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
