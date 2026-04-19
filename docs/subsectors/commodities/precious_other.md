# comm_precious_other

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **120** (109 contested)
- Total 24h volume: **$4,995**
- Total open interest: **27,103**
- Top-OI mean spread (median across series): **20.7 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **116**
- Median spread: **29.0c**
- Median TOB bid / ask size: **141 / 141** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **10**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 208 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 192 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 812 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSILVERMON-26APR3017-T81.99 | above $81.99 | 46c | 4.0c | 5 | 548 | 5 | 548 | 2077 | $77 | 7-30d |
| KXSILVERMON-26APR3017-T73.99 | above $73.99 | 70c | 29.0c | 748 | 108 | 0 | 0 | 1964 | $4 | 7-30d |
| KXSILVERMON-26APR3017-T72.99 | above $72.99 | 82c | 22.0c | 20 | 621 | 0 | 0 | 1660 | $1 | 7-30d |
| KXSILVERMON-26APR3017-T94.99 | above $94.99 | 12c | 18.0c | 64 | 224 | 0 | 0 | 1517 | $888 | 7-30d |
| KXSILVERMON-26APR3017-T93.99 | above $93.99 | 5c | 5.0c | 100 | 126 | 1061 | 226 | 1343 | $0 | 7-30d |
| KXSILVERMON-26APR3017-T79.99 | above $79.99 | 64c | 13.0c | 5 | 384 | 0 | 0 | 1322 | $92 | 7-30d |
| KXSILVERMON-26APR3017-T74.99 | above $74.99 | 68c | 27.0c | 728 | 100 | 0 | 0 | 1206 | $21 | 7-30d |
| KXSILVERMON-26APR3017-T78.99 | above $78.99 | 66c | 22.0c | 40 | 10 | 0 | 0 | 1104 | $2 | 7-30d |
| KXSILVERMON-26APR3017-T88.99 | above $88.99 | 24c | 36.0c | 92 | 284 | 0 | 0 | 1088 | $1 | 7-30d |
| KXSILVERMON-26APR3017-T75.99 | above $75.99 | 68c | 17.0c | 100 | 100 | 0 | 0 | 994 | $251 | 7-30d |
| KXSILVERD-26APR2017-T83.75 | above $83.75 | 20c | 9.0c | 775 | 114 | 775 | 114 | 777 | $681 | 1-3d |
| KXSILVERMON-26APR3017-T76.99 | above $76.99 | 76c | 19.0c | 5 | 108 | 0 | 0 | 756 | $67 | 7-30d |
| KXSILVERMON-26APR3017-T67.99 | above $67.99 | 80c | 33.0c | 728 | 348 | 0 | 0 | 749 | $1 | 7-30d |
| KXSILVERMON-26APR3017-T77.99 | above $77.99 | 64c | 36.0c | 728 | 324 | 0 | 0 | 711 | $96 | 7-30d |
| KXSILVERMON-26APR3017-T82.99 | above $82.99 | 38c | 33.0c | 848 | 324 | 0 | 0 | 666 | $1 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSILVERMON | Silver Monthly Price | monthly | 40 | 37 | $766 | 22,192 | 21.0c |
| KXSILVERD | Silver daily | daily | 40 | 40 | $3,510 | 4,186 | 20.7c |
| KXSILVERW | Silver Weekly Price | weekly | 40 | 32 | $719 | 725 | 12.7c |

## Curated notes

<!-- KEEP-START -->
### Market structure
- Series: KXSILVERD (daily), plus weekly/monthly variants.
- Platinum / palladium likely have some series but limited listings.
- Resolution: COMEX SI settlement for silver.
- Structure: strike ladder.
- Close time: 21:00 UTC daily.

### Informed flow profile
- **Primarily retail silver-bugs.** Smaller following than gold.
- **HFT presence: very light.** Observed 35c median spread; wider than gold.
- Silver is more volatile than gold — spreads widen to compensate.
- Informed flow smaller than gold, but industrial-demand traders exist (silver has
  large industrial use: solar panels, electronics).

### Time windows (UTC)
- Same general pattern as gold but with silver-specific noise:
  - Silver / gold ratio trades (GLD/SLV pairs) can move Kalshi markets.
  - Industrial news (solar panel manufacturing, EV demand) adds extra shocks.
- SAFE / QUIET / DANGEROUS windows: match gold.

### Correlation / basket structure
- Silver ~ 0.80 correlated with gold.
- Silver volatility typically 1.5-2x gold vol.
- Strike ladder gives correlation arb within silver too.

### Verdict
- **v0 target: secondary — add after oil + gold are working.**
- Why: wider spreads than gold (35c vs 20c) but also more vol risk; lower volumes.
- Caveats:
  - Smaller counterparty pool; fill rate may be low.
  - Higher realized vol means bigger adverse moves per fill.
- Path: layer in after primary track is stable.
<!-- KEEP-END -->
