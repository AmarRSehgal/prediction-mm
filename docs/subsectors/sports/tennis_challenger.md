# sports_tennis_challenger

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **144** (115 contested)
- Total 24h volume: **$971,013**
- Total open interest: **945,468**
- Top-OI mean spread (median across series): **2.8 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **130**
- Median spread: **4.5c**
- Median TOB bid / ask size: **136 / 66** contracts
- Median depth within 5c of best bid / ask — **1741 / 2508** contracts
- Median depth within 10c of best bid / ask — **3765 / 4621** contracts
- Median depth within 5c of midpoint — bid: **334** / ask: **164** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **50**
- Mean informed-signal proxy: **-0.437** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.91c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 10528 | 0.81 | -0.202 | 3.00 | 151.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXATPCHALLENGERMATCH-26APR18TUNIVA-TUN | Tung-Lin Wu | nanc | nanc | nan | nan | nan | nan | nan | nan | 251935 | $325452 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18CHUPAR-PAR | Tom Paris | 48c | 1.0c | 200 | 7589 | 1472 | 9968 | 13326 | 11309 | 110281 | $89614 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18TUNIVA-IVA | Ilya Ivashka | nanc | nanc | nan | nan | nan | nan | nan | nan | 97924 | $127097 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19RIEYUN-YUN | Yunchaokete Bu | 58c | 1.0c | 258 | 1159 | 23331 | 18934 | 26897 | 20481 | 28433 | $28360 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18CHUPAR-CHU | Yun Seong Chung | 52c | 5.0c | 757 | 987 | 4182 | 15502 | 4184 | 24402 | 28261 | $27465 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18DELSHI-SHI | Yuta Shimizu | nanc | nanc | nan | nan | nan | nan | nan | nan | 25031 | $24938 | 7-30d |
| KXATPCHALLENGERMATCH-26APR18DELSHI-DEL | Jake Delaney | nanc | nanc | nan | nan | nan | nan | nan | nan | 21578 | $18584 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19SUNTUL-SUN | Fajing Sun | 40c | 1.0c | 509 | 6988 | 26311 | 48546 | 32124 | 58376 | 18328 | $17738 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19SUNTUL-TUL | Li Tu | 60c | 2.0c | 8049 | 1073 | 21620 | 24098 | 21658 | 29879 | 13799 | $16908 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19SATMAT-MAT | Hayato Matsuoka | 94c | 1.0c | 1 | 14125 | 1200 | 37492 | 1321 | 37492 | 12547 | $12931 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19KIRKEL-KIR | Ergi Kirkin | 70c | 9.0c | 164 | 154 | 349 | 4193 | 454 | 5475 | 8133 | $8289 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19SORGUE-SOR | Sebastian Sorger | 34c | 1.0c | 1271 | 773 | 4029 | 2987 | 7369 | 5777 | 6984 | $6984 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19ROYSAF-ROY | Valentin Royer | 57c | 1.0c | 640 | 2127 | 5418 | 6080 | 7929 | 8116 | 5819 | $5829 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19MORSEK-SEK | Philip Sekulic | 71c | 2.0c | 25 | 274 | 12487 | 10928 | 13149 | 11709 | 5068 | $4572 | 7-30d |
| KXATPCHALLENGERMATCH-26APR19RIEYUN-RIE | Leandro Riedi | 43c | 1.0c | 282 | 89 | 4554 | 29417 | 20154 | 29792 | 3286 | $3143 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXATPCHALLENGERMATCH | Challenger ATP  | custom | 100 | 75 | $965,264 | 940,149 | 1.3c |
| KXWTACHALLENGERMATCH | Challenger WTA | custom | 44 | 40 | $5,750 | 5,319 | 4.3c |

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
