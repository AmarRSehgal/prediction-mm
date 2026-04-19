# fin_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **2** (2 contested)
- Total 24h volume: **$36**
- Total open interest: **10,186**
- Top-OI mean spread (median across series): **3.5 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **2**
- Median spread: **3.5c**
- Median TOB bid / ask size: **22 / 15** contracts
- Median depth within 5c of best bid / ask — **630 / 318** contracts
- Median depth within 10c of best bid / ask — **631 / 568** contracts
- Median depth within 5c of midpoint — bid: **630** / ask: **65** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **614**
- Mean informed-signal proxy: **-0.947** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.90c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 1227 | 1.89 | -0.956 | 5.00 | 12.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPRICEINCREASEAZICEDTEA-26 | anything greater than 0% | 18c | 3.0c | 43 | 28 | 760 | 618 | 762 | 618 | 5293 | $9 | 30d+ |
| KXPRICEINCREASEAPPLEMUSIC-26 | Before 2027 | 35c | 4.0c | 1 | 1 | 501 | 18 | 501 | 518 | 4893 | $27 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPRICEINCREASEAZICEDTEA | ARIZONA ICED TEA PRICE INCREASE | custom | 1 | 1 | $9 | 5,293 | 3.0c |
| KXPRICEINCREASEAPPLEMUSIC | PRICE INCREASE APPLE MUSIC | one_off | 1 | 1 | $27 | 4,893 | 4.0c |

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
