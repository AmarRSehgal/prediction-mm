# sports_rugby_nrl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **32** (32 contested)
- Total 24h volume: **$3,629**
- Total open interest: **3,244**
- Top-OI mean spread (median across series): **51.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **32**
- Median spread: **95.0c**
- Median TOB bid / ask size: **500 / 72** contracts
- Median depth within 5c of best bid / ask — **500 / 2796** contracts
- Median depth within 10c of best bid / ask — **500 / 2796** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **-3.834** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **7.90c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 55 | 7.71 | -0.059 | 52.00 | 96.6 |
| 30d+ | 16 | 5.36 | -0.636 | 21.00 | 46.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXRUGBYNRLMATCH-26APR19PARCBB-PAR | Parramatta Eels | 51c | 96.0c | 20 | 0 | 1100 | 0 | 1100 | 0 | 1863 | $1789 | 7-30d |
| KXRUGBYNRLMATCH-26APR19PARCBB-TIE | Tie | 50c | 96.0c | 1 | 33 | 11 | 33 | 11 | 33 | 1047 | $1809 | 7-30d |
| KXNRLCHAMP-26-PEN | Penrith Panthers | 40c | 9.0c | 122 | 555 | 122 | 855 | 122 | 855 | 122 | $0 | 30d+ |
| KXNRLCHAMP-26-WTG | Wests Tigers | 7c | 6.0c | 48 | 200 | 48 | 400 | 48 | 400 | 48 | $0 | 30d+ |
| KXNRLCHAMP-26-SYD | Sydney Roosters | 16c | 9.0c | 47 | 400 | 47 | 1511 | 47 | 1511 | 47 | $0 | 30d+ |
| KXNRLCHAMP-26-BRI | Brisbane Broncos | 17c | 8.0c | 47 | 420 | 47 | 1535 | 47 | 1535 | 47 | $0 | 30d+ |
| KXNRLCHAMP-26-MBS | Melbourne Storm | 11c | 9.0c | 39 | 420 | 136 | 420 | 136 | 420 | 39 | $0 | 30d+ |
| KXRUGBYNRLMATCH-26APR19PARCBB-CBB | Canterbury Bulldogs | 48c | 94.0c | 13 | 5 | 13 | 1293 | 13 | 1293 | 21 | $21 | 7-30d |
| KXRUGBYNRLMATCH-26APR23WTGCBR-CBR | Canberra Raiders | 48c | 93.0c | 10 | 1111 | 510 | 5102 | 510 | 5102 | 11 | $11 | 7-30d |
| KXRUGBYNRLMATCH-26APR24BRICBB-CBB | Canterbury Bulldogs | 48c | 94.0c | 500 | 1111 | 500 | 4970 | 500 | 4970 | 0 | $0 | 7-30d |
| KXRUGBYNRLMATCH-26APR25SGISYD-SYD | Sydney Roosters | 48c | 95.0c | 500 | 72 | 500 | 2798 | 500 | 2798 | 0 | $0 | 7-30d |
| KXRUGBYNRLMATCH-26APR25SGISYD-SGI | St. George Illawarra Dragons | 48c | 95.0c | 500 | 72 | 500 | 2796 | 500 | 2796 | 0 | $0 | 7-30d |
| KXRUGBYNRLMATCH-26APR24BRICBB-TIE | Tie | 48c | 94.0c | 500 | 1111 | 500 | 4990 | 500 | 4990 | 0 | $0 | 7-30d |
| KXRUGBYNRLMATCH-26APR24NQUCSS-CSS | Cronulla Sharks | 48c | 94.0c | 500 | 1111 | 500 | 4976 | 500 | 4976 | 0 | $0 | 7-30d |
| KXRUGBYNRLMATCH-26APR24BRICBB-BRI | Brisbane Broncos | 48c | 94.0c | 500 | 1111 | 500 | 4986 | 500 | 4986 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXRUGBYNRLMATCH | Parramatta Eels | nan | 27 | 27 | $3,629 | 2,941 | 95.3c |
| KXNRLCHAMP | Penrith Panthers | nan | 5 | 5 | $0 | 303 | 8.0c |

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
