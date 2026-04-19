# eco_gdp

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **21** (21 with open markets)
- Open markets: **387** (157 contested)
- Total 24h volume: **$4,973**
- Total open interest: **582,903**
- Top-OI mean spread (median across series): **9.2 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **10.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median depth within 5c of best bid / ask — **230 / 400** contracts
- Median depth within 10c of best bid / ask — **252 / 452** contracts
- Median depth within 5c of midpoint — bid: **200** / ask: **200** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **65**
- Mean informed-signal proxy: **-1.202** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.72c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 4886 | 0.59 | -0.273 | 2.10 | 41.7 |
| 30d+ | 8204 | 1.10 | -0.345 | 5.00 | 29.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXGDP-26APR30-T1.0 | 1.0% | 86c | 1.8c | 519 | 4770 | 4679 | 10489 | 4839 | 12476 | 69146 | $465 | 7-30d |
| KXGDP-26APR30-T2.0 | 2.0% | 53c | 1.5c | 2000 | 9 | 5523 | 2275 | 8463 | 2307 | 60505 | $571 | 7-30d |
| KXGDP-26APR30-T2.5 | 2.5% | 31c | 0.9c | 22 | 26 | 4637 | 2147 | 6641 | 2150 | 44611 | $1019 | 7-30d |
| KXGDP-26APR30-T1.5 | 1.5% | 71c | 2.1c | 37 | 2000 | 2199 | 3961 | 4854 | 3966 | 44244 | $420 | 7-30d |
| KXGDP-26APR30-T3.0 | 3.0% | 13c | 1.6c | 31 | 12 | 3572 | 2298 | 11548 | 2298 | 35412 | $349 | 7-30d |
| KXGDPUSMAX-28-5 | Above 5% | 59c | 6.0c | 499 | 20 | 9197 | 7358 | 11033 | 7548 | 31327 | $7 | 30d+ |
| KXGDP-26APR30-T3.5 | 3.5% | 5c | 1.1c | 2648 | 118 | 26366 | 3451 | 26366 | 3862 | 21936 | $395 | 7-30d |
| CHINAUSGDP-30 | By 2030 | 21c | 4.0c | 1518 | 1163 | 17593 | 11163 | 17647 | 11291 | 19149 | $1 | 30d+ |
| KXGDPYEAR-26-T0.1 | 0.0 or below | 5c | 0.9c | 21 | 3200 | 9653 | 11129 | 9653 | 13229 | 13714 | $0 | 30d+ |
| KXGDPSHAREMANU-29 | Before 2029 | 16c | 8.6c | 1 | 2500 | 2502 | 2510 | 3853 | 2609 | 11087 | $2 | 30d+ |
| KXGDPYEAR-26-B2.3 | 2.1 to 2.5 | 27c | 0.8c | 20 | 996 | 6230 | 2017 | 11214 | 2017 | 9320 | $0 | 30d+ |
| KXGDPYEAR-26-B1.8 | 1.6 to 2.0 | 24c | 3.7c | 1000 | 209 | 1197 | 2209 | 8978 | 7209 | 8631 | $0 | 30d+ |
| KXGDPYEAR-26-B2.8 | 2.6 to 3.0 | 15c | 1.3c | 250 | 1199 | 8640 | 2502 | 8640 | 5002 | 7227 | $0 | 30d+ |
| KXGDPYEAR-26-B1.3 | 1.1 to 1.5 | 13c | 5.3c | 1000 | 1199 | 2159 | 3199 | 19211 | 3209 | 5638 | $0 | 30d+ |
| KXGDPNOM-FRA26-3.4 | Above $3.4 trillion | 83c | 10.0c | 27 | 200 | 227 | 200 | 227 | 1073 | 5203 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXGDP | US GDP growth | custom | 12 | 9 | $3,548 | 326,288 | 1.4c |
| KXGDPYEAR | Annual GDP | custom | 14 | 4 | $1,210 | 106,280 | 1.9c |
| KXGDPNOM | Nominal GDP  | one_off | 158 | 59 | $40 | 58,873 | 10.7c |
| KXGDPUSMAX | US GDP peak  | annual | 1 | 1 | $7 | 31,327 | 6.0c |
| KXCHINAUSGDP | China overtakes US GDP | one_off | 1 | 1 | $1 | 19,149 | 4.0c |
| KXDEFGDP | U.S. federal deficit-to-GDP above/below  | one_off | 1 | 0 | $26 | 13,648 | nanc |
| KXGDPSHAREMANU | GDP share manufacturing | custom | 1 | 1 | $2 | 11,087 | 8.6c |
| KXBRAZILGDP | Brazilian GDP Growth | one_off | 14 | 13 | $0 | 5,995 | 7.6c |
| KXNGDPQ | Quarterly NGDP growth | custom | 5 | 3 | $100 | 5,566 | 6.0c |
| KXFRGDPYOYP | France GDP Growth Rate YoY Prel (quarter | custom | 15 | 7 | $7 | 1,029 | 11.3c |

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
