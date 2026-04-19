# sports_soccer_mls

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **166** (113 contested)
- Total 24h volume: **$33,435**
- Total open interest: **275,967**
- Top-OI mean spread (median across series): **1.8 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **118**
- Median spread: **7.0c**
- Median TOB bid / ask size: **154 / 164** contracts
- Median depth within 5c of best bid / ask — **692 / 941** contracts
- Median depth within 10c of best bid / ask — **962 / 1089** contracts
- Median depth within 5c of midpoint — bid: **200** / ask: **271** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **19**
- Mean informed-signal proxy: **-0.336** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.38c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 879 | 1.24 | -0.244 | 5.00 | 37.6 |
| 30d+ | 1391 | 1.95 | -0.237 | 9.30 | 74.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMLSCUP-26-LAFC | Los Angeles F | 17c | 1.0c | 4070 | 57 | 30031 | 28422 | 30031 | 28424 | 27192 | $2061 | 30d+ |
| KXMLSCUP-26-MIA | Miami | 15c | 1.0c | 4890 | 4504 | 27718 | 27724 | 27746 | 28375 | 19352 | $765 | 30d+ |
| KXMLSCUP-26-VAN | Vancouver | 9c | 1.0c | 4968 | 6238 | 28516 | 29702 | 32685 | 29802 | 11694 | $92 | 30d+ |
| KXMLSCUP-26-NSH | Nashville | 6c | 1.0c | 4668 | 4324 | 45090 | 29430 | 45090 | 29537 | 9785 | $1656 | 30d+ |
| KXMLSGAME-26APR19LAFCSJ-SJ | San Jose | 20c | 1.0c | 1146 | 350 | 28777 | 31114 | 29902 | 32255 | 7963 | $4397 | 7-30d |
| KXMLSWEST-26-LAFC | Los Angeles F | 24c | 45.0c | 5 | 1029 | 15 | 1029 | 15 | 1029 | 4212 | $0 | 30d+ |
| KXMLSGAME-26APR19LAFCSJ-LAFC | Los Angeles F | 57c | 1.0c | 803 | 210 | 38097 | 29025 | 38897 | 29165 | 3591 | $2085 | 7-30d |
| KXMLSWEST-26-SEA | Seattle | 14c | 23.0c | 5 | 928 | 5 | 928 | 5 | 928 | 3250 | $0 | 30d+ |
| KXMLSWEST-26-SJ | San Jose | 11c | 18.0c | 5 | 1000 | 15 | 1000 | 15 | 1000 | 2832 | $0 | 30d+ |
| KXMLSSPREAD-26APR19LAFCSJ-LAFC1 | Los Angeles F wins by over 1.5 goals | 34c | 1.0c | 1083 | 2180 | 3751 | 5009 | 3951 | 5769 | 2385 | $4718 | 7-30d |
| KXMLSWEST-26-VAN | Vancouver | 18c | 31.0c | 5 | 1100 | 15 | 1100 | 15 | 1100 | 2078 | $0 | 30d+ |
| KXMLSWEST-26-SD | San Diego | 8c | 11.0c | 5 | 10 | 105 | 158 | 105 | 158 | 1863 | $0 | 30d+ |
| KXMLSGAME-26APR22HOUSD-SD | San Diego FC | 30c | 3.0c | 593 | 119 | 1346 | 857 | 1886 | 857 | 1357 | $1306 | 7-30d |
| KXMLSGAME-26APR25SDPOR-TIE | Tie | 12c | 10.0c | 31 | 38 | 1338 | 597 | 9570 | 680 | 727 | $1435 | 7-30d |
| KXMLSGAME-26APR22DALMIN-DAL | Dallas | 46c | 2.0c | 27 | 80 | 853 | 1833 | 892 | 1874 | 700 | $676 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMLSCUP | MLS Cup champion | custom | 30 | 2 | $11,831 | 219,361 | 1.0c |
| KXMLSGAME | Major League Soccer Game | custom | 81 | 81 | $14,801 | 20,423 | 1.7c |
| KXMLSWEST | MLS Western Conference winner? | annual | 15 | 5 | $55 | 18,773 | 28.7c |
| KXMLSEAST | MLS Western Conference winner? | annual | 15 | 3 | $1,033 | 14,148 | 20.0c |
| KXMLSSPREAD | MLS Spread | custom | 4 | 2 | $5,400 | 2,736 | 1.0c |
| KXMLSTOTAL | MLS Total | custom | 4 | 4 | $168 | 266 | 1.7c |
| KXMLSBTTS | MLS BTTS | custom | 1 | 1 | $129 | 225 | 2.0c |
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
