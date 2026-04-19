# sports_soccer_kleague

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **36** (24 contested)
- Total 24h volume: **$4,788**
- Total open interest: **4,268**
- Top-OI mean spread (median across series): **1.0 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **24**
- Median spread: **8.0c**
- Median TOB bid / ask size: **756 / 55** contracts
- Median depth within 5c of best bid / ask — **1500 / 734** contracts
- Median depth within 10c of best bid / ask — **1500 / 887** contracts
- Median depth within 5c of midpoint — bid: **1000** / ask: **152** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **27**
- Mean informed-signal proxy: **-1.442** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.03c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 638 | 1.19 | -0.168 | 5.00 | 98.6 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXKLEAGUEGAME-26APR19ULSGWA-ULS | Ulsan HD | 80c | 3.0c | 10 | 15 | 52 | 4326 | 52 | 7503 | 3082 | $3339 | 7-30d |
| KXKLEAGUEGAME-26APR19POHANY-POH | Pohang Steelers | 43c | 1.0c | 1664 | 81 | 4495 | 4401 | 4495 | 4901 | 934 | $921 | 7-30d |
| KXKLEAGUEGAME-26APR19ULSGWA-GWA | Gwangju | 5c | 1.0c | 10 | 81 | 4039 | 3284 | 4039 | 3652 | 136 | $264 | 7-30d |
| KXKLEAGUEGAME-26APR19POHANY-ANY | FC Anyang | 25c | 2.0c | 2039 | 2039 | 4602 | 4328 | 4602 | 4828 | 117 | $176 | 7-30d |
| KXKLEAGUEGAME-26APR21SEOBUC-BUC | Bucheon | 18c | 9.0c | 400 | 29 | 400 | 429 | 2134 | 429 | 80 | $160 | 7-30d |
| KXKLEAGUEGAME-26APR19ULSGWA-TIE | Tie | 16c | 2.0c | 68 | 20 | 179 | 3942 | 1079 | 3942 | 47 | $48 | 7-30d |
| KXKLEAGUEGAME-26APR21SEOBUC-SEO | Seoul | 58c | 5.0c | 40 | 1360 | 440 | 1360 | 440 | 1360 | 40 | $40 | 7-30d |
| KXKLEAGUEGAME-26APR19POHANY-TIE | Tie | 31c | 1.0c | 1896 | 168 | 4378 | 3954 | 4378 | 4954 | 6 | $6 | 7-30d |
| KXKLEAGUEGAME-26APR22ANYULS-ANY | FC Anyang | 43c | 77.0c | 512 | 100 | 6339 | 734 | 6339 | 887 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21JEOINC-JEO | Jeonbuk | 49c | 8.0c | 1000 | 2 | 1500 | 502 | 1500 | 502 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21JEOINC-TIE | Tie | 27c | 8.0c | 1000 | 1 | 1500 | 693 | 1500 | 693 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21GISGAW-GAW | Gangwon | 39c | 8.0c | 1000 | 1 | 1400 | 401 | 1400 | 401 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21GISGAW-GIS | Gimcheon Sangmu | 33c | 8.0c | 1000 | 1 | 1400 | 550 | 1400 | 550 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21GISGAW-TIE | Tie | 28c | 7.0c | 1000 | 1 | 1400 | 522 | 1400 | 522 | 0 | $0 | 7-30d |
| KXKLEAGUEGAME-26APR21SEOBUC-TIE | Tie | 26c | 9.0c | 1000 | 400 | 1400 | 400 | 1400 | 400 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXKLEAGUEGAME | Korea K League Game | custom | 24 | 24 | $4,788 | 4,268 | 1.0c |
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
