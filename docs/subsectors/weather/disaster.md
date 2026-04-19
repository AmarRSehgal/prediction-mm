# weather_disaster

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **12** (12 with open markets)
- Open markets: **53** (35 contested)
- Total 24h volume: **$7,183**
- Total open interest: **532,522**
- Top-OI mean spread (median across series): **4.5 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **40**
- Median spread: **5.0c**
- Median TOB bid / ask size: **38 / 60** contracts
- Median depth within 5c of best bid / ask — **693 / 712** contracts
- Median depth within 10c of best bid / ask — **2200 / 850** contracts
- Median depth within 5c of midpoint — bid: **98** / ask: **92** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **224**
- Mean informed-signal proxy: **-3.677** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **5.99c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1194 | 2.65 | -0.420 | 11.00 | 26.7 |
| 30d+ | 7778 | 2.10 | -0.677 | 8.00 | 48.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXEARTHQUAKECALIFORNIA-27 | Before 2027 | 7c | 1.0c | 127 | 135 | 3270 | 3298 | 13946 | 4274 | 85372 | $63 | 30d+ |
| KXEMERCUTS-26-T0 | 0 cuts | 87c | 1.5c | 9 | 2954 | 1680 | 6946 | 2308 | 11015 | 75950 | $199 | 30d+ |
| KXFEDMEET-27-JAN01 | Before Jan 1, 2027 | 15c | 4.5c | 9 | 11 | 3130 | 1770 | 5331 | 1831 | 72319 | $334 | 30d+ |
| KXEMERCUTS-26-T1 | 1 cuts | 7c | 0.7c | 180 | 190 | 2270 | 1860 | 17935 | 1860 | 48411 | $84 | 30d+ |
| KXTRYFIREPOWELL-26MAY12-GOV1 | Before May 15, 2026 | 10c | 1.0c | 1 | 9 | 783 | 366 | 21049 | 5234 | 33070 | $217 | 7-30d |
| KXTRUMPFIRE-27-0 | 0 | 60c | 2.0c | 997 | 148 | 1717 | 398 | 2092 | 398 | 25182 | $22 | 30d+ |
| KXEARTHQUAKEJAPAN-30 | Before 2030 | 50c | 7.0c | 375 | 12 | 405 | 126 | 490 | 134 | 14183 | $0 | 30d+ |
| KXEARTHQUAKECALIFORNIA-35 | Before 2035 | 56c | 5.0c | 23 | 10 | 23 | 292 | 23 | 294 | 13076 | $26 | 30d+ |
| KXTRYFIREPOWELL-26MAY12-GOV2 | Before 2027 | 39c | 4.0c | 77 | 35 | 827 | 788 | 879 | 792 | 11466 | $299 | 30d+ |
| KXERUPTSUPER-0-50JAN01 | Before Jan 1, 2050 | 20c | 3.0c | 53 | 17 | 2017 | 208 | 5354 | 410 | 10402 | $2 | 30d+ |
| KXTRUMPFIRE-27-2 | 2 | 16c | 3.0c | 52 | 14 | 497 | 497 | 497 | 710 | 8713 | $370 | 30d+ |
| KXELECTIONEMERGENCY-26NOV04 | Before Nov 4, 2026 | 36c | 5.0c | 48 | 5 | 805 | 852 | 805 | 852 | 7796 | $14 | 30d+ |
| KXTRUMPFIRE-27-3 | 3 | 14c | 3.0c | 125 | 26 | 375 | 478 | 455 | 924 | 6350 | $0 | 30d+ |
| KXEARTHQUAKECALIFORNIA-28 | Before 2028 | 14c | 5.0c | 5 | 213 | 252 | 849 | 5480 | 849 | 5765 | $0 | 30d+ |
| KXTRUMPFIRE-27-1 | 1 | 6c | 2.5c | 59 | 200 | 8379 | 1446 | 8379 | 1446 | 5329 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXEMERCUTS | Emergency rate cuts | custom | 5 | 1 | $283 | 160,461 | 1.5c |
| KXEARTHQUAKECALIFORNIA | Earthquake in California | custom | 3 | 2 | $89 | 104,213 | 4.5c |
| KXFEDMEET | Fed emergency meeting | custom | 1 | 1 | $334 | 72,319 | 4.5c |
| KXTRUMPFIRE | Trump firings | annual | 6 | 3 | $393 | 55,451 | 3.3c |
| KXTRYFIREPOWELL | try to fire powell | one_off | 3 | 3 | $803 | 48,275 | 3.0c |
| KXTORNADO | Number of Tornadoes | monthly | 11 | 5 | $5,106 | 45,223 | 3.3c |
| KXELECTIONEMERGENCY | Will Trump declare an election emergency | one_off | 4 | 2 | $15 | 15,909 | 5.0c |
| KXEARTHQUAKEJAPAN | Earthquake in Japan | custom | 1 | 1 | $0 | 14,183 | 7.0c |
| KXERUPTSUPER | Supervolcano | custom | 1 | 1 | $2 | 10,402 | 3.0c |
| KXHURCTOTMAJ | Number of major hurricanes | annual | 8 | 8 | $155 | 3,788 | 8.3c |

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
