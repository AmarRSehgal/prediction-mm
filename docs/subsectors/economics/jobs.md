# eco_jobs

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **432** (185 contested)
- Total 24h volume: **$3,529**
- Total open interest: **364,316**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **8.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median depth within 5c of best bid / ask — **200 / 216** contracts
- Median depth within 10c of best bid / ask — **202 / 230** contracts
- Median depth within 5c of midpoint — bid: **200** / ask: **200** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **33**
- Mean informed-signal proxy: **-3.015** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.37c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 12 | 3.20 | -2.600 | 6.55 | 26.8 |
| 7-30d | 1251 | 2.17 | -0.792 | 7.00 | 41.6 |
| 30d+ | 5394 | 2.13 | -1.325 | 10.00 | 45.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXU3MAX-27-5 | Above 5% | 35c | 0.6c | 1000 | 5065 | 1160 | 8450 | 1165 | 18467 | 124515 | $87 | 30d+ |
| KXU3MAX-27-6 | Above 6% | 15c | 0.4c | 858 | 1000 | 1994 | 8896 | 1994 | 8896 | 80315 | $688 | 30d+ |
| KXU3MAX-27-7 | Above 7% | 5c | 3.8c | 1000 | 13 | 12293 | 3182 | 12293 | 7529 | 41049 | $6 | 30d+ |
| KXPAYROLLS-26APR-T60000 | 60,000 | 54c | 1.0c | 1012 | 1020 | 1012 | 1020 | 1064 | 1056 | 6746 | $16 | 7-30d |
| KXPAYROLLS-26APR-T0 | 0 | 82c | 1.0c | 2211 | 1016 | 2233 | 3116 | 2233 | 3116 | 3844 | $57 | 7-30d |
| KXPAYROLLS-26APR-T-25000 | -25,000 | 86c | 1.0c | 1019 | 3948 | 2221 | 9147 | 2221 | 9548 | 3544 | $7 | 7-30d |
| KXPAYROLLS-26APR-T70000 | 70,000 | 48c | 7.0c | 42 | 1000 | 1419 | 1000 | 1919 | 1090 | 3163 | $88 | 7-30d |
| KXPAYROLLS-26APR-T100000 | 100,000 | 33c | 2.0c | 1022 | 1014 | 1022 | 1135 | 1921 | 1135 | 3145 | $290 | 7-30d |
| KXPAYROLLS-26APR-T50000 | 50,000 | 58c | 1.0c | 1020 | 1011 | 1020 | 1011 | 1046 | 1011 | 2631 | $18 | 7-30d |
| KXPAYROLLS-26APR-T30000 | 30,000 | 66c | 1.0c | 1009 | 1022 | 1009 | 1022 | 1059 | 1022 | 2348 | $95 | 7-30d |
| KXU3MAX-30-10 | Above 10% | 34c | 13.0c | 100 | 100 | 100 | 600 | 100 | 650 | 2249 | $3 | 30d+ |
| KXECONSTATU3-26APR-T4.3 | Exactly 4.3% | 32c | 1.0c | 80 | 100 | 2625 | 600 | 2625 | 600 | 2075 | $0 | 7-30d |
| KXU3-26APR-T4.4 | 4.4% | 14c | 3.0c | 90 | 1000 | 1090 | 1000 | 4809 | 1018 | 1956 | $82 | 7-30d |
| KXECONSTATU3-26APR-T4.4 | Exactly 4.4% | 23c | 4.0c | 85 | 100 | 585 | 758 | 585 | 758 | 1853 | $0 | 7-30d |
| KXUE-MEX26APR-2.5 | Above 2.5% | 36c | 5.0c | 200 | 89 | 200 | 289 | 235 | 289 | 1674 | $1 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXU3MAX | Unemployment spike | annual | 20 | 10 | $834 | 279,979 | 4.7c |
| KXPAYROLLS | Jobs numbers | monthly | 110 | 105 | $1,718 | 42,465 | 1.0c |
| KXECONSTATU3 | UNEMPLOYMENT RATE MONTHLY | custom | 184 | 27 | $0 | 11,058 | 2.7c |
| KXBRAZILU | Brazil unemployment | custom | 2 | 1 | $20 | 10,906 | 10.0c |
| KXUE | Monthly Unemployment | monthly | 100 | 35 | $176 | 10,017 | 5.0c |
| KXU3 | Unemployment | monthly | 10 | 3 | $781 | 8,838 | 3.3c |
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
