# pol_race

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **189** (189 with open markets)
- Open markets: **870** (323 contested)
- Total 24h volume: **$154,400**
- Total open interest: **13,697,642**
- Top-OI mean spread (median across series): **3.1 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **2.0c**
- Median TOB bid / ask size: **250 / 300** contracts
- Median cumulative depth within 5c of mid — bid: **1310** / ask: **2284** contracts
- Median cumulative depth within 10c of mid — bid: **3653** / ask: **2925** contracts
- Mean trades per market (last 3000): **376**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 123 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 75020 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSENATETXR-26-KP | Ken Paxton | 62c | 1.0c | 7694 | 585 | 13818 | 13250 | 1740811 | $8695 | 30d+ |
| KXSENATETXR-26-JC | :: Current incumbent | 38c | 1.0c | 1688 | 3411 | 15648 | 9654 | 1118188 | $4882 | 30d+ |
| CONTROLS-2026-R | Republican Party | 48c | 1.0c | 1538 | 3103 | 35027 | 60884 | 1085649 | $36505 | 30d+ |
| CONTROLS-2026-D | Democratic Party | 52c | 1.0c | 2882 | 15297 | 52348 | 53028 | 1022277 | $5858 | 30d+ |
| SENATETX-26-D | :: Democratic | 44c | 1.0c | 1691 | 727 | 23895 | 8426 | 863129 | $4333 | 30d+ |
| SENATETX-26-R | :: Current incumbent: John Cornyn | 55c | 1.0c | 543 | 605 | 4044 | 9098 | 511094 | $952 | 30d+ |
| KXTXSENCOMBO-26NOV-TALPAX | Talarico vs. Paxton | 57c | 1.0c | 2107 | 1 | 3658 | 4883 | 379983 | $3929 | 30d+ |
| GOVPARTYCA-26-R | Republican party | 12c | 2.0c | 599 | 2921 | 7256 | 16674 | 310903 | $1524 | 30d+ |
| KXTXSENCOMBO-26NOV-TALCOR | Talarico vs. Cornyn | 43c | 1.0c | 860 | 3559 | 5191 | 4720 | 289584 | $4350 | 30d+ |
| KXDSENATESEATS-27-ABOVE52 | Above 52 | 24c | 1.0c | 622 | 689 | 10126 | 14182 | 138286 | $288 | 30d+ |
| GOVPARTYAZ-26-D | :: Current incumbent: Katie Hobbs | 77c | 4.0c | 518 | 552 | 3054 | 2663 | 115152 | $89 | 30d+ |
| SENATEME-26-R | :: Current incumbent: Susan Collins | 28c | 2.0c | 3104 | 760 | 13140 | 3556 | 103776 | $2265 | 30d+ |
| GOVPARTYAZ-26-R | Republican party | 22c | 3.0c | 73 | 1021 | 714 | 3771 | 98839 | $0 | 30d+ |
| GOVPARTYCA-26-D | Democratic party | 88c | 1.0c | 46 | 2242 | 85612 | 8877 | 94097 | $1343 | 30d+ |
| SENATEOHS-26-R | :: Current incumbent: Jon Husted | 38c | 1.0c | 31 | 1461 | 2609 | 6299 | 81687 | $250 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSENATETXR | Texas Republican Senate nominee | custom | 2 | 2 | $13,115 | 2,858,995 | 1.5c |
| CONTROLS | Senate winner | custom | 2 | 2 | $42,188 | 2,107,491 | 1.0c |
| SENATETX | Texas Senate race | custom | 2 | 2 | $5,185 | 1,374,188 | 1.0c |
| KXSENATEMED | MED | one_off | 7 | 0 | $3,993 | 1,249,417 | nanc |
| KXTXSENCOMBO | Texas Senate matchup | one_off | 2 | 2 | $8,214 | 669,566 | 1.0c |
| KXDSENATESEATS | Democratic Senate seats | one_off | 10 | 5 | $27,070 | 442,194 | 1.0c |
| GOVPARTYCA | California Governor | custom | 2 | 2 | $2,721 | 404,855 | 1.5c |
| GOVPARTYAZ | Arizona Governor | custom | 2 | 2 | $620 | 213,992 | 3.5c |
| KXHOUSERACE | House Race Winner? | one_off | 200 | 56 | $1,137 | 191,147 | 2.3c |
| KXLOSEPRIMARYSENATER | How many Senate Republicans will lose th | one_off | 5 | 3 | $9,703 | 190,338 | 2.3c |

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
