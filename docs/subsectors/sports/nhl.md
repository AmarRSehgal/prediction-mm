# sports_nhl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **14** (14 with open markets)
- Open markets: **731** (496 contested)
- Total 24h volume: **$2,142,077**
- Total open interest: **3,684,142**
- Top-OI mean spread (median across series): **14.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **4.0c**
- Median TOB bid / ask size: **208 / 301** contracts
- Median cumulative depth within 5c of mid — bid: **1206** / ask: **1020** contracts
- Median cumulative depth within 10c of mid — bid: **2343** / ask: **2076** contracts
- Mean trades per market (last 3000): **115**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 12139 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 10791 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNHLHART-26-NMAC | :: | 14c | 5.0c | 216 | 28 | 765 | 215 | 312085 | $2302 | 30d+ |
| KXNHLSERIES-26OTTCARR1-CAR | Carolina Hurricanes | 74c | 1.0c | 3153 | 53664 | 18685 | 232577 | 194125 | $193916 | 7-30d |
| KXNHLHART-26-KKUC | :: | 40c | 1.0c | 174 | 509 | 1100 | 509 | 171006 | $3302 | 30d+ |
| KXNHLHART-26-CMCD | :: | 52c | 1.0c | 827 | 143 | 869 | 217 | 130770 | $3900 | 30d+ |
| KXNHLSERIES-26OTTCARR1-OTT | Ottawa Senators | 26c | 1.0c | 19 | 12087 | 7516 | 19485 | 112631 | $99932 | 7-30d |
| KXNHLADAMS-26-LRUF | :: | 80c | 13.0c | 435 | 1000 | 0 | 0 | 110606 | $95 | 30d+ |
| KXNHLSERIES-26LACOLR1-COL | Colorado Avalanche | 82c | 1.0c | 3944 | 18582 | 12849 | 262396 | 109560 | $106625 | 7-30d |
| KXNHLSERIES-26MINDALR1-MIN | Minnesota Wild | 62c | 1.0c | 6948 | 3501 | 11765 | 33898 | 79437 | $50199 | 7-30d |
| KXNHLSERIES-26MINDALR1-DAL | Dallas Stars | 36c | 1.0c | 3549 | 42648 | 4672 | 50656 | 66737 | $61805 | 7-30d |
| KXNHLSERIES-26PHIPITR1-PIT | Pittsburgh Penguins | 40c | 2.0c | 91 | 6177 | 998 | 14804 | 61187 | $42981 | 7-30d |
| KXNHLGAME-26APR19LACOL-COL | COL Avalanche | 70c | 1.0c | 17725 | 197254 | 127858 | 975737 | 58890 | $51137 | 7-30d |
| KXNHLSERIES-26PHIPITR1-PHI | Philadelphia Flyers | 61c | 2.0c | 4 | 4 | 976 | 1365 | 44660 | $23546 | 7-30d |
| KXNHLNORRIS-26-ZWER | :: | 72c | 1.0c | 330 | 635 | 5650 | 635 | 43893 | $76 | 30d+ |
| KXNHLGAME-26APR19BOSBUF-BUF | BUF Sabres | 58c | 1.0c | 58842 | 14111 | 124574 | 642260 | 41129 | $38331 | 7-30d |
| KXNHLSERIES-26MTLTBR1-MTL | Montreal Canadiens | 32c | 2.0c | 32 | 3500 | 6082 | 9062 | 37395 | $16469 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNHLGAME | NHL Game | custom | 58 | 58 | $1,268,939 | 1,250,653 | 1.3c |
| KXNHLHART | NHL Hart Memorial Trophy | annual | 30 | 3 | $15,855 | 849,024 | 1.0c |
| KXNHLSERIES | NHL Series Winner | custom | 16 | 16 | $667,162 | 840,227 | 1.7c |
| KXNHLADAMS | NHL Jack Adams Award | annual | 32 | 1 | $112 | 212,481 | 11.0c |
| KXNHLNORRIS | NHL James Norris Memorial Trophy | annual | 30 | 2 | $3,123 | 145,656 | 2.0c |
| KXNHLSERIESSCORE | NHL Series Exact Score | one_off | 62 | 45 | $51,608 | 95,725 | 30.3c |
| KXNHLVEZINA | NHL Vezina Trophy | annual | 30 | 1 | $232 | 94,126 | 19.0c |
| KXNHLSPREAD | NHL Spread | custom | 116 | 113 | $110,112 | 92,573 | 3.7c |
| KXNHLCALDER | NHL Calder Memorial Trophy | annual | 30 | 0 | $477 | 73,784 | nanc |
| KXNHLSERIESSPREAD | NHL Series Game Spread | custom | 46 | 35 | $16,016 | 21,036 | 18.3c |

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
