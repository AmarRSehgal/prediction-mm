# eco_ratedecisions

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **107** (29 contested)
- Total 24h volume: **$7,154**
- Total open interest: **2,364,039**
- Top-OI mean spread (median across series): **7.8 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **35**
- Median spread: **7.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median cumulative depth within 5c of mid — bid: **300** / ask: **200** contracts
- Median cumulative depth within 10c of mid — bid: **360** / ask: **201** contracts
- Mean trades per market (last 3000): **302**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2059 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 8505 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXRATECUTCOUNT-26DEC31-T0 | 0:: 0 bps | 36c | 0.1c | 40 | 1855 | 4226 | 6068 | 289226 | $3275 | 30d+ |
| KXRATECUTCOUNT-26DEC31-T2 | 2:: 50 bps | 17c | 1.7c | 9 | 15 | 6095 | 5012 | 162585 | $491 | 30d+ |
| KXRATECUTCOUNT-26DEC31-T3 | 3:: 75 bps | 8c | 0.1c | 2000 | 1207 | 4284 | 9260 | 152569 | $264 | 30d+ |
| KXRATECUTCOUNT-26DEC31-T1 | 1:: 25 bps | 25c | 0.9c | 997 | 2005 | 5039 | 5845 | 118372 | $388 | 30d+ |
| KXCBDECISIONJAPAN-26APR27-H25 | Hike 25bps | 7c | 3.0c | 79 | 132 | 492 | 2132 | 14859 | $1090 | 7-30d |
| KXCBDECISIONJAPAN-26APR27-HOLD | Maintain current rate | 92c | 1.0c | 1975 | 1147 | 4509 | 4348 | 11174 | $5 | 7-30d |
| KXCBDECISIONCANADA-26JUN-H0 | Maintains rate | 84c | 5.0c | 400 | 200 | 900 | 200 | 5428 | $0 | 30d+ |
| KXCBDECISIONENGLAND-26APR30-HOLD | Maintain current rate | 87c | 24.0c | 309 | 606 | 0 | 0 | 3162 | $2 | 7-30d |
| KXCBDECISIONMEXICO-26MAY07-HOLD | Maintain current rate | 54c | 5.0c | 1000 | 103 | 1510 | 304 | 3119 | $312 | 7-30d |
| KXCBDECISIONJAPAN-26JUN15-H25 | Hike 25bps | 70c | 25.0c | 45 | 2 | 0 | 0 | 1987 | $12 | 30d+ |
| KXCBDECISIONCANADA-26JUN-C25 | Cut 25bps | 5c | 4.0c | 200 | 222 | 622 | 600 | 1377 | $0 | 30d+ |
| KXCBDECISIONMEXICO-26MAY07-C25 | Cut 25bps | 43c | 5.0c | 32 | 118 | 602 | 693 | 1245 | $234 | 7-30d |
| KXCBDECISIONKOREA-26MAY27-HOLD | Maintain current rate | 88c | 7.0c | 100 | 32 | 700 | 532 | 1082 | $0 | 30d+ |
| KXCBDECISIONRUSSIA-26APR24-C25 | Cut 25bps | 70c | 9.0c | 500 | 500 | 500 | 500 | 981 | $0 | 3-7d |
| KXCBDECISIONAUSTRALIA-26MAY05-HOLD | Maintain current rate | 31c | 42.0c | 56 | 31 | 0 | 0 | 920 | $19 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXRATECUTCOUNT | Number of rate cuts | annual | 21 | 3 | $3,423 | 2,212,640 | 1.4c |
| KXCBDECISIONCANADA | Bank Of Canada policy interest rate deci | custom | 30 | 13 | $929 | 54,227 | 4.0c |
| KXCBDECISIONJAPAN | Bank Of Japan policy interest rate decis | custom | 10 | 2 | $930 | 35,594 | 21.0c |
| KXCBDECISIONBRAZIL | Brazil | one_off | 7 | 0 | $198 | 22,243 | nanc |
| KXCBDECISIONEU | EU CENTRAL BANK POLICY INTEREST RATE | custom | 5 | 0 | $891 | 21,736 | nanc |
| KXCBDECISIONMEXICO | Bank Of MEXICO policy interest rate deci | custom | 7 | 2 | $546 | 4,849 | 5.5c |
| KXCBDECISIONAUSTRALIA | Bank Of AUSTRALIA policy interest rate d | custom | 10 | 5 | $162 | 4,763 | 46.7c |
| KXCBDECISIONRUSSIA | Russia | one_off | 7 | 2 | $74 | 3,178 | 8.5c |
| KXCBDECISIONENGLAND | Bank Of ENGLAND policy interest rate dec | custom | 5 | 1 | $2 | 3,162 | 23.0c |
| KXCBDECISIONKOREA | Bank Of KOREA policy interest rate decis | custom | 5 | 1 | $0 | 1,646 | 7.0c |

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
