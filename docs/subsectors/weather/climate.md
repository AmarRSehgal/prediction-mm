# weather_climate

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **4** (4 with open markets)
- Open markets: **13** (7 contested)
- Total 24h volume: **$1,276**
- Total open interest: **20,984**
- Top-OI mean spread (median across series): **6.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **10**
- Median spread: **6.5c**
- Median TOB bid / ask size: **45 / 156** contracts
- Median cumulative depth within 5c of mid — bid: **402** / ask: **502** contracts
- Median cumulative depth within 10c of mid — bid: **686** / ask: **508** contracts
- Mean trades per market (last 3000): **112**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 18 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 1101 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXWARMING-50 | Before 2050 | 78c | 3.0c | 35 | 20 | 1036 | 1037 | 5046 | $13 | 30d+ |
| KXHMONTHRANGE-26APR-B1.200 | 1.17 to 1.23 | 46c | 8.0c | 25 | 265 | 25 | 265 | 1065 | $21 | 7-30d |
| KXCO2LEVEL-30-445 | At least 445 | 41c | 6.0c | 505 | 37 | 505 | 637 | 798 | $0 | 30d+ |
| KXHMONTHRANGE-26APR-B1.130 | 1.10 to 1.16 | 28c | 9.0c | 250 | 22 | 250 | 22 | 769 | $0 | 7-30d |
| KXCO2LEVEL-30-450 | At least 450 | 20c | 9.0c | 49 | 500 | 49 | 500 | 667 | $0 | 30d+ |
| KXCO2LEVEL-30-460 | At least 460 | 5c | 4.0c | 179 | 29 | 3179 | 530 | 623 | $0 | 30d+ |
| KXCO2LEVEL-30-455 | At least 455 | 10c | 7.0c | 41 | 500 | 541 | 515 | 564 | $0 | 30d+ |
| KXCO2LEVEL-30-440 | At least 440 | 88c | 9.0c | 505 | 505 | 505 | 505 | 546 | $0 | 30d+ |
| KXHMONTHRANGE-26APR-B1.270 | 1.24 to 1.30 | 15c | 4.0c | 20 | 268 | 77 | 268 | 451 | $1 | 7-30d |
| KXHMONTHRANGE-26APR-T1.30 | 1.30001 or above | 9c | 6.0c | 12 | 47 | 299 | 297 | 300 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXHMONTH | Hottest month instance | monthly | 1 | 0 | $1,161 | 9,928 | nanc |
| KXWARMING | Global warming | one_off | 1 | 1 | $13 | 5,046 | 3.0c |
| KXCO2LEVEL | CO2 level | custom | 5 | 3 | $0 | 3,198 | 8.0c |
| KXHMONTHRANGE | Monthly Temperature Increase (ºC) | custom | 6 | 3 | $102 | 2,813 | 6.7c |

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
