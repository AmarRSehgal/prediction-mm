# sports_baseball_us

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **16** (16 with open markets)
- Open markets: **925** (97 contested)
- Total 24h volume: **$124,581**
- Total open interest: **1,817,954**
- Top-OI mean spread (median across series): **5.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **143**
- Median spread: **7.0c**
- Median TOB bid / ask size: **76 / 85** contracts
- Median cumulative depth within 5c of mid — bid: **104** / ask: **100** contracts
- Median cumulative depth within 10c of mid — bid: **550** / ask: **559** contracts
- Mean trades per market (last 3000): **73**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 76 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 10338 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMLBAL-26-SEA | Seattle | 17c | 1.0c | 5002 | 1827 | 34604 | 32585 | 134224 | $536 | 30d+ |
| KXMLBAL-26-NYY | New York Y | 18c | 1.0c | 7069 | 2309 | 33094 | 31664 | 87933 | $4970 | 30d+ |
| KXMLBNL-26-LAD | Los Angeles D | 43c | 1.0c | 5385 | 14042 | 36341 | 70695 | 83761 | $3558 | 30d+ |
| KXMLBAL-26-DET | Detroit | 10c | 1.0c | 7271 | 5157 | 39137 | 35336 | 79462 | $502 | 30d+ |
| KXMLBNL-26-ATL | Atlanta | 8c | 1.0c | 8223 | 4538 | 37650 | 30396 | 72577 | $7307 | 30d+ |
| KXMLBNL-26-NYM | New York M | 7c | 1.0c | 4917 | 7233 | 32536 | 41802 | 55516 | $3793 | 30d+ |
| KXMLBAL-26-CLE | Cleveland | 6c | 1.0c | 1508 | 5542 | 41409 | 33196 | 54371 | $256 | 30d+ |
| KXMLBAL-26-HOU | Houston | 6c | 1.0c | 4893 | 9820 | 879451 | 48068 | 49893 | $187 | 30d+ |
| KXMLBAL-26-BOS | Boston | 7c | 1.0c | 9922 | 9371 | 42354 | 40919 | 48927 | $2348 | 30d+ |
| KXMLBNL-26-PHI | Philadelphia | 7c | 1.0c | 5733 | 6200 | 35174 | 41482 | 45032 | $1076 | 30d+ |
| KXMLBNL-26-CHC | Chicago C | 6c | 1.0c | 6668 | 1173 | 883912 | 46847 | 43363 | $12 | 30d+ |
| KXMLBAL-26-KC | Kansas City | 6c | 1.0c | 4663 | 15695 | 31459 | 48199 | 39915 | $824 | 30d+ |
| KXMLBAL-26-TEX | Texas | 7c | 1.0c | 10949 | 7379 | 36968 | 38074 | 37803 | $197 | 30d+ |
| KXMLBAL-26-BAL | Baltimore | 6c | 1.0c | 8927 | 5154 | 41608 | 44520 | 30274 | $0 | 30d+ |
| KXMLBAL-26-TOR | Toronto | 7c | 1.0c | 7500 | 5929 | 184206 | 40233 | 27107 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMLBAL | MLB American League Championship | annual | 15 | 3 | $29,816 | 789,384 | 1.0c |
| KXMLBNL | MLB National League Championship | annual | 15 | 1 | $27,893 | 673,063 | 1.0c |
| KXLEADERMLBHR | MLB Home Runs Leader | annual | 22 | 4 | $3,811 | 94,345 | 2.7c |
| KXMLBMENTION | MLB Announcers | one_off | 95 | 59 | $59,981 | 59,205 | 29.3c |
| KXLEADERMLBWINS | MLB Wins Leader | annual | 50 | 2 | $0 | 41,280 | 5.0c |
| KXLEADERMLBSTEALS | MLB Steals Leader | annual | 50 | 3 | $1,928 | 35,701 | 5.0c |
| KXLEADERMLBRBI | MLB RBIs Leader | annual | 62 | 2 | $92 | 23,402 | 5.5c |
| KXLEADERMLBWAR | MLB WAR Leader | annual | 50 | 2 | $0 | 19,355 | 7.0c |
| KXLEADERMLBAVG | MLB Batting Average Leader | annual | 50 | 3 | $109 | 17,054 | 7.7c |
| KXLEADERMLBHITS | MLB Hits Leader | annual | 62 | 2 | $368 | 14,489 | 7.0c |

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
