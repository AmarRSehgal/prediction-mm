# pol_exotic

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **11** (11 with open markets)
- Open markets: **21** (17 contested)
- Total 24h volume: **$1,086**
- Total open interest: **253,998**
- Top-OI mean spread (median across series): **3.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **18**
- Median spread: **5.0c**
- Median TOB bid / ask size: **202 / 146** contracts
- Median cumulative depth within 5c of mid — bid: **300** / ask: **446** contracts
- Median cumulative depth within 10c of mid — bid: **403** / ask: **524** contracts
- Mean trades per market (last 3000): **328**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 261 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 5638 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMUSKOAI-26 | Before 2027 | 40c | 3.0c | 23 | 56 | 1180 | 1598 | 130537 | $353 | 30d+ |
| KXSPACEXMARS-30 | Before 2030 | 29c | 2.0c | 104 | 34 | 1193 | 3125 | 21298 | $28 | 30d+ |
| KXROBOTMARS-35 | Before 2035 | 50c | 2.0c | 22 | 19 | 22 | 1269 | 16525 | $2 | 30d+ |
| STARSHIPMARS-29DEC31 | Before 2030 | 15c | 2.0c | 25 | 83 | 7256 | 1653 | 10363 | $267 | 30d+ |
| KXCOLONIZEMARS-50 | Before 2050 | 18c | 1.2c | 45 | 108 | 2490 | 474 | 8956 | $0 | 30d+ |
| KXMARSVRAIL-50 | Before 2050 | 26c | 5.0c | 303 | 131 | 1369 | 262 | 4504 | $34 | 30d+ |
| KXMUSKNW-26APR30-T600 | Above $600 billion | 90c | 7.0c | 13 | 300 | 313 | 300 | 2622 | $0 | 7-30d |
| KXMUSKCHARGE-27JAN01 | Yes | 16c | 5.0c | 6 | 8 | 31 | 582 | 2199 | $0 | 30d+ |
| KXMUSKNW-26APR30-T610 | Above $610 billion | 84c | 9.0c | 301 | 300 | 301 | 300 | 1802 | $0 | 7-30d |
| KXMUSKNW-26APR30-T670 | Above $670 billion | 34c | 4.0c | 5 | 300 | 205 | 300 | 1129 | $16 | 7-30d |
| KXMUSKNW-26APR30-T700 | Above $700 billion | 15c | 5.0c | 30 | 10 | 330 | 310 | 1058 | $53 | 7-30d |
| KXMUSKNW-26APR30-T620 | Above $620 billion | 76c | 9.0c | 301 | 300 | 301 | 300 | 771 | $0 | 7-30d |
| KXMUSKNW-26APR30-T660 | Above $660 billion | 38c | 4.0c | 300 | 133 | 300 | 433 | 514 | $2 | 7-30d |
| KXMUSKNW-26APR30-T630 | Above $630 billion | 68c | 9.0c | 300 | 300 | 300 | 300 | 436 | $0 | 7-30d |
| KXMUSKNW-26APR30-T650 | Above $650 billion | 47c | 4.0c | 300 | 160 | 300 | 460 | 412 | $2 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMUSKOAI | Elon Win vs Open AI | one_off | 1 | 1 | $428 | 130,537 | 3.0c |
| KXELONMARS | Elon Mars | custom | 1 | 0 | $255 | 30,846 | nanc |
| KXSPACEXMARS | SpaceX Mars | custom | 1 | 1 | $28 | 21,298 | 2.0c |
| KXROBOTMARS | Humanoid robot on Mars | custom | 1 | 1 | $2 | 16,525 | 2.0c |
| KXACTORELONMUSK | ELON MUSK IN WHAT MOVIE | one_off | 1 | 0 | $0 | 16,112 | nanc |
| KXSTARSHIPMARS | Starship launch to Mars | one_off | 1 | 1 | $265 | 10,363 | 3.0c |
| KXMUSKNW | Elon Musk net worth on [date] | monthly | 11 | 10 | $74 | 9,001 | 6.3c |
| KXCOLONIZEMARS | Colonize Mars | custom | 1 | 1 | $0 | 8,956 | 2.4c |
| KXMARSVRAIL | Mars CA rail | custom | 1 | 1 | $34 | 4,504 | 5.0c |
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
