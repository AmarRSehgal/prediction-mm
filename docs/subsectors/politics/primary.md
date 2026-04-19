# pol_primary

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **66** (66 with open markets)
- Open markets: **1230** (324 contested)
- Total 24h volume: **$1,387,681**
- Total open interest: **91,388,525**
- Top-OI mean spread (median across series): **4.2 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **4.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median cumulative depth within 5c of mid — bid: **370** / ask: **376** contracts
- Median cumulative depth within 10c of mid — bid: **994** / ask: **694** contracts
- Mean trades per market (last 3000): **249**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 49865 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPRESNOMD-28-GN | Gavin Newsom | 24c | 1.0c | 7495 | 26188 | 31126 | 81636 | 2528880 | $22956 | 30d+ |
| KXPRESNOMD-28-KH | Kamala Harris | 6c | 0.1c | 2092 | 834 | 119867 | 124658 | 2512823 | $41466 | 30d+ |
| KXPRESNOMD-28-JOSS | Jon Ossoff | 7c | 0.2c | 30 | 5001 | 57657 | 111839 | 2431895 | $34348 | 30d+ |
| KXPRESNOMD-28-AOC | Alexandria Ocasio-Cortez | 9c | 0.1c | 145 | 15868 | 55824 | 111276 | 2423860 | $11823 | 30d+ |
| KXPRESNOMD-28-PB | Pete Buttigieg | 6c | 0.1c | 738 | 13602 | 64737 | 218978 | 2204023 | $27836 | 30d+ |
| KXPRESNOMD-28-JS | Josh Shapiro | 5c | 0.1c | 17542 | 24326 | 86194 | 204615 | 1962218 | $2406 | 30d+ |
| KXPRESNOMR-28-MR | Marco Rubio | 26c | 1.0c | 6111 | 73207 | 20243 | 82243 | 1902651 | $2982 | 30d+ |
| KXPRESNOMR-28-JDV | J.D. Vance | 38c | 1.0c | 95189 | 69596 | 218714 | 73745 | 1291841 | $139763 | 30d+ |
| KXKY4R-26-TMAS | Thomas Massie | 70c | 1.0c | 524 | 1343 | 6624 | 207507 | 393624 | $4439 | 30d+ |
| KXKY4R-26-EGAL | Ed Gallrein | 29c | 2.0c | 1604 | 691 | 6698 | 7626 | 224302 | $2421 | 30d+ |
| KXGOVCAPRIMARY-26-MMAH | :: Democratic | 11c | 2.0c | 1476 | 10997 | 4446 | 12497 | 49927 | $232 | 30d+ |
| KXNY12D-26-JSCH | Jack Schlossberg | 20c | 1.0c | 124 | 9 | 3176 | 2566 | 48265 | $22 | 30d+ |
| KXLOSEPRIMARYHOUSER-26NOV03-6T | 7 or more | 31c | 4.0c | 126 | 108 | 326 | 129 | 42007 | $40 | 30d+ |
| KXGOVCAPRIMARY-26-TSTE | :: Democratic | 70c | 1.0c | 227 | 9 | 6389 | 226 | 39641 | $4561 | 30d+ |
| KXGOVCAPRIMARY-26-XBEC | :: Democratic | 26c | 1.0c | 22 | 50 | 1597 | 13399 | 30213 | $5673 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPRESNOMD | Democratic Primary winner | custom | 44 | 1 | $1,067,266 | 63,822,463 | 1.0c |
| KXPRESNOMR | Republican Primary winner | custom | 35 | 2 | $253,040 | 25,440,901 | 1.0c |
| KXKY4R | Kentucky 4 Republican primary | one_off | 4 | 2 | $9,819 | 618,343 | 1.0c |
| KXGOVCAPRIMARY | CA primary | one_off | 15 | 4 | $11,820 | 239,764 | 1.3c |
| KXNY12D | ny 12 democratic primary | one_off | 20 | 3 | $183 | 147,316 | 1.7c |
| KXLOSEPRIMARYHOUSER | How many House Republicans will lose the | one_off | 8 | 5 | $40 | 126,854 | 4.0c |
| KXPRIMARYMOV | Primary margins of victory | one_off | 35 | 14 | $10,096 | 88,003 | 2.3c |
| KXTXPRIMARY | Texas Primary Winners | one_off | 89 | 16 | $124 | 84,806 | 5.7c |
| KXCAGOVPRIMARY1ST | Who will finish first in the California  | one_off | 8 | 3 | $5,707 | 78,801 | 4.3c |
| KXKYPRIMARY | Kentucky Primary Winners | one_off | 34 | 10 | $136 | 75,429 | 3.0c |

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
