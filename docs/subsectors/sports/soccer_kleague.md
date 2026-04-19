# sports_soccer_kleague

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **36** (24 contested)
- Total 24h volume: **$494**
- Total open interest: **361**
- Top-OI mean spread (median across series): **1.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **24**
- Median spread: **8.0c**
- Median TOB bid / ask size: **756 / 10** contracts
- Median cumulative depth within 5c of mid — bid: **1400** / ask: **400** contracts
- Median cumulative depth within 10c of mid — bid: **1400** / ask: **570** contracts
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 60 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXKLEAGUEGAME-26APR19POHANY-POH | Pohang Steelers | 43c | 1.0c | 1 | 1773 | 3278 | 4950 | 573 | $196 | 7-30d |
| KXKLEAGUEGAME-26APR19POHANY-ANY | FC Anyang | 26c | 1.0c | 1 | 1753 | 3793 | 4583 | 117 | $127 | 7-30d |
| KXKLEAGUEGAME-26APR19ULSGWA-GWA | Gwangju | 15c | 1.0c | 2234 | 7 | 6162 | 3537 | 63 | $183 | 7-30d |
| KXKLEAGUEGAME-26APR19ULSGWA-ULS | Ulsan HD | 62c | 1.0c | 325 | 1760 | 4490 | 5887 | 61 | $58 | 7-30d |
| KXKLEAGUEGAME-26APR21SEOBUC-SEO | Seoul | 58c | 5.0c | 40 | 1360 | 40 | 1360 | 40 | $40 | 7-30d |
| KXKLEAGUEGAME-26APR19ULSGWA-TIE | Tie | 24c | 1.0c | 21 | 1589 | 5790 | 4272 | 8 | $9 | 7-30d |
| KXKLEAGUEGAME-26APR19POHANY-TIE | Tie | 31c | 1.0c | 1715 | 159 | 6839 | 3614 | 6 | $6 | 7-30d |
| KXKLEAGUEGAME-26APR22ANYULS-ANY | FC Anyang | 42c | 76.0c | 512 | 10 | 0 | 0 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21JEOINC-JEO | Jeonbuk | 48c | 8.0c | 1000 | 2 | 1400 | 402 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21JEOINC-TIE | Tie | 28c | 8.0c | 1000 | 1 | 1400 | 593 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21GISGAW-GAW | Gangwon | 39c | 8.0c | 1000 | 1 | 1400 | 401 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21GISGAW-GIS | Gimcheon Sangmu | 31c | 5.0c | 1000 | 1 | 1400 | 201 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21GISGAW-TIE | Tie | 29c | 8.0c | 1000 | 1 | 1400 | 548 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21SEOBUC-BUC | Bucheon | 18c | 9.0c | 400 | 29 | 400 | 29 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21SEOBUC-TIE | Tie | 26c | 9.0c | 1000 | 400 | 1000 | 400 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXKLEAGUEGAME | Korea K League Game | custom | 24 | 24 | $494 | 361 | 1.0c |
| KXKLEAGUE | Korea K League Winner | annual | 12 | 0 | $0 | 0 | nanc |

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
