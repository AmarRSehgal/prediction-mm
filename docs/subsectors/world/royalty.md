# world_royalty

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **59** (3 contested)
- Total 24h volume: **$64,672**
- Total open interest: **220,252**
- Top-OI mean spread (median across series): **7.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **3**
- Median spread: **7.0c**
- Median TOB bid / ask size: **501 / 23** contracts
- Median depth within 5c of best bid / ask — **501 / 509** contracts
- Median depth within 10c of best bid / ask — **591 / 509** contracts
- Median depth within 5c of midpoint — bid: **501** / ask: **509** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **76**
- Mean informed-signal proxy: **-0.850** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **6.63c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 227 | 3.86 | -1.187 | 8.00 | 79.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMAYOROFKINGSTOWN-27JAN01 | Yes | 50c | 7.0c | 501 | 23 | 501 | 523 | 501 | 523 | 2287 | $2 | 30d+ |
| KXSAFEBANK-27JAN01 | Yes | 24c | 7.0c | 109 | 0 | 309 | 322 | 591 | 322 | 2209 | $0 | 30d+ |
| KXANDREWSUCCESSION-27JAN01 | Yes | 69c | 8.0c | 522 | 509 | 902 | 509 | 902 | 509 | 2059 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNETFLIXRANKSHOW | Netflix TV ranking | weekly | 14 | 0 | $31,447 | 111,175 | nanc |
| KXNETFLIXRANKMOVIE | Netflix movie ranking | weekly | 19 | 0 | $20,826 | 66,981 | nanc |
| KXNETFLIXRANKSHOWGLOBAL | Netflix TV ranking | weekly | 13 | 0 | $6,693 | 19,029 | nanc |
| KXNETFLIXRANKMOVIEGLOBAL | Netflix movie ranking | weekly | 10 | 0 | $5,704 | 16,512 | nanc |
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
