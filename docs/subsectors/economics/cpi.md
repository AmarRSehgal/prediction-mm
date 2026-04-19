# eco_cpi

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **9** (9 with open markets)
- Open markets: **156** (92 contested)
- Total 24h volume: **$17,727**
- Total open interest: **223,336**
- Top-OI mean spread (median across series): **9.5 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **110**
- Median spread: **9.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median depth within 5c of best bid / ask — **201 / 280** contracts
- Median depth within 10c of best bid / ask — **202 / 324** contracts
- Median depth within 5c of midpoint — bid: **200** / ask: **200** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **115**
- Mean informed-signal proxy: **-0.960** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.70c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2115 | 1.37 | -0.328 | 5.00 | 60.7 |
| 30d+ | 10542 | 2.73 | -1.158 | 10.00 | 19.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCPI-26APR-T0.5 | 0.5% | 36c | 2.0c | 9 | 5773 | 742 | 6106 | 942 | 6155 | 25423 | $1185 | 7-30d |
| KXCPI-26APR-T0.4 | 0.4% | 74c | 2.0c | 826 | 367 | 1411 | 10337 | 1413 | 10484 | 24588 | $3829 | 7-30d |
| KXCPICORE-26APR-T0.3 | 0.3 | 48c | 3.0c | 505 | 25 | 505 | 849 | 505 | 879 | 21238 | $10 | 7-30d |
| KXCPICORE-26APR-T0.4 | 0.4 | 20c | 2.0c | 500 | 30 | 550 | 784 | 550 | 869 | 18892 | $0 | 7-30d |
| KXCPI-26APR-T0.6 | 0.6% | 16c | 5.0c | 365 | 529 | 370 | 551 | 370 | 551 | 17277 | $3209 | 7-30d |
| KXCPI-26APR-T0.3 | 0.3% | 94c | 1.0c | 355 | 16274 | 1386 | 17684 | 1386 | 17684 | 16351 | $5213 | 7-30d |
| KXCPI-26APR-T0.7 | 0.7% | 8c | 2.0c | 355 | 650 | 2090 | 651 | 2147 | 653 | 8746 | $432 | 7-30d |
| KXCPICORE-26APR-T0.2 | 0.2 | 78c | 4.0c | 519 | 37 | 519 | 788 | 535 | 940 | 7049 | $68 | 7-30d |
| KXCPI-26MAY-T1.0 | 1.0% | 7c | 2.0c | 702 | 200 | 955 | 596 | 955 | 597 | 2445 | $456 | 30d+ |
| KXCPI-26MAY-T0.1 | 0.1% | 42c | 2.0c | 1 | 200 | 3 | 202 | 203 | 202 | 1721 | $51 | 30d+ |
| KXCPI-26MAY-T0.5 | 0.5% | 14c | 8.0c | 200 | 6 | 200 | 309 | 200 | 311 | 1656 | $5 | 30d+ |
| KXCPI-26MAY-T0.3 | 0.3% | 23c | 10.0c | 1 | 200 | 201 | 290 | 201 | 290 | 1574 | $104 | 30d+ |
| KXCPI-26MAY-T0.4 | 0.4% | 20c | 2.0c | 1 | 1 | 288 | 202 | 288 | 203 | 1510 | $96 | 30d+ |
| KXCPI-26MAY-T0.2 | 0.2% | 34c | 3.0c | 81 | 79 | 82 | 279 | 282 | 279 | 1194 | $6 | 30d+ |
| KXCPI-26MAY-T0.6 | 0.6% | 13c | 11.0c | 200 | 200 | 200 | 200 | 288 | 317 | 1085 | $181 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCPI | CPI | monthly | 68 | 56 | $17,414 | 148,478 | 3.0c |
| KXCPICORE | CPI core | monthly | 38 | 11 | $98 | 54,065 | 3.0c |
| KXPPIVSCPI | PPI YoY exceeds CPI YoY for [time period | custom | 1 | 0 | $0 | 12,760 | nanc |
| KXUSEDCARCPI | US used cars and trucks CPI in [month] | monthly | 7 | 3 | $0 | 2,822 | 5.3c |
| KXUSGASCPI | US gasoline CPI in [month] | monthly | 15 | 4 | $200 | 2,657 | 16.7c |
| KXSHELTERCPI | US shelter CPI in [month] | monthly | 5 | 3 | $15 | 1,863 | 9.7c |
| KXAIRFARECPI | US airline fares CPI in [month] | monthly | 11 | 4 | $0 | 689 | 9.3c |
| KXTOBACCPI | Tobacco CPI higher in [month]? | monthly | 1 | 1 | $0 | 1 | 16.0c |
| KXTRUFEGGS | Truflation US CPI Eggs Index | daily | 10 | 10 | $0 | 0 | 98.0c |

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
