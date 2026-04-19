# sports_combat

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **29** (29 with open markets)
- Open markets: **296** (141 contested)
- Total 24h volume: **$173,886**
- Total open interest: **1,105,119**
- Top-OI mean spread (median across series): **19.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **146**
- Median spread: **91.0c**
- Median TOB bid / ask size: **50 / 250** contracts
- Median depth within 5c of best bid / ask — **50 / 250** contracts
- Median depth within 10c of best bid / ask — **50 / 436** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **90**
- Mean informed-signal proxy: **-3.599** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **10.41c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1667 | 0.39 | -0.315 | 2.00 | 49.2 |
| 30d+ | 11533 | 3.44 | -0.967 | 15.00 | 30.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBOXING-26APR25MTYSFMAY-MTYS | Mike Tyson | 26c | 2.0c | 2696 | 24814 | 20856 | 32852 | 25593 | 36161 | 156724 | $8160 | 7-30d |
| KXBOXING-26APR25MTYSFMAY-FMAY | Floyd Mayweather | 74c | 1.0c | 76 | 31261 | 5621 | 86145 | 5625 | 120193 | 120456 | $1996 | 7-30d |
| KXBOXING-26SEP19FMAYMPAC-MPAC | Manny Pacquiao | 36c | 3.0c | 12 | 6593 | 127 | 16593 | 228 | 41627 | 28944 | $1087 | 30d+ |
| KXUFCWHITEHOUSE-26JUL05 | Before Jul 5, 2026 | 90c | 7.0c | 2 | 277 | 3187 | 9369 | 3187 | 18879 | 28197 | $75 | 30d+ |
| KXUFCFLYWEIGHTTITLE-26-APAN | Alexandre Pantoja | 42c | 27.0c | 5 | 1000 | 124 | 1000 | 129 | 1000 | 28002 | $18 | 30d+ |
| KXBOXING-26SEP19FMAYMPAC-FMAY | Floyd Mayweather Jr. | 59c | 6.0c | 17 | 32 | 97 | 10921 | 224 | 21022 | 22768 | $294 | 30d+ |
| KXUFCLHEAVYWEIGHTTITLE-26-KCHI | Khamzat Chimaev | 19c | 20.0c | 72 | 8 | 649 | 1501 | 2420 | 1517 | 11757 | $818 | 30d+ |
| KXUFCLHEAVYWEIGHTTITLE-26-CULB | Carlos Ulberg | 52c | 6.0c | 1943 | 395 | 1943 | 395 | 1943 | 395 | 11391 | $412 | 30d+ |
| KXUFCMIDDLEWEIGHTTITLE-26-KCHI | Khamzat Chimaev | 74c | 1.0c | 21 | 1230 | 21 | 1230 | 129 | 1230 | 11148 | $0 | 30d+ |
| KXUFCFLYWEIGHTTITLE-26-TTAI | Tatsuro Taira | 24c | 20.0c | 500 | 997 | 504 | 1006 | 521 | 1006 | 10144 | $27 | 30d+ |
| KXUFCMIDDLEWEIGHTTITLE-26-SSTR | Sean Strickland | 20c | 4.0c | 42 | 1210 | 42 | 1210 | 42 | 1210 | 9699 | $86 | 30d+ |
| KXUFCFLYWEIGHTTITLE-26-JVAN | Joshua Van | 16c | 5.0c | 19 | 209 | 151 | 209 | 664 | 209 | 9501 | $21 | 30d+ |
| KXUFCLHEAVYWEIGHTTITLE-26-MANK | Magomed Ankalaev | 12c | 8.0c | 69 | 3 | 1081 | 558 | 4509 | 558 | 9187 | $320 | 30d+ |
| KXUFCLIGHTWEIGHTTITLE-26-ATSA | Arman Tsarukyan | 22c | 5.0c | 9 | 393 | 159 | 545 | 161 | 1055 | 8498 | $8 | 30d+ |
| KXFLOYDTYSONFIGHT-27JAN01 | Before Jan 1, 2027 | 56c | 4.0c | 510 | 57 | 2236 | 57 | 2295 | 1865 | 7164 | $203 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBOXING | Boxing Match Champion | custom | 24 | 24 | $11,583 | 329,715 | 1.7c |
| KXCARDPRESENCEUFCWH | UFC White House event | custom | 5 | 0 | $11,893 | 189,911 | nanc |
| KXFLOYDTYSONFIGHT | Floyd vs Tyson Fight | custom | 2 | 1 | $17,606 | 99,196 | 5.0c |
| KXUFCMOV | UFC Method of Victory | custom | 7 | 0 | $104,194 | 90,849 | nanc |
| KXUFCLHEAVYWEIGHTTITLE | UFC Light Heavyweight Title | custom | 10 | 3 | $2,881 | 85,327 | 12.0c |
| KXUFCFLYWEIGHTTITLE | UFC Flyweight Title | custom | 9 | 4 | $63 | 62,633 | 17.3c |
| KXUFCMIDDLEWEIGHTTITLE | UFC Middleweight Title | custom | 8 | 2 | $86 | 44,266 | 2.5c |
| KXUFCLIGHTWEIGHTTITLE | UFC Lightweight Title | custom | 11 | 2 | $17 | 37,942 | 23.5c |
| KXUFCWELTERWEIGHTTITLE | UFC Welterweight Title | custom | 10 | 3 | $806 | 31,875 | 17.7c |
| KXUFCWHITEHOUSE | UFC at White House | one_off | 1 | 1 | $75 | 28,197 | 8.0c |

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
