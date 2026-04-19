# tech_space

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **12** (12 with open markets)
- Open markets: **52** (29 contested)
- Total 24h volume: **$44,742**
- Total open interest: **908,774**
- Top-OI mean spread (median across series): **4.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **34**
- Median spread: **6.0c**
- Median TOB bid / ask size: **500 / 369** contracts
- Median cumulative depth within 5c of mid — bid: **516** / ask: **517** contracts
- Median cumulative depth within 10c of mid — bid: **589** / ask: **555** contracts
- Mean trades per market (last 3000): **391**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1538 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 11772 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MOON-27DEC31 | Before 2028 | 7c | 1.0c | 221 | 9 | 6028 | 2049 | 58494 | $533 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-CITIX | Citigroup | 88c | 3.0c | 515 | 15 | 715 | 20 | 41881 | $32 | 30d+ |
| KXSPACEXSTARSHIP-12-26MAY31 | By May 31, 2026 | 88c | 3.0c | 52 | 250 | 504 | 8694 | 34937 | $1895 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-GSX | Goldman Sachs | 93c | 2.0c | 115 | 121 | 1531 | 1267 | 34200 | $0 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-BOAX | Bank of America | 95c | 2.0c | 635 | 2971 | 882 | 4358 | 32646 | $74 | 30d+ |
| KXMOONMAN-31-USA | United States | 58c | 1.0c | 22 | 557 | 768 | 2121 | 30579 | $176 | 30d+ |
| KXSPACEXCOUNT-26APR-10 | above 10 | 78c | 8.0c | 3 | 43 | 364 | 46 | 28136 | $2290 | 7-30d |
| KXSPACEXCOUNT-26B-160 | Above 160 | 56c | 3.0c | 84 | 1 | 584 | 3608 | 26308 | $370 | 30d+ |
| KXBLUESPACEX-30 | Before 2030 | 70c | 5.0c | 64 | 1984 | 564 | 2484 | 25477 | $19 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-JPMX | JPMorgan Chase | 88c | 5.0c | 2321 | 36 | 2321 | 152 | 24406 | $61 | 30d+ |
| KXSTARSHIPDOCK-28 | Before 2028 | 46c | 5.0c | 37 | 501 | 437 | 501 | 19764 | $20 | 30d+ |
| KXMOONMAN-31-PRC | China | 29c | 1.5c | 968 | 338 | 1468 | 731 | 18765 | $36 | 30d+ |
| KXSPACEXCOUNT-26B-180 | Above 180 | 22c | 5.0c | 27 | 32 | 143 | 532 | 12862 | $717 | 30d+ |
| KXSPACEXCOUNT-26B-190 | Above 190 | 10c | 5.0c | 14 | 5 | 538 | 514 | 9929 | $42 | 30d+ |
| KXSPACEXCOUNT-26B-170 | Above 170 | 36c | 6.0c | 5 | 202 | 565 | 711 | 9637 | $61 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSPACEXCOUNT | SpaceX launches | custom | 15 | 5 | $31,055 | 250,382 | 3.7c |
| KXSPACEXSTARSHIP | SpaceX Starship launch | custom | 2 | 1 | $11,977 | 197,332 | 3.0c |
| KXSPACEXBANKPUBLIC | SpaceX | one_off | 5 | 2 | $223 | 171,422 | 4.0c |
| KXMOON | NASA lands on the moon | one_off | 4 | 2 | $1,188 | 154,571 | 7.0c |
| KXMOONMAN | Manned mission to the Moon | custom | 5 | 2 | $248 | 61,409 | 1.2c |
| KXBLUESPACEX | Blue Origin SpaceX moon | custom | 1 | 1 | $19 | 25,477 | 1.0c |
| KXSTARSHIPDOCK | Starships dock | custom | 1 | 1 | $20 | 19,764 | 5.0c |
| KXNATIONALIZESPACEX | Nationalize SpaceX | custom | 2 | 0 | $0 | 12,909 | nanc |
| KXTOKENLAUNCH | Who will launch a token this year?  | one_off | 14 | 14 | $13 | 8,639 | 7.3c |
| KXMUSKNASA | Musk NASA contracts | custom | 1 | 0 | $0 | 6,565 | nanc |

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
