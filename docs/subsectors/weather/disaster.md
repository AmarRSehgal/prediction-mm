# weather_disaster

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **12** (12 with open markets)
- Open markets: **53** (35 contested)
- Total 24h volume: **$7,934**
- Total open interest: **532,266**
- Top-OI mean spread (median across series): **4.5 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **40**
- Median spread: **5.0c**
- Median TOB bid / ask size: **38 / 42** contracts
- Median cumulative depth within 5c of mid — bid: **98** / ask: **70** contracts
- Median cumulative depth within 10c of mid — bid: **542** / ask: **594** contracts
- Mean trades per market (last 3000): **230**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1191 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 8005 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXEARTHQUAKECALIFORNIA-27 | Before 2027 | 7c | 1.0c | 127 | 135 | 3270 | 3298 | 85372 | $63 | 30d+ |
| KXEMERCUTS-26-T0 | 0 cuts | 87c | 1.5c | 9 | 2954 | 1680 | 4946 | 75950 | $199 | 30d+ |
| KXFEDMEET-27-JAN01 | Before Jan 1, 2027 | 15c | 4.5c | 9 | 11 | 3080 | 1273 | 72319 | $334 | 30d+ |
| KXEMERCUTS-26-T1 | 1 cuts | 7c | 0.7c | 180 | 190 | 1872 | 1860 | 48411 | $84 | 30d+ |
| KXTRYFIREPOWELL-26MAY12-GOV1 | Before May 15, 2026 | 10c | 1.0c | 1 | 9 | 783 | 273 | 33070 | $216 | 7-30d |
| KXTRUMPFIRE-27-0 | 0 | 60c | 2.0c | 997 | 148 | 1715 | 398 | 25182 | $22 | 30d+ |
| KXEARTHQUAKEJAPAN-30 | Before 2030 | 50c | 7.0c | 375 | 12 | 405 | 12 | 14183 | $0 | 30d+ |
| KXEARTHQUAKECALIFORNIA-35 | Before 2035 | 56c | 5.0c | 23 | 10 | 23 | 10 | 13076 | $26 | 30d+ |
| KXTRYFIREPOWELL-26MAY12-GOV2 | Before 2027 | 39c | 4.0c | 77 | 35 | 827 | 288 | 11444 | $306 | 30d+ |
| KXERUPTSUPER-0-50JAN01 | Before Jan 1, 2050 | 20c | 3.0c | 53 | 17 | 1697 | 208 | 10402 | $5 | 30d+ |
| KXTRUMPFIRE-27-2 | 2 | 12c | 1.0c | 195 | 54 | 452 | 54 | 8560 | $218 | 30d+ |
| KXELECTIONEMERGENCY-26NOV04 | Before Nov 4, 2026 | 36c | 5.0c | 48 | 5 | 355 | 652 | 7796 | $14 | 30d+ |
| KXTRUMPFIRE-27-3 | 3 | 14c | 3.0c | 125 | 26 | 375 | 253 | 6350 | $0 | 30d+ |
| KXEARTHQUAKECALIFORNIA-28 | Before 2028 | 13c | 4.0c | 5 | 16 | 52 | 508 | 5765 | $0 | 30d+ |
| KXTRUMPFIRE-27-1 | 1 | 6c | 2.5c | 59 | 200 | 3110 | 1446 | 5329 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXEMERCUTS | Emergency rate cuts | custom | 5 | 1 | $278 | 160,461 | 1.5c |
| KXEARTHQUAKECALIFORNIA | Earthquake in California | custom | 3 | 2 | $89 | 104,213 | 4.5c |
| KXFEDMEET | Fed emergency meeting | custom | 1 | 1 | $334 | 72,319 | 4.6c |
| KXTRUMPFIRE | Trump firings | annual | 6 | 3 | $240 | 55,298 | 2.0c |
| KXTRYFIREPOWELL | try to fire powell | one_off | 3 | 3 | $739 | 48,218 | 2.7c |
| KXTORNADO | Number of Tornadoes | monthly | 11 | 5 | $6,066 | 45,194 | 4.0c |
| KXELECTIONEMERGENCY | Will Trump declare an election emergency | one_off | 4 | 2 | $15 | 15,909 | 5.0c |
| KXEARTHQUAKEJAPAN | Earthquake in Japan | custom | 1 | 1 | $0 | 14,183 | 7.0c |
| KXERUPTSUPER | Supervolcano | custom | 1 | 1 | $5 | 10,402 | 3.0c |
| KXHURCTOTMAJ | Number of major hurricanes | annual | 8 | 8 | $166 | 3,773 | 8.0c |

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
