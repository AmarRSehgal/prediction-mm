# sports_esports_r6

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **8** (8 contested)
- Total 24h volume: **$36**
- Total open interest: **299**
- Top-OI mean spread (median across series): **92.3 cents**
- **MM profile: Wide but dead**

## Book depth (from comprehensive scan)

- Markets sampled: **8**
- Median spread: **93.5c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median depth within 5c of best bid / ask — **1354 / 1338** contracts
- Median depth within 10c of best bid / ask — **1354 / 1338** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **-1.238** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **7.81c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 14 | 14.55 | -2.727 | 73.50 | 21.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXR6GAME-26APR201700130SSG-SSG | Spacestation Gaming | 50c | 93.0c | 100 | 163 | 700 | 639 | 700 | 639 | 159 | $36 | 7-30d |
| KXR6GAME-26APR201700130SSG-130 | 1 of 30 | 49c | 92.0c | 100 | 80 | 700 | 1731 | 700 | 1731 | 138 | $0 | 7-30d |
| KXR6GAME-26APR202000WCGM80-M80 | M80 | 49c | 92.0c | 100 | 4 | 1227 | 826 | 1227 | 826 | 2 | $0 | 7-30d |
| KXR6GAME-26APR191500LIQUIDFAZE-LIQUID | Team Liquid | 50c | 94.0c | 100 | 100 | 1482 | 1338 | 1482 | 1338 | 0 | $0 | 7-30d |
| KXR6GAME-26APR191500LIQUIDFAZE-FAZE | FaZe Clan | 50c | 94.0c | 100 | 100 | 1482 | 1338 | 1482 | 1338 | 0 | $0 | 7-30d |
| KXR6GAME-26APR191200FLULOS-LOS | LOS | 50c | 94.0c | 100 | 100 | 1482 | 1338 | 1482 | 1338 | 0 | $0 | 7-30d |
| KXR6GAME-26APR191200FLULOS-FLU | Fluxo W7M | 50c | 94.0c | 100 | 100 | 1482 | 1338 | 1482 | 1338 | 0 | $0 | 7-30d |
| KXR6GAME-26APR202000WCGM80-WCG | Wildcard Gaming | 52c | 87.0c | 5 | 2 | 5 | 478 | 1222 | 478 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXR6GAME | Spacestation Gaming | nan | 8 | 8 | $36 | 299 | 92.3c |

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
