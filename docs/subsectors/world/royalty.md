# world_royalty

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **59** (3 contested)
- Total 24h volume: **$86,997**
- Total open interest: **215,734**
- Top-OI mean spread (median across series): **7.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **3**
- Median spread: **7.0c**
- Median TOB bid / ask size: **501 / 23** contracts
- Median cumulative depth within 5c of mid — bid: **501** / ask: **509** contracts
- Median cumulative depth within 10c of mid — bid: **501** / ask: **509** contracts
- Mean trades per market (last 3000): **76**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 227 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMAYOROFKINGSTOWN-27JAN01 | Yes | 50c | 7.0c | 501 | 23 | 501 | 523 | 2287 | $2 | 30d+ |
| KXSAFEBANK-27JAN01 | Yes | 24c | 7.0c | 109 | 0 | 309 | 122 | 2209 | $0 | 30d+ |
| KXANDREWSUCCESSION-27JAN01 | Yes | 69c | 8.0c | 522 | 509 | 622 | 509 | 2059 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNETFLIXRANKSHOW | Netflix TV ranking | weekly | 14 | 0 | $52,644 | 107,063 | nanc |
| KXNETFLIXRANKMOVIE | Netflix movie ranking | weekly | 19 | 0 | $21,651 | 66,602 | nanc |
| KXNETFLIXRANKSHOWGLOBAL | Netflix TV ranking | weekly | 13 | 0 | $6,536 | 19,002 | nanc |
| KXNETFLIXRANKMOVIEGLOBAL | Netflix movie ranking | weekly | 10 | 0 | $6,163 | 16,512 | nanc |
| KXMAYOROFKINGSTOWN | Will Paramount release season 5 of Mayor | one_off | 1 | 1 | $2 | 2,287 | 7.0c |
| KXSAFEBANK | Will cannabis banking insurance protecti | one_off | 1 | 1 | $0 | 2,209 | 7.0c |
| KXANDREWSUCCESSION | Will Prince Andrew be removed from the r | one_off | 1 | 1 | $0 | 2,059 | 8.0c |

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
