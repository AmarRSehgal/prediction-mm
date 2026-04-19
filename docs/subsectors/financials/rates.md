# fin_rates

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **107** (30 contested)
- Total 24h volume: **$626**
- Total open interest: **9,201**
- Top-OI mean spread (median across series): **11.5 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **37**
- Median spread: **10.0c**
- Median TOB bid / ask size: **500 / 300** contracts
- Median cumulative depth within 5c of mid — bid: **300** / ask: **21** contracts
- Median cumulative depth within 10c of mid — bid: **300** / ask: **300** contracts
- Mean trades per market (last 3000): **8**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 263 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXTREASBLOCKCHAIN-26-27 | Before 2027 | 17c | 4.0c | 237 | 188 | 2315 | 2198 | 3095 | $0 | 30d+ |
| KXUSDTTBILL-27FEB28-T64.0 | Above 64.0% | 56c | 8.0c | 521 | 45 | 521 | 45 | 2143 | $0 | 30d+ |
| KX3MTBILL-26JUN30-T3.50 | Above 3.50% | 86c | 3.0c | 500 | 218 | 800 | 218 | 754 | $0 | 30d+ |
| KX3MTBILL-26JUN30-T4.00 | Above 4.00% | 12c | 2.0c | 501 | 147 | 501 | 455 | 712 | $0 | 30d+ |
| KXUSDTTBILL-27FEB28-T70.0 | Above 70.0% | 8c | 9.0c | 500 | 500 | 500 | 500 | 534 | $0 | 30d+ |
| KX10Y2Y-26DEC31-T1.00 | 1.00% | 36c | 52.0c | 682 | 1 | 0 | 0 | 522 | $0 | 30d+ |
| KXTNOTED-26APR20-B4.24 | 4.23% to 4.25% | 25c | 9.0c | 300 | 195 | 300 | 195 | 369 | $369 | 1-3d |
| KXUSDTTBILL-27FEB28-T60.0 | Above 60.0% | 84c | 10.0c | 500 | 500 | 500 | 500 | 300 | $0 | 30d+ |
| KXTNOTEW-26APR24-B4.24 | 4.23% to 4.25% | 20c | 9.0c | 300 | 21 | 300 | 21 | 277 | $277 | 3-7d |
| KXUSTYLD-5Y26JUN30-T3.30 | Above 3.30% | 50c | 98.0c | 10000 | 271 | 0 | 0 | 271 | $0 | 30d+ |
| KXTNOTEW-26APR24-B4.33 | 4.32% to 4.34% | 6c | 5.0c | 300 | 10 | 300 | 460 | 235 | $235 | 3-7d |
| KXTNOTEW-26APR24-B4.30 | 4.29% to 4.31% | 12c | 4.0c | 300 | 38 | 300 | 236 | 146 | $146 | 3-7d |
| KXTNOTEW-26APR24-B4.27 | 4.26% to 4.28% | 20c | 9.0c | 300 | 324 | 300 | 324 | 124 | $124 | 3-7d |
| KX10Y3M-26DEC31-T0.75 | 0.75% | 50c | 77.0c | 932 | 441 | 0 | 0 | 80 | $0 | 30d+ |
| KXTNOTED-26APR20-B4.27 | 4.26% to 4.28% | 24c | 10.0c | 300 | 21 | 300 | 21 | 54 | $94 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTREASBLOCKCHAIN | Treasury transaction on blockchain | custom | 1 | 1 | $0 | 3,095 | 4.0c |
| KXUSDTTBILL | USDT reserve share in direct U.S. Treasu | one_off | 8 | 6 | $4 | 2,983 | 8.7c |
| KX3MTBILL | Treasury 3-month yield above/below | custom | 3 | 3 | $0 | 1,466 | 14.3c |
| KX10Y2Y | Treasury spread 10Y-2Y | custom | 1 | 1 | $0 | 522 | 52.0c |
| KXTNOTEW | Treasury 10Y weekly yield | weekly | 15 | 4 | $509 | 509 | 5.0c |
| KXUSTYLD | Treasury note yield on date | one_off | 63 | 10 | $0 | 473 | 98.0c |
| KX10Y3M | Treasury spread 10Y-3M | custom | 1 | 1 | $0 | 80 | 77.0c |
| KXTNOTED | Treasury 10Y daily yield | daily | 15 | 4 | $114 | 74 | 7.3c |

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
