# eco_jobs

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **432** (184 contested)
- Total 24h volume: **$3,339**
- Total open interest: **363,438**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **7.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median cumulative depth within 5c of mid — bid: **200** / ask: **200** contracts
- Median cumulative depth within 10c of mid — bid: **201** / ask: **230** contracts
- Mean trades per market (last 3000): **36**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 12 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 1244 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 6036 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXU3MAX-27-5 | Above 5% | 35c | 0.6c | 1000 | 5065 | 1160 | 8450 | 124515 | $87 | 30d+ |
| KXU3MAX-27-6 | Above 6% | 15c | 0.4c | 858 | 1000 | 1994 | 8896 | 80315 | $838 | 30d+ |
| KXU3MAX-27-7 | Above 7% | 5c | 3.8c | 1000 | 13 | 12293 | 3182 | 41049 | $6 | 30d+ |
| KXPAYROLLS-26APR-T60000 | 60,000 | 54c | 1.0c | 1012 | 1020 | 1012 | 1020 | 6746 | $214 | 7-30d |
| KXPAYROLLS-26APR-T0 | 0 | 82c | 1.0c | 1344 | 1016 | 1366 | 3116 | 3844 | $59 | 7-30d |
| KXPAYROLLS-26APR-T-25000 | -25,000 | 86c | 1.0c | 1019 | 3948 | 1021 | 6147 | 3544 | $7 | 7-30d |
| KXPAYROLLS-26APR-T70000 | 70,000 | 48c | 7.0c | 1022 | 1000 | 1022 | 1000 | 3158 | $87 | 7-30d |
| KXPAYROLLS-26APR-T100000 | 100,000 | 31c | 1.0c | 1018 | 168 | 1018 | 1168 | 2977 | $0 | 7-30d |
| KXPAYROLLS-26APR-T50000 | 50,000 | 58c | 1.0c | 1020 | 1011 | 1020 | 1011 | 2631 | $18 | 7-30d |
| KXPAYROLLS-26APR-T30000 | 30,000 | 66c | 1.0c | 1009 | 1022 | 1009 | 1022 | 2348 | $95 | 7-30d |
| KXU3MAX-30-10 | Above 10% | 34c | 13.0c | 100 | 100 | 0 | 0 | 2249 | $3 | 30d+ |
| KXECONSTATU3-26APR-T4.3 | Exactly 4.3% | 32c | 1.0c | 80 | 100 | 2825 | 600 | 2075 | $0 | 7-30d |
| KXU3-26APR-T4.4 | 4.4% | 14c | 3.0c | 90 | 2179 | 90 | 2179 | 1956 | $82 | 7-30d |
| KXECONSTATU3-26APR-T4.4 | Exactly 4.4% | 23c | 4.0c | 85 | 146 | 585 | 646 | 1853 | $0 | 7-30d |
| KXUE-MEX26APR-2.5 | Above 2.5% | 36c | 5.0c | 200 | 124 | 200 | 324 | 1674 | $20 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXU3MAX | Unemployment spike | annual | 20 | 10 | $984 | 279,979 | 4.7c |
| KXPAYROLLS | Jobs numbers | monthly | 110 | 105 | $1,198 | 41,611 | 1.0c |
| KXECONSTATU3 | UNEMPLOYMENT RATE MONTHLY | custom | 184 | 26 | $0 | 11,058 | 2.3c |
| KXBRAZILU | Brazil unemployment | custom | 2 | 1 | $1 | 10,906 | 10.0c |
| KXUE | Monthly Unemployment | monthly | 100 | 35 | $398 | 10,017 | 5.0c |
| KXU3 | Unemployment | monthly | 10 | 3 | $757 | 8,813 | 4.0c |
| KXCHCUTS | US Challenger job cuts in [month] | monthly | 6 | 4 | $0 | 1,052 | 8.3c |

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
