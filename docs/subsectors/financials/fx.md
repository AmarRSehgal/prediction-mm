# fin_fx

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **40** (6 contested)
- Total 24h volume: **$1,755**
- Total open interest: **15,870**
- Top-OI mean spread (median across series): **31.5 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **13**
- Median spread: **11.0c**
- Median TOB bid / ask size: **200 / 112** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **200** / ask: **200** contracts
- Mean trades per market (last 3000): **27**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 12 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 333 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXUSDBRLMAX-26DEC31-T5.9999 | 6 or above | 39c | 63.0c | 86 | 1 | 0 | 0 | 6754 | $0 | 30d+ |
| KXUSDBRLMAX-26DEC31-T5.4999 | 5.5 or above | 43c | 68.0c | 99 | 18 | 0 | 0 | 1658 | $4 | 30d+ |
| KXUSDBRLMAX-26DEC31-T6.7499 | 6.75 or above | 21c | 40.0c | 1000 | 2 | 0 | 0 | 1205 | $0 | 30d+ |
| KXUSDBRLMAX-26DEC31-T5.7499 | 5.75 or above | 48c | 90.0c | 1500 | 11 | 0 | 0 | 1192 | $0 | 30d+ |
| KXUSDBRLMAX-26DEC31-T6.4999 | 6.5 or above | 44c | 87.0c | 1000 | 50 | 0 | 0 | 818 | $0 | 30d+ |
| KXEURUSD-26APR2010-B1.177 | 1.17600 to 1.17799 | 10c | 6.0c | 200 | 145 | 200 | 345 | 89 | $121 | 1-3d |
| KXEURUSD-26APR2010-B1.171 | 1.17000 to 1.17199 | 6c | 6.0c | 200 | 92 | 200 | 292 | 21 | $10 | 1-3d |
| KXEURUSD-26APR2010-B1.175 | 1.17400 to 1.17599 | 10c | 7.0c | 200 | 200 | 200 | 311 | 18 | $0 | 1-3d |
| KXEURUSD-26APR2010-B1.173 | 1.17200 to 1.17399 | 8c | 7.0c | 200 | 310 | 200 | 310 | 9 | $0 | 1-3d |
| KXEURUSD-26APR2010-B1.169 | 1.16800 to 1.16999 | 6c | 10.0c | 200 | 200 | 200 | 200 | 9 | $0 | 1-3d |
| KXEURUSD-26APR2010-B1.179 | 1.17800 to 1.17999 | 9c | 6.0c | 200 | 112 | 200 | 312 | 8 | $0 | 1-3d |
| KXEURUSD-26APR2010-B1.183 | 1.18200 to 1.18399 | 8c | 11.0c | 200 | 200 | 0 | 0 | 0 | $0 | 1-3d |
| KXEURUSD-26APR2010-B1.181 | 1.18000 to 1.18199 | 10c | 11.0c | 200 | 200 | 0 | 0 | 0 | $0 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXUSDBRLMAX | USD/BRL max | annual | 10 | 5 | $4 | 13,013 | 57.0c |
| KXUSDJPY | USD/JPY daily range | daily | 15 | 0 | $1,630 | 2,684 | nanc |
| KXEURUSD | EUR/USD daily range | daily | 15 | 1 | $121 | 173 | 6.0c |

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
