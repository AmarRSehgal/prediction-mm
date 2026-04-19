# sports_rugby

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **6** (6 with open markets)
- Open markets: **77** (37 contested)
- Total 24h volume: **$1,116**
- Total open interest: **2,231**
- Top-OI mean spread (median across series): **25.1 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **39**
- Median spread: **93.0c**
- Median TOB bid / ask size: **500 / 10** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 58 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 16 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXRUGBYNRLMATCH-26APR19SYDNEW-SYD | Sydney Roosters | 44c | 80.0c | 225 | 5 | 0 | 0 | 571 | $567 | 7-30d |
| KXRUGBYNRLMATCH-26APR19SYDNEW-NEW | Newcastle Knights | 21c | 10.0c | 6 | 2 | 0 | 2 | 477 | $453 | 7-30d |
| KXRUGBYFRA14MATCH-26APR19RACSFP-RAC | Racing 92 | 50c | 94.0c | 10 | 5 | 0 | 0 | 127 | $127 | 7-30d |
| KXNRLCHAMP-26-PEN | Penrith Panthers | 40c | 9.0c | 122 | 555 | 122 | 555 | 122 | $0 | 30d+ |
| KXRUGBYESLMATCH-26APR19WGWCAS-TIE | Tie | 8c | 14.0c | 10 | 98 | 0 | 0 | 100 | $100 | 7-30d |
| KXRUGBYNRLMATCH-26APR19PARCBB-PAR | Parramatta Eels | 20c | 2.0c | 50 | 3 | 736 | 937 | 74 | $5 | 7-30d |
| KXNRLCHAMP-26-WTG | Wests Tigers | 7c | 6.0c | 48 | 200 | 48 | 400 | 48 | $0 | 30d+ |
| KXNRLCHAMP-26-SYD | Sydney Roosters | 16c | 9.0c | 47 | 400 | 47 | 400 | 47 | $0 | 30d+ |
| KXNRLCHAMP-26-BRI | Brisbane Broncos | 17c | 8.0c | 47 | 420 | 47 | 1535 | 47 | $0 | 30d+ |
| KXNRLCHAMP-26-MBS | Melbourne Storm | 11c | 9.0c | 39 | 420 | 39 | 420 | 39 | $0 | 30d+ |
| KXRUGBYNRLMATCH-26APR23WTGCBR-CBR | Canberra Raiders | 48c | 93.0c | 10 | 1111 | 0 | 0 | 11 | $11 | 7-30d |
| KXRUGBYFRA14MATCH-26APR19RACSFP-TIE | Tie | 49c | 94.0c | 25 | 10 | 0 | 0 | 1 | $1 | 7-30d |
| KXRUGBYNRLMATCH-26APR24BRICBB-BRI | Brisbane Broncos | 48c | 93.0c | 500 | 10 | 0 | 0 | 0 | $0 | 7-30d |
| KXRUGBYNRLMATCH-26APR25SGISYD-SYD | Sydney Roosters | 48c | 94.0c | 500 | 10 | 0 | 0 | 0 | $0 | 7-30d |
| KXRUGBYNRLMATCH-26APR25SGISYD-SGI | St. George Illawarra Dragons | 48c | 94.0c | 500 | 10 | 0 | 0 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXRUGBYNRLMATCH | Rugby NRL Match | custom | 30 | 28 | $888 | 987 | 2.7c |
| KXNRLCHAMP | National Rugby League Champion | annual | 17 | 4 | $0 | 708 | 8.7c |
| KXPREMCHAMP | Gallagher Premiership Champion | custom | 10 | 0 | $0 | 308 | nanc |
| KXRUGBYFRA14MATCH | Rugby French 14 Match | custom | 3 | 3 | $128 | 128 | 70.3c |
| KXRUGBYESLMATCH | England Super League Rugby Match | custom | 3 | 2 | $100 | 100 | 41.5c |
| KXFRA14CHAMP | France Top 14 Champion | annual | 14 | 0 | $0 | 0 | nanc |

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
