# sports_soccer_belgian

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **43** (29 contested)
- Total 24h volume: **$372**
- Total open interest: **3,305**
- Top-OI mean spread (median across series): **47.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **29**
- Median spread: **2.0c**
- Median TOB bid / ask size: **500 / 89** contracts
- Median depth within 5c of best bid / ask — **2690 / 853** contracts
- Median depth within 10c of best bid / ask — **4434 / 888** contracts
- Median depth within 5c of midpoint — bid: **1122** / ask: **371** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **-1.071** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.94c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 47 | 0.68 | -0.226 | 1.50 | 34.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBELGIANPLGAME-26APR19KAASTT-KAA | Gent | 38c | 2.0c | 629 | 2569 | 3846 | 5069 | 3846 | 5069 | 714 | $689 | 7-30d |
| KXBELGIANPL-26-USG | Union Saint-Gilloise | 50c | 94.0c | 500 | 552 | 500 | 753 | 500 | 753 | 329 | $0 | 30d+ |
| KXBELGIANPL-26-BRU | Club Brugge | 47c | 92.0c | 200 | 262 | 200 | 814 | 200 | 3080 | 150 | $0 | 30d+ |
| KXBELGIANPLGAME-26APR19KAASTT-TIE | Tie | 28c | 1.0c | 1 | 156 | 2690 | 5709 | 5190 | 5709 | 72 | $72 | 7-30d |
| KXBELGIANPLGAME-26APR19DENCER-CER | Cercle Brugge | 52c | 1.0c | 1436 | 1 | 4276 | 3492 | 4276 | 3492 | 32 | $32 | 7-30d |
| KXBELGIANPLGAME-26APR19KAASTT-STT | St. Truidense | 36c | 1.0c | 1 | 2622 | 2502 | 5323 | 5002 | 5323 | 26 | $25 | 7-30d |
| KXBELGIANPLGAME-26APR21GENRCH-RCH | Royal Charleroi | 24c | 5.0c | 595 | 1 | 1095 | 853 | 1095 | 853 | 17 | $17 | 7-30d |
| KXBELGIANPLGAME-26APR19RAALZUL-ZUL | Zulte Waregem | 36c | 1.0c | 1 | 56 | 4943 | 4798 | 4943 | 4798 | 16 | $15 | 7-30d |
| KXBELGIANPLGAME-26APR21OHLWES-WES | Westerlo | 35c | 2.0c | 367 | 1 | 867 | 388 | 867 | 888 | 12 | $12 | 7-30d |
| KXBELGIANPLGAME-26APR21OHLWES-OHL | Leuven | 36c | 1.0c | 357 | 1 | 865 | 319 | 865 | 819 | 8 | $0 | 7-30d |
| KXBELGIANPLGAME-26APR21GENRCH-GEN | Genk | 49c | 2.0c | 260 | 2 | 760 | 757 | 760 | 757 | 8 | $0 | 7-30d |
| KXBELGIANPLGAME-26APR21STARAFC-STA | Standard | 38c | 3.0c | 337 | 1 | 837 | 712 | 837 | 712 | 8 | $0 | 7-30d |
| KXBELGIANPLGAME-26APR19USGBRU-BRU | Club Brugge | 29c | 2.0c | 86 | 143 | 5164 | 2820 | 5164 | 2820 | 6 | $6 | 7-30d |
| KXBELGIANPLGAME-26APR22USGKAA-USG | Union Gilloise | 43c | 77.0c | 512 | 100 | 6736 | 200 | 6736 | 300 | 2 | $2 | 7-30d |
| KXBELGIANPLGAME-26APR22BRUYRM-BRU | Club Brugge | 43c | 77.0c | 512 | 100 | 6735 | 200 | 6735 | 300 | 2 | $2 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBELGIANPL | Belgian Pro League Champion | annual | 16 | 2 | $0 | 2,651 | 93.0c |
| KXBELGIANPLGAME | Belgian Pro League Game | custom | 27 | 27 | $372 | 654 | 1.0c |

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
