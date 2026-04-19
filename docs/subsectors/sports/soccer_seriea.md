# sports_soccer_seriea

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **9** (9 with open markets)
- Open markets: **169** (104 contested)
- Total 24h volume: **$134,234**
- Total open interest: **586,034**
- Top-OI mean spread (median across series): **2.0 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **110**
- Median spread: **2.0c**
- Median TOB bid / ask size: **586 / 575** contracts
- Median depth within 5c of best bid / ask — **8091 / 7324** contracts
- Median depth within 10c of best bid / ask — **10040 / 7739** contracts
- Median depth within 5c of midpoint — bid: **4979** / ask: **3551** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **16**
- Mean informed-signal proxy: **-1.145** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.95c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1287 | 0.43 | -0.305 | 2.00 | 142.2 |
| 30d+ | 509 | 4.33 | -1.349 | 22.00 | 38.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSERIEAGAME-26APR19VERACM-ACM | Milan | 65c | 2.0c | 5245 | 39144 | 208660 | 219242 | 209091 | 219946 | 90755 | $89345 | 7-30d |
| KXSERIEAGAME-26APR19CRETOR-TOR | Torino | 36c | 1.0c | 4855 | 29161 | 76273 | 246848 | 76473 | 248232 | 13262 | $11613 | 7-30d |
| KXSERIEAGAME-26APR19JUVBFC-JUV | Juventus | 68c | 1.0c | 3500 | 17008 | 221599 | 205856 | 222124 | 206757 | 7894 | $6600 | 7-30d |
| KXSERIEAGAME-26APR19CRETOR-CRE | Cremonese | 34c | 1.0c | 3514 | 4791 | 154460 | 213814 | 154988 | 215214 | 6056 | $6254 | 7-30d |
| KXSERIEAGAME-26APR19PISGEN-GEN | Genoa | 40c | 1.0c | 3514 | 22361 | 69687 | 274196 | 70087 | 275097 | 4348 | $1682 | 7-30d |
| KXSERIEAGAME-26APR19CRETOR-TIE | Tie | 31c | 1.0c | 24380 | 3500 | 410021 | 240555 | 412521 | 242259 | 4202 | $3500 | 7-30d |
| KXSERIEATOP4-26-NAP | Napoli | 77c | 44.0c | 200 | 200 | 200 | 200 | 200 | 200 | 4067 | $0 | 30d+ |
| KXSERIEATOP4-26-COM | Como | 52c | 93.0c | 500 | 1454 | 2731 | 1454 | 2731 | 1454 | 3894 | $0 | 30d+ |
| KXSERIEATOTAL-26APR19CRETOR-2 | Over 2.5 goals scored | 43c | 1.0c | 275 | 2368 | 22924 | 24301 | 23574 | 24601 | 3364 | $4306 | 7-30d |
| KXSERIEATOP4-26-JUV | Juventus | 74c | 44.0c | 109 | 22 | 109 | 122 | 209 | 122 | 1790 | $28 | 30d+ |
| KXSERIEAGAME-26APR19JUVBFC-BFC | Bologna | 12c | 1.0c | 6975 | 3500 | 251058 | 259844 | 297750 | 261942 | 1666 | $4675 | 7-30d |
| KXSERIEATOP4-26-ROM | Roma | 26c | 49.0c | 199 | 262 | 199 | 262 | 199 | 362 | 1500 | $0 | 30d+ |
| KXSERIEARELEGATION-26-CRE | Cremonese | 40c | 79.0c | 300 | 96 | 300 | 96 | 300 | 96 | 1243 | $0 | 30d+ |
| KXSERIEATOTAL-26APR19VERACM-4 | Over 4.5 goals scored | 10c | 1.0c | 136 | 250 | 1218 | 1678 | 5724 | 7278 | 958 | $1007 | 7-30d |
| KXSERIEAGAME-26APR19VERACM-VER | Hellas Verona | 12c | 1.0c | 5949 | 3515 | 353560 | 199109 | 360285 | 199631 | 826 | $967 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSERIEA | Serie A  | annual | 20 | 0 | $541 | 421,411 | nanc |
| KXSERIEAGAME | Serie A Game | custom | 39 | 38 | $124,910 | 127,457 | 1.0c |
| KXSERIEATOP4 | Serie A Top 4 Finishers | annual | 20 | 5 | $28 | 16,983 | 53.0c |
| KXSERIEARELEGATION | Serie A Relegation | annual | 20 | 3 | $0 | 10,378 | 75.7c |
| KXSERIEATOTAL | Serie A Total | custom | 20 | 18 | $6,694 | 6,898 | 1.0c |
| KXSERIEASPREAD | Serie A Spread | custom | 20 | 10 | $859 | 1,709 | 2.0c |
| KXSERIEABTTS | Serie A BTTS | custom | 5 | 5 | $768 | 772 | 1.7c |
| KXSERIEA1H | Serie A First Half Winner | custom | 15 | 15 | $434 | 424 | 2.0c |
| KXBBSERIEAGAME | Italy Serie A Basketball Game | custom | 10 | 10 | $1 | 1 | 59.0c |

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
