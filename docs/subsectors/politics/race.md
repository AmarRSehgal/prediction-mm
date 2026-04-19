# pol_race

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **189** (189 with open markets)
- Open markets: **870** (322 contested)
- Total 24h volume: **$151,404**
- Total open interest: **13,705,374**
- Top-OI mean spread (median across series): **3.0 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **2.0c**
- Median TOB bid / ask size: **244 / 292** contracts
- Median depth within 5c of best bid / ask — **2490 / 2650** contracts
- Median depth within 10c of best bid / ask — **4019 / 3445** contracts
- Median depth within 5c of midpoint — bid: **1328** / ask: **2379** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **258**
- Mean informed-signal proxy: **-0.395** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.29c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 123 | 1.39 | -0.648 | 6.00 | 22.9 |
| 30d+ | 51491 | 0.98 | -0.343 | 4.00 | 88.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSENATETXR-26-KP | Ken Paxton | 62c | 1.0c | 6923 | 658 | 13269 | 14180 | 17332 | 40778 | 1741710 | $9705 | 30d+ |
| KXSENATETXR-26-JC | :: Current incumbent | 38c | 1.0c | 1885 | 3438 | 20679 | 9547 | 50191 | 16888 | 1118188 | $4735 | 30d+ |
| CONTROLS-2026-R | Republican Party | 48c | 1.0c | 1536 | 2986 | 35025 | 61807 | 35269 | 63850 | 1085864 | $36822 | 30d+ |
| CONTROLS-2026-D | Democratic Party | 52c | 1.0c | 2882 | 15196 | 52449 | 53338 | 57739 | 60950 | 1022286 | $5885 | 30d+ |
| SENATETX-26-D | :: Democratic | 44c | 1.0c | 1691 | 726 | 26958 | 8425 | 66117 | 9954 | 863141 | $4602 | 30d+ |
| SENATETX-26-R | :: Current incumbent: John Cornyn | 55c | 1.0c | 543 | 605 | 4044 | 10443 | 12380 | 18290 | 511094 | $824 | 30d+ |
| KXTXSENCOMBO-26NOV-TALPAX | Talarico vs. Paxton | 58c | 1.0c | 31 | 1255 | 3615 | 7864 | 6106 | 9013 | 380100 | $4448 | 30d+ |
| GOVPARTYCA-26-R | Republican party | 12c | 2.0c | 599 | 2859 | 8646 | 18752 | 21445 | 22723 | 310965 | $1557 | 30d+ |
| KXTXSENCOMBO-26NOV-TALCOR | Talarico vs. Cornyn | 43c | 1.0c | 708 | 3559 | 10891 | 4720 | 16049 | 6199 | 289626 | $4544 | 30d+ |
| KXDSENATESEATS-27-ABOVE52 | Above 52 | 24c | 1.0c | 622 | 653 | 13476 | 14146 | 24305 | 16946 | 138321 | $322 | 30d+ |
| GOVPARTYAZ-26-D | :: Current incumbent: Katie Hobbs | 77c | 4.0c | 518 | 552 | 3360 | 2663 | 3860 | 7296 | 115152 | $89 | 30d+ |
| SENATEME-26-R | :: Current incumbent: Susan Collins | 28c | 2.0c | 3104 | 760 | 16078 | 3568 | 16079 | 7747 | 103776 | $2265 | 30d+ |
| GOVPARTYAZ-26-R | Republican party | 22c | 3.0c | 73 | 1021 | 2705 | 3771 | 8520 | 4021 | 98839 | $0 | 30d+ |
| GOVPARTYCA-26-D | Democratic party | 88c | 1.0c | 75 | 2240 | 86142 | 14237 | 89023 | 60271 | 94100 | $1345 | 30d+ |
| SENATEOHS-26-R | :: Current incumbent: Jon Husted | 38c | 1.0c | 31 | 1461 | 3359 | 6565 | 9109 | 6566 | 81687 | $250 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSENATETXR | Texas Republican Senate nominee | custom | 2 | 2 | $14,145 | 2,859,898 | 1.5c |
| CONTROLS | Senate winner | custom | 2 | 2 | $42,441 | 2,107,818 | 1.0c |
| SENATETX | Texas Senate race | custom | 2 | 2 | $5,426 | 1,374,235 | 1.0c |
| KXSENATEMED | MED | one_off | 7 | 0 | $3,995 | 1,249,417 | nanc |
| KXTXSENCOMBO | Texas Senate matchup | one_off | 2 | 2 | $8,992 | 669,726 | 1.0c |
| KXDSENATESEATS | Democratic Senate seats | one_off | 10 | 5 | $27,129 | 442,205 | 1.0c |
| GOVPARTYCA | California Governor | custom | 2 | 2 | $2,902 | 405,065 | 1.5c |
| GOVPARTYAZ | Arizona Governor | custom | 2 | 2 | $89 | 213,992 | 3.5c |
| KXHOUSERACE | House Race Winner? | one_off | 200 | 56 | $1,138 | 191,232 | 2.3c |
| KXLOSEPRIMARYSENATER | How many Senate Republicans will lose th | one_off | 5 | 2 | $7,846 | 190,304 | 3.0c |

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
