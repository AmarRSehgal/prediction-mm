# sports_soccer_mls

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **223** (144 contested)
- Total 24h volume: **$1,247,326**
- Total open interest: **1,038,022**
- Top-OI mean spread (median across series): **15.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **117**
- Median spread: **7.0c**
- Median TOB bid / ask size: **150 / 165** contracts
- Median cumulative depth within 5c of mid — bid: **200** / ask: **250** contracts
- Median cumulative depth within 10c of mid — bid: **386** / ask: **1058** contracts
- Mean trades per market (last 3000): **19**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2920 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 1384 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMLSCUP-26-LAFC | Los Angeles F | 18c | 1.0c | 36 | 4924 | 28020 | 28407 | 27636 | $1551 | 30d+ |
| KXMLSCUP-26-MIA | Miami | 15c | 1.0c | 4841 | 4510 | 27669 | 27772 | 19346 | $765 | 30d+ |
| KXMLSCUP-26-VAN | Vancouver | 9c | 1.0c | 4976 | 6248 | 28524 | 29684 | 11694 | $92 | 30d+ |
| KXMLSSPREAD-26APR18RSLSD-RSL1 | Salt Lake wins by over 1.5 goals | nanc | nanc | nan | nan | nan | nan | 9796 | $11667 | 7-30d |
| KXMLSCUP-26-NSH | Nashville | 6c | 1.0c | 4668 | 4308 | 45054 | 29414 | 9785 | $1656 | 30d+ |
| KXMLSSPREAD-26APR18SEASTL-SEA1 | Seattle wins by over 1.5 goals | nanc | nanc | nan | nan | nan | nan | 8739 | $10513 | 7-30d |
| KXMLSTOTAL-26APR18SEASTL-4 | Over 4.5 goals scored | nanc | nanc | nan | nan | nan | nan | 6706 | $4553 | 7-30d |
| KXMLSGAME-26APR19LAFCSJ-SJ | San Jose | 21c | 2.0c | 682 | 17507 | 35893 | 44397 | 6554 | $3290 | 7-30d |
| KXMLSSPREAD-26APR18RSLSD-RSL2 | Salt Lake wins by over 2.5 goals | nanc | nanc | nan | nan | nan | nan | 5269 | $6831 | 7-30d |
| KXMLSTOTAL-26APR18SEASTL-3 | Over 3.5 goals scored | nanc | nanc | nan | nan | nan | nan | 4622 | $6051 | 7-30d |
| KXMLSWEST-26-LAFC | Los Angeles F | 24c | 45.0c | 5 | 1029 | 0 | 0 | 4212 | $0 | 30d+ |
| KXMLSWEST-26-SEA | Seattle | 14c | 23.0c | 5 | 928 | 0 | 0 | 3250 | $0 | 30d+ |
| KXMLSGAME-26APR19LAFCSJ-LAFC | Los Angeles F | 57c | 1.0c | 803 | 2042 | 30583 | 35251 | 3242 | $2336 | 7-30d |
| KXMLSWEST-26-SJ | San Jose | 11c | 18.0c | 5 | 1000 | 0 | 0 | 2832 | $0 | 30d+ |
| KXMLSSPREAD-26APR18SEASTL-SEA2 | Seattle wins by over 2.5 goals | nanc | nanc | nan | nan | nan | nan | 2689 | $2844 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMLSGAME | Major League Soccer Game | custom | 96 | 92 | $1,126,111 | 681,104 | 1.7c |
| KXMLSCUP | MLS Cup champion | custom | 30 | 2 | $6,519 | 214,798 | 1.0c |
| KXMLSTOTAL | MLS Total | custom | 18 | 14 | $56,877 | 55,638 | 22.7c |
| KXMLSSPREAD | MLS Spread | custom | 28 | 10 | $50,333 | 47,158 | 22.0c |
| KXMLSWEST | MLS Western Conference winner? | annual | 15 | 5 | $0 | 18,718 | 28.7c |
| KXMLSEAST | MLS Western Conference winner? | annual | 15 | 3 | $1,137 | 14,145 | 20.0c |
| KXMLSBTTS | MLS BTTS | custom | 5 | 3 | $6,329 | 6,427 | 7.0c |
| KXMLSJOIN | MLS Transfers | custom | 16 | 15 | $19 | 35 | 10.0c |

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
