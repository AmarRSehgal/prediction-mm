# world_mideast

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **18** (18 with open markets)
- Open markets: **88** (42 contested)
- Total 24h volume: **$12,630**
- Total open interest: **1,707,479**
- Top-OI mean spread (median across series): **4.4 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **51**
- Median spread: **6.0c**
- Median TOB bid / ask size: **500 / 201** contracts
- Median cumulative depth within 5c of mid — bid: **140** / ask: **220** contracts
- Median cumulative depth within 10c of mid — bid: **720** / ask: **539** contracts
- Mean trades per market (last 3000): **320**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 16322 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPAHLAVIHEAD-27JAN-RPAH | Reza Pahlavi | 12c | 1.0c | 2145 | 270 | 5712 | 4547 | 498382 | $1356 | 30d+ |
| KXPAHLAVIVISITA-27JAN01 | Yes | 15c | 1.0c | 5625 | 530 | 10230 | 12086 | 496350 | $3230 | 30d+ |
| KXRECOGPERSONIRAN-26 | Before 2027 | 13c | 2.0c | 18007 | 1083 | 19323 | 5224 | 249704 | $262 | 30d+ |
| KXIRANEMBASSY-27 | Before 2027 | 17c | 3.0c | 511 | 115 | 2215 | 765 | 45647 | $1003 | 30d+ |
| KXWCIRAN-26 | Yes | 74c | 3.0c | 14 | 557 | 275 | 560 | 19536 | $338 | 30d+ |
| KXELECTIRAN-27JAN01 | Before Jan 1, 2027 | 12c | 3.0c | 37 | 21 | 542 | 26 | 15087 | $279 | 30d+ |
| KXNEXTISRAELPM-45JAN01-NBEN | Naftali Bennett | 31c | 5.0c | 537 | 51 | 1037 | 82 | 6765 | $14 | 30d+ |
| KXISRAELKNESSET-26-LIK | :: | 72c | 1.0c | 5169 | 4990 | 5169 | 4990 | 5003 | $0 | 30d+ |
| KXRECOGPALESTINE-27-JAP | Japan | 13c | 7.1c | 500 | 500 | 500 | 1021 | 4758 | $0 | 30d+ |
| KXRECOGPALESTINE-27-ITA | Italy | 16c | 5.0c | 27 | 509 | 27 | 509 | 4114 | $14 | 30d+ |
| KXNEXTISRAELPM-45JAN01-IKAT | :: | 10c | 0.1c | 500 | 201 | 500 | 201 | 4025 | $40 | 30d+ |
| KXRECOGPALESTINE-27-GRE | Greece | 11c | 2.1c | 500 | 20 | 560 | 220 | 3665 | $0 | 30d+ |
| KXRECOGPALESTINE-27-SWI | Switzerland | 13c | 7.3c | 500 | 500 | 720 | 500 | 3648 | $0 | 30d+ |
| KXRECOGPALESTINE-27-AUS | Austria | 8c | 6.1c | 500 | 1 | 500 | 101 | 3507 | $0 | 30d+ |
| KXKANYEISRAEL-27JAN01 | Yes | 16c | 5.0c | 503 | 5 | 503 | 43 | 3348 | $36 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPAHLAVIHEAD | Will Pahlavi lead Iran? | one_off | 1 | 1 | $1,318 | 498,382 | 1.0c |
| KXPAHLAVIVISITA | Will Reza Pahlavi enter Iran before Sept | one_off | 1 | 1 | $3,560 | 496,340 | 1.0c |
| KXRECOGPERSONIRAN | Recognize Reza Pahlavi | custom | 1 | 1 | $168 | 249,610 | 2.0c |
| KXVISITIRAN | Who will visit Iran? | one_off | 8 | 0 | $2,901 | 182,099 | nanc |
| KXIRANDEMOCRACY | Will Iran become a democracy in 2026? | one_off | 1 | 0 | $1,263 | 102,185 | nanc |
| KXIRANEMBASSY | Will the US reopen its embassy in Iran? | one_off | 1 | 1 | $1,021 | 45,647 | 3.0c |
| KXRECOGPALESTINE | Palestine recognition | custom | 13 | 8 | $86 | 32,830 | 4.4c |
| KXELECTIRAN | Will Iran hold a presidential election? | one_off | 2 | 1 | $1,199 | 30,180 | 4.0c |
| KXNEXTISRAELPM | Next Prime Minister of Israel | one_off | 12 | 2 | $106 | 27,895 | 5.5c |
| KXWCIRAN | Iran World Cup | custom | 1 | 1 | $168 | 19,536 | 3.0c |

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
