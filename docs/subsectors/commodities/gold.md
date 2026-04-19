# comm_gold

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **6** (6 with open markets)
- Open markets: **128** (102 contested)
- Total 24h volume: **$39,131**
- Total open interest: **1,024,328**
- Top-OI mean spread (median across series): **17.5 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **111**
- Median spread: **26.0c**
- Median TOB bid / ask size: **138 / 186** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **49**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 601 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 199 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 2061 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 2633 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBTCVSGOLD-26 | In 2026 | 32c | 2.8c | 500 | 500 | 711 | 708 | 54113 | $44 | 30d+ |
| KXGOLDMON-26APR3017-T5106.99 | above $5106.99 | 15c | 16.0c | 96 | 1 | 0 | 0 | 5032 | $1 | 7-30d |
| KXGOLDMON-26APR3017-T5146.99 | above $5146.99 | 8c | 11.0c | 5514 | 604 | 0 | 0 | 4649 | $16 | 7-30d |
| KXGOLDMON-26APR3017-T4626.99 | above $4626.99 | 70c | 15.0c | 308 | 332 | 0 | 0 | 3898 | $153 | 7-30d |
| KXGOLDMON-26APR3017-T4706.99 | above $4706.99 | 59c | 12.0c | 404 | 20 | 0 | 0 | 3459 | $94 | 7-30d |
| KXGOLDMON-26APR3017-T5066.99 | above $5066.99 | 27c | 36.0c | 260 | 748 | 0 | 0 | 3348 | $15 | 7-30d |
| KXGOLDMON-26APR3017-T5026.99 | above $5026.99 | 29c | 30.0c | 7 | 2 | 0 | 0 | 2941 | $126 | 7-30d |
| KXGOLDMON-26APR3017-T4666.99 | above $4666.99 | 64c | 15.0c | 324 | 196 | 0 | 0 | 2775 | $51 | 7-30d |
| KXGOLDD-26APR2017-T4624 | above $4624 | 95c | 2.0c | 42 | 89 | 42 | 2364 | 1642 | $330 | 1-3d |
| KXGOLDMON-26APR3017-T4826.99 | above $4826.99 | 52c | 14.0c | 5 | 80 | 0 | 0 | 1575 | $308 | 7-30d |
| KXGOLDD-26APR2017-T4614 | above $4614 | 94c | 4.0c | 4 | 223 | 4 | 1531 | 1446 | $171 | 1-3d |
| KXGOLDMON-26APR3017-T4786.99 | above $4786.99 | 54c | 26.0c | 237 | 284 | 0 | 0 | 1413 | $99 | 7-30d |
| KXGOLDMON-26APR3017-T4746.99 | above $4746.99 | 56c | 25.0c | 40 | 40 | 0 | 0 | 1396 | $13 | 7-30d |
| KXGOLDMON-26APR3017-T4586.99 | above $4586.99 | 80c | 1.0c | 5 | 92 | 5 | 122 | 1385 | $243 | 7-30d |
| KXGOLDD-26APR2017-T4914 | above $4914 | 38c | 33.0c | 1 | 417 | 0 | 0 | 1276 | $809 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXGOLDCARDS | Gold cards sold | custom | 6 | 0 | $26,445 | 902,937 | nanc |
| KXBTCVSGOLD | BTC vs Gold | custom | 1 | 1 | $44 | 54,113 | 2.8c |
| KXGOLDMON | Gold Monthly Price | monthly | 40 | 31 | $2,430 | 46,402 | 15.3c |
| KXGOLDD | Gold Daily | daily | 40 | 31 | $9,525 | 15,337 | 19.7c |
| KXRANKLISTSONGGOL | GOLD RANK 1-10 | one_off | 1 | 0 | $0 | 4,857 | nanc |
| KXGOLDW | Gold Weekly price  | weekly | 40 | 39 | $687 | 682 | 28.3c |

## Curated notes

<!-- KEEP-START -->
### Market structure
- Series: KXGOLDD (daily), KXGOLDW (weekly), KXGOLDMON (monthly), KXGOLDPRICE (one-off), GOLD (aggregate).
- Resolution: COMEX GC settlement (or equivalent spot fix for some variants).
- Frequency: daily primary.
- Structure: strike ladder — "Gold above $X" for X in a grid around current spot.
- Close time: 21:00 UTC daily.

### Informed flow profile
- **Mostly retail gold-bugs + some institutional hedgers.**
- **HFT presence: light to moderate.** Observed 20-35c spreads on shoulder strikes
  even at OI 1000+. Nearest-the-money strike can tighten to 2-3c.
- Informed flow sources:
  - Fed-day repositioning (rate decisions move gold hard via USD).
  - Geopolitical spikes (gold is a safe-haven bid on news).
  - Central bank buying rumors.

### Time windows (UTC)
- **SAFE**: 00:00 - 08:00 UTC (Asian gold session quiet; US / London closed).
- **QUIET**: 08:00 - 12:00 UTC (London pre-open and open; moderate flow).
- **QUIET/DANGEROUS**: 12:00 - 14:00 UTC (US pre-open; CPI / PPI / jobs release times).
- **DANGEROUS**: 14:00 - 16:00 UTC (US cash open and volatility window).
- **VERY DANGEROUS**:
  - Scheduled data releases: CPI (monthly, Wed 13:30 UTC), NFP (Fri 13:30 UTC),
    PPI (monthly, 13:30 UTC), FOMC (18:00-19:30 UTC on scheduled Wednesdays).
  - Geopolitical breaking news (Middle East, Russia-Ukraine).
- **DANGEROUS**: 20:00 - 21:00 UTC (close-hour convergence).

### Correlation / basket structure
- Monotone strike ladder — same arb / CDF-fitting opportunity as oil.
- Gold correlates:
  - Negatively with USD (real rates).
  - Positively with silver (~0.80).
  - Positively with safe-haven assets (Swiss franc, JPY).
- Cross-commodity hedge: long Kalshi gold strike can be offset with short silver strike
  on days when the ratio is stable.

### Verdict
- **v0 target: YES — secondary to oil.**
- Why: wide shoulder spreads, clean resolution, predictable dangerous windows.
- Caveats:
  - News-driven jump risk is higher than oil (geopolitics).
  - Correlation with silver makes family-level inventory cap important.
- Path: include in commodity strike-ladder paper trade, but weight smaller than oil
  given jump risk.
<!-- KEEP-END -->
