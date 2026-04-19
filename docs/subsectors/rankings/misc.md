# rankings_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **6** (6 with open markets)
- Open markets: **129** (32 contested)
- Total 24h volume: **$103,572**
- Total open interest: **984,524**
- Top-OI mean spread (median across series): **5.8 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **52**
- Median spread: **7.0c**
- Median TOB bid / ask size: **50 / 100** contracts
- Median depth within 5c of best bid / ask — **294 / 256** contracts
- Median depth within 10c of best bid / ask — **439 / 336** contracts
- Median depth within 5c of midpoint — bid: **74** / ask: **200** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **48**
- Mean informed-signal proxy: **-4.998** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **5.63c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 2481 | 2.04 | -1.087 | 8.00 | 32.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXRANKLISTGOOGLESEARCH-26DEC-DON | Donald Trump | 18c | 2.0c | 28 | 667 | 1290 | 3602 | 1290 | 7787 | 17984 | $4 | 30d+ |
| KXRANKLISTGOOGLESEARCHTOP5-26DEC-DON | Donald Trump | 22c | 4.0c | 101 | 12 | 301 | 1075 | 1790 | 3309 | 7304 | $20 | 30d+ |
| KXRANKLISTGOOGLESEARCHTOP5-26DEC-BAD | Bad Bunny | 76c | 6.0c | 21 | 181 | 321 | 381 | 321 | 381 | 3662 | $0 | 30d+ |
| KXRANKLISTGOOGLESEARCHTOP5-26DEC-SAV | Savannah Guthrie | 57c | 4.0c | 16 | 100 | 4966 | 400 | 4966 | 400 | 2537 | $0 | 30d+ |
| KXRANKLISTGOOGLESEARCH2-26DEC-BAD | Bad Bunny | 20c | 6.0c | 100 | 20 | 1100 | 1021 | 1145 | 1021 | 2104 | $58 | 30d+ |
| KXRANKLISTGOOGLESEARCH-26DEC-BAD | Bad Bunny | 17c | 4.0c | 10 | 50 | 2013 | 800 | 2013 | 800 | 2018 | $0 | 30d+ |
| KXRANKLIST1SONG-26MAY30-DRO | :: Olivia Rodrigo | 74c | 4.0c | 86 | 5 | 336 | 257 | 479 | 314 | 1479 | $385 | 30d+ |
| KXRANKLISTGOOGLESEARCH-26DEC-ELO | Elon Musk | 7c | 4.0c | 129 | 250 | 1721 | 750 | 1721 | 750 | 1169 | $5 | 30d+ |
| KXRANKLISTGOOGLESEARCH2-26DEC-DON | Donald Trump | 8c | 7.0c | 1 | 1000 | 1276 | 1000 | 1276 | 1000 | 1103 | $0 | 30d+ |
| KXRANKLISTGOOGLESEARCH-26DEC-TAY | Taylor Swift | 6c | 1.0c | 16 | 175 | 1489 | 925 | 1489 | 925 | 1005 | $0 | 30d+ |
| KXRANKLISTDJMAGTOP10-26DEC-JOH | John Summit | 15c | 12.0c | 87 | 12 | 287 | 212 | 1486 | 212 | 797 | $0 | 30d+ |
| KXRANKLISTGOOGLESEARCHTOP5-26DEC-ELO | Elon Musk | 15c | 6.0c | 100 | 100 | 350 | 591 | 2250 | 591 | 741 | $0 | 30d+ |
| KXRANKLISTGOOGLESEARCHTOP5-26DEC-TAY | Taylor Swift | 14c | 7.0c | 100 | 100 | 355 | 500 | 7391 | 500 | 739 | $0 | 30d+ |
| KXRANKLIST1SONG-26MAY30-ELI | :: Taylor Swift | 6c | 5.0c | 100 | 97 | 500 | 347 | 500 | 347 | 501 | $0 | 30d+ |
| KXRANKLISTGOOGLESEARCHTOP5-26DEC-NIC | Nick Shirley | 11c | 4.0c | 200 | 28 | 400 | 228 | 4652 | 428 | 444 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXRANKLIST1SONG | WHICH SONG WILL BE NUMBER THIS MONTH | monthly | 21 | 2 | $103,483 | 939,191 | 5.5c |
| KXRANKLISTGOOGLESEARCH | #1 most searched on google | one_off | 11 | 2 | $9 | 22,940 | 3.0c |
| KXRANKLISTGOOGLESEARCHTOP5 | top 5 good search for people | one_off | 15 | 9 | $22 | 15,922 | 4.7c |
| KXRANKLISTGOOGLESEARCH2 | Runner up top Search on google this year | one_off | 11 | 1 | $58 | 4,454 | 6.0c |
| KXRANKLISTDJMAGTOP10 | TOP TEN DJ'S ON DJ MAGS TOP 100 | one_off | 51 | 12 | $0 | 2,006 | 12.0c |
| KXRANKLISTDJMAGCLUBS | DJ MAG TOP 5 CLUBS | one_off | 20 | 6 | $0 | 12 | 12.0c |

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
