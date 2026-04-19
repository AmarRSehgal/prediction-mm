# eco_macro_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **27** (27 with open markets)
- Open markets: **723** (284 contested)
- Total 24h volume: **$26,944**
- Total open interest: **1,169,188**
- Top-OI mean spread (median across series): **7.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **5.5c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median cumulative depth within 5c of mid — bid: **260** / ask: **260** contracts
- Median cumulative depth within 10c of mid — bid: **522** / ask: **346** contracts
- Mean trades per market (last 3000): **104**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 28 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 160 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 4628 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 15964 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCAWEALTHTAX-26 | In 2026 | 36c | 5.0c | 42 | 13 | 1542 | 67 | 122855 | $487 | 30d+ |
| KXLCPIMAXYOY-27-P4.5 | At least 4.5% | 29c | 6.0c | 10 | 19 | 28 | 1019 | 40738 | $538 | 30d+ |
| KXLCPIMAXYOY-27-P4 | At least 4% | 45c | 1.0c | 3 | 59 | 1273 | 1059 | 38094 | $197 | 30d+ |
| KXLCPIMAXYOY-27-P3.5 | At least 3.5% | 95c | 2.9c | 1000 | 479 | 3152 | 2030 | 34760 | $0 | 30d+ |
| KXECONSTATCPICORE-26MAY-T-0.2 | Exactly -0.2% | 11c | 6.0c | 20 | 14 | 20 | 411 | 30368 | $0 | 30d+ |
| KXCPIYOY-26APR-T3.7 | 3.7 | 21c | 6.0c | 1000 | 10 | 2200 | 1010 | 26567 | $187 | 7-30d |
| KXECONSTATCPIYOY-26MAY-T3.3 | Exactly 3.3% | 16c | 5.0c | 222 | 209 | 5222 | 346 | 24425 | $149 | 30d+ |
| KXMUSKWEALTH-27-900 | More than $900 Billion | 84c | 5.0c | 41 | 500 | 641 | 654 | 24378 | $0 | 30d+ |
| KXLCPIMAXYOY-27-P5 | At least 5% | 20c | 4.9c | 17 | 329 | 1017 | 2338 | 23376 | $1400 | 30d+ |
| KXCPIYOY-26APR-T3.6 | 3.6 | 37c | 2.0c | 1000 | 5 | 2000 | 4782 | 20931 | $342 | 7-30d |
| KXMUSKWEALTH-27-1000 | More than $1 trillion | 80c | 1.0c | 54 | 510 | 554 | 510 | 15687 | $0 | 30d+ |
| KXJPMOMINF-26APR17-T-0.1 | Above -0.1% | 31c | 60.0c | 10 | 26 | 0 | 0 | 12243 | $0 | 3-7d |
| KXCPIYOY-26APR-T3.5 | 3.5 | 70c | 1.0c | 1330 | 75 | 2597 | 4548 | 10973 | $155 | 7-30d |
| KXUSFUND-27 | Before 2027 | 24c | 3.0c | 295 | 1185 | 443 | 1359 | 10783 | $0 | 30d+ |
| KXCPIYOY-26APR-T3.8 | 3.8 | 12c | 3.0c | 74 | 1017 | 74 | 1017 | 10557 | $400 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXECONSTATCPIYOY | year over year inflation | custom | 134 | 28 | $6,027 | 410,266 | 3.0c |
| KXLCPIMAXYOY | Inflation surge this year | one_off | 7 | 3 | $2,274 | 149,774 | 3.9c |
| KXCPIYOY | Inflation | monthly | 56 | 24 | $2,292 | 141,893 | 3.3c |
| KXCAWEALTHTAX | Will the California billionaire wealth t | one_off | 1 | 1 | $350 | 123,030 | 4.0c |
| KXMUSKWEALTH | Musk wealth | custom | 6 | 6 | $24 | 68,224 | 2.7c |
| KXECONSTATCPICORE | month over month core inflation | custom | 69 | 27 | $0 | 51,352 | 4.3c |
| KXJPMOMINF | Japan inflation MoM in [month] | monthly | 9 | 5 | $25 | 35,397 | 48.0c |
| KXECONSTATCPI | month over month inflation | custom | 76 | 35 | $486 | 31,909 | 3.0c |
| KXCPICOREYOY | Core inflation | monthly | 30 | 9 | $864 | 24,581 | 5.0c |
| KXPCECORE | US Core PCE inflation | monthly | 45 | 25 | $2,778 | 22,095 | 7.3c |

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
