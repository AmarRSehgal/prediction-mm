# sports_esports_dota

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **44** (44 contested)
- Total 24h volume: **$36,238**
- Total open interest: **30,473**
- Top-OI mean spread (median across series): **5.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **44**
- Median spread: **5.0c**
- Median TOB bid / ask size: **500 / 497** contracts
- Median depth within 5c of best bid / ask — **1759 / 1558** contracts
- Median depth within 10c of best bid / ask — **1767 / 1639** contracts
- Median depth within 5c of midpoint — bid: **1730** / ask: **1354** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **17**
- Mean informed-signal proxy: **-0.578** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.66c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 745 | 1.71 | -0.336 | 7.00 | 52.7 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXDOTA2GAME-26APR190300AURXTREME-XTREME | Xtreme Gaming | 52c | 7.0c | 275 | 60 | 364 | 684 | 484 | 835 | 9341 | $10501 | 7-30d |
| KXDOTA2GAME-26APR190300AURXTREME-AUR | Aurora | 48c | 7.0c | 251 | 50 | 444 | 247 | 444 | 1050 | 8266 | $13711 | 7-30d |
| KXDOTA2GAME-26APR190300NAVIVG-NAVI | Natus Vincere | 66c | 5.0c | 218 | 50 | 343 | 250 | 668 | 939 | 2246 | $2180 | 7-30d |
| KXDOTA2MAP-26APR190300NAVIVG-2-NAVI | Natus Vincere | 30c | 3.0c | 1 | 67 | 1 | 80 | 136 | 142 | 1897 | $1140 | 7-30d |
| KXDOTA2MAP-26APR190300AURXTREME-2-XTREME | Xtreme Gaming | 10c | 7.0c | 2 | 97 | 65 | 175 | 65 | 175 | 1677 | $1711 | 7-30d |
| KXDOTA2GAME-26APR190300NAVIVG-VG | Vici Gaming | 34c | 6.0c | 200 | 291 | 450 | 392 | 570 | 1044 | 1614 | $1339 | 7-30d |
| KXDOTA2GAME-26APR190600BBLIQUID-LIQUID | Team Liquid | 48c | 5.0c | 500 | 758 | 2742 | 3876 | 2742 | 4476 | 1180 | $1180 | 7-30d |
| KXDOTA2GAME-26APR190900FLCTS-FLC | Team Falcons | 61c | 2.0c | 500 | 3290 | 1711 | 5694 | 3088 | 5786 | 962 | $962 | 7-30d |
| KXDOTA2MAP-26APR190300AURXTREME-2-AUR | Aurora | 92c | 5.0c | 66 | 6 | 132 | 79 | 196 | 79 | 856 | $1340 | 7-30d |
| KXDOTA2GAME-26APR191200VPTUNDRA-VP | Virtus.pro | 20c | 4.0c | 525 | 1153 | 2829 | 3042 | 2829 | 6007 | 680 | $680 | 7-30d |
| KXDOTA2MAP-26APR190300NAVIVG-2-VG | Vici Gaming | 72c | 13.0c | 4 | 4 | 50 | 4 | 145 | 95 | 408 | $120 | 7-30d |
| KXDOTA2GAME-26APR190600BBLIQUID-BB | BetBoom Team | 52c | 5.0c | 600 | 520 | 2841 | 3759 | 2841 | 4359 | 365 | $365 | 7-30d |
| KXDOTA2GAME-26APR190900FLCTS-TS | Team Spirit | 38c | 2.0c | 768 | 191 | 2859 | 3744 | 2859 | 5869 | 283 | $283 | 7-30d |
| KXDOTA2GAME-26APR190600GLMOUZ-GL | GamerLegion | 53c | 4.0c | 525 | 805 | 2816 | 3947 | 2816 | 4547 | 273 | $273 | 7-30d |
| KXDOTA2GAME-26APR190900SARTY-TY | Team Yandex | 82c | 7.0c | 50 | 27 | 550 | 343 | 767 | 3327 | 133 | $133 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXDOTA2GAME | Xtreme Gaming | nan | 16 | 16 | $31,797 | 25,506 | 6.3c |
| KXDOTA2MAP | Natus Vincere | nan | 28 | 28 | $4,442 | 4,967 | 5.0c |

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
