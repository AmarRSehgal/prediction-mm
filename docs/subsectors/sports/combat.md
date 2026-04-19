# sports_combat

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **30** (30 with open markets)
- Open markets: **326** (160 contested)
- Total 24h volume: **$1,729,412**
- Total open interest: **3,224,812**
- Top-OI mean spread (median across series): **12.5 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **147**
- Median spread: **91.0c**
- Median TOB bid / ask size: **47 / 250** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **119**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1649 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 15904 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBOXING-26APR25MTYSFMAY-MTYS | Mike Tyson | 26c | 2.0c | 2839 | 25266 | 14477 | 30304 | 156813 | $9495 | 7-30d |
| KXBOXING-26APR25MTYSFMAY-FMAY | Floyd Mayweather | 74c | 1.0c | 89 | 31459 | 5599 | 82559 | 120154 | $1858 | 7-30d |
| KXBOXING-26SEP19FMAYMPAC-MPAC | Manny Pacquiao | 36c | 2.0c | 12 | 16 | 95 | 11594 | 28956 | $1156 | 30d+ |
| KXUFCWHITEHOUSE-26JUL05 | Before Jul 5, 2026 | 90c | 7.0c | 2 | 273 | 11 | 2293 | 28197 | $75 | 30d+ |
| KXUFCFLYWEIGHTTITLE-26-APAN | Alexandre Pantoja | 42c | 27.0c | 1 | 1020 | 0 | 0 | 28002 | $18 | 30d+ |
| KXBOXING-26SEP19FMAYMPAC-FMAY | Floyd Mayweather Jr. | 64c | 2.0c | 18 | 6740 | 18 | 15888 | 22752 | $459 | 30d+ |
| KXUFCLHEAVYWEIGHTTITLE-26-KCHI | Khamzat Chimaev | 12c | 6.0c | 35 | 29 | 557 | 68 | 11584 | $654 | 30d+ |
| KXUFCLHEAVYWEIGHTTITLE-26-CULB | Carlos Ulberg | 52c | 6.0c | 1963 | 416 | 1963 | 416 | 11370 | $400 | 30d+ |
| KXUFCMIDDLEWEIGHTTITLE-26-KCHI | Khamzat Chimaev | 74c | 1.0c | 21 | 1230 | 21 | 1230 | 11148 | $0 | 30d+ |
| KXUFCFLYWEIGHTTITLE-26-TTAI | Tatsuro Taira | 32c | 4.0c | 13 | 1000 | 13 | 1009 | 10141 | $24 | 30d+ |
| KXUFCMIDDLEWEIGHTTITLE-26-SSTR | Sean Strickland | 20c | 4.0c | 42 | 1210 | 42 | 1210 | 9699 | $86 | 30d+ |
| KXUFCFLYWEIGHTTITLE-26-JVAN | Joshua Van | 16c | 5.0c | 30 | 209 | 38 | 209 | 9501 | $21 | 30d+ |
| KXUFCLHEAVYWEIGHTTITLE-26-MANK | Magomed Ankalaev | 13c | 9.0c | 11 | 61 | 11 | 61 | 9154 | $329 | 30d+ |
| KXUFCLIGHTWEIGHTTITLE-26-ATSA | Arman Tsarukyan | 22c | 5.0c | 9 | 413 | 159 | 413 | 8490 | $0 | 30d+ |
| KXFLOYDTYSONFIGHT-27JAN01 | Before Jan 1, 2027 | 57c | 5.0c | 510 | 57 | 2236 | 57 | 7164 | $203 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXUFCFIGHT | UFC Fight | custom | 4 | 4 | $1,442,217 | 1,968,033 | 1.7c |
| KXBOXING | Boxing Match Champion | custom | 24 | 24 | $13,964 | 329,129 | 2.0c |
| KXUFCMOV | UFC Method of Victory | custom | 14 | 8 | $204,211 | 224,386 | 3.3c |
| KXCARDPRESENCEUFCWH | UFC White House event | custom | 5 | 0 | $8,575 | 189,544 | nanc |
| KXFLOYDTYSONFIGHT | Floyd vs Tyson Fight | custom | 2 | 1 | $15,356 | 97,326 | 5.0c |
| KXUFCLHEAVYWEIGHTTITLE | UFC Light Heavyweight Title | custom | 10 | 2 | $2,128 | 84,619 | 7.0c |
| KXUFCFLYWEIGHTTITLE | UFC Flyweight Title | custom | 9 | 4 | $62 | 62,633 | 13.3c |
| KXUFCMIDDLEWEIGHTTITLE | UFC Middleweight Title | custom | 8 | 2 | $86 | 44,266 | 2.5c |
| KXUFCLIGHTWEIGHTTITLE | UFC Lightweight Title | custom | 11 | 2 | $9 | 37,934 | 8.5c |
| KXUFCWELTERWEIGHTTITLE | UFC Welterweight Title | custom | 10 | 3 | $467 | 31,563 | 14.3c |

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
