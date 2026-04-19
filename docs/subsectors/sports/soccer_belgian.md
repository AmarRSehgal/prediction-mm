# sports_soccer_belgian

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **43** (29 contested)
- Total 24h volume: **$149**
- Total open interest: **2,803**
- Top-OI mean spread (median across series): **48.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **29**
- Median spread: **4.0c**
- Median TOB bid / ask size: **59 / 5** contracts
- Median cumulative depth within 5c of mid — bid: **1500** / ask: **312** contracts
- Median cumulative depth within 10c of mid — bid: **1916** / ask: **792** contracts
- Mean trades per market (last 3000): **1**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 27 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBELGIANPL-26-USG | Union Saint-Gilloise | 50c | 94.0c | 500 | 552 | 0 | 0 | 329 | $0 | 30d+ |
| KXBELGIANPL-26-BRU | Club Brugge | 47c | 92.0c | 200 | 262 | 0 | 0 | 150 | $0 | 30d+ |
| KXBELGIANPLGAME-26APR19KAASTT-TIE | Tie | 28c | 1.0c | 1 | 75 | 2655 | 5718 | 72 | $72 | 7-30d |
| KXBELGIANPLGAME-26APR19KAASTT-KAA | Gent | 36c | 1.0c | 1 | 181 | 2462 | 5810 | 70 | $70 | 7-30d |
| KXBELGIANPLGAME-26APR21GENRCH-RCH | Royal Charleroi | 24c | 8.0c | 1125 | 1 | 1125 | 300 | 17 | $17 | 7-30d |
| KXBELGIANPLGAME-26APR19RAALZUL-ZUL | Zulte Waregem | 36c | 1.0c | 1 | 56 | 2443 | 4798 | 16 | $15 | 7-30d |
| KXBELGIANPLGAME-26APR21OHLWES-WES | Westerlo | 34c | 5.0c | 1000 | 1 | 1500 | 179 | 12 | $12 | 7-30d |
| KXBELGIANPLGAME-26APR19DENCER-CER | Cercle Brugge | 48c | 2.0c | 59 | 1908 | 4711 | 4309 | 12 | $4 | 7-30d |
| KXBELGIANPLGAME-26APR21OHLWES-OHL | Leuven | 35c | 4.0c | 8 | 1 | 508 | 127 | 8 | $8 | 7-30d |
| KXBELGIANPLGAME-26APR21GENRCH-GEN | Genk | 50c | 1.0c | 8 | 2 | 268 | 757 | 8 | $8 | 7-30d |
| KXBELGIANPLGAME-26APR21STARAFC-STA | Standard | 39c | 2.0c | 8 | 1 | 845 | 712 | 8 | $8 | 7-30d |
| KXBELGIANPLGAME-26APR19USGBRU-BRU | Club Brugge | 31c | 1.0c | 1 | 1844 | 1553 | 4425 | 6 | $6 | 7-30d |
| KXBELGIANPLGAME-26APR19KAASTT-STT | St. Truidense | 38c | 1.0c | 1 | 74 | 2447 | 5855 | 1 | $0 | 7-30d |
| KXBELGIANPLGAME-26APR19DENCER-TIE | Tie | 26c | 1.0c | 1 | 182 | 3600 | 4755 | 1 | $0 | 7-30d |
| KXBELGIANPLGAME-26APR19USGBRU-TIE | Tie | 29c | 1.0c | 0 | 1 | 2036 | 2326 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBELGIANPL | Belgian Pro League Champion | annual | 16 | 2 | $0 | 2,651 | 93.0c |
| KXBELGIANPLGAME | Belgian Pro League Game | custom | 27 | 27 | $149 | 152 | 4.3c |

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
