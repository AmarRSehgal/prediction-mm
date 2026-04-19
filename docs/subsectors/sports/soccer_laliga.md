# sports_soccer_laliga

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **193** (128 contested)
- Total 24h volume: **$49,836**
- Total open interest: **718,328**
- Top-OI mean spread (median across series): **2.8 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **141**
- Median spread: **3.0c**
- Median TOB bid / ask size: **537 / 440** contracts
- Median depth within 5c of best bid / ask — **3921 / 3047** contracts
- Median depth within 10c of best bid / ask — **11057 / 3331** contracts
- Median depth within 5c of midpoint — bid: **3061** / ask: **2814** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **17**
- Mean informed-signal proxy: **-1.469** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.65c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1834 | 0.81 | -0.361 | 3.00 | 72.3 |
| 30d+ | 543 | 5.67 | -3.232 | 29.20 | 19.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLALIGAGAME-26APR22ELCATM-ATM | Atletico | 38c | 2.0c | 6454 | 12976 | 21754 | 38611 | 28054 | 38822 | 23517 | $11686 | 7-30d |
| KXLALIGAGAME-26APR22BARRCC-RCC | Celta Vigo | 9c | 1.0c | 211 | 6144 | 25739 | 57692 | 52228 | 76978 | 12874 | $1728 | 7-30d |
| KXLALIGAGAME-26APR21RMAALA-RMA | Real Madrid | 78c | 1.0c | 6026 | 6093 | 49318 | 96764 | 65221 | 98227 | 10459 | $5064 | 7-30d |
| KXLALIGAGAME-26APR21RMAALA-ALA | Alaves | 7c | 1.0c | 7617 | 7001 | 55221 | 62268 | 76675 | 79040 | 5917 | $2068 | 7-30d |
| KXLALIGAGAME-26APR22BARRCC-BAR | Barcelona | 80c | 1.0c | 319 | 1144 | 37103 | 66034 | 50455 | 68040 | 5822 | $938 | 7-30d |
| KXLALIGAGAME-26APR21ATHOSA-ATH | Bilbao | 54c | 2.0c | 6035 | 6351 | 35796 | 43053 | 41600 | 44053 | 4674 | $4920 | 7-30d |
| KXLALIGAGAME-26APR21ATHOSA-OSA | Osasuna | 20c | 1.0c | 6001 | 6092 | 29747 | 41481 | 60672 | 42584 | 3545 | $1984 | 7-30d |
| KXLALIGAGAME-26APR21MALVCF-MAL | Mallorca | 38c | 1.0c | 6350 | 6001 | 29862 | 25868 | 36142 | 27328 | 2638 | $433 | 7-30d |
| KXLALIGAGAME-26APR22RSOGET-RSO | Real Sociedad | 45c | 2.0c | 6250 | 1107 | 37104 | 26196 | 52644 | 26196 | 2163 | $788 | 7-30d |
| KXLALIGARELEGATION-26-ELC | Elche | 36c | 5.0c | 334 | 500 | 834 | 1170 | 834 | 1170 | 2057 | $0 | 30d+ |
| KXLALIGASPREAD-26APR21RMAALA-RMA1 | Real Madrid wins by over 1.5 goals | 56c | 3.0c | 672 | 132 | 3301 | 3672 | 3741 | 3867 | 2022 | $1832 | 7-30d |
| KXLALIGAGAME-26APR21MALVCF-TIE | Tie | 30c | 2.0c | 10191 | 6250 | 45488 | 37258 | 51688 | 38258 | 1511 | $1122 | 7-30d |
| KXLALIGAGAME-26APR25GETBAR-BAR | Barcelona | 62c | 3.0c | 250 | 3523 | 13631 | 4877 | 20031 | 5135 | 1454 | $1454 | 7-30d |
| KXLALIGARELEGATION-26-ALA | Alaves | 30c | 7.0c | 210 | 289 | 720 | 789 | 720 | 789 | 1350 | $3 | 30d+ |
| KXLALIGAGAME-26APR21MALVCF-VCF | Valencia | 32c | 2.0c | 6565 | 6001 | 25189 | 34243 | 31469 | 35543 | 1305 | $1074 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXLALIGA | LA LIGA | annual | 20 | 0 | $5,122 | 586,414 | nanc |
| KXLALIGAGAME | La Liga Game | custom | 57 | 55 | $37,103 | 83,038 | 1.0c |
| KXLALIGARELEGATION | La Liga Relegation | annual | 20 | 6 | $14 | 29,796 | 56.0c |
| KXLALIGATOP4 | La Liga Top 4 Finishers | annual | 20 | 0 | $186 | 13,158 | nanc |
| KXLALIGASPREAD | La Liga Spread | custom | 16 | 7 | $3,039 | 2,986 | 3.0c |
| KXLALIGATOTAL | La Liga Total | custom | 16 | 16 | $2,459 | 1,252 | 1.7c |
| KXLALIGA2GAME | LaLiga 2 Game | custom | 18 | 18 | $450 | 1,212 | 1.3c |
| KXLALIGA1H | La Liga First Half Winner | one_off | 12 | 12 | $368 | 349 | 2.7c |
| KXLALIGABTTS | La Liga BTTS | custom | 4 | 4 | $1,095 | 124 | 3.0c |
| KXNEXTMANAGERLALIGA | La Liga Next Manager | custom | 10 | 10 | $0 | 0 | 98.0c |

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
