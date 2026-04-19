# sports_motor_nascar

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **117** (117 contested)
- Total 24h volume: **$284,381**
- Total open interest: **1,104,723**
- Top-OI mean spread (median across series): **14.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **117**
- Median spread: **27.0c**
- Median TOB bid / ask size: **994 / 300** contracts
- Median depth within 5c of best bid / ask — **1991 / 675** contracts
- Median depth within 10c of best bid / ask — **1993 / 1479** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **82**
- Mean informed-signal proxy: **0.299** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.65c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2027 | 1.04 | -0.150 | 4.00 | 202.5 |
| 30d+ | 7592 | 1.06 | -0.455 | 4.00 | 94.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNASCARCUPSERIES-NCS26-TRED | Tyler Reddick | 19c | 3.0c | 9 | 487 | 4203 | 4009 | 29957 | 32165 | 149197 | $1449 | 30d+ |
| KXNASCARRACE-ADV26-TYGI | Ty Gibbs | 8c | 1.0c | 899 | 15301 | 22015 | 31366 | 29619 | 33474 | 102471 | $93485 | 7-30d |
| KXNASCARCUPSERIES-NCS26-KLAR | Kyle Larson | 10c | 2.0c | 7713 | 1034 | 31743 | 3843 | 36826 | 8860 | 90736 | $2123 | 30d+ |
| KXNASCARCUPSERIES-NCS26-DHAM | Denny Hamlin | 14c | 3.0c | 131 | 702 | 4839 | 4552 | 19960 | 14567 | 90092 | $1773 | 30d+ |
| KXNASCARRACE-ADV26-CHBE | Christopher Bell | 14c | 1.0c | 300 | 34227 | 7340 | 40286 | 17498 | 40286 | 89797 | $31100 | 7-30d |
| KXNASCARCUPSERIES-NCS26-CBEL | Christopher Bell | 8c | 2.0c | 11 | 741 | 11649 | 4038 | 21248 | 26260 | 84322 | $41 | 30d+ |
| KXNASCARCUPSERIES-NCS26-WBYR | William Byron | 7c | 2.0c | 4992 | 1637 | 14868 | 10805 | 14868 | 11758 | 82027 | $128 | 30d+ |
| KXNASCARCUPSERIES-NCS26-RBLA | Ryan Blaney | 10c | 2.0c | 23 | 742 | 16258 | 5843 | 22831 | 21770 | 81763 | $1464 | 30d+ |
| KXNASCARCUPSERIES-NCS26-CELL | Chase Elliott | 7c | 2.0c | 2651 | 526 | 26018 | 2526 | 26018 | 2536 | 73076 | $1195 | 30d+ |
| KXNASCARRACE-ADV26-TYRE | Tyler Reddick | 19c | 1.0c | 14997 | 73482 | 63197 | 79813 | 64811 | 80094 | 45216 | $30005 | 7-30d |
| KXNASCARRACE-ADV26-KYLA | Kyle Larson | 12c | 1.0c | 117 | 4178 | 11164 | 76697 | 20793 | 78416 | 42240 | $30501 | 7-30d |
| KXNASCARRACE-ADV26-RYBL | Ryan Blaney | 6c | 1.0c | 12205 | 75069 | 22189 | 89296 | 22189 | 94096 | 32317 | $20836 | 7-30d |
| KXNASCARRACE-ADV26-DEHA | Denny Hamlin | 16c | 1.0c | 1802 | 83321 | 13142 | 85916 | 18939 | 90096 | 29555 | $21936 | 7-30d |
| KXNASCARRACE-ADV26-CHBR | Chase Briscoe | 6c | 1.0c | 521 | 85831 | 19387 | 91854 | 19387 | 92900 | 24735 | $12366 | 7-30d |
| KXNASCARAUTOPARTSSERIES-NAPS26-CDAY | Corey Day | 6c | 3.0c | 111 | 5489 | 35140 | 5489 | 35140 | 6252 | 5505 | $12 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNASCARCUPSERIES | Tyler Reddick | nan | 7 | 7 | $8,173 | 651,212 | 2.7c |
| KXNASCARRACE | Ty Gibbs | nan | 7 | 7 | $240,228 | 366,331 | 1.0c |
| KXNASCARTOP10 | Chris Buescher | nan | 27 | 27 | $24,699 | 37,500 | 23.0c |
| KXNASCARAUTOPARTSSERIES | Corey Day | nan | 7 | 7 | $1,312 | 20,555 | 6.3c |
| KXNASCARTOP5 | Christopher Bell | nan | 16 | 16 | $6,484 | 12,000 | 34.7c |
| KXNASCARTRUCKSERIES | Kaden Honeycutt | nan | 5 | 5 | $88 | 9,706 | 3.7c |
| KXNASCARTOP3 | Christopher Bell | nan | 12 | 12 | $2,816 | 4,295 | 27.3c |
| KXNASCARTOP20 | Connor Zilisch | nan | 36 | 36 | $581 | 3,123 | 77.3c |

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
