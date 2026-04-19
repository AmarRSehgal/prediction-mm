# sports_soccer_worldcup

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **8** (8 contested)
- Total 24h volume: **$108,673**
- Total open interest: **4,818,110**
- Top-OI mean spread (median across series): **0.6 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **8**
- Median spread: **0.2c**
- Median TOB bid / ask size: **9984 / 12500** contracts
- Median depth within 5c of best bid / ask — **92044 / 289172** contracts
- Median depth within 10c of best bid / ask — **376912 / 298353** contracts
- Median depth within 5c of midpoint — bid: **91544** / ask: **289172** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **966**
- Mean informed-signal proxy: **-0.115** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.16c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 7727 | 0.17 | -0.114 | 1.00 | 350.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMENWORLDCUP-26-FR | France | 17c | 0.5c | 10540 | 111 | 99464 | 99876 | 163844 | 103806 | 1182290 | $46615 | 30d+ |
| KXMENWORLDCUP-26-ES | Spain | 17c | 0.1c | 2817 | 69996 | 107563 | 245883 | 111625 | 249834 | 844818 | $6619 | 30d+ |
| KXMENWORLDCUP-26-PT | Portugal | 8c | 0.1c | 11027 | 90820 | 85081 | 434342 | 591001 | 439235 | 734166 | $15292 | 30d+ |
| KXMENWORLDCUP-26-AR | Argentina | 9c | 0.3c | 9968 | 12500 | 98242 | 226823 | 606377 | 231140 | 579323 | $2771 | 30d+ |
| KXMENWORLDCUP-26-BR | Brazil | 9c | 0.1c | 402 | 12500 | 80222 | 371584 | 595683 | 376184 | 525103 | $2110 | 30d+ |
| KXMENWORLDCUP-26-GB | England | 11c | 0.1c | 10125 | 299 | 95109 | 332462 | 104956 | 346871 | 454125 | $11688 | 30d+ |
| KXMENWORLDCUP-26-DE | Germany | 6c | 0.5c | 10000 | 37490 | 88979 | 418879 | 589979 | 428286 | 417506 | $22291 | 30d+ |
| KXBOYCOTTWC-26 | Before 2026 | 8c | 0.9c | 53 | 15 | 1396 | 125 | 12128 | 441 | 80778 | $1286 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMENWORLDCUP | France | nan | 7 | 7 | $107,387 | 4,737,332 | 0.2c |
| KXBOYCOTTWC | Before 2026 | nan | 1 | 1 | $1,286 | 80,778 | 0.9c |

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
