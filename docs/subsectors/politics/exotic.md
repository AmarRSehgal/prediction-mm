# pol_exotic

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **11** (11 with open markets)
- Open markets: **21** (17 contested)
- Total 24h volume: **$961**
- Total open interest: **254,006**
- Top-OI mean spread (median across series): **3.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **18**
- Median spread: **5.0c**
- Median TOB bid / ask size: **300 / 120** contracts
- Median depth within 5c of best bid / ask — **358 / 490** contracts
- Median depth within 10c of best bid / ask — **396 / 538** contracts
- Median depth within 5c of midpoint — bid: **301** / ask: **434** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **217**
- Mean informed-signal proxy: **-0.527** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.13c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 261 | 2.33 | -0.504 | 8.00 | 50.3 |
| 30d+ | 3638 | 1.27 | -0.741 | 5.00 | 18.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMUSKOAI-26 | Before 2027 | 39c | 4.0c | 38 | 51 | 1277 | 2114 | 2307 | 2114 | 130562 | $333 | 30d+ |
| KXSPACEXMARS-30 | Before 2030 | 29c | 2.0c | 104 | 34 | 1193 | 3125 | 3205 | 3935 | 21298 | $28 | 30d+ |
| KXROBOTMARS-35 | Before 2035 | 46c | 7.0c | 335 | 10 | 1585 | 1269 | 1601 | 1269 | 16525 | $2 | 30d+ |
| STARSHIPMARS-29DEC31 | Before 2030 | 15c | 2.0c | 25 | 83 | 7282 | 1615 | 8307 | 1887 | 10363 | $267 | 30d+ |
| KXCOLONIZEMARS-50 | Before 2050 | 18c | 1.2c | 45 | 108 | 2792 | 474 | 6092 | 640 | 8956 | $0 | 30d+ |
| KXMARSVRAIL-50 | Before 2050 | 26c | 5.0c | 303 | 131 | 2369 | 1262 | 2396 | 1262 | 4504 | $2 | 30d+ |
| KXMUSKNW-26APR30-T600 | Above $600 billion | 90c | 7.0c | 13 | 300 | 386 | 1827 | 386 | 1827 | 2622 | $0 | 7-30d |
| KXMUSKCHARGE-27JAN01 | Yes | 16c | 5.0c | 6 | 8 | 534 | 582 | 534 | 582 | 2199 | $0 | 30d+ |
| KXMUSKNW-26APR30-T610 | Above $610 billion | 84c | 9.0c | 301 | 300 | 301 | 600 | 301 | 3379 | 1802 | $0 | 7-30d |
| KXMUSKNW-26APR30-T670 | Above $670 billion | 34c | 4.0c | 5 | 300 | 405 | 300 | 405 | 300 | 1129 | $16 | 7-30d |
| KXMUSKNW-26APR30-T700 | Above $700 billion | 15c | 5.0c | 30 | 10 | 330 | 310 | 1722 | 310 | 1058 | $53 | 7-30d |
| KXMUSKNW-26APR30-T620 | Above $620 billion | 76c | 9.0c | 301 | 300 | 301 | 300 | 301 | 309 | 771 | $0 | 7-30d |
| KXMUSKNW-26APR30-T660 | Above $660 billion | 38c | 4.0c | 300 | 109 | 300 | 409 | 300 | 409 | 514 | $2 | 7-30d |
| KXMUSKNW-26APR30-T630 | Above $630 billion | 68c | 9.0c | 300 | 300 | 300 | 300 | 300 | 300 | 436 | $0 | 7-30d |
| KXMUSKNW-26APR30-T650 | Above $650 billion | 47c | 4.0c | 300 | 194 | 300 | 494 | 300 | 494 | 412 | $2 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMUSKOAI | Elon Win vs Open AI | one_off | 1 | 1 | $334 | 130,545 | 4.0c |
| KXELONMARS | Elon Mars | custom | 1 | 0 | $255 | 30,846 | nanc |
| KXSPACEXMARS | SpaceX Mars | custom | 1 | 1 | $28 | 21,298 | 2.0c |
| KXROBOTMARS | Humanoid robot on Mars | custom | 1 | 1 | $2 | 16,525 | 2.0c |
| KXACTORELONMUSK | ELON MUSK IN WHAT MOVIE | one_off | 1 | 0 | $0 | 16,112 | nanc |
| KXSTARSHIPMARS | Starship launch to Mars | one_off | 1 | 1 | $267 | 10,363 | 2.0c |
| KXMUSKNW | Elon Musk net worth on [date] | monthly | 11 | 10 | $73 | 9,001 | 6.0c |
| KXCOLONIZEMARS | Colonize Mars | custom | 1 | 1 | $0 | 8,956 | 1.2c |
| KXMARSVRAIL | Mars CA rail | custom | 1 | 1 | $2 | 4,504 | 5.0c |
| KXMUSKSPORTS | Elon Musk buys major sports team | custom | 1 | 0 | $0 | 3,656 | nanc |

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
