# sports_soccer_seriea

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **9** (9 with open markets)
- Open markets: **169** (102 contested)
- Total 24h volume: **$110,013**
- Total open interest: **561,978**
- Top-OI mean spread (median across series): **2.8 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **109**
- Median spread: **2.0c**
- Median TOB bid / ask size: **581 / 677** contracts
- Median cumulative depth within 5c of mid — bid: **3949** / ask: **4440** contracts
- Median cumulative depth within 10c of mid — bid: **8504** / ask: **7701** contracts
- Mean trades per market (last 3000): **13**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1004 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 456 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSERIEAGAME-26APR19VERACM-ACM | Milan | 64c | 1.0c | 3527 | 4385 | 201230 | 226943 | 87640 | $86124 | 7-30d |
| KXSERIEAGAME-26APR19JUVBFC-JUV | Juventus | 68c | 1.0c | 3500 | 18526 | 240592 | 254206 | 7176 | $5897 | 7-30d |
| KXSERIEAGAME-26APR19CRETOR-TOR | Torino | 36c | 1.0c | 3500 | 16504 | 276541 | 100440 | 6434 | $5972 | 7-30d |
| KXSERIEATOP4-26-COM | Como | 50c | 85.0c | 500 | 500 | 0 | 0 | 3894 | $0 | 30d+ |
| KXSERIEAGAME-26APR19PISGEN-GEN | Genoa | 40c | 1.0c | 3514 | 5151 | 172994 | 242872 | 2917 | $251 | 7-30d |
| KXSERIEAGAME-26APR19CRETOR-TIE | Tie | 31c | 1.0c | 17451 | 3500 | 428339 | 249005 | 2453 | $1751 | 7-30d |
| KXSERIEATOP4-26-JUV | Juventus | 74c | 43.0c | 109 | 100 | 0 | 0 | 1790 | $28 | 30d+ |
| KXSERIEATOP4-26-ROM | Roma | 24c | 45.0c | 100 | 500 | 0 | 0 | 1500 | $0 | 30d+ |
| KXSERIEAGAME-26APR19JUVBFC-BFC | Bologna | 14c | 1.0c | 16 | 4836 | 210214 | 239103 | 1435 | $4443 | 7-30d |
| KXSERIEARELEGATION-26-CRE | Cremonese | 40c | 77.0c | 1000 | 100 | 0 | 0 | 1243 | $0 | 30d+ |
| KXSERIEATOP4-26-ACM | Milan | 82c | 32.0c | 1000 | 500 | 0 | 0 | 793 | $0 | 30d+ |
| KXSERIEARELEGATION-26-CAG | Cagliari | 40c | 78.0c | 99 | 500 | 0 | 0 | 776 | $0 | 30d+ |
| KXSERIEAGAME-26APR19CRETOR-CRE | Cremonese | 32c | 1.0c | 5546 | 3501 | 301956 | 263016 | 733 | $1372 | 7-30d |
| KXSERIEAGAME-26APR19VERACM-VER | Hellas Verona | 12c | 1.0c | 15325 | 3506 | 381867 | 233494 | 676 | $680 | 7-30d |
| KXSERIEATOTAL-26APR19CRETOR-4 | Over 4.5 goals scored | 9c | 2.0c | 905 | 712 | 12274 | 732 | 568 | $757 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSERIEA | Serie A  | annual | 20 | 0 | $443 | 421,327 | nanc |
| KXSERIEAGAME | Serie A Game | custom | 39 | 38 | $106,607 | 109,178 | 1.3c |
| KXSERIEATOP4 | Serie A Top 4 Finishers | annual | 20 | 4 | $28 | 16,983 | 40.7c |
| KXSERIEARELEGATION | Serie A Relegation | annual | 20 | 3 | $0 | 10,378 | 76.3c |
| KXSERIEATOTAL | Serie A Total | custom | 20 | 17 | $2,018 | 2,319 | 1.7c |
| KXSERIEASPREAD | Serie A Spread | custom | 20 | 10 | $370 | 1,242 | 1.0c |
| KXSERIEABTTS | Serie A BTTS | custom | 5 | 5 | $442 | 446 | 2.3c |
| KXSERIEA1H | Serie A First Half Winner | custom | 15 | 15 | $103 | 104 | 3.3c |
| KXBBSERIEAGAME | Italy Serie A Basketball Game | custom | 10 | 10 | $1 | 1 | 60.0c |

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
