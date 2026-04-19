# sports_soccer_jleague

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **12** (12 contested)
- Total 24h volume: **$38,070**
- Total open interest: **37,794**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **9**
- Median spread: **1.0c**
- Median TOB bid / ask size: **512 / 1500** contracts
- Median depth within 5c of best bid / ask — **6535 / 4842** contracts
- Median depth within 10c of best bid / ask — **6535 / 5896** contracts
- Median depth within 5c of midpoint — bid: **5517** / ask: **4797** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **21**
- Mean informed-signal proxy: **-0.111** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.56c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1776 | 1.67 | -0.319 | 6.00 | 99.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXJLEAGUEGAME-26APR19MITREY-REY | Kashiwa | nanc | nanc | nan | nan | nan | nan | nan | nan | 18360 | $19570 | 7-30d |
| KXJLEAGUEGAME-26APR19MITREY-MIT | Mito H | nanc | nanc | nan | nan | nan | nan | nan | nan | 12486 | $11158 | 7-30d |
| KXJLEAGUEGAME-26APR19MITREY-TIE | Tie | nanc | nanc | nan | nan | nan | nan | nan | nan | 7028 | $7629 | 7-30d |
| KXJLEAGUEGAME-26APR19GAMFAG-GAM | Gamba | 57c | 1.0c | 1501 | 629 | 5648 | 23869 | 6150 | 25493 | 3129 | $3012 | 7-30d |
| KXJLEAGUEGAME-26APR19NGEAVI-NGE | Nagoya | 57c | 1.0c | 10 | 20086 | 4254 | 22890 | 4756 | 22890 | 1020 | $1002 | 7-30d |
| KXJLEAGUEGAME-26APR19GAMFAG-TIE | Tie | 26c | 1.0c | 350 | 3294 | 7017 | 4842 | 7017 | 5896 | 586 | $587 | 7-30d |
| KXJLEAGUEGAME-26APR19GAMFAG-FAG | Fagiano O | 18c | 1.0c | 426 | 1895 | 7901 | 5286 | 8016 | 6476 | 269 | $313 | 7-30d |
| KXJLEAGUEGAME-26APR19NGEAVI-TIE | Tie | 25c | 2.0c | 661 | 1843 | 5726 | 5614 | 5726 | 6114 | 72 | $73 | 7-30d |
| KXJLEAGUEGAME-26APR19NGEAVI-AVI | Avispa | 19c | 1.0c | 337 | 1500 | 8050 | 4642 | 8077 | 5642 | 22 | $38 | 7-30d |
| KXJLEAGUEGAME-26APR22GAMAVI-TIE | Tie | 43c | 77.0c | 512 | 100 | 6535 | 200 | 6535 | 349 | 0 | $0 | 7-30d |
| KXJLEAGUEGAME-26APR22GAMAVI-GAM | Gamba | 43c | 77.0c | 512 | 100 | 6334 | 200 | 6334 | 349 | 0 | $0 | 7-30d |
| KXJLEAGUEGAME-26APR22GAMAVI-AVI | Avispa | 43c | 77.0c | 512 | 100 | 6634 | 200 | 6634 | 349 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXJLEAGUEGAME | Japan J League Game | custom | 12 | 12 | $38,070 | 37,794 | 5.0c |

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
