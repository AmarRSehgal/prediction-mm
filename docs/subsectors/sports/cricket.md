# sports_cricket

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **4** (4 with open markets)
- Open markets: **56** (54 contested)
- Total 24h volume: **$605,786**
- Total open interest: **663,700**
- Top-OI mean spread (median across series): **24.0 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **54**
- Median spread: **52.5c**
- Median TOB bid / ask size: **17 / 114** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **106**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 4748 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 990 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXIPLGAME-26APR19RRKKR-RR | Rajasthan Royals | 62c | 1.0c | 5117 | 87160 | 6867 | 253343 | 279870 | $258404 | 3-7d |
| KXIPLGAME-26APR19RRKKR-KKR | Kolkata Knight Riders | 38c | 1.0c | 101746 | 155300 | 107539 | 310731 | 188963 | $186948 | 3-7d |
| KXIPLGAME-26APR19LSGPBKS-PBKS | Punjab Kings | 62c | 1.0c | 107023 | 8161 | 109434 | 108559 | 147036 | $120548 | 3-7d |
| KXIPLGAME-26APR19LSGPBKS-LSG | Lucknow Super Giants | 38c | 1.0c | 101555 | 70900 | 101672 | 172781 | 60384 | $57555 | 3-7d |
| KXIPLGAME-26APR20MIGT-MI | Mumbai Indians | 53c | 2.0c | 650 | 328 | 1433 | 2049 | 11712 | $7452 | 3-7d |
| KXIPLGAME-26APR20MIGT-GT | Gujarat Titans | 48c | 2.0c | 126 | 501 | 1489 | 1882 | 8421 | $5356 | 3-7d |
| KXPSLGAME-26APR19MUSKKI-MUS | Multan Sultans | 60c | 11.0c | 1 | 39 | 0 | 0 | 4493 | $4376 | 3-7d |
| KXCRICKETODIMATCH-26APR20NZBAN-NZ | New Zealand | 52c | 17.0c | 19 | 3 | 0 | 0 | 4346 | $4355 | 3-7d |
| KXIPLGAME-26APR21DCSRH-SRH | Sunrisers Hyderabad | 52c | 5.0c | 41 | 99 | 51 | 117 | 3814 | $2124 | 3-7d |
| KXIPLGAME-26APR21DCSRH-DC | Delhi Capitals | 50c | 3.0c | 117 | 113 | 131 | 476 | 3074 | $1709 | 3-7d |
| KXPSLGAME-26APR19QGLPZA-PZA | Peshawar Zalmi | 65c | 10.0c | 250 | 235 | 250 | 235 | 3043 | $2881 | 3-7d |
| KXCRICKETODIMATCH-26APR20NZBAN-BAN | Bangladesh | 55c | 10.0c | 1 | 7 | 1 | 7 | 2525 | $2572 | 3-7d |
| KXIPLGAME-26APR22RRLSG-RR | Rajasthan Royals | 65c | 4.0c | 263 | 101 | 999 | 1956 | 1872 | $475 | 3-7d |
| KXIPLGAME-26APR23CSKMI-CSK | Chennai Super Kings | 42c | 5.0c | 50 | 108 | 65 | 108 | 1724 | $478 | 7-30d |
| KXIPLGAME-26APR23CSKMI-MI | Mumbai Indians | 60c | 3.0c | 33 | 168 | 33 | 538 | 1070 | $639 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXIPLGAME | Indian Premier League Cricket Game | custom | 24 | 24 | $588,033 | 645,496 | 1.0c |
| KXPSLGAME | Pakistan Super League Cricket Game | custom | 22 | 22 | $8,522 | 9,129 | 26.0c |
| KXCRICKETODIMATCH | Cricket ODI Match | custom | 2 | 2 | $6,766 | 6,666 | 22.0c |
| KXT20MATCH | T20 Match | custom | 8 | 6 | $2,466 | 2,410 | 58.0c |

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
