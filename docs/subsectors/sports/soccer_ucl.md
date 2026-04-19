# sports_soccer_ucl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **12** (12 with open markets)
- Open markets: **66** (47 contested)
- Total 24h volume: **$275,098**
- Total open interest: **4,861,503**
- Top-OI mean spread (median across series): **2.6 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **50**
- Median spread: **2.5c**
- Median TOB bid / ask size: **432 / 187** contracts
- Median depth within 5c of best bid / ask — **5062 / 1175** contracts
- Median depth within 10c of best bid / ask — **5693 / 2807** contracts
- Median depth within 5c of midpoint — bid: **1296** / ask: **1175** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **454**
- Mean informed-signal proxy: **-0.976** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.23c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 5978 | 0.67 | -0.300 | 3.00 | 86.0 |
| 30d+ | 16746 | 1.66 | -0.696 | 7.00 | 81.1 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXUCL-26-BMU | Bayern Munich | 35c | 2.0c | 90822 | 329563 | 325308 | 435691 | 325308 | 481123 | 935893 | $34802 | 30d+ |
| KXUCL-26-ARS | Arsenal | 28c | 1.0c | 13367 | 367 | 249198 | 390175 | 291209 | 464107 | 772755 | $29583 | 30d+ |
| KXUCL-26-PSG | PSG | 26c | 1.0c | 5522 | 19291 | 259893 | 284436 | 260068 | 321536 | 677315 | $19634 | 30d+ |
| KXUCL-26-ATM | Atletico | 12c | 1.0c | 4551 | 90976 | 100124 | 167003 | 364933 | 167003 | 653293 | $11841 | 30d+ |
| KXUSAIRANAGREEMENT-27-26MAY | Before May | 19c | 1.0c | 543 | 1026 | 3943 | 2508 | 11485 | 2690 | 397137 | $42037 | 7-30d |
| KXREACTOR-26DEC31 | By Dec 31, 2026 | 27c | 1.3c | 38 | 75 | 6123 | 4830 | 9963 | 4899 | 210235 | $1857 | 30d+ |
| KXUSAIRANAGREEMENT-27-26JUN | Before June | 43c | 1.0c | 767 | 1012 | 3499 | 1114 | 5608 | 3186 | 191581 | $13581 | 30d+ |
| KXUSAIRANAGREEMENT-27 | Before 2027 | 76c | 1.0c | 2485 | 1248 | 5785 | 4607 | 7202 | 4607 | 170629 | $12258 | 30d+ |
| KXUSAIRANAGREEMENT-27-26AUG | Before August | 62c | 1.0c | 31 | 44 | 5746 | 975 | 5777 | 1071 | 158661 | $13716 | 30d+ |
| KXUCLGAME-26APR29ATMARS-ATM | Atletico | 33c | 2.0c | 669 | 109 | 51971 | 187491 | 51977 | 322091 | 120469 | $12434 | 7-30d |
| KXUCLGAME-26APR28PSGBMU-PSG | PSG | 43c | 1.0c | 765 | 38327 | 57354 | 199751 | 57355 | 248755 | 107139 | $12155 | 7-30d |
| KXUCLGAME-26APR28PSGBMU-BMU | Bayern Munich | 34c | 2.0c | 364 | 33733 | 51264 | 232596 | 51264 | 321256 | 81454 | $23795 | 7-30d |
| KXCRITICALITY-26AUG-VALAR | Valar Atomics | 72c | 5.0c | 16 | 522 | 16756 | 522 | 16826 | 522 | 39021 | $17 | 30d+ |
| KXUSAIRANAGREEMENT-27-26JUL | Before July | 56c | 3.0c | 46 | 480 | 46 | 1077 | 896 | 1432 | 32518 | $7431 | 30d+ |
| KXTEAMSINUCL-26-BMUATM | Bayern vs Atletico | 22c | 3.0c | 300 | 16 | 1428 | 12921 | 1428 | 13921 | 28874 | $4340 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXUCL | UEFA Champions League | custom | 4 | 4 | $96,379 | 3,039,111 | 1.3c |
| KXUSAIRANAGREEMENT | US Iran nuclear deal | custom | 8 | 8 | $92,805 | 979,296 | 1.3c |
| KXUCLGAME | UEFA Champions League Game | custom | 9 | 9 | $61,098 | 337,246 | 1.7c |
| KXREACTOR | US grants license for new nuclear reacto | custom | 1 | 1 | $1,831 | 210,235 | 1.3c |
| KXTEAMSINUCL | Champions League Final Matchup | custom | 4 | 4 | $18,219 | 95,331 | 2.0c |
| KXCRITICALITY | Nuclear power criticality | custom | 10 | 7 | $1,192 | 81,457 | 5.7c |
| KXUCLFINALIST | UCL Advance to the Finals | annual | 4 | 4 | $2,380 | 77,603 | 1.7c |
| KXLEADERUCLGOALS | UCL Top Goalscorer | annual | 9 | 2 | $905 | 19,210 | 4.5c |
| KXFUSION | Nuclear fusion | custom | 3 | 3 | $7 | 16,683 | 3.2c |
| KXDATACENTER | Data center nuclear | custom | 1 | 1 | $27 | 3,544 | 5.0c |

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
