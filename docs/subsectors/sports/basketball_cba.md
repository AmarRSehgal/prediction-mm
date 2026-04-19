# sports_basketball_cba

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **20** (18 contested)
- Total 24h volume: **$9,976**
- Total open interest: **10,641**
- Top-OI mean spread (median across series): **1.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **20**
- Median spread: **4.0c**
- Median TOB bid / ask size: **50 / 59** contracts
- Median depth within 5c of best bid / ask — **200 / 1393** contracts
- Median depth within 10c of best bid / ask — **1466 / 5059** contracts
- Median depth within 5c of midpoint — bid: **150** / ask: **707** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **21**
- Mean informed-signal proxy: **0.079** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.11c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 414 | 1.26 | -0.174 | 6.00 | 47.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCBAGAME-26APR190735BRFZHE-ZHE | Zhejiang Lions | 64c | 1.0c | 109 | 1178 | 3990 | 5768 | 5641 | 7001 | 4672 | $4934 | 7-30d |
| KXCBAGAME-26APR190735BRFZHE-BRF | Beijing Royal Fighters | 36c | 3.0c | 155 | 1109 | 4817 | 4448 | 6870 | 5859 | 2530 | $2096 | 7-30d |
| KXCBAGAME-26APR200735SBWJIA-SBW | Sichuan Blue Whales | 6c | 1.0c | 77 | 514 | 22518 | 10677 | 22518 | 10677 | 1673 | $1098 | 7-30d |
| KXCBAGAME-26APR190735SHALEO-LEO | Shenzhen Leopards | 68c | 1.0c | 50 | 1161 | 2303 | 4265 | 5416 | 5002 | 1218 | $1218 | 7-30d |
| KXCBAGAME-26APR190735BEDQIN-BED | Beijing Ducks | 66c | 1.0c | 40 | 50 | 5424 | 3197 | 5434 | 6889 | 916 | $1108 | 7-30d |
| KXCBAGAME-26APR190735BEDQIN-QIN | Qingdao Eagles | 32c | 1.0c | 60 | 454 | 4346 | 5672 | 4346 | 6950 | 841 | $1346 | 7-30d |
| KXCBAGAME-26APR200735SBWJIA-JIA | Jiangsu Dragons | 94c | 2.0c | 15 | 126 | 15 | 12449 | 15 | 12449 | 736 | $130 | 7-30d |
| KXCBAGAME-26APR190800NANXIN-XIN | Xinjiang Flying Tigers | 64c | 1.0c | 20 | 52 | 4360 | 3680 | 6078 | 6451 | 277 | $277 | 7-30d |
| KXCBAGAME-26APR190800NANXIN-NAN | Nanjing Monkey Kings | 36c | 1.0c | 10 | 1795 | 3431 | 5831 | 4820 | 6756 | 257 | $257 | 7-30d |
| KXCBAGAME-26APR190735SHALEO-SHA | Shandong Kirin | 32c | 1.0c | 1255 | 8 | 5121 | 2261 | 5785 | 5353 | 106 | $116 | 7-30d |
| KXCBAGAME-26APR200735JILNIN-NIN | Ningbo Rockets | 82c | 11.0c | 50 | 201 | 50 | 524 | 50 | 5116 | 90 | $170 | 7-30d |
| KXCBAGAME-26APR200735LIASHAD-LIA | Liaoning Flying Leopards | 16c | 5.0c | 100 | 50 | 200 | 50 | 1500 | 50 | 89 | $23 | 7-30d |
| KXCBAGAME-26APR200735JILNIN-JIL | Jilin Northeast Tigers | 18c | 8.0c | 100 | 149 | 200 | 199 | 1431 | 199 | 80 | $80 | 7-30d |
| KXCBAGAME-26APR200735LIASHAD-SHAD | Shanghai Sharks | 84c | 5.0c | 50 | 8 | 50 | 427 | 50 | 1702 | 34 | $18 | 7-30d |
| KXCBAGAME-26APR200735TIAZGB-ZGB | Zhejiang Golden Bulls | 78c | 5.0c | 50 | 5 | 50 | 18 | 50 | 445 | 16 | $16 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCBAGAME | Chinese Basketball Association Game  | one_off | 20 | 18 | $9,976 | 10,641 | 1.7c |

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
