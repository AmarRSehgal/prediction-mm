# sports_ncaabball

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **5** (5 with open markets)
- Open markets: **215** (63 contested)
- Total 24h volume: **$116,707**
- Total open interest: **2,378,282**
- Top-OI mean spread (median across series): **33.0 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **61**
- Median spread: **86.0c**
- Median TOB bid / ask size: **300 / 5** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **175**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 209 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 54 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 10610 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMARMAD-27-MICH | Michigan | 15c | 2.0c | 5009 | 14090 | 36483 | 48112 | 116023 | $7510 | 30d+ |
| KXNCAABASEBALL-26-TEX | Texas | 10c | 2.0c | 883 | 4807 | 11604 | 12164 | 110700 | $1192 | 30d+ |
| KXNCAABASEBALL-26-UCLA | UCLA | 16c | 1.0c | 27 | 1194 | 1953 | 8607 | 107985 | $1746 | 30d+ |
| KXNCAABASEBALL-26-GT | Georgia Tech | 10c | 1.0c | 1827 | 458 | 4431 | 9549 | 77882 | $3569 | 30d+ |
| KXMARMAD-27-DUKE | Duke | 12c | 2.0c | 99 | 82 | 13484 | 26143 | 58186 | $4370 | 30d+ |
| KXNCAABASEBALL-26-TXAM | Texas A&M | 5c | 2.0c | 1439 | 797 | 6612 | 7421 | 56852 | $1953 | 30d+ |
| KXNCAABASEBALL-26-UGA | Georgia | 6c | 2.0c | 1472 | 1953 | 4347 | 5983 | 52752 | $327 | 30d+ |
| KXNCAABASEBALL-26-UNC | North Carolina | 6c | 1.0c | 16126 | 3282 | 20194 | 3336 | 47419 | $2157 | 30d+ |
| KXMARMAD-27-ILL | Illinois | 8c | 2.7c | 268 | 300 | 18764 | 15621 | 40657 | $4524 | 30d+ |
| KXMARMAD-27-FLA | Florida | 8c | 3.4c | 500 | 149 | 12102 | 5648 | 30575 | $1342 | 30d+ |
| KXMARMAD-27-CONN | UConn | 8c | 0.9c | 98 | 102 | 9704 | 7528 | 29455 | $8703 | 30d+ |
| KXMARMAD-27-ARIZ | Arizona | 5c | 0.1c | 400 | 1202 | 22759 | 8798 | 11234 | $844 | 30d+ |
| KXNCAABBGS-26-RCHO | :: UCLA | 72c | 47.0c | 500 | 80 | 0 | 0 | 2130 | $52 | 30d+ |
| KXNCAABBGAME-26APR182105WASUNL-WAS | Washington State | nanc | nanc | nan | nan | nan | nan | 986 | $986 | 1-3d |
| KXNCAABBGS-26-AREE | :: Mississippi State | 8c | 8.0c | 500 | 500 | 500 | 500 | 552 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNCAABASEBALL | College Baseball Champion | custom | 42 | 3 | $65,176 | 1,801,425 | 1.3c |
| KXMARMAD | College Basketball Champion | custom | 71 | 2 | $40,511 | 561,777 | 2.0c |
| KXNCAABBGAME | College Baseball Game | custom | 28 | 22 | $10,969 | 9,552 | 59.3c |
| KXNCAABBGS | College Baseball Golden Spikes Award | custom | 32 | 2 | $52 | 5,528 | 33.0c |
| KXNCAABBPLAYOFFS | College Baseball Playoff Qualifiers | custom | 42 | 34 | $0 | 0 | 93.0c |

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
