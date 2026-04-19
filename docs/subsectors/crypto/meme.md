# crypto_meme

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **9** (9 with open markets)
- Open markets: **373** (19 contested)
- Total 24h volume: **$34,598**
- Total open interest: **662,720**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **42**
- Median spread: **98.0c**
- Median TOB bid / ask size: **10 / 1** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **168**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 12-24h | 28 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 543 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 6496 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCABOUT-26APR-PHEG | Pete Hegseth | 16c | 1.0c | 25 | 6 | 1453 | 1584 | 77503 | $9652 | 30d+ |
| KXCABOUT-26APR-TGAB | Tulsi Gabbard | 11c | 4.0c | 74 | 500 | 4077 | 1502 | 62801 | $4404 | 30d+ |
| KXCABOUT-26APR-LCDR | Lori Chavez-DeRemer | 57c | 1.0c | 55 | 13 | 1889 | 931 | 52271 | $4306 | 30d+ |
| KXDOGEMAXMON-DOGE-26APR30-011 | Above $0.11 | 18c | 1.0c | 66 | 344 | 458 | 565 | 4474 | $1089 | 7-30d |
| KXDOGEMAXMON-DOGE-26APR30-012 | Above $0.12 | 8c | 5.0c | 10 | 300 | 360 | 300 | 2736 | $131 | 7-30d |
| KXDOGEMAXMON-DOGE-26APR30-013 | Above $0.13 | 6c | 6.0c | 336 | 300 | 491 | 300 | 1224 | $18 | 7-30d |
| KXDOGEMAXMON-DOGE-26APR30-014 | Above $0.14 | 6c | 6.0c | 300 | 300 | 461 | 300 | 1106 | $0 | 7-30d |
| KXDOGEMINMON-DOGE-26APR30-007 | Below $0.07 | 7c | 4.0c | 510 | 12 | 760 | 12 | 682 | $43 | 7-30d |
| KXDOGEMINMON-DOGE-26APR30-008 | Below $0.08 | 24c | 5.0c | 500 | 1 | 500 | 1 | 679 | $3 | 7-30d |
| KXDOGE-26APR2417-B0.092 | $0.09 to 0.0949999 | 22c | 13.0c | 191 | 6 | 0 | 0 | 47 | $0 | 3-7d |
| KXDOGE-26APR2417-B0.102 | $0.1 to 0.1049999 | 16c | 19.0c | 250 | 26 | 0 | 0 | 26 | $26 | 3-7d |
| KXDOGE-26APR2417-B0.087 | $0.085 to 0.0899999 | 16c | 17.0c | 250 | 25 | 0 | 0 | 25 | $25 | 3-7d |
| KXDOGED-26APR1917-T0.0949999 | $0.095 or above | 60c | 72.0c | 4 | 300 | 0 | 0 | 7 | $43 | 12-24h |
| KXDOGE-26APR1917-B0.092 | $0.09 to 0.0949999 | 38c | 34.0c | 219 | 1 | 0 | 0 | 3 | $5 | 12-24h |
| KXDOGED-26APR1823-T0.0949999 | $0.095 or above | nanc | nanc | nan | nan | nan | nan | 3 | $3 | past_expiry |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCABOUT | Next Cabinet memeber out | custom | 23 | 3 | $21,564 | 473,362 | 3.7c |
| KXDOGEMAX1 | Dogecoin hitting $1 | custom | 3 | 0 | $2,363 | 166,498 | nanc |
| KXDOGEMAXMON | Doge Max Monthly | monthly | 7 | 1 | $1,309 | 10,697 | 1.0c |
| KXSHIBA | Shiba range | daily | 32 | 0 | $6,782 | 6,782 | nanc |
| KXDOGEMINMON | Doge min monthly | monthly | 7 | 1 | $46 | 2,547 | 5.0c |
| KXDOGE | Dogecoin range | hourly | 134 | 6 | $1,018 | 1,056 | 16.3c |
| KXDOGE15M | Dogecoin 15 Minute | fifteen_min | 1 | 0 | $667 | 935 | nanc |
| KXDOGED | Dogecoin price Above/below | hourly | 134 | 8 | $840 | 835 | 49.3c |
| KXSHIBAD | Shiba price Above/below | daily | 32 | 0 | $8 | 8 | nanc |

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
