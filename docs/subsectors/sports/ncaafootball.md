# sports_ncaafootball

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **64** (64 with open markets)
- Open markets: **560** (237 contested)
- Total 24h volume: **$82,314**
- Total open interest: **2,736,591**
- Top-OI mean spread (median across series): **4.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **5.0c**
- Median TOB bid / ask size: **103 / 268** contracts
- Median depth within 5c of best bid / ask — **839 / 807** contracts
- Median depth within 10c of best bid / ask — **1496 / 1260** contracts
- Median depth within 5c of midpoint — bid: **491** / ask: **697** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **86**
- Mean informed-signal proxy: **-0.829** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.33c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1248 | 2.46 | -0.234 | 11.00 | 20.7 |
| 30d+ | 15893 | 1.87 | -0.510 | 7.00 | 79.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNCAAF-27-TEX | Texas | 10c | 1.0c | 1449 | 292 | 30504 | 38912 | 1056149 | 44389 | 124344 | $16588 | 30d+ |
| KXNCAAF-27-MIA | Miami (FL) | 6c | 1.0c | 24383 | 50865 | 441005 | 68692 | 441005 | 74237 | 101595 | $2346 | 30d+ |
| KXNCAAF-27-UGA | Georgia | 6c | 1.0c | 9731 | 715 | 953325 | 45382 | 953325 | 51213 | 99671 | $3353 | 30d+ |
| KXNCAAF-27-LSU | LSU | 6c | 1.0c | 9504 | 43423 | 113732 | 66397 | 113732 | 66497 | 97847 | $0 | 30d+ |
| KXNCAAF-27-ND | Notre Dame | 10c | 1.0c | 17606 | 34886 | 61478 | 77824 | 933706 | 77958 | 83154 | $4179 | 30d+ |
| KXNCAAF-27-OSU | Ohio St. | 10c | 1.0c | 6264 | 37238 | 19534 | 78187 | 1112831 | 78287 | 76026 | $516 | 30d+ |
| KXTRUMPBEARCASECOMBO-27DEC-26 | Yes | 18c | 5.0c | 488 | 125 | 1489 | 5904 | 13348 | 16762 | 68845 | $22 | 30d+ |
| KXNCAAF-27-TTU | Texas Tech | 6c | 1.0c | 10214 | 19426 | 81749 | 80430 | 81749 | 80973 | 66616 | $313 | 30d+ |
| KXPERUPRES2ND-26MAR25-2-RALI | Rafael López Aliaga | 16c | 2.0c | 49 | 310 | 1480 | 2283 | 4480 | 8083 | 61660 | $11535 | 30d+ |
| KXNYSECIRCUIT-27 | Before 2027 | 22c | 2.4c | 500 | 500 | 4474 | 2088 | 5622 | 10183 | 59668 | $129 | 30d+ |
| KXNCAAF-27-ORE | Oregon | 8c | 1.0c | 52071 | 53906 | 61868 | 102275 | 906819 | 103304 | 56843 | $528 | 30d+ |
| KXNCAAFUNDEFEATED-26-TTU | Texas Tech | 38c | 3.0c | 1 | 249 | 1646 | 1279 | 2171 | 2230 | 54957 | $124 | 30d+ |
| KXNCAAF-27-IND | Indiana | 10c | 1.0c | 444 | 72140 | 11336 | 100815 | 1084923 | 100965 | 45974 | $73 | 30d+ |
| KXNCAAFUNDEFEATED-26-IND | Indiana | 20c | 3.0c | 252 | 76 | 5311 | 1239 | 5463 | 2539 | 36899 | $0 | 30d+ |
| KXPERUPRES2ND-26MAR25-2-RPAL | Roberto Sánchez Palomino | 84c | 4.0c | 1120 | 541 | 4760 | 5489 | 8749 | 5489 | 35421 | $9384 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNCAAF | NCAAF Championship | annual | 50 | 4 | $41,469 | 1,624,068 | 1.0c |
| KXTRUMPBULLCASECOMBO | Trump's year: Bull (dream) case? | annual | 1 | 0 | $320 | 175,946 | nanc |
| KXPERUPRES2ND | Peru presidential election: first round  | one_off | 9 | 2 | $22,325 | 124,393 | 4.0c |
| KXNCAAFUNDEFEATED | Undefeated in College Football Regular S | annual | 27 | 8 | $555 | 123,295 | 2.7c |
| KXLUTNICKOUT | Howard Lutnick out as Commerce Secretary | one_off | 4 | 3 | $1,946 | 102,114 | 4.0c |
| KXTRUMPBEARCASECOMBO | Trump's year: Bear (nightmare) case? | annual | 1 | 1 | $22 | 68,845 | 5.0c |
| KXNYSECIRCUIT | NYSE circuit breaker day | custom | 1 | 1 | $129 | 59,668 | 2.4c |
| KXCOACHOUTNCAAFB | NCAAFB Coaches Out | custom | 14 | 2 | $0 | 37,121 | 7.5c |
| KXNCAAFB12 | Big 12 Champion | annual | 16 | 2 | $742 | 36,794 | 2.5c |
| KXEOTRUMPTERM | EOs in Trump's second term | one_off | 12 | 4 | $4,469 | 30,838 | 1.6c |

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
