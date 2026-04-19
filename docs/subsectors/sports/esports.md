# sports_esports

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **16** (16 with open markets)
- Open markets: **749** (522 contested)
- Total 24h volume: **$349,619**
- Total open interest: **469,163**
- Top-OI mean spread (median across series): **6.9 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **6.0c**
- Median TOB bid / ask size: **500 / 500** contracts
- Median cumulative depth within 5c of mid — bid: **1246** / ask: **1160** contracts
- Median cumulative depth within 10c of mid — bid: **2004** / ask: **2169** contracts
- Mean trades per market (last 3000): **14**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2741 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 109 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCS2GAME-26APR191300VITTS-VIT | Vitality | 76c | 1.0c | 3227 | 39170 | 45586 | 221167 | 19015 | $18569 | 7-30d |
| KXCS2-IEMRIO26-VIT | Vitality | 77c | 6.0c | 5 | 14 | 4127 | 10196 | 12026 | $10057 | 7-30d |
| KXLOLGAME-26APR190600T1DRX-T1 | T1 | 82c | 2.0c | 1025 | 60662 | 18586 | 208908 | 8115 | $7567 | 7-30d |
| KXLOLGAME-26APR191100GXVIT-VIT | Team Vitality | 58c | 2.0c | 300 | 469 | 4325 | 7638 | 7251 | $4834 | 7-30d |
| KXCS2-IEMRIO26-TS | Spirit | 23c | 8.0c | 24 | 4820 | 10024 | 5236 | 7053 | $8194 | 7-30d |
| KXLOLGAME-26APR190400NSBRO-NS | Nongshim Red Force | 70c | 1.0c | 4294 | 16078 | 15174 | 150533 | 5396 | $3687 | 7-30d |
| KXCS2GAME-26APR190930FURIAFAL-FAL | Team Falcons | 50c | 1.0c | 10692 | 3805 | 42293 | 196080 | 4625 | $4605 | 7-30d |
| KXCS2GAME-26APR190930FURIAFAL-FURIA | FURIA | 50c | 1.0c | 200 | 41430 | 62500 | 183421 | 3904 | $3697 | 7-30d |
| KXVALORANTGAME-26APR190600GENGNS-GENG | Gen.G Esports | 35c | 2.0c | 445 | 292 | 3280 | 32722 | 3792 | $2776 | 7-30d |
| KXLOLGAME-26APR190600T1DRX-DRX | DRX | 18c | 1.0c | 525 | 10498 | 3568 | 150551 | 3601 | $4792 | 7-30d |
| KXVALORANTMAP-26APR190700XLGAG-2-XLG | XLG Gaming | 59c | 6.0c | 1500 | 490 | 2754 | 1688 | 2780 | $77 | 7-30d |
| KXLOLGAME-26APR190400NSBRO-BRO | OKSavingsBank BRION | 29c | 2.0c | 5315 | 29867 | 6095 | 153117 | 2624 | $2673 | 7-30d |
| KXCS2GAME-26APR191300VITTS-TS | Spirit | 24c | 1.0c | 11000 | 20689 | 22862 | 157792 | 2430 | $2424 | 7-30d |
| KXNEWCITY-29 | Before 2029 | 39c | 8.0c | 105 | 100 | 105 | 301 | 2291 | $0 | 30d+ |
| KXVALORANTMAP-26APR201030DPETE-1-DP | Dark Passage | 29c | 6.0c | 1000 | 1001 | 2498 | 2177 | 2173 | $86 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXROLEATEVENTLOLLA | Who will headline Lollapalooza | one_off | 16 | 0 | $1,490 | 168,694 | nanc |
| KXLOLGAME | League of Legends Game | custom | 94 | 92 | $176,981 | 127,389 | 1.3c |
| KXVALORANTGAME | Valorant game winner | custom | 48 | 46 | $96,956 | 83,279 | 1.7c |
| KXCS2GAME | Counter-Strike 2 Game | custom | 20 | 18 | $30,412 | 31,309 | 1.0c |
| KXCS2 | CS2 Tournament Winner | custom | 4 | 2 | $28,492 | 30,886 | 7.5c |
| KXVALORANTMAP | Valorant Map Winner | custom | 96 | 94 | $3,401 | 12,257 | 19.0c |
| KXLOLTOTALMAPS | League of Legends Total Maps | custom | 36 | 35 | $6,956 | 7,116 | 21.3c |
| KXNEWCITY | New federal city | custom | 1 | 1 | $0 | 2,291 | 8.0c |
| KXDOTA2GAME | Dota 2 Game | custom | 16 | 16 | $1,520 | 1,520 | 5.0c |
| KXOWGAME | Overwatch Game | custom | 8 | 8 | $1,307 | 1,275 | 6.3c |

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
