# sports_soccer_dfb

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **4** (4 contested)
- Total 24h volume: **$20**
- Total open interest: **1,986**
- Top-OI mean spread (median across series): **36.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **4**
- Median spread: **9.0c**
- Median TOB bid / ask size: **358 / 553** contracts
- Median depth within 5c of best bid / ask — **1024 / 876** contracts
- Median depth within 10c of best bid / ask — **1024 / 876** contracts
- Median depth within 5c of midpoint — bid: **108** / ask: **492** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **12**
- Mean informed-signal proxy: **-1.370** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.24c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 47 | 2.22 | -1.391 | 9.25 | 41.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXDFBPOKAL-26-BMU | Bayern Munich | 65c | 66.0c | 50 | 913 | 50 | 1113 | 50 | 1113 | 1986 | $20 | 30d+ |
| KXDFBPOKALGAME-26APR22LEVBMU-TIE | Tie | 21c | 10.0c | 500 | 668 | 1392 | 668 | 1392 | 668 | 0 | $0 | 7-30d |
| KXDFBPOKALGAME-26APR22LEVBMU-LEV | Leverkusen | 20c | 8.0c | 500 | 149 | 1333 | 815 | 1333 | 815 | 0 | $0 | 7-30d |
| KXDFBPOKALGAME-26APR22LEVBMU-BMU | Bayern Munich | 60c | 4.0c | 215 | 438 | 715 | 938 | 715 | 938 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXDFBPOKAL | Bayern Munich | nan | 1 | 1 | $20 | 1,986 | 66.0c |
| KXDFBPOKALGAME | Tie | nan | 3 | 3 | $0 | 0 | 7.3c |

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
