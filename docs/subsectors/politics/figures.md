# pol_figures

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **63** (63 with open markets)
- Open markets: **439** (318 contested)
- Total 24h volume: **$407,153**
- Total open interest: **8,185,570**
- Top-OI mean spread (median across series): **4.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **3.0c**
- Median TOB bid / ask size: **29 / 74** contracts
- Median cumulative depth within 5c of mid — bid: **500** / ask: **493** contracts
- Median cumulative depth within 10c of mid — bid: **911** / ask: **782** contracts
- Mean trades per market (last 3000): **484**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 6-12h | 15 | 0.00 | 0.000 | 0.00 | 0.0 |
| 12-24h | 219 | 0.00 | 0.000 | 0.00 | 0.0 |
| 1-3d | 3737 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 4837 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 13689 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 74246 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXTRUMPOUT27-27-DJT | Before 2027 | 16c | 1.0c | 1798 | 49 | 38033 | 70668 | 2196394 | $12631 | 30d+ |
| KXTRUMPOUT27-27-26AUG01 | Before August 1, 2026 | 7c | 1.7c | 350 | 690 | 92385 | 121088 | 1667120 | $43801 | 30d+ |
| KXTRUMPOUT27-27-28 | Before 2028 | 31c | 1.0c | 1628 | 4981 | 16790 | 25533 | 339447 | $2205 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-PHEG | :: Secretary of Defense | 48c | 3.0c | 1287 | 94 | 2071 | 4204 | 248763 | $6073 | 30d+ |
| KX14AMENDCASE-26-AUG | Before August 2026 | 10c | 1.1c | 500 | 1066 | 10452 | 5807 | 231021 | $2215 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-KPAT | :: Director of the FBI | 76c | 1.0c | 147 | 1 | 1082 | 2370 | 206770 | $31640 | 30d+ |
| KXTRUMPOUT27-27-JAN2029 | Before January 20, 2029 | 40c | 1.0c | 68 | 5 | 10110 | 18332 | 206640 | $1367 | 30d+ |
| KXTRUMPREMOVE | Before his term ends | 28c | 2.0c | 118 | 9 | 34935 | 4881 | 154311 | $2245 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-TGAB | :: Director of National Intelligence | 52c | 2.0c | 1 | 15 | 1724 | 2021 | 97285 | $816 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-KLEA | :: White House Press Secretary | 47c | 2.0c | 257 | 203 | 1305 | 3780 | 91361 | $1561 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-HLUT | :: Secretary of Commerce | 52c | 2.0c | 514 | 263 | 3190 | 1165 | 81881 | $2444 | 30d+ |
| KXTRUMPRESIGN | Before his term ends | 24c | 2.0c | 15 | 2020 | 64 | 5423 | 59061 | $32 | 30d+ |
| KXTRUMPCOUNTRIES-27JAN01-CHI | China | 90c | 1.0c | 50 | 64 | 2512 | 1936 | 53588 | $193 | 30d+ |
| KXTRUMPIRAN-27JAN01 | Before Jan 1, 2027 | 12c | 1.0c | 1000 | 1010 | 5569 | 6646 | 51069 | $1736 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-LCHA | :: Secretary of Labor | 84c | 1.0c | 2 | 505 | 390 | 1717 | 50549 | $546 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTRUMPOUT27 | Trump out as President? | one_off | 4 | 3 | $56,501 | 4,406,102 | 1.3c |
| KXTRUMPADMINLEAVE | Who will leave the Trump administration | annual | 33 | 33 | $53,983 | 1,037,672 | 2.7c |
| KXTRUMPSAY | What will trump say | one_off | 22 | 6 | $210,148 | 465,150 | 5.3c |
| KXTRUMPIRAN | Will Trump visit Iran? | one_off | 3 | 1 | $6,948 | 266,602 | 1.0c |
| KX14AMENDCASE | Trump birthright citizenship case | custom | 1 | 1 | $2,202 | 231,044 | 1.0c |
| KXTRUMPCOUNTRIES | What countries will Trump visit this yea | annual | 24 | 21 | $3,225 | 173,819 | 4.0c |
| KXTRUMPREMOVE | Trump removed | custom | 1 | 1 | $2,220 | 154,257 | 3.0c |
| KXTRUMPPARDONS | Who will Trump pardon? | one_off | 49 | 48 | $1,645 | 134,253 | 2.7c |
| KXTRUMPCHINA | When will Trump visit China? | one_off | 6 | 3 | $13,100 | 129,183 | 14.0c |
| KXTRUMPSAYMONTH | Trump Monthly | one_off | 11 | 9 | $12,492 | 97,213 | 3.3c |

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
