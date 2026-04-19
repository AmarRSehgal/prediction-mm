# sports_tennis_challenger

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **134** (111 contested)
- Total 24h volume: **$124,236**
- Total open interest: **98,142**
- Top-OI mean spread (median across series): **30.2 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **120**
- Median spread: **4.0c**
- Median TOB bid / ask size: **144 / 187** contracts
- Median cumulative depth within 5c of mid — bid: **487** / ask: **676** contracts
- Median cumulative depth within 10c of mid — bid: **1260** / ask: **1493** contracts
- Mean trades per market (last 3000): **27**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 9184 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXATPCHALLENGERMATCH-26APR18TROZAH-ZAH | Patrick Zahraj | nanc | nanc | nan | nan | nan | nan | 59877 | $26175 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18TROZAH-TRO | James Kent Trotter | nanc | nanc | nan | nan | nan | nan | 49232 | $49422 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18TUNIVA-TUN | Tung-Lin Wu | 86c | 1.0c | 5255 | 11739 | 35645 | 22677 | 10646 | $6983 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19SORGUE-SOR | Sebastian Sorger | 36c | 1.0c | 1278 | 358 | 3351 | 2216 | 6984 | $6984 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18DELSHI-SHI | Yuta Shimizu | 78c | 1.0c | 28 | 972 | 5502 | 4260 | 3842 | $3507 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19RIEYUN-YUN | Yunchaokete Bu | 60c | 1.0c | 7514 | 5389 | 8388 | 6624 | 3552 | $3425 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19SUNTUL-TUL | Li Tu | 57c | 3.0c | 2195 | 3435 | 12152 | 7904 | 2857 | $3374 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19ORLBET-ORL | Vladyslav Orlov | 94c | 3.0c | 400 | 486 | 920 | 3079 | 2403 | $2701 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18DELSHI-DEL | Jake Delaney | 22c | 1.0c | 1226 | 32 | 3140 | 4333 | 2257 | $2551 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19SUNTUL-SUN | Fajing Sun | 43c | 2.0c | 2719 | 91 | 8070 | 7255 | 1913 | $1981 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19MACCRE-MAC | Jamie Mackenzie | 38c | 1.0c | 366 | 711 | 1373 | 1035 | 1731 | $1731 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18TUNIVA-IVA | Ilya Ivashka | 14c | 1.0c | 150 | 7081 | 10430 | 48544 | 1625 | $731 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19ROYSAF-ROY | Valentin Royer | 57c | 2.0c | 767 | 953 | 4754 | 3600 | 1513 | $1485 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18CHUPAR-PAR | Tom Paris | 66c | 1.0c | 55 | 69 | 2008 | 1771 | 1499 | $916 | 7-30d |
| KXWTACHALLENGERMATCH-26APR19KUDCAS-CAS | Beatriz Castro | 6c | 1.0c | 519 | 401 | 7941 | 944 | 1310 | $1357 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXATPCHALLENGERMATCH | Challenger ATP  | custom | 90 | 71 | $120,589 | 94,542 | 1.3c |
| KXWTACHALLENGERMATCH | Challenger WTA | custom | 44 | 40 | $3,647 | 3,600 | 59.0c |

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
