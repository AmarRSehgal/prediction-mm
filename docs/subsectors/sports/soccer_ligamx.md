# sports_soccer_ligamx

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **45** (29 contested)
- Total 24h volume: **$371,337**
- Total open interest: **467,725**
- Top-OI mean spread (median across series): **7.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **28**
- Median spread: **3.5c**
- Median TOB bid / ask size: **86 / 87** contracts
- Median cumulative depth within 5c of mid — bid: **1654** / ask: **720** contracts
- Median cumulative depth within 10c of mid — bid: **2172** / ask: **878** contracts
- Mean trades per market (last 3000): **461**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 10488 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 2430 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLIGAMXGAME-26APR18AMETOL-TOL | Toluca | 16c | 3.0c | 149 | 125 | 7993 | 312 | 158348 | $122342 | 7-30d |
| KXLIGAMXGAME-26APR18AMETOL-AME | America | 60c | 1.0c | 61 | 157 | 2379 | 2705 | 39480 | $37252 | 7-30d |
| KXLIGAMX-26CLA-CDG | Guadalajara | 28c | 2.0c | 5 | 9 | 23 | 9 | 25463 | $759 | 30d+ |
| KXLIGAMXGAME-26APR18LEOJUA-LEO | Leon | 88c | 1.0c | 1499 | 585 | 3229 | 3436 | 24135 | $19843 | 7-30d |
| KXLIGAMXGAME-26APR18AMETOL-TIE | Tie | 25c | 2.0c | 2109 | 1780 | 4834 | 3858 | 14504 | $13505 | 7-30d |
| KXLIGAMX-26CLA-CRA | Cruz Azul | 14c | 16.0c | 5 | 0 | 0 | 0 | 13992 | $23 | 30d+ |
| KXLIGAMXGAME-26APR18LEOJUA-JUA | Juarez | 3c | 2.0c | 972 | 7215 | 6433 | 8527 | 12157 | $10078 | 7-30d |
| KXLIGAMX-26CLA-TOL | Toluca | 20c | 36.0c | 5 | 12 | 0 | 0 | 10702 | $22 | 30d+ |
| KXLIGAMX-26CLA-PUM | Pumas UNAM | 18c | 33.0c | 5 | 5 | 0 | 0 | 10385 | $329 | 30d+ |
| KXLIGAMXGAME-26APR18LEOJUA-TIE | Tie | 9c | 2.0c | 1753 | 5990 | 3560 | 9054 | 8226 | $7512 | 7-30d |
| KXLIGAMX-26CLA-AME | America | 4c | 5.0c | 5 | 90 | 83 | 90 | 7687 | $13 | 30d+ |
| KXLIGAMX-26CLA-TIG | Tigres | 20c | 33.0c | 5 | 101 | 0 | 0 | 7650 | $408 | 30d+ |
| KXLIGAMXGAME-26APR19SLAATL-ATL | Atlas | 38c | 1.0c | 275 | 1300 | 35187 | 19878 | 3691 | $2739 | 7-30d |
| KXLIGAMX-26CLA-PAC | Pachuca | 12c | 20.0c | 5 | 60 | 0 | 0 | 1422 | $0 | 30d+ |
| KXLIGAMXGAME-26APR19SLAATL-SLA | Santos Laguna | 38c | 1.0c | 1 | 1603 | 34180 | 15839 | 693 | $591 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXLIGAMXGAME | Liga MX Game | custom | 27 | 24 | $369,601 | 378,226 | 1.3c |
| KXLIGAMX | Liga MX Winner | annual | 18 | 5 | $1,737 | 89,499 | 13.3c |

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
