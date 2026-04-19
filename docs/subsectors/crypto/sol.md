# crypto_sol

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **432** (40 contested)
- Total 24h volume: **$8,515**
- Total open interest: **225,904**
- Top-OI mean spread (median across series): **5.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **67**
- Median spread: **7.0c**
- Median TOB bid / ask size: **1002 / 1000** contracts
- Median depth within 5c of best bid / ask — **5000 / 5000** contracts
- Median depth within 10c of best bid / ask — **5000 / 5000** contracts
- Median depth within 5c of midpoint — bid: **5000** / ask: **3000** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **44**
- Mean informed-signal proxy: **-1.935** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.10c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 0-15m | 216 | 1.00 | -0.237 | 4.00 | 11.7 |
| 12-24h | 100 | 3.25 | -1.978 | 13.00 | 49.1 |
| 3-7d | 21 | 4.40 | -3.200 | 7.00 | 6.7 |
| 7-30d | 1356 | 1.63 | -0.116 | 7.00 | 55.6 |
| 30d+ | 1503 | 2.36 | -0.954 | 8.00 | 59.6 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSOLD26-27JAN0100-T99.99 | 100 or above | 40c | 8.0c | 3 | 1000 | 1003 | 1000 | 2389 | 1482 | 17192 | $44 | 30d+ |
| KXSOLD26-27JAN0100-T149.99 | 150 or above | 20c | 5.0c | 11 | 1001 | 1365 | 1001 | 2384 | 1183 | 12275 | $3 | 30d+ |
| KXSOLMAXY-27JAN01-300 | Above $300.00 | 11c | 5.0c | 9 | 1000 | 1059 | 1142 | 3412 | 1142 | 11756 | $0 | 30d+ |
| KXSOLMAXMON-SOL-26APR30-10000 | Above $100.00 | 12c | 8.0c | 3000 | 161 | 4740 | 3725 | 6575 | 3753 | 10651 | $183 | 7-30d |
| KXSOLMAXMON-SOL-26APR30-9500 | Above $95.00 | 30c | 9.0c | 95 | 3000 | 3369 | 3000 | 3369 | 3000 | 9989 | $559 | 7-30d |
| KXSOLD26-27JAN0100-T199.99 | 200 or above | 12c | 3.0c | 1005 | 1000 | 5054 | 1042 | 6904 | 1127 | 9808 | $0 | 30d+ |
| KXSOLMAXY-27JAN01-250 | Above $250.00 | 12c | 5.0c | 1005 | 1000 | 1005 | 1077 | 1404 | 1077 | 9733 | $112 | 30d+ |
| KXSOLMAXY-27JAN01-150 | Above $150.00 | 36c | 4.0c | 1000 | 1000 | 2000 | 2000 | 2000 | 2000 | 8362 | $52 | 30d+ |
| KXSOLMAXY-27JAN01-160 | Above $160.00 | 31c | 5.0c | 1000 | 1000 | 2000 | 1000 | 2048 | 1000 | 7988 | $0 | 30d+ |
| KXSOLMAXY-27JAN01-200 | Above $200.00 | 16c | 5.0c | 1002 | 1000 | 1002 | 1030 | 1590 | 1554 | 7566 | $0 | 30d+ |
| KXSOLMAXY-27JAN01-190 | Above $190.00 | 20c | 4.0c | 10 | 1000 | 25 | 1000 | 1163 | 1000 | 7503 | $0 | 30d+ |
| KXSOLMINMON-SOL-26APR30-7500 | Below $75.00 | 25c | 4.0c | 500 | 211 | 3500 | 3812 | 3500 | 3812 | 7375 | $104 | 7-30d |
| KXSOLMAXMON-SOL-26APR30-10500 | Above $105.00 | 8c | 7.0c | 1582 | 100 | 6344 | 3235 | 6344 | 3235 | 6796 | $585 | 7-30d |
| KXSOLMAXMON-SOL-26APR30-11000 | Above $110.00 | 5c | 6.0c | 287 | 3690 | 1287 | 3690 | 1287 | 3690 | 6347 | $131 | 7-30d |
| KXSOLMAXY-27JAN01-180 | Above $180.00 | 22c | 3.0c | 1005 | 1000 | 1005 | 1000 | 1424 | 1000 | 5144 | $2 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSOLMAXY | Solana Max Yearly | annual | 8 | 8 | $180 | 61,634 | 4.7c |
| KXSOL26500 | Sol above 500 in 2026 | one_off | 1 | 0 | $341 | 52,045 | nanc |
| KXSOLD26 | SOL price end of 2026? | annual | 8 | 3 | $47 | 46,067 | 5.3c |
| KXSOLMAXMON | SOL Monthly One touch  | monthly | 7 | 2 | $1,464 | 40,800 | 8.0c |
| KXSOLMINMON | SOL Min monthly | monthly | 7 | 1 | $162 | 18,841 | 2.0c |
| KXSOLD | SOL Directional | hourly | 200 | 21 | $6,065 | 5,882 | 15.3c |
| KXSOL15M | Solana 15 minutes | fifteen_min | 1 | 1 | $1 | 416 | 2.0c |
| KXSOLE | SOL Range | hourly | 200 | 4 | $254 | 220 | 11.3c |

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
