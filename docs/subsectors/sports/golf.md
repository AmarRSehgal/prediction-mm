# sports_golf

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **31** (31 with open markets)
- Open markets: **1299** (225 contested)
- Total 24h volume: **$13,237,849**
- Total open interest: **51,471,938**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **3.0c**
- Median TOB bid / ask size: **231 / 232** contracts
- Median cumulative depth within 5c of mid — bid: **1727** / ask: **4487** contracts
- Median cumulative depth within 10c of mid — bid: **3327** / ask: **8604** contracts
- Mean trades per market (last 3000): **183**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 6000 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 11903 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 18694 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPGATOUR-RBH26-SSCH | Scottie Scheffler | 26c | 1.0c | 39675 | 839146 | 129724 | 2355560 | 4327419 | $2946002 | 1-3d |
| KXPGATOUR-RBH26-MFIT | Matt Fitzpatrick | 54c | 1.0c | 566 | 408527 | 287310 | 1233676 | 1429671 | $1050236 | 1-3d |
| KXPGATOUR-PGC26-SSCH | Scottie Scheffler | 18c | 1.0c | 12756 | 2225 | 21713 | 52884 | 111568 | $13364 | 30d+ |
| KXPGATOP20-RBH26-JSPI | Jordan Spieth | 10c | 3.0c | 2173 | 857 | 6231 | 6111 | 111050 | $5683 | 7-30d |
| KXPGATOUR-PGC26-RMCI | Rory McIlroy | 9c | 1.0c | 3941 | 943 | 13211 | 177984 | 106489 | $8103 | 30d+ |
| KXPGATOP5-RBH26-SSCH | Scottie Scheffler | 80c | 3.0c | 4 | 45 | 1916 | 45 | 104381 | $37058 | 7-30d |
| KXPGATOP10-RBH26-SSCH | Scottie Scheffler | 90c | 1.0c | 999 | 222 | 1943 | 222 | 62583 | $20601 | 7-30d |
| KXPGATOP20-RBH26-PCAN | Patrick Cantlay | 90c | 3.0c | 72 | 712 | 571 | 25020 | 56306 | $2953 | 7-30d |
| KXPGAMAJORWIN-26-SSCH | Scottie Scheffler | 46c | 3.0c | 33 | 5745 | 1344 | 22460 | 45289 | $564 | 30d+ |
| KXPGATOP20-RBH26-BHAR | Brian Harman | 86c | 2.0c | 6648 | 2 | 12530 | 474 | 40615 | $4422 | 7-30d |
| KXPGATOP20-RBH26-CAME | Cameron Young | 52c | 1.0c | 18 | 4678 | 1180 | 5955 | 36124 | $4109 | 7-30d |
| KXPGATOP20-RBH26-LABE | Ludvig Aberg | 86c | 1.0c | 50 | 328 | 1049 | 5968 | 34369 | $2984 | 7-30d |
| KXPGAMAJORWIN-26-CYOU | Cameron Young | 19c | 2.0c | 33 | 1746 | 3346 | 5646 | 28826 | $292 | 30d+ |
| KXPGATOP20-RBH26-JBRI | Jacob Bridgeman | 30c | 1.0c | 10 | 4520 | 1541 | 4707 | 28233 | $2138 | 7-30d |
| KXPGATOP20-RBH26-SBUR | Sam Burns | 50c | 6.0c | 1 | 1 | 1927 | 1 | 27210 | $675 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPGATOUR | PGA Tour | custom | 148 | 3 | $12,791,715 | 48,461,025 | 1.0c |
| KXPGATOP20 | PGA Top 20 Finisher | custom | 147 | 41 | $101,020 | 1,353,015 | 3.0c |
| KXPGATOP10 | PGA Top 10 Finisher | custom | 147 | 27 | $81,396 | 530,315 | 3.7c |
| KXPGATOP5 | PGA Top 5 Finisher | custom | 147 | 18 | $75,250 | 434,933 | 5.7c |
| KXPGAMAJORWIN | PGA Major Winner | custom | 52 | 9 | $1,864 | 285,340 | 3.3c |
| KXLPGATOUR | PGA Tour | custom | 65 | 4 | $56,999 | 114,818 | 9.0c |
| KXPGAMAJORTOP10 | PGA Top 10 for All 4 Majors | annual | 11 | 7 | $586 | 60,659 | 1.7c |
| KXPGAHOLEINONE | PGA Hole in One | custom | 3 | 1 | $21,299 | 37,429 | 1.0c |
| KXGOLFMAJORS | Golf Majors Won | custom | 3 | 2 | $447 | 32,099 | 1.0c |
| KXPGAPLAYOFF | Golf Playoff | custom | 1 | 1 | $16,286 | 26,431 | 2.0c |

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
