# pol_figures

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **63** (63 with open markets)
- Open markets: **439** (322 contested)
- Total 24h volume: **$414,196**
- Total open interest: **8,227,755**
- Top-OI mean spread (median across series): **3.4 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **3.9c**
- Median TOB bid / ask size: **30 / 98** contracts
- Median depth within 5c of best bid / ask — **756 / 739** contracts
- Median depth within 10c of best bid / ask — **1388 / 819** contracts
- Median depth within 5c of midpoint — bid: **468** / ask: **518** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **343**
- Mean informed-signal proxy: **-0.599** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.89c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 4092 | 2.62 | -0.773 | 11.00 | 16.8 |
| 3-7d | 4276 | 3.11 | -0.850 | 14.00 | 13.2 |
| 7-30d | 13323 | 2.21 | -0.639 | 10.00 | 21.8 |
| 30d+ | 46991 | 1.38 | -0.447 | 5.00 | 58.6 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXTRUMPOUT27-27-DJT | Before 2027 | 16c | 2.0c | 3062 | 17076 | 39698 | 71205 | 40034 | 71808 | 2196344 | $14048 | 30d+ |
| KXTRUMPOUT27-27-26AUG01 | Before August 1, 2026 | 7c | 1.2c | 806 | 25 | 93098 | 123398 | 113449 | 124400 | 1667736 | $44318 | 30d+ |
| KXTRUMPOUT27-27-28 | Before 2028 | 31c | 1.0c | 1627 | 4906 | 21950 | 25458 | 21972 | 25465 | 339596 | $2354 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-PHEG | :: Secretary of Defense | 48c | 1.0c | 881 | 99 | 5866 | 5160 | 9753 | 6428 | 250168 | $8046 | 30d+ |
| KX14AMENDCASE-26-AUG | Before August 2026 | 10c | 1.1c | 500 | 1066 | 21580 | 5807 | 236190 | 11447 | 231022 | $2207 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-KPAT | :: Director of the FBI | 76c | 2.0c | 4 | 688 | 1728 | 3678 | 4974 | 5081 | 208357 | $29797 | 30d+ |
| KXTRUMPOUT27-27-JAN2029 | Before January 20, 2029 | 40c | 1.0c | 630 | 120 | 10649 | 18465 | 11085 | 18465 | 206635 | $1371 | 30d+ |
| KXTRUMPREMOVE | Before his term ends | 28c | 2.0c | 5 | 141 | 35927 | 7102 | 57730 | 7189 | 155001 | $2924 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-TGAB | :: Director of National Intelligence | 50c | 1.0c | 1381 | 2 | 3702 | 2011 | 4218 | 2137 | 97233 | $832 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-KLEA | :: White House Press Secretary | 47c | 2.0c | 257 | 203 | 1305 | 3780 | 4201 | 5235 | 91367 | $1487 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-HLUT | :: Secretary of Commerce | 52c | 2.0c | 514 | 263 | 3191 | 1682 | 5082 | 3415 | 81881 | $2444 | 30d+ |
| KXTRUMPRESIGN | Before his term ends | 24c | 2.0c | 23 | 2018 | 2686 | 5567 | 14199 | 6231 | 59061 | $32 | 30d+ |
| KXTRUMPCOUNTRIES-27JAN01-CHI | China | 90c | 1.0c | 50 | 64 | 3012 | 2949 | 4822 | 36925 | 53588 | $193 | 30d+ |
| KXTRUMPIRAN-27JAN01 | Before Jan 1, 2027 | 12c | 2.0c | 1005 | 2199 | 5768 | 5771 | 19384 | 9273 | 51069 | $1601 | 30d+ |
| KXTRUMPADMINLEAVE-26DEC31-LCHA | :: Secretary of Labor | 84c | 1.0c | 20 | 1000 | 603 | 2612 | 3367 | 2683 | 50553 | $417 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTRUMPOUT27 | Trump out as President? | one_off | 4 | 3 | $62,092 | 4,410,312 | 1.3c |
| KXTRUMPADMINLEAVE | Who will leave the Trump administration | annual | 33 | 33 | $49,868 | 1,041,853 | 1.7c |
| KXTRUMPSAY | What will trump say | one_off | 22 | 10 | $212,158 | 491,880 | 6.7c |
| KXTRUMPIRAN | Will Trump visit Iran? | one_off | 3 | 1 | $5,936 | 266,685 | 1.0c |
| KX14AMENDCASE | Trump birthright citizenship case | custom | 1 | 1 | $2,207 | 231,022 | 1.1c |
| KXTRUMPCOUNTRIES | What countries will Trump visit this yea | annual | 24 | 21 | $3,016 | 173,502 | 4.0c |
| KXTRUMPREMOVE | Trump removed | custom | 1 | 1 | $2,917 | 155,001 | 2.0c |
| KXTRUMPPARDONS | Who will Trump pardon? | one_off | 49 | 48 | $1,664 | 134,272 | 2.7c |
| KXTRUMPCHINA | When will Trump visit China? | one_off | 6 | 3 | $12,137 | 129,318 | 2.3c |
| KXTRUMPSAYMONTH | Trump Monthly | one_off | 11 | 9 | $15,347 | 100,421 | 3.3c |

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
