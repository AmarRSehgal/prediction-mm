# pol_primary

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **66** (66 with open markets)
- Open markets: **1230** (317 contested)
- Total 24h volume: **$1,944,594**
- Total open interest: **92,018,935**
- Top-OI mean spread (median across series): **3.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **4.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median depth within 5c of best bid / ask — **605 / 551** contracts
- Median depth within 10c of best bid / ask — **1340 / 858** contracts
- Median depth within 5c of midpoint — bid: **324** / ask: **383** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **156**
- Mean informed-signal proxy: **-0.060** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.83c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 31223 | 1.49 | -0.281 | 6.00 | 175.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPRESNOMD-28-GN | Gavin Newsom | 24c | 1.0c | 7414 | 26288 | 31767 | 81936 | 42687 | 139360 | 2528739 | $23237 | 30d+ |
| KXPRESNOMD-28-KH | Kamala Harris | 6c | 0.1c | 2092 | 774 | 119867 | 124848 | 13071840 | 143767 | 2512823 | $41489 | 30d+ |
| KXPRESNOMD-28-JOSS | Jon Ossoff | 7c | 0.3c | 780 | 339 | 63664 | 107582 | 14026821 | 131069 | 2447642 | $48911 | 30d+ |
| KXPRESNOMD-28-AOC | Alexandria Ocasio-Cortez | 9c | 0.1c | 220 | 15767 | 56903 | 110925 | 57628 | 121341 | 2424685 | $12649 | 30d+ |
| KXPRESNOMD-28-PB | Pete Buttigieg | 6c | 0.1c | 738 | 13503 | 70566 | 218879 | 20181409 | 228948 | 2204122 | $27917 | 30d+ |
| KXPRESNOMD-28-JS | Josh Shapiro | 5c | 0.1c | 17542 | 24905 | 92275 | 205193 | 10853830 | 209505 | 1962391 | $2545 | 30d+ |
| KXPRESNOMR-28-MR | Marco Rubio | 26c | 1.0c | 6111 | 73276 | 20243 | 82312 | 21141 | 82567 | 1902508 | $3171 | 30d+ |
| KXPRESNOMR-28-JDV | J.D. Vance | 38c | 1.0c | 95178 | 70061 | 225996 | 74410 | 232684 | 86274 | 1291876 | $137008 | 30d+ |
| KXKY4R-26-TMAS | Thomas Massie | 70c | 1.0c | 524 | 1333 | 9652 | 207998 | 13200 | 214142 | 393651 | $3002 | 30d+ |
| KXKY4R-26-EGAL | Ed Gallrein | 29c | 2.0c | 1604 | 691 | 7200 | 9562 | 10947 | 16565 | 224302 | $2416 | 30d+ |
| KXGOVCAPRIMARY-26-MMAH | :: Democratic | 11c | 2.0c | 1476 | 10997 | 5156 | 12497 | 10825 | 14606 | 49927 | $232 | 30d+ |
| KXNY12D-26-JSCH | Jack Schlossberg | 20c | 1.0c | 1 | 9 | 2984 | 2500 | 4161 | 2503 | 48265 | $22 | 30d+ |
| KXLOSEPRIMARYHOUSER-26NOV03-6T | 7 or more | 30c | 3.0c | 26 | 26 | 326 | 326 | 326 | 2216 | 42007 | $40 | 30d+ |
| KXGOVCAPRIMARY-26-TSTE | :: Democratic | 70c | 1.0c | 227 | 9 | 6389 | 1226 | 6389 | 1851 | 39641 | $3929 | 30d+ |
| KXGOVCAPRIMARY-26-XBEC | :: Democratic | 26c | 2.0c | 88 | 94 | 1622 | 13461 | 1622 | 14460 | 30213 | $2944 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPRESNOMD | Democratic Primary winner | custom | 44 | 1 | $1,597,955 | 64,402,913 | 1.0c |
| KXPRESNOMR | Republican Primary winner | custom | 35 | 2 | $259,578 | 25,461,389 | 1.0c |
| KXKY4R | Kentucky 4 Republican primary | one_off | 4 | 2 | $5,437 | 619,205 | 1.0c |
| KXGOVCAPRIMARY | CA primary | one_off | 15 | 4 | $10,513 | 239,858 | 1.7c |
| KXNY12D | ny 12 democratic primary | one_off | 20 | 3 | $183 | 147,316 | 3.3c |
| KXLOSEPRIMARYHOUSER | How many House Republicans will lose the | one_off | 8 | 4 | $2,030 | 128,211 | 3.3c |
| KXTXPRIMARY | Texas Primary Winners | one_off | 89 | 16 | $23,176 | 107,864 | 5.7c |
| KXPRIMARYMOV | Primary margins of victory | one_off | 35 | 14 | $11,281 | 89,791 | 3.0c |
| KXCAGOVPRIMARY1ST | Who will finish first in the California  | one_off | 8 | 3 | $4,147 | 78,768 | 4.0c |
| KXKYPRIMARY | Kentucky Primary Winners | one_off | 34 | 10 | $92 | 75,429 | 3.0c |

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
