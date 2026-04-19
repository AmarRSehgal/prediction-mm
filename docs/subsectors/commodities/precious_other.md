# comm_precious_other

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **120** (109 contested)
- Total 24h volume: **$4,932**
- Total open interest: **28,067**
- Top-OI mean spread (median across series): **16.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **112**
- Median spread: **28.0c**
- Median TOB bid / ask size: **60 / 60** contracts
- Median depth within 5c of best bid / ask — **368 / 314** contracts
- Median depth within 10c of best bid / ask — **378 / 368** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **11**
- Mean informed-signal proxy: **-1.461** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.49c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 237 | 3.38 | -1.874 | 10.00 | 18.4 |
| 3-7d | 171 | 4.91 | -3.290 | 17.30 | 9.3 |
| 7-30d | 813 | 3.52 | -0.615 | 12.00 | 43.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSILVERMON-26APR3017-T81.99 | above $81.99 | 45c | 2.0c | 5 | 493 | 5 | 576 | 5 | 576 | 2077 | $75 | 7-30d |
| KXSILVERMON-26APR3017-T73.99 | above $73.99 | 73c | 24.0c | 284 | 92 | 385 | 224 | 385 | 297 | 1964 | $4 | 7-30d |
| KXSILVERMON-26APR3017-T72.99 | above $72.99 | 78c | 29.0c | 20 | 621 | 20 | 1475 | 116 | 1733 | 1660 | $1 | 7-30d |
| KXSILVERMON-26APR3017-T94.99 | above $94.99 | 11c | 15.0c | 12 | 208 | 1232 | 208 | 1232 | 208 | 1537 | $908 | 7-30d |
| KXSILVERMON-26APR3017-T93.99 | above $93.99 | 5c | 5.0c | 92 | 126 | 1053 | 226 | 1053 | 226 | 1383 | $40 | 7-30d |
| KXSILVERMON-26APR3017-T79.99 | above $79.99 | 64c | 13.0c | 5 | 384 | 10 | 662 | 10 | 662 | 1322 | $92 | 7-30d |
| KXSILVERMON-26APR3017-T74.99 | above $74.99 | 69c | 28.0c | 364 | 672 | 465 | 697 | 465 | 784 | 1206 | $21 | 7-30d |
| KXSILVERMON-26APR3017-T78.99 | above $78.99 | 63c | 18.0c | 40 | 40 | 160 | 130 | 160 | 271 | 1104 | $1 | 7-30d |
| KXSILVERMON-26APR3017-T88.99 | above $88.99 | 24c | 36.0c | 124 | 284 | 1107 | 580 | 1107 | 580 | 1088 | $1 | 7-30d |
| KXSILVERMON-26APR3017-T75.99 | above $75.99 | 68c | 17.0c | 124 | 92 | 124 | 248 | 225 | 248 | 994 | $260 | 7-30d |
| KXSILVERD-26APR2017-T83.75 | above $83.75 | 19c | 8.0c | 592 | 162 | 592 | 360 | 692 | 360 | 777 | $645 | 1-3d |
| KXSILVERMON-26APR3017-T76.99 | above $76.99 | 74c | 19.0c | 5 | 30 | 35 | 464 | 35 | 464 | 756 | $67 | 7-30d |
| KXSILVERMON-26APR3017-T67.99 | above $67.99 | 80c | 33.0c | 728 | 348 | 728 | 684 | 728 | 684 | 749 | $1 | 7-30d |
| KXSILVERMON-26APR3017-T77.99 | above $77.99 | 63c | 26.0c | 10 | 10 | 212 | 126 | 212 | 327 | 711 | $96 | 7-30d |
| KXSILVERMON-26APR3017-T82.99 | above $82.99 | 38c | 26.0c | 10 | 40 | 262 | 136 | 262 | 418 | 666 | $11 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSILVERMON | Silver Monthly Price | monthly | 40 | 38 | $1,644 | 23,040 | 21.7c |
| KXSILVERD | Silver daily | daily | 40 | 39 | $3,034 | 4,298 | 10.7c |
| KXSILVERW | Silver Weekly Price | weekly | 40 | 32 | $254 | 728 | 16.7c |

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
