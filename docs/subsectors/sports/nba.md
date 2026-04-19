# sports_nba

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **38** (38 with open markets)
- Open markets: **1496** (745 contested)
- Total 24h volume: **$7,362,609**
- Total open interest: **66,685,906**
- Top-OI mean spread (median across series): **9.5 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **198**
- Median spread: **7.0c**
- Median TOB bid / ask size: **46 / 97** contracts
- Median depth within 5c of best bid / ask — **783 / 1332** contracts
- Median depth within 10c of best bid / ask — **1620 / 2304** contracts
- Median depth within 5c of midpoint — bid: **76** / ask: **252** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **141**
- Mean informed-signal proxy: **-1.137** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 5340 | 1.52 | -0.564 | 7.00 | 80.9 |
| 30d+ | 22675 | 1.05 | -0.370 | 5.00 | 220.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNBA-26-SAS | San Antonio | 17c | 1.0c | 182 | 184847 | 59625 | 577573 | 153229 | 581267 | 7102226 | $617922 | 30d+ |
| KXNBA-26-OKC | Oklahoma City | 48c | 1.0c | 125868 | 34188 | 286711 | 271324 | 299058 | 280620 | 5169366 | $527165 | 30d+ |
| KXNBA-26-DEN | Denver | 7c | 1.0c | 132144 | 136517 | 161984 | 827194 | 677635 | 899349 | 4339470 | $421246 | 30d+ |
| KXNBA-26-BOS | Boston | 14c | 1.0c | 2977 | 303792 | 161964 | 574404 | 362594 | 577416 | 4046273 | $268441 | 30d+ |
| KXNBAWEST-26-SAS | San Antonio | 20c | 1.0c | 1517 | 10 | 14174 | 10569 | 46439 | 23220 | 1471474 | $70060 | 30d+ |
| KXNBAEAST-26-BOS | Boston | 41c | 2.0c | 62 | 89332 | 22599 | 118948 | 38524 | 118948 | 1301434 | $126315 | 30d+ |
| KXNBAEAST-26-DET | Detroit | 19c | 1.0c | 24614 | 28178 | 69521 | 58233 | 124699 | 70866 | 960261 | $46854 | 30d+ |
| KXNBAEAST-26-NYK | New York | 15c | 1.0c | 14227 | 3321 | 16277 | 14046 | 120202 | 14524 | 958760 | $68645 | 30d+ |
| KXNBAEAST-26-CLE | Cleveland | 22c | 3.0c | 2722 | 25628 | 11539 | 36880 | 34619 | 36979 | 862363 | $66027 | 30d+ |
| KXNBAWEST-26-OKC | Oklahoma City | 64c | 2.0c | 661 | 117901 | 7148 | 131245 | 77343 | 167840 | 753683 | $91370 | 30d+ |
| KXNBAWEST-26-DEN | Denver | 14c | 2.0c | 500 | 7720 | 19186 | 15723 | 193392 | 15951 | 593536 | $82023 | 30d+ |
| KXTEAMSINNBAF-26-OKCBOS | Oklahoma City vs Boston | 31c | 1.3c | 25 | 1123 | 577 | 3181 | 3433 | 3245 | 130645 | $26131 | 30d+ |
| KXNBADRAFT1-26-ADYB | AJ Dybantsa | 67c | 2.0c | 246 | 397 | 1371 | 1782 | 1371 | 2782 | 127397 | $50 | 30d+ |
| KXNBADRAFT1-26-DPET | Darryn Peterson | 24c | 2.0c | 134 | 198 | 1195 | 1574 | 1195 | 1574 | 108493 | $152 | 30d+ |
| KXNBADRAFT1-26-CBOO | Cameron Boozer | 9c | 1.0c | 147 | 259 | 2489 | 2417 | 5163 | 2417 | 90511 | $224 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNBA | NBA Championship | annual | 16 | 3 | $5,838,589 | 52,211,424 | 1.0c |
| KXNBAEAST | NBA Eastern Conference Championship | annual | 8 | 4 | $528,406 | 6,731,899 | 1.7c |
| KXNBAWEST | NBA Western Conference Championship | annual | 8 | 3 | $506,581 | 5,643,361 | 2.7c |
| KXTEAMSINNBAF | Teams in NBA Finals | custom | 64 | 4 | $122,476 | 597,854 | 3.4c |
| KXNBADRAFT1 | NBA Draft First Pick | annual | 8 | 2 | $601 | 406,963 | 2.0c |
| KXNBASERIESSCORE | NBA Series Exact Score | custom | 60 | 36 | $196,575 | 356,066 | 3.7c |
| KXNBA1STTEAM | All-NBA 1st Team | annual | 17 | 2 | $7,114 | 246,970 | 2.0c |
| KXNBASERIESSPREAD | NBA Series Game Spread | custom | 44 | 27 | $53,644 | 96,505 | 13.3c |
| KXNBA2NDTEAM | All-NBA 2nd Team | annual | 22 | 7 | $1,163 | 96,395 | 21.3c |
| KXTEAMSINNBAEF | Teams in NBA Eastern Conference Finals | custom | 16 | 4 | $5,176 | 46,335 | 2.3c |

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
