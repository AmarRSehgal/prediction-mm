# sports_baseball_npb

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **48** (35 contested)
- Total 24h volume: **$9,798**
- Total open interest: **22,940**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **36**
- Median spread: **86.0c**
- Median TOB bid / ask size: **10 / 10** contracts
- Median depth within 5c of best bid / ask — **968 / 923** contracts
- Median depth within 10c of best bid / ask — **968 / 1304** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **43**
- Mean informed-signal proxy: **-0.130** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **5.19c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 1040 | 1.99 | -0.508 | 8.00 | 41.6 |
| 3-7d | 506 | 11.36 | 0.181 | 78.45 | 55.1 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNPBGAME-26APR190000ORIFUK-ORI | Orix Buffaloes | 26c | 7.0c | 6 | 5 | 41 | 47 | 80 | 811 | 5412 | $1986 | 1-3d |
| KXNPBGAME-26APR190000SAIHOK-HOK | Hokkaido Nippon-Ham Fighters | 11c | 8.0c | 45 | 9 | 383 | 81 | 709 | 816 | 4298 | $2311 | 1-3d |
| KXNPBGAME-26APR190030YOKHIR-YOK | Yokohama DeNA BayStars | 70c | 9.0c | 18 | 1 | 78 | 737 | 276 | 1337 | 3510 | $2221 | 1-3d |
| KXNPBGAME-26APR190000SAIHOK-SAI | Saitama Seibu Lions | 85c | 10.0c | 70 | 44 | 256 | 966 | 356 | 3542 | 3467 | $2181 | 1-3d |
| KXNPBGAME-26APR190100CHUHAN-HAN | Hanshin Tigers | 66c | 4.0c | 302 | 18 | 452 | 22 | 456 | 1270 | 3449 | $1346 | 1-3d |
| KXNPBGAME-26APR190000ORIFUK-FUK | Fukuoka Hawks | 77c | 6.0c | 25 | 5 | 111 | 1129 | 117 | 1131 | 3435 | $2131 | 1-3d |
| KXNPBGAME-26APR190100CHUHAN-CHU | Chunichi Dragons | 31c | 4.0c | 1 | 9 | 345 | 776 | 496 | 1522 | 2989 | $876 | 1-3d |
| KXNPBGAME-26APR190030YOKHIR-HIR | Hiroshima Toyo Carp | 32c | 11.0c | 40 | 69 | 75 | 146 | 230 | 1025 | 2720 | $996 | 1-3d |
| KXNPBGAME-26APR190500YOMYAK-YAK | Tokyo Yakult Swallows | 43c | 2.0c | 48 | 526 | 2472 | 1774 | 2618 | 1920 | 1359 | $705 | 3-7d |
| KXNPBGAME-26APR190300CHITOH-TOH | Tohoku Rakuten Golden Eagles | 60c | 3.0c | 726 | 19 | 2553 | 2206 | 2693 | 2206 | 1347 | $1370 | 3-7d |
| KXNPBGAME-26APR190500YOMYAK-YOM | Yomiuri Giants | 58c | 3.0c | 1 | 13 | 2410 | 2348 | 2556 | 2445 | 820 | $97 | 3-7d |
| KXNPBGAME-26APR190300CHITOH-CHI | Chiba Lotte Marines | 38c | 3.0c | 48 | 64 | 2688 | 2254 | 2688 | 2395 | 322 | $418 | 3-7d |
| KXNPBGAME-26APR210445HANYOK-HAN | Hanshin Tigers | 50c | 87.0c | 10 | 22 | 3737 | 1536 | 3737 | 4533 | 1 | $1 | 3-7d |
| KXNPBGAME-26APR210445HANYOK-YOK | Yokohama DeNA BayStars | 50c | 87.0c | 10 | 20 | 3733 | 1529 | 3733 | 4512 | 1 | $1 | 3-7d |
| KXNPBGAME-26APR210500YAKHIR-YAK | Tokyo Yakult Swallows | 50c | 87.0c | 10 | 22 | 3746 | 1529 | 3746 | 4515 | 0 | $0 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNPBGAME | Japan NPB Game | custom | 36 | 35 | $9,798 | 22,940 | 5.0c |
| KXNPB | NPB Champion | custom | 12 | 0 | $0 | 0 | nanc |

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
