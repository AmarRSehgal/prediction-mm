# sports_esports_cs2

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **18** (18 contested)
- Total 24h volume: **$82,092**
- Total open interest: **76,643**
- Top-OI mean spread (median across series): **1.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **18**
- Median spread: **12.5c**
- Median TOB bid / ask size: **104 / 84** contracts
- Median depth within 5c of best bid / ask — **1892 / 233** contracts
- Median depth within 10c of best bid / ask — **2078 / 270** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **36**
- Mean informed-signal proxy: **-1.261** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.62c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 649 | 1.34 | -0.776 | 7.00 | 131.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCS2GAME-26APR191300VITTS-VIT | Vitality | 76c | 1.0c | 2223 | 154283 | 34648 | 507124 | 34749 | 507147 | 27555 | $27345 | 7-30d |
| KXCS2GAME-26APR190930FURIAFAL-FAL | Team Falcons | 55c | 2.0c | 310 | 59894 | 35693 | 232513 | 35909 | 232513 | 18336 | $21366 | 7-30d |
| KXCS2GAME-26APR191300VITTS-TS | Spirit | 24c | 1.0c | 36505 | 846 | 68192 | 259610 | 68193 | 259670 | 13878 | $15885 | 7-30d |
| KXCS2GAME-26APR190930FURIAFAL-FURIA | FURIA | 45c | 1.0c | 2000 | 92188 | 6549 | 265671 | 7048 | 265786 | 13816 | $14884 | 7-30d |
| KXCS2GAME-26APR191300MOUZNEYE-EYE | EYEBALLERS | 64c | 3.0c | 79 | 16 | 2198 | 96 | 2218 | 97 | 1848 | $1194 | 7-30d |
| KXCS2GAME-26APR191300MOUZNEYE-MOUZN | MOUZ NXT | 38c | 3.0c | 1080 | 16 | 2100 | 51 | 2100 | 673 | 794 | $812 | 7-30d |
| KXCS2GAME-26APR191100TNCYN-YN | Young Ninjas | 55c | 3.0c | 1051 | 186 | 2099 | 1086 | 2099 | 3086 | 218 | $135 | 7-30d |
| KXCS2GAME-26APR191400UNITYCLU-CLU | Clutchain | 40c | 35.0c | 100 | 300 | 101 | 300 | 102 | 300 | 64 | $43 | 7-30d |
| KXCS2GAME-26APR191100TNCYN-TNC | TNC | 44c | 4.0c | 230 | 67 | 1291 | 2089 | 2291 | 2089 | 49 | $353 | 7-30d |
| KXCS2GAME-26APR191400UNITYCLU-UNITY | UNiTY esports | 67c | 24.0c | 2964 | 1 | 2964 | 3 | 2964 | 146 | 45 | $37 | 7-30d |
| KXCS2GAME-26APR201330ALLKOL-ALL | Alliance | 78c | 12.0c | 108 | 36 | 108 | 94 | 312 | 133 | 27 | $25 | 7-30d |
| KXCS2GAME-26APR211100JSTRI-JS | Johnny Speeds | 57c | 22.0c | 100 | 152 | 100 | 152 | 130 | 152 | 10 | $10 | 7-30d |
| KXCS2GAME-26APR211100JSTRI-TRI | Tricked | 48c | 24.0c | 100 | 54 | 130 | 54 | 130 | 201 | 2 | $2 | 7-30d |
| KXCS2GAME-26APR211330QUAFNC-FNC | fnatic | 50c | 93.0c | 2 | 100 | 1727 | 1030 | 1727 | 1030 | 1 | $1 | 7-30d |
| KXCS2GAME-26APR211330QUAFNC-QUA | Qual4 | 22c | 37.0c | 30 | 10 | 1230 | 10 | 1230 | 20 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCS2GAME | Vitality | nan | 18 | 18 | $82,092 | 76,643 | 1.3c |

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
