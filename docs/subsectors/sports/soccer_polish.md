# sports_soccer_polish

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **30** (13 contested)
- Total 24h volume: **$825**
- Total open interest: **1,730**
- Top-OI mean spread (median across series): **40.2 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **13**
- Median spread: **2.0c**
- Median TOB bid / ask size: **58 / 105** contracts
- Median depth within 5c of best bid / ask — **944 / 850** contracts
- Median depth within 10c of best bid / ask — **964 / 850** contracts
- Median depth within 5c of midpoint — bid: **757** / ask: **646** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **4**
- Mean informed-signal proxy: **-0.195** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.17c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 51 | 0.91 | -0.209 | 3.00 | 37.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXEKSTRAKLASAGAME-26APR19NIEPLO-PLO | Wisla Plock | 36c | 2.0c | 102 | 1070 | 1157 | 1458 | 1157 | 1458 | 1156 | $877 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19ARKJAG-JAG | Jagiellonia | 44c | 2.0c | 59 | 58 | 944 | 558 | 944 | 558 | 182 | $88 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19NIEPLO-NIE | Nieciecza | 36c | 1.0c | 1 | 226 | 1004 | 1489 | 1004 | 1989 | 67 | $41 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19CZECRA-TIE | Tie | 28c | 1.0c | 1 | 197 | 584 | 1673 | 985 | 1673 | 17 | $17 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19NIEPLO-TIE | Tie | 29c | 1.0c | 1 | 244 | 964 | 1728 | 964 | 1728 | 16 | $16 | 7-30d |
| KXEKSTRAKLASA-26-JAG | Jagiellonia | 60c | 79.0c | 1 | 1 | 1 | 1 | 1 | 1 | 14 | $0 | 30d+ |
| KXEKSTRAKLASAGAME-26APR19CZECRA-CZE | Czestochowa | 52c | 1.0c | 36 | 1566 | 381 | 2067 | 882 | 2067 | 11 | $11 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19CZECRA-CRA | Cracovia Krakow | 24c | 1.0c | 0 | 257 | 1075 | 1676 | 1076 | 1677 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR20LECPGL-TIE | Tie | 24c | 8.0c | 1025 | 1 | 1026 | 577 | 1026 | 577 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR20LECPGL-PGL | Gliwice | 30c | 3.0c | 431 | 1 | 832 | 783 | 832 | 783 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR20LECPGL-LEC | Lechia Gdansk | 44c | 8.0c | 312 | 1 | 713 | 646 | 713 | 646 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19ARKJAG-TIE | Tie | 26c | 1.0c | 58 | 80 | 983 | 717 | 983 | 717 | 0 | $0 | 7-30d |
| KXEKSTRAKLASAGAME-26APR19ARKJAG-ARK | Arka Gdynia | 29c | 2.0c | 86 | 105 | 878 | 850 | 878 | 850 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXEKSTRAKLASAGAME | Polish Ekstraklasa Game | custom | 12 | 12 | $825 | 1,159 | 1.3c |
| KXEKSTRAKLASA | Ekstraklasa Champion | custom | 18 | 1 | $0 | 571 | 79.0c |

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
