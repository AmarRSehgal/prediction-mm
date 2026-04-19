# sports_tennis_itf

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **194** (194 contested)
- Total 24h volume: **$4,921**
- Total open interest: **2,188**
- Top-OI mean spread (median across series): **13.7 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **192**
- Median spread: **88.0c**
- Median TOB bid / ask size: **116 / 20** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **9**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 8398 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXITFWMATCH-26APR18BAISHI-SHI | Han Shi | nanc | nanc | nan | nan | nan | nan | 4029 | $3883 | 7-30d |
| KXITFWMATCH-26APR18WONIVA-WON | Hong Yi Cody Wong | nanc | nanc | nan | nan | nan | nan | 2959 | $3183 | 7-30d |
| KXITFWMATCH-26APR18WONIVA-IVA | Valentina Ivanov | nanc | nanc | nan | nan | nan | nan | 2130 | $2298 | 7-30d |
| KXITFWMATCH-26APR18BAISHI-BAI | Zhuoxuan Bai | nanc | nanc | nan | nan | nan | nan | 1382 | $1389 | 7-30d |
| KXITFMATCH-26APR18MATOHX-OHX | Chan-Yeong Oh | nanc | nanc | nan | nan | nan | nan | 1349 | $1434 | 7-30d |
| KXITFWMATCH-26APR18SUNCUI-CUI | Angela Cui | 77c | 13.0c | 11 | 13 | 0 | 0 | 1189 | $1191 | 7-30d |
| KXITFMATCH-26APR18MATOHX-MAT | Koki Matsuda | nanc | nanc | nan | nan | nan | nan | 1066 | $1007 | 7-30d |
| KXITFMATCH-26APR18STRTRE-TRE | Simon TREMOLIERES | 21c | 10.0c | 7 | 6 | 0 | 6 | 918 | $1775 | 7-30d |
| KXITFMATCH-26APR18TREKAM-TRE | Julien Tremolieres | 15c | 12.0c | 14 | 2 | 0 | 0 | 629 | $1199 | 7-30d |
| KXITFMATCH-26APR18STRTRE-STR | Tristan Stringer | 74c | 28.0c | 5 | 4 | 0 | 0 | 166 | $411 | 7-30d |
| KXITFWMATCH-26APR18HANMES-HAN | chengwei Han | nanc | nanc | nan | nan | nan | nan | 163 | $8 | 7-30d |
| KXITFMATCH-26APR18TREKAM-KAM | Udit Kamboj | 50c | 89.0c | 1 | 2 | 0 | 0 | 157 | $342 | 7-30d |
| KXITFWMATCH-26APR18SUNCUI-SUN | Junjie Sun | 24c | 8.0c | 70 | 50 | 70 | 53 | 123 | $123 | 7-30d |
| KXITFWMATCH-26APR18KINCHA-KIN | Hayu Kinoshita | 89c | 2.0c | 110 | 877 | 1780 | 7524 | 62 | $62 | 7-30d |
| KXITFWMATCH-26APR18ANXYEX-YEX | Qiu Yu Ye | 62c | 65.0c | 8 | 72 | 0 | 0 | 61 | $102 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXITFMATCH | ITF Men's Match | custom | 64 | 64 | $4,455 | 1,850 | 21.7c |
| KXITFWMATCH | ITF Women's Match | custom | 130 | 130 | $466 | 338 | 5.7c |

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
