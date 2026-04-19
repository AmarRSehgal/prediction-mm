# sports_soccer_polish

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **30** (13 contested)
- Total 24h volume: **$535**
- Total open interest: **1,200**
- Top-OI mean spread (median across series): **40.5 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **13**
- Median spread: **1.0c**
- Median TOB bid / ask size: **58 / 134** contracts
- Median cumulative depth within 5c of mid — bid: **927** / ask: **646** contracts
- Median cumulative depth within 10c of mid — bid: **959** / ask: **754** contracts
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 28 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXEKSTRAKLASAGAME-26APR19NIEPLO-PLO | Wisla Plock | 36c | 1.0c | 13 | 179 | 668 | 1618 | 413 | $413 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19ARKJAG-JAG | Jagiellonia | 44c | 2.0c | 59 | 166 | 544 | 666 | 160 | $66 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19NIEPLO-NIE | Nieciecza | 36c | 1.0c | 58 | 163 | 969 | 1426 | 67 | $67 | 7-30d |
| KXEKSTRAKLASA-26-JAG | Jagiellonia | 60c | 79.0c | 1 | 1 | 0 | 0 | 14 | $0 | 30d+ |
| KXEKSTRAKLASAGAME-26APR19CZECRA-CZE | Czestochowa | 52c | 1.0c | 36 | 428 | 350 | 929 | 2 | $2 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19CZECRA-CRA | Cracovia Krakow | 24c | 1.0c | 0 | 134 | 1655 | 700 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR20LECPGL-TIE | Tie | 24c | 8.0c | 1025 | 1 | 1026 | 177 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR20LECPGL-PGL | Gliwice | 30c | 3.0c | 431 | 1 | 831 | 335 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR20LECPGL-LEC | Lechia Gdansk | 44c | 8.0c | 312 | 1 | 712 | 646 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19ARKJAG-TIE | Tie | 26c | 1.0c | 58 | 1 | 1983 | 354 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19ARKJAG-ARK | Arka Gdynia | 29c | 2.0c | 61 | 187 | 927 | 423 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19CZECRA-TIE | Tie | 26c | 1.0c | 54 | 1 | 958 | 374 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19NIEPLO-TIE | Tie | 29c | 1.0c | 1 | 203 | 1964 | 1287 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXEKSTRAKLASAGAME | Polish Ekstraklasa Game | custom | 12 | 12 | $535 | 629 | 2.0c |
| KXEKSTRAKLASA | Ekstraklasa Champion | custom | 18 | 1 | $0 | 571 | 79.0c |

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
