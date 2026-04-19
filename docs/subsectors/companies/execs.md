# companies_execs

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **19** (19 with open markets)
- Open markets: **115** (83 contested)
- Total 24h volume: **$16,388**
- Total open interest: **804,538**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **95**
- Median spread: **5.0c**
- Median TOB bid / ask size: **25 / 72** contracts
- Median depth within 5c of best bid / ask — **455 / 736** contracts
- Median depth within 10c of best bid / ask — **847 / 1060** contracts
- Median depth within 5c of midpoint — bid: **150** / ask: **495** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **191**
- Mean informed-signal proxy: **-1.164** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.58c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 958 | 2.65 | 0.079 | 12.00 | 34.8 |
| 30d+ | 17174 | 1.81 | -0.615 | 7.00 | 40.7 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLAYOFFSYINFO-26-494000 | Above 494000 | 84c | 0.9c | 30 | 593 | 1388 | 4108 | 2793 | 4259 | 139272 | $2103 | 30d+ |
| KXRETIREMM-26 | Before election day 2026 | 20c | 2.0c | 9 | 36 | 2020 | 4642 | 2151 | 4742 | 71516 | $245 | 30d+ |
| KXAAPLCEOCHANGE-JUL | Before Jul 1, 2026 | 8c | 3.0c | 500 | 3 | 4447 | 1322 | 7624 | 2277 | 31965 | $0 | 30d+ |
| KXMLBPLAYOFFS-26-PIT | Pittsburgh | 49c | 2.0c | 40 | 40 | 119 | 2089 | 179 | 2210 | 30065 | $640 | 30d+ |
| KXAAPLCEOCHANGE-26 | Before Jan 1, 2027 | 19c | 4.0c | 32 | 37 | 771 | 652 | 1222 | 652 | 29223 | $252 | 30d+ |
| KXOPENAICEOCHANGE-26 | Hires | 36c | 4.0c | 52 | 18 | 745 | 566 | 745 | 566 | 26611 | $383 | 30d+ |
| KXNEWROLECEOAPPLE-27JAN-TERN | John Ternus | 30c | 5.0c | 37 | 235 | 769 | 736 | 999 | 1036 | 17090 | $51 | 30d+ |
| KXMLBPLAYOFFS-26-LAA | Los Angeles A | 26c | 5.0c | 44 | 20 | 94 | 1740 | 246 | 1800 | 16594 | $738 | 30d+ |
| KXMLBPLAYOFFS-26-MIL | Milwaukee | 61c | 2.0c | 35 | 516 | 45 | 1619 | 105 | 1685 | 15940 | $2028 | 30d+ |
| KXCOMPANYACTIONLAYOFF-26JUL01 | Before July | 83c | 4.0c | 992 | 290 | 1492 | 1843 | 1542 | 3287 | 15646 | $361 | 30d+ |
| KXNFLPLAYOFF-27-LV | Las Vegas | 20c | 7.0c | 5 | 10 | 366 | 1885 | 866 | 3153 | 15245 | $465 | 30d+ |
| KXMLBPLAYOFFS-26-ATH | A's | 34c | 10.0c | 21 | 84 | 415 | 1104 | 1609 | 1204 | 14631 | $88 | 30d+ |
| KXMLBPLAYOFFS-26-STL | St. Louis | 20c | 15.0c | 32 | 100 | 5949 | 1189 | 10714 | 1189 | 12927 | $76 | 30d+ |
| KXMLBPLAYOFFS-26-SD | San Diego | 48c | 4.0c | 60 | 560 | 228 | 568 | 1046 | 688 | 12406 | $20 | 30d+ |
| KXKASHANNOUNCEOUT-26APR-MAY01 | Before May 1, 2026 | 36c | 3.0c | 105 | 30 | 431 | 296 | 432 | 617 | 12251 | $1821 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMLBPLAYOFFS | Pro Baseball Playoff Qualifiers | annual | 30 | 26 | $8,715 | 289,654 | 3.7c |
| KXLAYOFFSYINFO | Tech layoffs | annual | 1 | 1 | $2,103 | 139,272 | 0.9c |
| KXRETIREMM | Mitch McConnell resigning | custom | 1 | 1 | $245 | 71,516 | 2.0c |
| KXAAPLCEOCHANGE | Tim Cook leaves Apple | custom | 2 | 1 | $252 | 61,188 | 5.0c |
| KXNFLPLAYOFF | Pro Football Playoff Qualifiers | annual | 32 | 30 | $834 | 52,929 | 5.7c |
| KXTESLACEOCHANGE | New Tesla CEO | custom | 1 | 0 | $0 | 29,231 | nanc |
| KXCOMPANYACTIONLAYOFF | Layoff | one_off | 4 | 3 | $367 | 28,221 | 4.3c |
| KXOPENAICEOCHANGE | OpenAI hires another CEO | custom | 1 | 1 | $383 | 26,611 | 4.0c |
| KXNEWROLEX | X NEW CEO | custom | 8 | 1 | $44 | 26,547 | 8.0c |
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
