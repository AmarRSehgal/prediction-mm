# world_mideast

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **18** (18 with open markets)
- Open markets: **88** (42 contested)
- Total 24h volume: **$13,356**
- Total open interest: **1,707,403**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **51**
- Median spread: **6.0c**
- Median TOB bid / ask size: **400 / 200** contracts
- Median depth within 5c of best bid / ask — **861 / 720** contracts
- Median depth within 10c of best bid / ask — **5443 / 1000** contracts
- Median depth within 5c of midpoint — bid: **141** / ask: **220** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **165**
- Mean informed-signal proxy: **-0.683** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.22c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 8406 | 1.48 | -0.458 | 6.00 | 70.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPAHLAVIHEAD-27JAN-RPAH | Reza Pahlavi | 12c | 1.0c | 100 | 270 | 9666 | 4547 | 53478 | 22834 | 498382 | $1206 | 30d+ |
| KXPAHLAVIVISITA-27JAN01 | Yes | 15c | 1.0c | 5625 | 534 | 30230 | 17759 | 45951 | 34977 | 496011 | $3696 | 30d+ |
| KXRECOGPERSONIRAN-26 | Before 2027 | 13c | 2.0c | 18007 | 1100 | 19323 | 5980 | 19794 | 11448 | 249704 | $262 | 30d+ |
| KXIRANEMBASSY-27 | Before 2027 | 17c | 3.0c | 511 | 115 | 2481 | 987 | 3847 | 1356 | 45647 | $1001 | 30d+ |
| KXWCIRAN-26 | Yes | 74c | 3.0c | 14 | 557 | 275 | 830 | 275 | 1383 | 19536 | $338 | 30d+ |
| KXELECTIRAN-27JAN01 | Before Jan 1, 2027 | 12c | 1.0c | 5 | 16 | 542 | 21 | 10820 | 776 | 15087 | $279 | 30d+ |
| KXNEXTISRAELPM-45JAN01-NBEN | Naftali Bennett | 31c | 5.0c | 537 | 51 | 1037 | 582 | 1037 | 596 | 6765 | $14 | 30d+ |
| KXISRAELKNESSET-26-LIK | :: | 72c | 1.0c | 5443 | 4835 | 5443 | 5411 | 5443 | 5911 | 5003 | $0 | 30d+ |
| KXRECOGPALESTINE-27-JAP | Japan | 13c | 7.1c | 500 | 500 | 1000 | 2046 | 18717 | 2046 | 4758 | $0 | 30d+ |
| KXRECOGPALESTINE-27-ITA | Italy | 16c | 5.0c | 27 | 509 | 619 | 509 | 669 | 509 | 4114 | $14 | 30d+ |
| KXNEXTISRAELPM-45JAN01-IKAT | :: | 10c | 0.1c | 500 | 201 | 500 | 201 | 13416 | 1812 | 4025 | $40 | 30d+ |
| KXRECOGPALESTINE-27-GRE | Greece | 11c | 2.1c | 500 | 20 | 551 | 720 | 24501 | 720 | 3665 | $0 | 30d+ |
| KXRECOGPALESTINE-27-SWI | Switzerland | 13c | 7.3c | 500 | 500 | 720 | 1389 | 20802 | 1389 | 3648 | $0 | 30d+ |
| KXRECOGPALESTINE-27-AUS | Austria | 8c | 6.1c | 500 | 1 | 13566 | 601 | 13566 | 601 | 3507 | $0 | 30d+ |
| KXKANYEISRAEL-27JAN01 | Yes | 16c | 5.0c | 503 | 5 | 503 | 803 | 1003 | 803 | 3348 | $36 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPAHLAVIHEAD | Will Pahlavi lead Iran? | one_off | 1 | 1 | $1,206 | 498,382 | 1.0c |
| KXPAHLAVIVISITA | Will Reza Pahlavi enter Iran before Sept | one_off | 1 | 1 | $3,582 | 496,011 | 1.0c |
| KXRECOGPERSONIRAN | Recognize Reza Pahlavi | custom | 1 | 1 | $262 | 249,704 | 2.0c |
| KXVISITIRAN | Who will visit Iran? | one_off | 8 | 0 | $3,234 | 182,225 | nanc |
| KXIRANDEMOCRACY | Will Iran become a democracy in 2026? | one_off | 1 | 0 | $1,369 | 102,185 | nanc |
| KXIRANEMBASSY | Will the US reopen its embassy in Iran? | one_off | 1 | 1 | $1,001 | 45,647 | 3.0c |
| KXRECOGPALESTINE | Palestine recognition | custom | 13 | 8 | $86 | 32,830 | 4.7c |
| KXELECTIRAN | Will Iran hold a presidential election? | one_off | 2 | 1 | $1,190 | 30,180 | 2.0c |
| KXNEXTISRAELPM | Next Prime Minister of Israel | one_off | 12 | 2 | $106 | 27,895 | 5.5c |
| KXWCIRAN | Iran World Cup | custom | 1 | 1 | $338 | 19,536 | 3.0c |

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
