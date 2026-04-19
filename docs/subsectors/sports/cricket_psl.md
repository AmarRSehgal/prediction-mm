# sports_cricket_psl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **26** (26 contested)
- Total 24h volume: **$17,960**
- Total open interest: **18,787**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **26**
- Median spread: **75.0c**
- Median TOB bid / ask size: **42 / 90** contracts
- Median depth within 5c of best bid / ask — **1335 / 146** contracts
- Median depth within 10c of best bid / ask — **1335 / 183** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **22**
- Mean informed-signal proxy: **-1.623** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **5.86c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 487 | 1.89 | -0.756 | 9.00 | 39.1 |
| 7-30d | 94 | 7.76 | -2.761 | 54.65 | 14.7 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPSLGAME-26APR19MUSKKI-MUS | Multan Sultans | 58c | 3.0c | 34 | 83 | 364 | 346 | 584 | 1072 | 8669 | $8994 | 3-7d |
| KXPSLGAME-26APR19QGLPZA-PZA | Peshawar Zalmi | 57c | 5.0c | 7 | 14 | 148 | 38 | 148 | 223 | 4462 | $4303 | 3-7d |
| KXPSLGAME-26APR19MUSKKI-KKI | Karachi Kings | 40c | 6.0c | 4 | 30 | 157 | 464 | 157 | 1424 | 3889 | $3879 | 3-7d |
| KXPSLGAME-26APR19QGLPZA-QGL | Quetta Gladiators | 36c | 20.0c | 56 | 4 | 750 | 223 | 750 | 920 | 683 | $638 | 3-7d |
| KXPSLGAME-26APR22PZAKKI-KKI | Karachi Kings | 42c | 76.0c | 1050 | 180 | 3191 | 180 | 3191 | 180 | 508 | $1 | 3-7d |
| KXPSLGAME-26APR24ISLHYD-HYD | Hyderabad Kingsmen | 40c | 75.0c | 5 | 6 | 1380 | 186 | 1380 | 186 | 233 | $73 | 7-30d |
| KXPSLGAME-26APR22PZAKKI-PZA | Peshawar Zalmi | 50c | 58.0c | 50 | 60 | 62 | 199 | 62 | 199 | 175 | $50 | 3-7d |
| KXPSLGAME-26APR24ISLHYD-ISL | Islamabad United | 50c | 55.0c | 1 | 60 | 4 | 240 | 4 | 240 | 147 | $1 | 7-30d |
| KXPSLGAME-26APR22MUSHYD-MUS | Multan Sultans | 42c | 75.0c | 50 | 60 | 1535 | 249 | 1535 | 249 | 20 | $20 | 3-7d |
| KXPSLGAME-26APR23KKILQA-LQA | Lahore Qalandars | 42c | 75.0c | 50 | 185 | 1335 | 185 | 1335 | 185 | 1 | $1 | 7-30d |
| KXPSLGAME-26APR21QGLLQA-QGL | Quetta Gladiators | 42c | 76.0c | 50 | 111 | 1335 | 111 | 1335 | 111 | 0 | $0 | 3-7d |
| KXPSLGAME-26APR21MUSRAW-MUS | Multan Sultans | 68c | 25.0c | 1000 | 111 | 1000 | 111 | 1000 | 111 | 0 | $0 | 3-7d |
| KXPSLGAME-26APR21MUSRAW-RAW | Rawalpindi Pindiz | 36c | 63.0c | 50 | 10 | 1560 | 58 | 1560 | 58 | 0 | $0 | 3-7d |
| KXPSLGAME-26APR23KKILQA-KKI | Karachi Kings | 42c | 75.0c | 50 | 186 | 1335 | 186 | 1335 | 186 | 0 | $0 | 7-30d |
| KXPSLGAME-26APR22MUSHYD-HYD | Hyderabad Kingsmen | 42c | 76.0c | 50 | 189 | 1335 | 189 | 1335 | 189 | 0 | $0 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPSLGAME | Multan Sultans | nan | 26 | 26 | $17,960 | 18,787 | 4.7c |

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
