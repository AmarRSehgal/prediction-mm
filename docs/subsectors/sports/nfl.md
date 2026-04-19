# sports_nfl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **16** (16 with open markets)
- Open markets: **719** (116 contested)
- Total 24h volume: **$56,457**
- Total open interest: **1,891,460**
- Top-OI mean spread (median across series): **26.2 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **139**
- Median spread: **23.0c**
- Median TOB bid / ask size: **200 / 157** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **71**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 3372 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 6440 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSUPERBOWLWHITEHOUSE-26DEC31 | Yes | 56c | 3.0c | 79 | 500 | 1579 | 1500 | 130527 | $335 | 30d+ |
| KXNFLDRAFTPICK-26-5-SSTY | Sonny Styles | 36c | 3.0c | 48 | 50 | 151 | 299 | 42339 | $4278 | 7-30d |
| KXNFLDRAFTPICK-26-5-RBAI | Rueben Bain Jr. | 10c | 13.0c | 20 | 77 | 0 | 0 | 17119 | $4741 | 7-30d |
| KXCOACHOUTNFL-26SEP01-MLAF | :: Green Bay | 10c | 15.0c | 4168 | 516 | 0 | 0 | 15536 | $0 | 30d+ |
| KXSTARTINGQBWEEK1-W1-26SEP15-CLE-DWAT | Deshaun Watson | 32c | 1.0c | 105 | 312 | 878 | 512 | 13168 | $0 | 30d+ |
| KXSTARTINGQBWEEK1-W1-26SEP15-CLE-SSAN | Shedeur Sanders | 47c | 4.0c | 214 | 627 | 559 | 928 | 9352 | $46 | 30d+ |
| KXNFLDRAFTPICK-26-10-CDOW | Caleb Downs | 26c | 5.0c | 11 | 155 | 79 | 3155 | 8146 | $2348 | 7-30d |
| KXNFLDRAFTPICK-26-6-CTAT | Carnell Tate | 26c | 1.0c | 111 | 501 | 161 | 558 | 8109 | $409 | 7-30d |
| KXNFLTRADE-26DEC01-ABRO | :: Philadelphia | 68c | 41.0c | 96 | 147 | 0 | 0 | 7477 | $4 | 30d+ |
| KXNFLDRAFTPICK-26-6-SSTY | Sonny Styles | 12c | 1.0c | 541 | 319 | 1960 | 663 | 7429 | $305 | 7-30d |
| KXSUPERBOWLHEADLINE-27-JAY | JAY-Z | 14c | 4.0c | 93 | 560 | 533 | 1060 | 6809 | $0 | 30d+ |
| KXNFLDRAFTPICK-26-8-JTYS | Jordyn Tyson | 20c | 1.0c | 26 | 450 | 1058 | 897 | 6738 | $1112 | 7-30d |
| KXNFLDRAFTPICK-26-9-MDEL | Mansoor Delane | 20c | 1.0c | 250 | 2 | 712 | 1153 | 6069 | $537 | 7-30d |
| KXNFLDRAFTPICK-26-10-JTYS | Jordyn Tyson | 26c | 6.0c | 13 | 15 | 28 | 64 | 5804 | $5524 | 7-30d |
| KXNFLDRAFTPICK-26-8-MDEL | Mansoor Delane | 11c | 2.0c | 516 | 450 | 1026 | 833 | 5465 | $301 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNFLDRAFT1 | NFL Draft First Pick | annual | 32 | 0 | $10,387 | 734,289 | nanc |
| KXNFLDRAFT1ST | Make the 1st pick in NFL Draft | annual | 32 | 0 | $3,914 | 546,241 | nanc |
| KXNFLDRAFTPICK | NFL Draft Pick | annual | 200 | 24 | $41,130 | 311,307 | 8.7c |
| KXSUPERBOWLWHITEHOUSE | WILL THE WINNERS OF THE PRO FOOTBALL CHA | one_off | 1 | 1 | $334 | 130,530 | 2.0c |
| KXCOACHOUTNFL | NFL Coach Out | custom | 22 | 3 | $135 | 59,659 | 47.0c |
| KXSUPERBOWLHEADLINE | Who will headline super bowl LX | one_off | 53 | 11 | $10 | 50,144 | 4.3c |
| KXSTARTINGQBWEEK1 | NFL Starting QB Week 1 | custom | 119 | 15 | $46 | 30,340 | 14.3c |
| KXNFLTRADE | NFL Trade | custom | 57 | 32 | $501 | 28,734 | 29.3c |
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
