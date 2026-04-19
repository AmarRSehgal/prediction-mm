# crypto_sol

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **432** (41 contested)
- Total 24h volume: **$7,870**
- Total open interest: **225,252**
- Top-OI mean spread (median across series): **7.2 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **57**
- Median spread: **8.0c**
- Median TOB bid / ask size: **1005 / 1000** contracts
- Median cumulative depth within 5c of mid — bid: **2000** / ask: **1042** contracts
- Median cumulative depth within 10c of mid — bid: **5000** / ask: **5000** contracts
- Mean trades per market (last 3000): **53**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 12-24h | 93 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 15 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 1410 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 1503 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSOLD26-27JAN0100-T99.99 | 100 or above | 40c | 8.0c | 3 | 1000 | 1003 | 1000 | 17192 | $67 | 30d+ |
| KXSOLD26-27JAN0100-T149.99 | 150 or above | 20c | 5.0c | 11 | 1001 | 1011 | 1001 | 12275 | $6 | 30d+ |
| KXSOLMAXY-27JAN01-300 | Above $300.00 | 11c | 5.0c | 1009 | 1000 | 1009 | 1100 | 11756 | $0 | 30d+ |
| KXSOLMAXMON-SOL-26APR30-10000 | Above $100.00 | 12c | 8.0c | 3000 | 161 | 3000 | 725 | 10651 | $186 | 7-30d |
| KXSOLMAXMON-SOL-26APR30-9500 | Above $95.00 | 28c | 11.0c | 3000 | 3000 | 0 | 0 | 9989 | $563 | 7-30d |
| KXSOLD26-27JAN0100-T199.99 | 200 or above | 12c | 3.0c | 1005 | 1000 | 1005 | 1042 | 9808 | $0 | 30d+ |
| KXSOLMAXY-27JAN01-250 | Above $250.00 | 13c | 4.0c | 1000 | 1000 | 1005 | 1015 | 9733 | $112 | 30d+ |
| KXSOLMAXY-27JAN01-150 | Above $150.00 | 36c | 4.0c | 1000 | 1000 | 2000 | 2000 | 8362 | $52 | 30d+ |
| KXSOLMAXY-27JAN01-160 | Above $160.00 | 32c | 7.0c | 1000 | 1000 | 2000 | 1000 | 7988 | $0 | 30d+ |
| KXSOLMAXY-27JAN01-200 | Above $200.00 | 16c | 5.0c | 1002 | 1000 | 1002 | 1030 | 7566 | $0 | 30d+ |
| KXSOLMAXY-27JAN01-190 | Above $190.00 | 20c | 5.0c | 7 | 1004 | 7 | 1004 | 7503 | $0 | 30d+ |
| KXSOLMINMON-SOL-26APR30-7500 | Below $75.00 | 26c | 3.0c | 500 | 211 | 500 | 3908 | 7375 | $104 | 7-30d |
| KXSOLMAXMON-SOL-26APR30-10500 | Above $105.00 | 8c | 7.0c | 1582 | 100 | 4582 | 3100 | 6796 | $585 | 7-30d |
| KXSOLMAXMON-SOL-26APR30-11000 | Above $110.00 | 5c | 6.0c | 287 | 3690 | 1287 | 3690 | 6347 | $134 | 7-30d |
| KXSOLMAXY-27JAN01-180 | Above $180.00 | 22c | 3.0c | 1005 | 1000 | 1005 | 1000 | 5144 | $2 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSOLMAXY | Solana Max Yearly | annual | 8 | 8 | $180 | 61,634 | 4.3c |
| KXSOL26500 | Sol above 500 in 2026 | one_off | 1 | 0 | $522 | 52,045 | nanc |
| KXSOLD26 | SOL price end of 2026? | annual | 8 | 3 | $73 | 46,067 | 5.3c |
| KXSOLMAXMON | SOL Monthly One touch  | monthly | 7 | 2 | $2,085 | 40,800 | 9.0c |
| KXSOLMINMON | SOL Min monthly | monthly | 7 | 2 | $161 | 18,840 | 3.0c |
| KXSOLD | SOL Directional | hourly | 200 | 21 | $4,356 | 4,374 | 12.0c |
| KXSOL15M | Solana 15 minutes | fifteen_min | 1 | 0 | $423 | 1,460 | nanc |
| KXSOLE | SOL Range | hourly | 200 | 5 | $70 | 34 | 11.0c |

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
