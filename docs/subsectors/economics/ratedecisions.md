# eco_ratedecisions

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **107** (29 contested)
- Total 24h volume: **$7,607**
- Total open interest: **2,364,752**
- Top-OI mean spread (median across series): **7.8 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **35**
- Median spread: **7.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median depth within 5c of best bid / ask — **500 / 364** contracts
- Median depth within 10c of best bid / ask — **800 / 388** contracts
- Median depth within 5c of midpoint — bid: **300** / ask: **200** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **189**
- Mean informed-signal proxy: **-1.772** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.16c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2059 | 1.10 | -0.114 | 5.00 | 30.3 |
| 30d+ | 4536 | 0.64 | -0.337 | 2.00 | 91.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXRATECUTCOUNT-26DEC31-T0 | 0:: 0 bps | 36c | 0.7c | 98 | 1875 | 4294 | 6098 | 6069 | 7049 | 289217 | $3300 | 30d+ |
| KXRATECUTCOUNT-26DEC31-T2 | 2:: 50 bps | 17c | 1.7c | 9 | 15 | 6095 | 5014 | 6196 | 15125 | 162585 | $383 | 30d+ |
| KXRATECUTCOUNT-26DEC31-T3 | 3:: 75 bps | 8c | 0.1c | 2000 | 1207 | 4284 | 9260 | 12063 | 44607 | 152569 | $379 | 30d+ |
| KXRATECUTCOUNT-26DEC31-T1 | 1:: 25 bps | 25c | 0.9c | 1012 | 2002 | 5154 | 5861 | 19812 | 6876 | 118390 | $348 | 30d+ |
| KXCBDECISIONJAPAN-26APR27-H25 | Hike 25bps | 7c | 3.0c | 101 | 204 | 5658 | 2204 | 5658 | 2876 | 14859 | $1090 | 7-30d |
| KXCBDECISIONJAPAN-26APR27-HOLD | Maintain current rate | 92c | 1.0c | 1984 | 2163 | 4518 | 6363 | 4578 | 10299 | 11174 | $5 | 7-30d |
| KXCBDECISIONCANADA-26JUN-H0 | Maintains rate | 84c | 5.0c | 400 | 200 | 1000 | 300 | 1200 | 825 | 5428 | $0 | 30d+ |
| KXCBDECISIONENGLAND-26APR30-HOLD | Maintain current rate | 87c | 24.0c | 318 | 628 | 1218 | 628 | 1218 | 628 | 3162 | $2 | 7-30d |
| KXCBDECISIONMEXICO-26MAY07-HOLD | Maintain current rate | 54c | 3.0c | 500 | 2 | 1019 | 2027 | 1019 | 2527 | 3119 | $122 | 7-30d |
| KXCBDECISIONJAPAN-26JUN15-H25 | Hike 25bps | 69c | 24.0c | 45 | 6 | 145 | 8 | 185 | 8 | 1987 | $12 | 30d+ |
| KXCBDECISIONCANADA-26JUN-C25 | Cut 25bps | 5c | 4.0c | 200 | 222 | 622 | 600 | 622 | 600 | 1377 | $0 | 30d+ |
| KXCBDECISIONMEXICO-26MAY07-C25 | Cut 25bps | 43c | 4.0c | 59 | 2 | 626 | 773 | 626 | 773 | 1245 | $222 | 7-30d |
| KXCBDECISIONKOREA-26MAY27-HOLD | Maintain current rate | 88c | 7.0c | 100 | 32 | 800 | 532 | 800 | 3477 | 1082 | $0 | 30d+ |
| KXCBDECISIONRUSSIA-26APR24-C25 | Cut 25bps | 70c | 9.0c | 500 | 500 | 500 | 500 | 500 | 500 | 981 | $0 | 3-7d |
| KXCBDECISIONAUSTRALIA-26MAY05-HOLD | Maintain current rate | 29c | 38.0c | 56 | 9 | 572 | 9 | 2226 | 9 | 920 | $1 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXRATECUTCOUNT | Number of rate cuts | annual | 21 | 3 | $4,879 | 2,212,880 | 0.9c |
| KXCBDECISIONCANADA | Bank Of Canada policy interest rate deci | custom | 30 | 13 | $135 | 54,227 | 4.0c |
| KXCBDECISIONJAPAN | Bank Of Japan policy interest rate decis | custom | 10 | 2 | $1,398 | 36,068 | 20.0c |
| KXCBDECISIONBRAZIL | Brazil | one_off | 7 | 0 | $198 | 22,243 | nanc |
| KXCBDECISIONEU | EU CENTRAL BANK POLICY INTEREST RATE | custom | 5 | 0 | $511 | 21,736 | nanc |
| KXCBDECISIONMEXICO | Bank Of MEXICO policy interest rate deci | custom | 7 | 2 | $344 | 4,849 | 4.0c |
| KXCBDECISIONAUSTRALIA | Bank Of AUSTRALIA policy interest rate d | custom | 10 | 5 | $136 | 4,763 | 45.3c |
| KXCBDECISIONRUSSIA | Russia | one_off | 7 | 2 | $4 | 3,178 | 8.5c |
| KXCBDECISIONENGLAND | Bank Of ENGLAND policy interest rate dec | custom | 5 | 1 | $2 | 3,162 | 24.0c |
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
