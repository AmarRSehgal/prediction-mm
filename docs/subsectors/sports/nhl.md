# sports_nhl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **14** (14 with open markets)
- Open markets: **723** (491 contested)
- Total 24h volume: **$1,084,343**
- Total open interest: **2,679,087**
- Top-OI mean spread (median across series): **14.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **4.0c**
- Median TOB bid / ask size: **104 / 436** contracts
- Median depth within 5c of best bid / ask — **4228 / 4721** contracts
- Median depth within 10c of best bid / ask — **12292 / 5812** contracts
- Median depth within 5c of midpoint — bid: **1198** / ask: **1274** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **96**
- Mean informed-signal proxy: **-0.865** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.08c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 12839 | 0.72 | -0.301 | 3.00 | 105.9 |
| 30d+ | 6428 | 1.41 | -0.288 | 6.00 | 101.7 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNHLHART-26-NMAC | :: | 12c | 1.0c | 90 | 632 | 1144 | 675 | 5040 | 703 | 312696 | $2651 | 30d+ |
| KXNHLSERIES-26OTTCARR1-CAR | Carolina Hurricanes | 74c | 1.0c | 2578 | 53892 | 13631 | 232572 | 15853 | 232585 | 197053 | $196490 | 7-30d |
| KXNHLHART-26-KKUC | :: | 40c | 1.0c | 69 | 944 | 995 | 944 | 1004 | 1194 | 170901 | $3417 | 30d+ |
| KXNHLHART-26-CMCD | :: | 52c | 1.0c | 833 | 632 | 874 | 720 | 874 | 720 | 130824 | $3954 | 30d+ |
| KXNHLGAME-26APR19LACOL-COL | COL Avalanche | 70c | 1.0c | 13333 | 159702 | 202145 | 798403 | 202145 | 799343 | 112750 | $93173 | 7-30d |
| KXNHLSERIES-26OTTCARR1-OTT | Ottawa Senators | 26c | 1.0c | 1132 | 12086 | 10129 | 19710 | 10267 | 19710 | 112509 | $103471 | 7-30d |
| KXNHLADAMS-26-LRUF | :: | 81c | 10.0c | 40 | 5 | 1357 | 3005 | 1657 | 3058 | 110611 | $100 | 30d+ |
| KXNHLSERIES-26LACOLR1-COL | Colorado Avalanche | 82c | 1.0c | 3944 | 17823 | 13362 | 138633 | 15398 | 211248 | 110286 | $106038 | 7-30d |
| KXNHLSERIES-26MINDALR1-MIN | Minnesota Wild | 63c | 2.0c | 10443 | 3500 | 13741 | 33793 | 14458 | 83793 | 80263 | $51006 | 7-30d |
| KXNHLSERIES-26MINDALR1-DAL | Dallas Stars | 36c | 1.0c | 23 | 45477 | 4346 | 50278 | 6826 | 50278 | 74816 | $66642 | 7-30d |
| KXNHLSERIES-26PHIPITR1-PIT | Pittsburgh Penguins | 39c | 4.0c | 907 | 6029 | 6749 | 29199 | 7005 | 129415 | 66838 | $52000 | 7-30d |
| KXNHLSERIES-26PHIPITR1-PHI | Philadelphia Flyers | 62c | 3.0c | 26 | 792 | 884 | 151364 | 5884 | 156838 | 44318 | $30793 | 7-30d |
| KXNHLGAME-26APR19BOSBUF-BUF | BUF Sabres | 58c | 1.0c | 32084 | 11788 | 192203 | 543073 | 192203 | 544609 | 44167 | $21107 | 7-30d |
| KXNHLNORRIS-26-ZWER | :: | 72c | 1.0c | 330 | 635 | 5650 | 635 | 5897 | 2635 | 43913 | $96 | 30d+ |
| KXNHLSERIES-26MTLTBR1-MTL | Montreal Canadiens | 31c | 1.0c | 32 | 3500 | 7082 | 29361 | 9056 | 31335 | 37453 | $15668 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNHLSERIES | NHL Series Winner | custom | 16 | 16 | $705,686 | 868,071 | 1.0c |
| KXNHLHART | NHL Hart Memorial Trophy | annual | 30 | 3 | $17,743 | 849,862 | 1.7c |
| KXNHLGAME | NHL Game | custom | 56 | 56 | $269,322 | 290,637 | 1.0c |
| KXNHLADAMS | NHL Jack Adams Award | annual | 32 | 1 | $400 | 212,613 | 11.0c |
| KXNHLNORRIS | NHL James Norris Memorial Trophy | annual | 30 | 2 | $2,474 | 145,582 | 4.0c |
| KXNHLVEZINA | NHL Vezina Trophy | annual | 30 | 0 | $301 | 94,099 | nanc |
| KXNHLSERIESSCORE | NHL Series Exact Score | one_off | 61 | 46 | $41,885 | 86,818 | 18.7c |
| KXNHLCALDER | NHL Calder Memorial Trophy | annual | 30 | 0 | $255 | 73,784 | nanc |
| KXNHLSPREAD | NHL Spread | custom | 112 | 111 | $21,314 | 26,758 | 1.3c |
| KXNHLSERIESSPREAD | NHL Series Game Spread | custom | 45 | 36 | $15,342 | 21,194 | 17.0c |

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
