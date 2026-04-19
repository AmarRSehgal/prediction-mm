# tech_space

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **12** (12 with open markets)
- Open markets: **52** (29 contested)
- Total 24h volume: **$42,991**
- Total open interest: **910,011**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **34**
- Median spread: **5.0c**
- Median TOB bid / ask size: **500 / 369** contracts
- Median depth within 5c of best bid / ask — **556 / 546** contracts
- Median depth within 10c of best bid / ask — **592 / 563** contracts
- Median depth within 5c of midpoint — bid: **516** / ask: **520** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **329**
- Mean informed-signal proxy: **-1.670** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.09c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1009 | 1.63 | -0.373 | 7.00 | 49.6 |
| 30d+ | 10184 | 1.66 | -0.598 | 6.00 | 44.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MOON-27DEC31 | Before 2028 | 7c | 1.0c | 221 | 9 | 6043 | 2049 | 133178 | 2349 | 58345 | $682 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-CITIX | Citigroup | 88c | 3.0c | 515 | 15 | 745 | 402 | 2745 | 3835 | 41881 | $25 | 30d+ |
| KXSPACEXSTARSHIP-12-26MAY31 | By May 31, 2026 | 86c | 3.0c | 52 | 4 | 591 | 8734 | 1208 | 23232 | 34973 | $1975 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-GSX | Goldman Sachs | 93c | 2.0c | 115 | 121 | 1986 | 13570 | 6245 | 13570 | 34200 | $0 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-BOAX | Bank of America | 95c | 2.0c | 635 | 2971 | 1382 | 4358 | 8498 | 4358 | 32646 | $0 | 30d+ |
| KXMOONMAN-31-USA | United States | 58c | 2.9c | 109 | 557 | 768 | 2057 | 768 | 2057 | 30579 | $182 | 30d+ |
| KXSPACEXCOUNT-26APR-10 | above 10 | 80c | 3.0c | 3 | 4 | 430 | 1264 | 505 | 1824 | 28459 | $2735 | 7-30d |
| KXSPACEXCOUNT-26B-160 | Above 160 | 56c | 2.0c | 32 | 1 | 584 | 3608 | 594 | 3820 | 26308 | $370 | 30d+ |
| KXBLUESPACEX-30 | Before 2030 | 70c | 5.0c | 69 | 1989 | 569 | 2489 | 697 | 2490 | 25522 | $91 | 30d+ |
| KXSPACEXBANKPUBLIC-28JAN01-JPMX | JPMorgan Chase | 88c | 5.0c | 2321 | 36 | 2321 | 833 | 2321 | 14875 | 24406 | $61 | 30d+ |
| KXSTARSHIPDOCK-28 | Before 2028 | 46c | 5.0c | 37 | 501 | 954 | 501 | 1084 | 501 | 19764 | $20 | 30d+ |
| KXMOONMAN-31-PRC | China | 29c | 1.5c | 968 | 338 | 1468 | 1231 | 4008 | 1311 | 18765 | $20 | 30d+ |
| KXSPACEXCOUNT-26B-180 | Above 180 | 22c | 5.0c | 27 | 32 | 711 | 532 | 859 | 714 | 12862 | $717 | 30d+ |
| KXSPACEXCOUNT-26B-190 | Above 190 | 10c | 5.0c | 52 | 5 | 565 | 509 | 5153 | 509 | 9929 | $42 | 30d+ |
| KXSPACEXCOUNT-26B-170 | Above 170 | 36c | 5.0c | 52 | 54 | 590 | 554 | 590 | 574 | 9637 | $61 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSPACEXCOUNT | SpaceX launches | custom | 15 | 5 | $30,750 | 252,200 | 5.3c |
| KXSPACEXSTARSHIP | SpaceX Starship launch | custom | 2 | 1 | $10,718 | 196,853 | 3.0c |
| KXSPACEXBANKPUBLIC | SpaceX | one_off | 5 | 2 | $105 | 171,422 | 4.0c |
| KXMOON | NASA lands on the moon | one_off | 4 | 2 | $1,064 | 154,424 | 7.0c |
| KXMOONMAN | Manned mission to the Moon | custom | 5 | 2 | $229 | 61,409 | 2.2c |
| KXBLUESPACEX | Blue Origin SpaceX moon | custom | 1 | 1 | $91 | 25,522 | 5.0c |
| KXSTARSHIPDOCK | Starships dock | custom | 1 | 1 | $20 | 19,764 | 5.0c |
| KXNATIONALIZESPACEX | Nationalize SpaceX | custom | 2 | 0 | $0 | 12,909 | nanc |
| KXTOKENLAUNCH | Who will launch a token this year?  | one_off | 14 | 14 | $13 | 8,639 | 9.0c |
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
