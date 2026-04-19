# world_china

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **30** (19 contested)
- Total 24h volume: **$844**
- Total open interest: **251,529**
- Top-OI mean spread (median across series): **4.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **24**
- Median spread: **6.0c**
- Median TOB bid / ask size: **375 / 250** contracts
- Median cumulative depth within 5c of mid — bid: **502** / ask: **500** contracts
- Median cumulative depth within 10c of mid — bid: **845** / ask: **508** contracts
- Mean trades per market (last 3000): **169**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 4055 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXTAIWANLVL4-27JAN01 | Before Jan 1, 2027 | 18c | 5.0c | 527 | 619 | 1327 | 1730 | 79628 | $16 | 30d+ |
| KXBESTLLMCHINA-27 | Before 2027 | 18c | 1.0c | 205 | 117 | 2114 | 2632 | 32737 | $129 | 30d+ |
| KXTAIWANLVL4-28JAN01 | Before Jan 1, 2028 | 29c | 3.0c | 507 | 27 | 1307 | 70 | 10207 | $0 | 30d+ |
| KXXITAIWAN-27JAN01 | Before 2027 | 8c | 2.9c | 98 | 3327 | 7752 | 3875 | 10173 | $235 | 30d+ |
| KXTARIFFRATEPRC-26JUL01-14 | Between 10% and 19.99% | 61c | 4.0c | 991 | 100 | 2126 | 300 | 7342 | $53 | 30d+ |
| KXTAIWANLVL4-30JAN01 | Before Jan 1, 2030 | 49c | 4.0c | 18 | 21 | 822 | 826 | 6552 | $7 | 30d+ |
| KXTAIWANLVL4-29JAN01 | Before Jan 1, 2029 | 42c | 3.0c | 818 | 17 | 818 | 46 | 5181 | $0 | 30d+ |
| KXTARIFFRATEPRC-26JUL01-5 | Below 10% | 14c | 5.0c | 32 | 392 | 232 | 592 | 5136 | $426 | 30d+ |
| KXTARIFFRATEPRC-26JUL01-24 | Between 20% and 29.99% | 15c | 3.0c | 62 | 150 | 262 | 650 | 4344 | $11 | 30d+ |
| KXTARIFFRATEPRC-26JUL01-34 | Between 30% and 39.99% | 6c | 1.0c | 754 | 35 | 2254 | 235 | 3952 | $0 | 30d+ |
| KXXITAIWAN-28JAN01 | Before 2028 | 24c | 5.0c | 695 | 9 | 695 | 9 | 3113 | $0 | 30d+ |
| KXXITAIWAN-29JAN01 | Before 2029 | 45c | 7.0c | 32 | 500 | 532 | 500 | 2753 | $66 | 30d+ |
| KXPRESTAIWAN-28-WLAI | :: DPP | 68c | 7.0c | 4 | 500 | 504 | 500 | 2325 | $0 | 30d+ |
| KXXITAIWAN-30JAN01 | Before 2030 | 53c | 8.0c | 500 | 500 | 500 | 500 | 1640 | $200 | 30d+ |
| KXLAIOUT-LCHI-27JUL01 | Before July 1, 2027 | 13c | 7.6c | 500 | 11 | 500 | 511 | 1173 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTAIWANLVL4 | Will Taiwan be issued a Level 4 travel w | one_off | 5 | 4 | $98 | 164,500 | 4.0c |
| KXBESTLLMCHINA | Chinese LLM best | custom | 1 | 1 | $126 | 32,735 | 1.0c |
| KXTARIFFRATEPRC | Tariff rate China | custom | 7 | 3 | $118 | 25,262 | 3.8c |
| KXXITAIWAN | Will Xi Jinping visit Taiwan? | one_off | 4 | 3 | $501 | 17,679 | 6.7c |
| KXLAIOUT | Wiliam Lai out as President of Taiwan | one_off | 4 | 2 | $0 | 4,362 | 4.3c |
| KXPRESTAIWAN | Taiwan presidential election | custom | 3 | 1 | $0 | 3,416 | 7.0c |
| KXF1CHINA | F1 team from China | custom | 1 | 0 | $0 | 3,051 | nanc |
| KXCNIMPORT | US imports of goods from China | one_off | 5 | 5 | $0 | 524 | 8.7c |

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
