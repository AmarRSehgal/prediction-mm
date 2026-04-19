# sports_draft

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **17** (17 with open markets)
- Open markets: **200** (200 contested)
- Total 24h volume: **$83,178**
- Total open interest: **896,101**
- Top-OI mean spread (median across series): **8.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **7.0c**
- Median TOB bid / ask size: **150 / 127** contracts
- Median depth within 5c of best bid / ask — **734 / 415** contracts
- Median depth within 10c of best bid / ask — **1188 / 556** contracts
- Median depth within 5c of midpoint — bid: **110** / ask: **161** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **120**
- Mean informed-signal proxy: **-0.951** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.67c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 16250 | 3.01 | -0.708 | 13.00 | 45.4 |
| 30d+ | 7762 | 3.93 | -1.379 | 18.00 | 57.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNFLDRAFTTOP-26-10-CDOW | Caleb Downs | 80c | 9.0c | 217 | 56 | 3399 | 897 | 3709 | 1036 | 27987 | $889 | 7-30d |
| KXNFLDRAFTTOP-26-5-JLOV | Jeremiyah Love | 71c | 2.0c | 22 | 4 | 1327 | 4 | 1947 | 8 | 25618 | $1997 | 7-30d |
| KXNFLDRAFTTOP-26-10-JTYS | Jordyn Tyson | 76c | 3.0c | 41 | 31 | 2788 | 547 | 4826 | 3541 | 24942 | $10636 | 7-30d |
| KXNFLDRAFTTOP-26-10-RBAI | Rueben Bain Jr. | 60c | 3.0c | 27 | 94 | 826 | 396 | 927 | 1518 | 23855 | $2088 | 7-30d |
| KXNFLDRAFTTOP-26-10-MFRE | Monroe Freeling | 13c | 2.0c | 56 | 11 | 668 | 743 | 6934 | 743 | 22465 | $804 | 7-30d |
| KXNBADRAFTTOP-26-3-DACU | Darius Acuff Jr. | 16c | 5.0c | 522 | 99 | 522 | 1535 | 537 | 1535 | 21167 | $19 | 30d+ |
| KXNFLDRAFTTOP-26-R1-TSIM | Ty Simpson | 73c | 15.0c | 2 | 3 | 525 | 359 | 1753 | 634 | 18945 | $5205 | 7-30d |
| KXNFLDRAFTTOP-26-5-AREE | Arvell Reese | 88c | 7.0c | 9 | 990 | 9 | 3106 | 9 | 5850 | 17765 | $1537 | 7-30d |
| KXNFLDRAFTWR-26P1-JTYS | Jordyn Tyson | 36c | 12.0c | 56 | 9 | 1260 | 9 | 2623 | 213 | 16505 | $1810 | 7-30d |
| KXNFLDRAFTWR-26P1-CTAT | Carnell Tate | 69c | 8.0c | 188 | 20 | 188 | 655 | 188 | 1155 | 15187 | $3151 | 7-30d |
| KXNFLDRAFTTOP-26-10-MLEM | Makai Lemon | 9c | 6.0c | 6 | 39 | 4767 | 328 | 4767 | 1941 | 14629 | $1090 | 7-30d |
| KXNBADRAFTTOP-26-5-DACU | Darius Acuff Jr. | 66c | 1.0c | 29 | 126 | 29 | 741 | 29 | 1241 | 14575 | $0 | 30d+ |
| KXNFLDRAFTDB-26P1-CDOW | Caleb Downs | 66c | 7.0c | 165 | 509 | 1165 | 2092 | 1165 | 2492 | 14363 | $260 | 7-30d |
| KXNBADRAFTTOP-26-5-KFLE | Kingston Flemings | 35c | 4.0c | 500 | 133 | 500 | 1143 | 500 | 1143 | 14191 | $0 | 30d+ |
| KXNFLDRAFTTOP-26-10-SFAN | Spencer Fano | 39c | 10.0c | 9 | 19 | 409 | 19 | 516 | 19 | 13229 | $1528 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNFLDRAFTTOP | Caleb Downs | nan | 67 | 67 | $40,707 | 450,672 | 4.7c |
| KXNBADRAFTTOP | Darius Acuff Jr. | nan | 22 | 22 | $2,128 | 106,069 | 3.3c |
| KXNFLDRAFTWR | Jordyn Tyson | nan | 16 | 16 | $10,767 | 80,765 | 8.0c |
| KXNFLDRAFTTEAM | New York J | nan | 27 | 27 | $13,777 | 58,511 | 9.7c |
| KXNBATOPPICK | Utah | nan | 8 | 8 | $5,174 | 40,914 | 2.3c |
| KXNFLDRAFTOL | Francis Mauigoa | nan | 11 | 11 | $3,313 | 37,232 | 3.0c |
| KXNFLDRAFTDB | Caleb Downs | nan | 3 | 3 | $1,586 | 31,897 | 11.7c |
| KXNFLDRAFTEDGE | Rueben Bain Jr. | nan | 10 | 10 | $970 | 24,170 | 22.3c |
| KXNFLDRAFTDT | Kayden McDonald | nan | 5 | 5 | $1,893 | 12,530 | 23.0c |
| KXNFLDRAFTLB | Sonny Styles | nan | 6 | 6 | $595 | 10,373 | 7.7c |

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
