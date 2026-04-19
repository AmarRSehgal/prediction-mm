# sports_baseball_us

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **16** (16 with open markets)
- Open markets: **893** (90 contested)
- Total 24h volume: **$78,505**
- Total open interest: **1,785,874**
- Top-OI mean spread (median across series): **5.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **144**
- Median spread: **7.0c**
- Median TOB bid / ask size: **62 / 100** contracts
- Median depth within 5c of best bid / ask — **691 / 551** contracts
- Median depth within 10c of best bid / ask — **798 / 745** contracts
- Median depth within 5c of midpoint — bid: **106** / ask: **110** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **67**
- Mean informed-signal proxy: **-1.403** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.69c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 92 | 5.65 | -2.984 | 24.60 | 20.7 |
| 30d+ | 9531 | 0.87 | -0.330 | 3.00 | 105.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMLBAL-26-SEA | Seattle | 17c | 1.0c | 5002 | 2002 | 32356 | 32752 | 33566 | 33402 | 134487 | $718 | 30d+ |
| KXMLBAL-26-NYY | New York Y | 18c | 1.0c | 6960 | 2184 | 34013 | 31542 | 38780 | 31892 | 88028 | $5060 | 30d+ |
| KXMLBNL-26-LAD | Los Angeles D | 43c | 1.0c | 5385 | 14036 | 36328 | 70689 | 36428 | 70790 | 83761 | $3582 | 30d+ |
| KXMLBAL-26-DET | Detroit | 10c | 1.0c | 7271 | 5157 | 39137 | 35336 | 886126 | 36136 | 79462 | $502 | 30d+ |
| KXMLBNL-26-ATL | Atlanta | 8c | 1.0c | 8223 | 4308 | 37878 | 30166 | 1397393 | 30298 | 72754 | $7400 | 30d+ |
| KXMLBNL-26-NYM | New York M | 7c | 1.0c | 4917 | 7233 | 32536 | 41802 | 2159700 | 41917 | 55577 | $3854 | 30d+ |
| KXMLBAL-26-CLE | Cleveland | 6c | 1.0c | 1508 | 5542 | 41391 | 33196 | 41391 | 33796 | 54371 | $256 | 30d+ |
| KXMLBAL-26-HOU | Houston | 6c | 1.0c | 4893 | 9820 | 879451 | 48068 | 879451 | 48068 | 49893 | $187 | 30d+ |
| KXMLBAL-26-BOS | Boston | 7c | 1.0c | 9922 | 9371 | 42354 | 40919 | 1391442 | 40919 | 48927 | $2348 | 30d+ |
| KXMLBNL-26-PHI | Philadelphia | 7c | 1.0c | 5733 | 6200 | 35174 | 41482 | 1385862 | 42282 | 45082 | $1125 | 30d+ |
| KXMLBNL-26-CHC | Chicago C | 6c | 1.0c | 6668 | 1173 | 883932 | 46847 | 883932 | 47647 | 43363 | $12 | 30d+ |
| KXMLBAL-26-KC | Kansas City | 6c | 1.0c | 4663 | 15695 | 36521 | 48249 | 36521 | 48349 | 39915 | $824 | 30d+ |
| KXMLBAL-26-TEX | Texas | 7c | 1.0c | 10949 | 7379 | 36968 | 38074 | 42054 | 41874 | 37803 | $197 | 30d+ |
| KXMLBAL-26-BAL | Baltimore | 6c | 1.0c | 8927 | 5154 | 41616 | 44520 | 41616 | 44520 | 30274 | $0 | 30d+ |
| KXMLBAL-26-TOR | Toronto | 7c | 1.0c | 7500 | 5929 | 184206 | 40179 | 2680874 | 41154 | 27107 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMLBAL | MLB American League Championship | annual | 15 | 3 | $19,695 | 792,780 | 1.0c |
| KXMLBNL | MLB National League Championship | annual | 15 | 1 | $34,170 | 679,264 | 1.0c |
| KXLEADERMLBHR | MLB Home Runs Leader | annual | 22 | 3 | $3,956 | 94,702 | 3.7c |
| KXLEADERMLBWINS | MLB Wins Leader | annual | 50 | 2 | $0 | 41,280 | 5.0c |
| KXLEADERMLBSTEALS | MLB Steals Leader | annual | 50 | 3 | $1,928 | 35,701 | 5.0c |
| KXLEADERMLBRBI | MLB RBIs Leader | annual | 62 | 2 | $72 | 23,402 | 5.5c |
| KXLEADERMLBWAR | MLB WAR Leader | annual | 50 | 2 | $0 | 19,355 | 7.0c |
| KXMLBMENTION | MLB Announcers | one_off | 63 | 53 | $17,556 | 17,103 | 8.3c |
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
