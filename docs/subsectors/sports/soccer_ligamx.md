# sports_soccer_ligamx

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **39** (27 contested)
- Total 24h volume: **$1,048,562**
- Total open interest: **973,465**
- Top-OI mean spread (median across series): **9.8 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **22**
- Median spread: **4.5c**
- Median TOB bid / ask size: **10 / 46** contracts
- Median depth within 5c of best bid / ask — **792 / 771** contracts
- Median depth within 10c of best bid / ask — **1119 / 771** contracts
- Median depth within 5c of midpoint — bid: **496** / ask: **556** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **124**
- Mean informed-signal proxy: **-0.574** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.23c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 3283 | 1.04 | -0.318 | 4.00 | 90.2 |
| 30d+ | 2439 | 4.04 | -1.029 | 20.00 | 53.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLIGAMXGAME-26APR18AMETOL-TOL | Toluca | nanc | nanc | nan | nan | nan | nan | nan | nan | 444289 | $554380 | 7-30d |
| KXLIGAMXGAME-26APR18AMETOL-AME | America | nanc | nanc | nan | nan | nan | nan | nan | nan | 214406 | $270906 | 7-30d |
| KXLIGAMXGAME-26APR18AMETOL-TIE | Tie | nanc | nanc | nan | nan | nan | nan | nan | nan | 120568 | $145471 | 7-30d |
| KXLIGAMX-26CLA-CDG | Guadalajara | 27c | 2.0c | 5 | 9 | 5 | 9 | 5 | 9 | 25433 | $789 | 30d+ |
| KXLIGAMX-26CLA-CRA | Cruz Azul | 14c | 15.0c | 10 | 0 | 15 | 304 | 158 | 320 | 13992 | $23 | 30d+ |
| KXLIGAMX-26CLA-TOL | Toluca | 20c | 36.0c | 5 | 12 | 35 | 12 | 35 | 12 | 10704 | $24 | 30d+ |
| KXLIGAMX-26CLA-PUM | Pumas UNAM | 18c | 33.0c | 5 | 5 | 35 | 61 | 35 | 61 | 10385 | $329 | 30d+ |
| KXLIGAMX-26CLA-AME | America | 29c | 53.0c | 27 | 16 | 28 | 16 | 28 | 16 | 7870 | $211 | 30d+ |
| KXLIGAMX-26CLA-TIG | Tigres | 20c | 35.0c | 27 | 5 | 42 | 70 | 42 | 70 | 7650 | $408 | 30d+ |
| KXLIGAMXGAME-26APR19SLAATL-ATL | Atlas | 38c | 1.0c | 1275 | 115 | 28730 | 10735 | 28732 | 11436 | 4331 | $3329 | 7-30d |
| KXLIGAMX-26CLA-PAC | Pachuca | 12c | 20.0c | 5 | 56 | 8 | 56 | 8 | 63 | 1422 | $0 | 30d+ |
| KXLIGAMXGAME-26APR19SLAATL-TIE | Tie | 26c | 1.0c | 1 | 1278 | 9202 | 13846 | 9733 | 13846 | 816 | $541 | 7-30d |
| KXLIGAMXGAME-26APR19SLAATL-SLA | Santos Laguna | 36c | 1.0c | 235 | 100 | 23462 | 9617 | 23462 | 10117 | 711 | $608 | 7-30d |
| KXLIGAMXGAME-26APR21QUECRA-CRA | Cruz Azul | 56c | 3.0c | 2 | 114 | 318 | 830 | 818 | 831 | 206 | $206 | 7-30d |
| KXLIGAMXGAME-26APR21LEOAME-AME | America | 53c | 6.0c | 135 | 36 | 637 | 891 | 637 | 891 | 152 | $400 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXLIGAMXGAME | Liga MX Game | custom | 21 | 20 | $1,046,624 | 883,772 | 1.7c |
| KXLIGAMX | Liga MX Winner | annual | 18 | 7 | $1,939 | 89,693 | 18.0c |

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
