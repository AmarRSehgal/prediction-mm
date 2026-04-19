# pol_religion

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **20** (8 contested)
- Total 24h volume: **$163**
- Total open interest: **74,134**
- Top-OI mean spread (median across series): **3.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **12**
- Median spread: **4.0c**
- Median TOB bid / ask size: **500 / 500** contracts
- Median depth within 5c of best bid / ask — **2002 / 745** contracts
- Median depth within 10c of best bid / ask — **3360 / 779** contracts
- Median depth within 5c of midpoint — bid: **592** / ask: **500** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **18**
- Mean informed-signal proxy: **-0.962** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.62c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 222 | 1.54 | -0.662 | 6.00 | 51.7 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPOPEVISIT-27JAN01-USA | USA | 7c | 2.0c | 500 | 44 | 32864 | 1110 | 32864 | 1610 | 26530 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-PER | Peru | 74c | 5.0c | 45 | 1000 | 5543 | 1000 | 5543 | 1000 | 4901 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-ARG | Argentina | 52c | 1.0c | 5 | 20 | 15 | 1333 | 815 | 1333 | 4091 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-UKR | Ukraine | 8c | 7.0c | 5500 | 500 | 9358 | 932 | 9358 | 1288 | 3649 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-MEX | Mexico | 24c | 5.0c | 32 | 12 | 685 | 512 | 685 | 512 | 3582 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-URU | Uruguay | 48c | 1.0c | 6867 | 5372 | 7367 | 5872 | 7367 | 5872 | 3188 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-SSUD | South Sudan | 10c | 1.0c | 138 | 500 | 138 | 500 | 3436 | 500 | 2151 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-ISR | Israel | 11c | 7.0c | 500 | 500 | 850 | 558 | 3285 | 558 | 1858 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-POR | Portugal | 30c | 7.0c | 500 | 500 | 500 | 500 | 500 | 500 | 597 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-JOR | Jordan | 10c | 3.0c | 8 | 500 | 508 | 500 | 3015 | 500 | 274 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-BRA | Brazil | 18c | 1.0c | 8306 | 5191 | 8806 | 5691 | 8806 | 5691 | 189 | $0 | 30d+ |
| KXPOPEVISIT-27JAN01-PHI | Philippines | 10c | 7.0c | 500 | 500 | 3153 | 500 | 3153 | 500 | 147 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPOPEVISIT | What countries will Pope Leo visit befor | one_off | 12 | 8 | $0 | 51,158 | 3.7c |
| KXNEWPOPE | New Pope | custom | 7 | 0 | $163 | 20,738 | nanc |
| KXPOPESWIFT | Taylor Swift Pope | custom | 1 | 0 | $0 | 2,238 | nanc |

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
