# companies_execs

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **19** (19 with open markets)
- Open markets: **115** (83 contested)
- Total 24h volume: **$17,760**
- Total open interest: **803,907**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **95**
- Median spread: **5.0c**
- Median TOB bid / ask size: **25 / 52** contracts
- Median cumulative depth within 5c of mid — bid: **150** / ask: **375** contracts
- Median cumulative depth within 10c of mid — bid: **599** / ask: **811** contracts
- Mean trades per market (last 3000): **225**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 957 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 20394 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLAYOFFSYINFO-26-494000 | Above 494000 | 84c | 1.0c | 522 | 610 | 1422 | 4002 | 139277 | $2716 | 30d+ |
| KXRETIREMM-26 | Before election day 2026 | 20c | 2.0c | 9 | 28 | 2020 | 4642 | 71516 | $246 | 30d+ |
| KXAAPLCEOCHANGE-JUL | Before Jul 1, 2026 | 8c | 3.0c | 500 | 3 | 3067 | 1222 | 31965 | $0 | 30d+ |
| KXMLBPLAYOFFS-26-PIT | Pittsburgh | 48c | 3.0c | 40 | 40 | 114 | 2084 | 30065 | $640 | 30d+ |
| KXAAPLCEOCHANGE-26 | Before Jan 1, 2027 | 18c | 5.0c | 567 | 69 | 739 | 134 | 29210 | $220 | 30d+ |
| KXOPENAICEOCHANGE-26 | Hires | 36c | 4.0c | 52 | 28 | 745 | 576 | 26611 | $436 | 30d+ |
| KXNEWROLECEOAPPLE-27JAN-TERN | John Ternus | 30c | 5.0c | 37 | 235 | 269 | 736 | 17090 | $51 | 30d+ |
| KXMLBPLAYOFFS-26-LAA | Los Angeles A | 24c | 2.0c | 32 | 8 | 59 | 28 | 16594 | $1719 | 30d+ |
| KXMLBPLAYOFFS-26-MIL | Milwaukee | 60c | 1.0c | 20 | 16 | 30 | 1579 | 15940 | $2008 | 30d+ |
| KXCOMPANYACTIONLAYOFF-26JUL01 | Before July | 83c | 4.0c | 992 | 291 | 1492 | 797 | 15646 | $360 | 30d+ |
| KXNFLPLAYOFF-27-LV | Las Vegas | 20c | 7.0c | 5 | 10 | 25 | 310 | 15245 | $465 | 30d+ |
| KXMLBPLAYOFFS-26-ATH | A's | 34c | 11.0c | 31 | 79 | 0 | 0 | 14626 | $124 | 30d+ |
| KXMLBPLAYOFFS-26-STL | St. Louis | 20c | 16.0c | 32 | 1029 | 0 | 0 | 12927 | $76 | 30d+ |
| KXMLBPLAYOFFS-26-SD | San Diego | 48c | 4.0c | 35 | 560 | 90 | 560 | 12406 | $60 | 30d+ |
| KXKASHANNOUNCEOUT-26APR-MAY01 | Before May 1, 2026 | 38c | 4.0c | 33 | 30 | 459 | 196 | 12251 | $2247 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMLBPLAYOFFS | Pro Baseball Playoff Qualifiers | annual | 30 | 26 | $9,683 | 289,190 | 3.0c |
| KXLAYOFFSYINFO | Tech layoffs | annual | 1 | 1 | $2,778 | 139,252 | 1.0c |
| KXRETIREMM | Mitch McConnell resigning | custom | 1 | 1 | $242 | 71,516 | 3.0c |
| KXAAPLCEOCHANGE | Tim Cook leaves Apple | custom | 2 | 1 | $195 | 61,170 | 5.0c |
| KXNFLPLAYOFF | Pro Football Playoff Qualifiers | annual | 32 | 30 | $762 | 52,933 | 4.7c |
| KXTESLACEOCHANGE | New Tesla CEO | custom | 1 | 0 | $0 | 29,231 | nanc |
| KXCOMPANYACTIONLAYOFF | Layoff | one_off | 4 | 3 | $378 | 28,221 | 4.0c |
| KXOPENAICEOCHANGE | OpenAI hires another CEO | custom | 1 | 1 | $438 | 26,611 | 4.0c |
| KXNEWROLEX | X NEW CEO | custom | 8 | 1 | $40 | 26,547 | 7.0c |
| KXNEWROLECEOAPPLE | Next Apple CEO | one_off | 5 | 1 | $51 | 18,201 | 5.0c |

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
