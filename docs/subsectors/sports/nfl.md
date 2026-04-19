# sports_nfl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **16** (16 with open markets)
- Open markets: **719** (114 contested)
- Total 24h volume: **$66,203**
- Total open interest: **1,902,596**
- Top-OI mean spread (median across series): **27.2 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **136**
- Median spread: **23.0c**
- Median TOB bid / ask size: **200 / 150** contracts
- Median depth within 5c of best bid / ask — **1000 / 605** contracts
- Median depth within 10c of best bid / ask — **1325 / 721** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **55**
- Mean informed-signal proxy: **-9.536** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **13.71c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 3264 | 2.36 | -0.337 | 10.00 | 54.6 |
| 30d+ | 4247 | 5.10 | -2.382 | 27.00 | 44.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSUPERBOWLWHITEHOUSE-26DEC31 | Yes | 56c | 3.0c | 79 | 500 | 1586 | 1500 | 1586 | 1502 | 130437 | $433 | 30d+ |
| KXNFLDRAFTPICK-26-5-SSTY | Sonny Styles | 34c | 1.0c | 50 | 847 | 1420 | 1093 | 1673 | 1093 | 42365 | $4304 | 7-30d |
| KXNFLDRAFTPICK-26-5-RBAI | Rueben Bain Jr. | 8c | 9.0c | 20 | 800 | 6507 | 850 | 6507 | 2258 | 17119 | $4741 | 7-30d |
| KXCOACHOUTNFL-26SEP01-MLAF | :: Green Bay | 10c | 15.0c | 4168 | 516 | 4715 | 3916 | 4715 | 4203 | 15536 | $0 | 30d+ |
| KXSTARTINGQBWEEK1-W1-26SEP15-CLE-DWAT | Deshaun Watson | 32c | 1.0c | 127 | 321 | 900 | 521 | 900 | 521 | 13168 | $0 | 30d+ |
| KXSTARTINGQBWEEK1-W1-26SEP15-CLE-SSAN | Shedeur Sanders | 47c | 4.0c | 214 | 627 | 1559 | 928 | 1559 | 928 | 9352 | $46 | 30d+ |
| KXNFLDRAFTPICK-26-10-CDOW | Caleb Downs | 26c | 5.0c | 6 | 98 | 2282 | 3073 | 2282 | 3073 | 8203 | $2405 | 7-30d |
| KXNFLDRAFTPICK-26-6-CTAT | Carnell Tate | 26c | 1.0c | 111 | 501 | 116 | 558 | 515 | 558 | 8156 | $423 | 7-30d |
| KXNFLTRADE-26DEC01-ABRO | :: Philadelphia | 68c | 41.0c | 96 | 147 | 96 | 197 | 96 | 5330 | 7477 | $4 | 30d+ |
| KXNFLDRAFTPICK-26-6-SSTY | Sonny Styles | 12c | 1.0c | 541 | 319 | 1960 | 663 | 4261 | 720 | 7429 | $305 | 7-30d |
| KXSUPERBOWLHEADLINE-27-JAY | JAY-Z | 14c | 4.0c | 93 | 560 | 1033 | 1362 | 4072 | 1362 | 6809 | $0 | 30d+ |
| KXNFLDRAFTPICK-26-8-JTYS | Jordyn Tyson | 20c | 1.0c | 28 | 450 | 1058 | 733 | 3115 | 733 | 6738 | $1112 | 7-30d |
| KXNFLDRAFTPICK-26-10-JTYS | Jordyn Tyson | 17c | 30.0c | 515 | 3 | 1807 | 730 | 1807 | 730 | 6554 | $6852 | 7-30d |
| KXNFLDRAFTPICK-26-9-MDEL | Mansoor Delane | 19c | 3.0c | 35 | 7 | 747 | 1153 | 797 | 1718 | 6077 | $950 | 7-30d |
| KXNFLDRAFTPICK-26-9-JTYS | Jordyn Tyson | 12c | 1.0c | 298 | 280 | 1957 | 791 | 4331 | 791 | 5550 | $369 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNFLDRAFT1 | NFL Draft First Pick | annual | 32 | 0 | $11,386 | 736,792 | nanc |
| KXNFLDRAFT1ST | Make the 1st pick in NFL Draft | annual | 32 | 0 | $3,708 | 546,243 | nanc |
| KXNFLDRAFTPICK | NFL Draft Pick | annual | 200 | 23 | $49,965 | 320,031 | 3.0c |
| KXSUPERBOWLWHITEHOUSE | WILL THE WINNERS OF THE PRO FOOTBALL CHA | one_off | 1 | 1 | $433 | 130,437 | 3.0c |
| KXCOACHOUTNFL | NFL Coach Out | custom | 22 | 2 | $154 | 59,659 | 69.5c |
| KXSUPERBOWLHEADLINE | Who will headline super bowl LX | one_off | 53 | 11 | $10 | 50,144 | 4.3c |
| KXSTARTINGQBWEEK1 | NFL Starting QB Week 1 | custom | 119 | 15 | $46 | 30,340 | 14.0c |
| KXNFLTRADE | NFL Trade | custom | 57 | 32 | $501 | 28,734 | 31.3c |
| KXLEADERNFLPTDS | NFL leader passing TDs | annual | 28 | 2 | $0 | 124 | 20.5c |
| KXLEADERNFLRYDS | NFL leader receiving yards | annual | 26 | 5 | $0 | 45 | 23.0c |

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
