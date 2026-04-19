# sports_baseball_npb

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **36** (23 contested)
- Total 24h volume: **$2,464**
- Total open interest: **15,034**
- Top-OI mean spread (median across series): **3.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **24**
- Median spread: **6.5c**
- Median TOB bid / ask size: **110 / 22** contracts
- Median cumulative depth within 5c of mid — bid: **893** / ask: **26** contracts
- Median cumulative depth within 10c of mid — bid: **1705** / ask: **1058** contracts
- Mean trades per market (last 3000): **17**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 405 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNPBGAME-26APR190000ORIFUK-FUK | Fukuoka Hawks | 64c | 4.0c | 64 | 45 | 1188 | 461 | 2432 | $1123 | 3-7d |
| KXNPBGAME-26APR190100CHUHAN-HAN | Hanshin Tigers | 60c | 3.0c | 794 | 97 | 2313 | 2338 | 2251 | $117 | 3-7d |
| KXNPBGAME-26APR190100CHUHAN-CHU | Chunichi Dragons | 40c | 3.0c | 185 | 958 | 1926 | 1978 | 2140 | $19 | 3-7d |
| KXNPBGAME-26APR190000ORIFUK-ORI | Orix Buffaloes | 37c | 2.0c | 33 | 7 | 756 | 66 | 1393 | $122 | 3-7d |
| KXNPBGAME-26APR190000SAIHOK-HOK | Hokkaido Nippon-Ham Fighters | 60c | 3.0c | 72 | 1023 | 1494 | 2241 | 1364 | $106 | 3-7d |
| KXNPBGAME-26APR190030YOKHIR-HIR | Hiroshima Toyo Carp | 52c | 3.0c | 302 | 697 | 2026 | 1914 | 1273 | $48 | 3-7d |
| KXNPBGAME-26APR190030YOKHIR-YOK | Yokohama DeNA BayStars | 50c | 3.0c | 2 | 1038 | 1940 | 2261 | 1189 | $87 | 3-7d |
| KXNPBGAME-26APR190500YOMYAK-YAK | Tokyo Yakult Swallows | 44c | 7.0c | 149 | 52 | 1381 | 52 | 937 | $192 | 3-7d |
| KXNPBGAME-26APR190000SAIHOK-SAI | Saitama Seibu Lions | 40c | 3.0c | 595 | 566 | 2317 | 1594 | 896 | $51 | 3-7d |
| KXNPBGAME-26APR190500YOMYAK-YOM | Yomiuri Giants | 58c | 3.0c | 10 | 1002 | 1030 | 2224 | 791 | $68 | 3-7d |
| KXNPBGAME-26APR190300CHITOH-CHI | Chiba Lotte Marines | 40c | 3.0c | 1 | 1000 | 1984 | 2535 | 299 | $363 | 3-7d |
| KXNPBGAME-26APR190300CHITOH-TOH | Tohoku Rakuten Golden Eagles | 60c | 2.0c | 900 | 761 | 2618 | 2205 | 243 | $266 | 3-7d |
| KXNPBGAME-26APR210445HANYOK-HAN | Hanshin Tigers | 48c | 89.0c | 1112 | 22 | 0 | 0 | 1 | $1 | 3-7d |
| KXNPBGAME-26APR210445HANYOK-YOK | Yokohama DeNA BayStars | 48c | 89.0c | 1112 | 21 | 0 | 0 | 1 | $1 | 3-7d |
| KXNPBGAME-26APR210500FUKSAI-SAI | Saitama Seibu Lions | 50c | 87.0c | 1 | 22 | 0 | 0 | 0 | $0 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNPBGAME | Japan NPB Game | custom | 24 | 23 | $2,464 | 15,034 | 3.0c |
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
