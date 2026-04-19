# sports_ncaafootball

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **64** (64 with open markets)
- Open markets: **560** (237 contested)
- Total 24h volume: **$83,730**
- Total open interest: **2,736,085**
- Top-OI mean spread (median across series): **4.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **5.0c**
- Median TOB bid / ask size: **100 / 251** contracts
- Median cumulative depth within 5c of mid — bid: **500** / ask: **692** contracts
- Median cumulative depth within 10c of mid — bid: **1002** / ask: **1049** contracts
- Mean trades per market (last 3000): **107**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2082 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 19300 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNCAAF-27-TEX | Texas | 10c | 1.0c | 1433 | 283 | 24987 | 38903 | 124344 | $16593 | 30d+ |
| KXNCAAF-27-MIA | Miami (FL) | 6c | 1.0c | 24383 | 50896 | 48846 | 68723 | 101595 | $2346 | 30d+ |
| KXNCAAF-27-UGA | Georgia | 6c | 1.0c | 9731 | 715 | 27853 | 45382 | 99671 | $3353 | 30d+ |
| KXNCAAF-27-LSU | LSU | 6c | 1.0c | 9504 | 43423 | 54922 | 66397 | 97847 | $0 | 30d+ |
| KXNCAAF-27-ND | Notre Dame | 10c | 1.0c | 17606 | 34886 | 61366 | 77824 | 83154 | $4222 | 30d+ |
| KXNCAAF-27-OSU | Ohio St. | 10c | 1.0c | 6264 | 37238 | 18534 | 78187 | 76026 | $159 | 30d+ |
| KXTRUMPBEARCASECOMBO-27DEC-26 | Yes | 18c | 5.0c | 488 | 125 | 1489 | 1166 | 68845 | $22 | 30d+ |
| KXNCAAF-27-TTU | Texas Tech | 6c | 1.0c | 10214 | 19426 | 81713 | 80430 | 66616 | $313 | 30d+ |
| KXPERUPRES2ND-26MAR25-2-RALI | Rafael López Aliaga | 16c | 3.0c | 44 | 878 | 900 | 3399 | 61660 | $11971 | 30d+ |
| KXNYSECIRCUIT-27 | Before 2027 | 22c | 2.6c | 500 | 500 | 3464 | 1507 | 59658 | $119 | 30d+ |
| KXNCAAF-27-ORE | Oregon | 8c | 1.0c | 52071 | 53906 | 61868 | 102275 | 56843 | $528 | 30d+ |
| KXNCAAFUNDEFEATED-26-TTU | Texas Tech | 38c | 3.0c | 1 | 249 | 1029 | 1164 | 54957 | $124 | 30d+ |
| KXLUTNICKOUT-26MAY01 | :: | 3c | 3.0c | 50 | 8 | 8593 | 668 | 54605 | $278 | 7-30d |
| KXNCAAF-27-IND | Indiana | 10c | 1.0c | 444 | 72140 | 11336 | 100815 | 45974 | $73 | 30d+ |
| KXNCAAFUNDEFEATED-26-IND | Indiana | 20c | 3.0c | 252 | 76 | 5314 | 638 | 36899 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNCAAF | NCAAF Championship | annual | 50 | 4 | $42,472 | 1,624,631 | 1.0c |
| KXTRUMPBULLCASECOMBO | Trump's year: Bull (dream) case? | annual | 1 | 0 | $326 | 175,946 | nanc |
| KXPERUPRES2ND | Peru presidential election: first round  | one_off | 9 | 2 | $24,084 | 124,276 | 2.0c |
| KXNCAAFUNDEFEATED | Undefeated in College Football Regular S | annual | 27 | 8 | $478 | 123,303 | 3.0c |
| KXLUTNICKOUT | Howard Lutnick out as Commerce Secretary | one_off | 4 | 3 | $868 | 102,629 | 3.3c |
| KXTRUMPBEARCASECOMBO | Trump's year: Bear (nightmare) case? | annual | 1 | 1 | $22 | 68,845 | 5.0c |
| KXNYSECIRCUIT | NYSE circuit breaker day | custom | 1 | 1 | $40 | 59,579 | 2.8c |
| KXCOACHOUTNCAAFB | NCAAFB Coaches Out | custom | 14 | 2 | $0 | 37,121 | 7.5c |
| KXNCAAFB12 | Big 12 Champion | annual | 16 | 2 | $742 | 36,794 | 2.5c |
| KXEOTRUMPTERM | EOs in Trump's second term | one_off | 12 | 4 | $4,370 | 30,838 | 1.6c |

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
