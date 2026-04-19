# sports_soccer_laliga

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **193** (129 contested)
- Total 24h volume: **$50,379**
- Total open interest: **715,671**
- Top-OI mean spread (median across series): **2.5 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **139**
- Median spread: **3.0c**
- Median TOB bid / ask size: **431 / 214** contracts
- Median cumulative depth within 5c of mid — bid: **2725** / ask: **2090** contracts
- Median cumulative depth within 10c of mid — bid: **4431** / ask: **3262** contracts
- Mean trades per market (last 3000): **16**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1773 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 489 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLALIGAGAME-26APR22ELCATM-ATM | Atletico | 38c | 1.0c | 6037 | 121 | 22206 | 40925 | 23485 | $13715 | 7-30d |
| KXLALIGAGAME-26APR22BARRCC-RCC | Celta Vigo | 9c | 1.0c | 211 | 6144 | 25979 | 43545 | 12041 | $948 | 7-30d |
| KXLALIGAGAME-26APR21RMAALA-RMA | Real Madrid | 78c | 1.0c | 6013 | 6093 | 47126 | 89254 | 10459 | $5177 | 7-30d |
| KXLALIGAGAME-26APR21RMAALA-ALA | Alaves | 7c | 1.0c | 7236 | 7459 | 68690 | 60368 | 5867 | $2219 | 7-30d |
| KXLALIGAGAME-26APR22BARRCC-BAR | Barcelona | 78c | 1.0c | 7324 | 615 | 33717 | 59922 | 5690 | $822 | 7-30d |
| KXLALIGAGAME-26APR21ATHOSA-ATH | Bilbao | 54c | 2.0c | 6035 | 6377 | 38656 | 30277 | 4674 | $4955 | 7-30d |
| KXLALIGAGAME-26APR21ATHOSA-OSA | Osasuna | 20c | 2.0c | 6562 | 6332 | 39906 | 38187 | 3367 | $1901 | 7-30d |
| KXLALIGAGAME-26APR21MALVCF-MAL | Mallorca | 38c | 1.0c | 6350 | 6001 | 32828 | 29840 | 2626 | $421 | 7-30d |
| KXLALIGAGAME-26APR22RSOGET-RSO | Real Sociedad | 44c | 1.0c | 6250 | 426 | 36132 | 19438 | 2156 | $781 | 7-30d |
| KXLALIGARELEGATION-26-ELC | Elche | 45c | 75.0c | 2512 | 221 | 0 | 0 | 2057 | $4 | 30d+ |
| KXLALIGASPREAD-26APR21RMAALA-RMA1 | Real Madrid wins by over 1.5 goals | 55c | 1.0c | 672 | 102 | 3301 | 3047 | 2022 | $1832 | 7-30d |
| KXLALIGAGAME-26APR21MALVCF-TIE | Tie | 30c | 2.0c | 10344 | 6000 | 40038 | 37359 | 1511 | $1122 | 7-30d |
| KXLALIGAGAME-26APR25GETBAR-BAR | Barcelona | 62c | 4.0c | 5085 | 3273 | 18545 | 9830 | 1454 | $1454 | 7-30d |
| KXLALIGARELEGATION-26-ALA | Alaves | 53c | 58.0c | 10 | 1000 | 0 | 0 | 1350 | $3 | 30d+ |
| KXLALIGAGAME-26APR21MALVCF-VCF | Valencia | 32c | 2.0c | 6054 | 6251 | 28444 | 37745 | 1271 | $1061 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXLALIGA | LA LIGA | annual | 20 | 0 | $5,426 | 586,292 | nanc |
| KXLALIGAGAME | La Liga Game | custom | 57 | 55 | $37,690 | 80,947 | 1.0c |
| KXLALIGARELEGATION | La Liga Relegation | annual | 20 | 6 | $24 | 29,796 | 50.3c |
| KXLALIGATOP4 | La Liga Top 4 Finishers | annual | 20 | 0 | $186 | 13,158 | nanc |
| KXLALIGASPREAD | La Liga Spread | custom | 16 | 8 | $3,039 | 2,986 | 2.3c |
| KXLALIGATOTAL | La Liga Total | custom | 16 | 16 | $2,437 | 1,230 | 1.7c |
| KXLALIGA2GAME | LaLiga 2 Game | custom | 18 | 18 | $114 | 789 | 2.0c |
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
