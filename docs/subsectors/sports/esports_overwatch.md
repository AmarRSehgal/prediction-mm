# sports_esports_overwatch

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **6** (6 contested)
- Total 24h volume: **$1,850**
- Total open interest: **1,859**
- Top-OI mean spread (median across series): **14.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **6**
- Median spread: **6.0c**
- Median TOB bid / ask size: **288 / 20** contracts
- Median depth within 5c of best bid / ask — **970 / 775** contracts
- Median depth within 10c of best bid / ask — **1444 / 1763** contracts
- Median depth within 5c of midpoint — bid: **520** / ask: **271** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **10**
- Mean informed-signal proxy: **-0.625** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.84c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 57 | 2.75 | -0.039 | 10.50 | 33.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXOWGAME-26APR190500CHENE-CHE | Cheeseburger | 74c | 4.0c | 500 | 21 | 2108 | 522 | 2108 | 1538 | 1015 | $1015 | 7-30d |
| KXOWGAME-26APR190330FALOSG-FAL | Falcons | 88c | 17.0c | 10 | 5 | 10 | 110 | 340 | 110 | 522 | $522 | 7-30d |
| KXOWGAME-26APR190330FALOSG-OSG | ONSIDE Gaming | 12c | 21.0c | 75 | 10 | 75 | 207 | 75 | 207 | 125 | $125 | 7-30d |
| KXOWGAME-26APR190500CHENE-NE | New Era | 24c | 5.0c | 21 | 519 | 535 | 1155 | 1485 | 2565 | 115 | $115 | 7-30d |
| KXOWGAME-26APR190700JDGWBG-WBG | Weibo Gaming | 87c | 6.0c | 604 | 20 | 1404 | 1027 | 1404 | 4681 | 81 | $72 | 7-30d |
| KXOWGAME-26APR190700JDGWBG-JDG | JD Gaming | 12c | 6.0c | 520 | 488 | 1455 | 1488 | 4858 | 1988 | 1 | $1 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXOWGAME | Cheeseburger | nan | 6 | 6 | $1,850 | 1,859 | 14.0c |

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
