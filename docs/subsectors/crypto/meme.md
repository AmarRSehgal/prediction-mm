# crypto_meme

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **9** (9 with open markets)
- Open markets: **373** (49 contested)
- Total 24h volume: **$34,866**
- Total open interest: **666,979**
- Top-OI mean spread (median across series): **3.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **15**
- Median spread: **5.0c**
- Median TOB bid / ask size: **74 / 55** contracts
- Median depth within 5c of best bid / ask — **461 / 300** contracts
- Median depth within 10c of best bid / ask — **500 / 300** contracts
- Median depth within 5c of midpoint — bid: **360** / ask: **12** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **289**
- Mean informed-signal proxy: **-0.774** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.58c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 0-15m | 115 | 1.53 | -0.581 | 5.55 | 11.3 |
| 12-24h | 28 | 16.46 | -11.846 | 76.25 | 1.8 |
| 7-30d | 496 | 3.83 | -0.973 | 10.00 | 33.2 |
| 30d+ | 3816 | 0.76 | -0.219 | 3.00 | 54.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCABOUT-26APR-PHEG | Pete Hegseth | 22c | 3.0c | 159 | 14 | 2079 | 2139 | 2724 | 2381 | 79574 | $11817 | 30d+ |
| KXCABOUT-26APR-TGAB | Tulsi Gabbard | 11c | 4.0c | 74 | 1002 | 4306 | 2042 | 62658 | 2077 | 62801 | $4344 | 30d+ |
| KXCABOUT-26APR-LCDR | Lori Chavez-DeRemer | 57c | 1.0c | 23 | 2070 | 149 | 2560 | 1945 | 2624 | 52271 | $4092 | 30d+ |
| KXCABOUT-26APR-HLUT | Howard Lutnick | 5c | 1.9c | 77 | 509 | 3362 | 4041 | 3362 | 4659 | 46923 | $1026 | 30d+ |
| KXDOGEMAXMON-DOGE-26APR30-011 | Above $0.11 | 16c | 1.0c | 61 | 344 | 543 | 424 | 543 | 582 | 4474 | $1080 | 7-30d |
| KXDOGEMAXMON-DOGE-26APR30-012 | Above $0.12 | 8c | 5.0c | 10 | 300 | 25810 | 300 | 25810 | 300 | 2736 | $115 | 7-30d |
| KXDOGEMAXMON-DOGE-26APR30-014 | Above $0.14 | 5c | 5.0c | 300 | 300 | 461 | 300 | 461 | 300 | 1106 | $0 | 7-30d |
| KXDOGEMINMON-DOGE-26APR30-007 | Below $0.07 | 6c | 5.0c | 510 | 12 | 760 | 512 | 760 | 512 | 682 | $31 | 7-30d |
| KXDOGEMINMON-DOGE-26APR30-008 | Below $0.08 | 25c | 4.0c | 500 | 1 | 500 | 501 | 500 | 501 | 679 | $3 | 7-30d |
| KXDOGE-26APR2417-B0.092 | $0.09 to 0.0949999 | 22c | 13.0c | 205 | 6 | 205 | 6 | 205 | 6 | 47 | $0 | 3-7d |
| KXDOGE15M-26APR190100-00 | Target Price: $0.0944302 | nanc | nanc | nan | nan | nan | nan | nan | nan | 26 | $0 | past_expiry |
| KXDOGE-26APR2417-B0.102 | $0.1 to 0.1049999 | nanc | nanc | nan | nan | nan | nan | nan | nan | 26 | $26 | 3-7d |
| KXDOGE-26APR2417-B0.087 | $0.085 to 0.0899999 | nanc | nanc | nan | nan | nan | nan | nan | nan | 25 | $25 | 3-7d |
| KXDOGED-26APR1917-T0.0949999 | $0.095 or above | 60c | 75.0c | 10 | 55 | 11 | 55 | 12 | 55 | 7 | $44 | 12-24h |
| KXDOGE-26APR1917-B0.092 | $0.09 to 0.0949999 | nanc | nanc | nan | nan | nan | nan | nan | nan | 3 | $6 | 12-24h |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCABOUT | Next Cabinet memeber out | custom | 23 | 3 | $22,477 | 478,018 | 3.0c |
| KXDOGEMAX1 | Dogecoin hitting $1 | custom | 3 | 0 | $1,981 | 166,544 | nanc |
| KXDOGEMAXMON | Doge Max Monthly | monthly | 7 | 1 | $1,266 | 10,697 | 1.0c |
| KXSHIBA | Shiba range | daily | 32 | 0 | $7,437 | 7,437 | nanc |
| KXDOGEMINMON | Doge min monthly | monthly | 7 | 1 | $34 | 2,547 | 3.0c |
| KXDOGE | Dogecoin range | hourly | 134 | 8 | $787 | 832 | 16.3c |
| KXDOGED | Dogecoin price Above/below | hourly | 134 | 30 | $867 | 828 | 90.3c |
| KXDOGE15M | Dogecoin 15 Minute | fifteen_min | 1 | 1 | $1 | 60 | 2.9c |
| KXSHIBAD | Shiba price Above/below | daily | 32 | 5 | $16 | 16 | 98.0c |

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
