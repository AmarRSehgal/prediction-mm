# eco_gdp

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **21** (21 with open markets)
- Open markets: **387** (157 contested)
- Total 24h volume: **$4,647**
- Total open interest: **583,324**
- Top-OI mean spread (median across series): **9.3 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **10.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median cumulative depth within 5c of mid — bid: **200** / ask: **200** contracts
- Median cumulative depth within 10c of mid — bid: **236** / ask: **400** contracts
- Mean trades per market (last 3000): **92**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 5169 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 13190 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXGDP-26APR30-T1.0 | 1.0% | 85c | 0.4c | 2000 | 63 | 4242 | 7489 | 69083 | $515 | 7-30d |
| KXGDP-26APR30-T2.0 | 2.0% | 53c | 1.7c | 2009 | 9 | 5524 | 2266 | 60504 | $564 | 7-30d |
| KXGDP-26APR30-T2.5 | 2.5% | 31c | 0.9c | 18 | 11 | 4622 | 2111 | 45128 | $485 | 7-30d |
| KXGDP-26APR30-T1.5 | 1.5% | 71c | 2.0c | 46 | 22 | 2199 | 3983 | 44244 | $430 | 7-30d |
| KXGDP-26APR30-T3.0 | 3.0% | 13c | 1.5c | 30 | 12 | 3556 | 2299 | 35412 | $349 | 7-30d |
| KXGDPUSMAX-28-5 | Above 5% | 59c | 6.0c | 505 | 5000 | 5561 | 5098 | 31321 | $0 | 30d+ |
| KXGDP-26APR30-T3.5 | 3.5% | 5c | 1.1c | 2648 | 121 | 5962 | 3354 | 21933 | $392 | 7-30d |
| CHINAUSGDP-30 | By 2030 | 21c | 4.0c | 1518 | 1163 | 17287 | 11204 | 19149 | $1 | 30d+ |
| KXGDPYEAR-26-T0.1 | 0.0 or below | 5c | 0.9c | 21 | 3200 | 3224 | 11129 | 13714 | $0 | 30d+ |
| KXGDPSHAREMANU-29 | Before 2029 | 16c | 8.7c | 1 | 6 | 1 | 2511 | 11087 | $1 | 30d+ |
| KXGDPYEAR-26-B2.3 | 2.1 to 2.5 | 27c | 0.8c | 20 | 996 | 6230 | 2017 | 9320 | $96 | 30d+ |
| KXGDPYEAR-26-B1.8 | 1.6 to 2.0 | 24c | 3.7c | 1000 | 209 | 1165 | 2209 | 8631 | $18 | 30d+ |
| KXGDPYEAR-26-B2.8 | 2.6 to 3.0 | 15c | 1.3c | 250 | 1199 | 8640 | 1952 | 7227 | $0 | 30d+ |
| KXGDPYEAR-26-B1.3 | 1.1 to 1.5 | 13c | 5.3c | 1000 | 1199 | 2159 | 1199 | 5638 | $0 | 30d+ |
| KXGDPNOM-FRA26-3.4 | Above $3.4 trillion | 83c | 10.0c | 27 | 200 | 27 | 200 | 5203 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXGDP | US GDP growth | custom | 12 | 9 | $3,103 | 326,717 | 1.0c |
| KXGDPYEAR | Annual GDP | custom | 14 | 4 | $1,324 | 106,280 | 1.9c |
| KXGDPNOM | Nominal GDP  | one_off | 158 | 59 | $40 | 58,873 | 10.7c |
| KXGDPUSMAX | US GDP peak  | annual | 1 | 1 | $0 | 31,321 | 6.0c |
| KXCHINAUSGDP | China overtakes US GDP | one_off | 1 | 1 | $1 | 19,149 | 4.0c |
| KXDEFGDP | U.S. federal deficit-to-GDP above/below  | one_off | 1 | 0 | $26 | 13,648 | nanc |
| KXGDPSHAREMANU | GDP share manufacturing | custom | 1 | 1 | $16 | 11,087 | 8.7c |
| KXBRAZILGDP | Brazilian GDP Growth | one_off | 14 | 13 | $0 | 5,995 | 7.6c |
| KXNGDPQ | Quarterly NGDP growth | custom | 5 | 3 | $100 | 5,566 | 5.7c |
| KXFRGDPYOYP | France GDP Growth Rate YoY Prel (quarter | custom | 15 | 7 | $7 | 1,029 | 11.0c |

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
