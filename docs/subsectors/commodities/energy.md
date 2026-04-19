# comm_energy

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **22** (22 with open markets)
- Open markets: **436** (268 contested)
- Total 24h volume: **$391,654**
- Total open interest: **1,838,037**
- Top-OI mean spread (median across series): **10.3 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **10.0c**
- Median TOB bid / ask size: **33 / 82** contracts
- Median cumulative depth within 5c of mid — bid: **3** / ask: **6** contracts
- Median cumulative depth within 10c of mid — bid: **102** / ask: **177** contracts
- Mean trades per market (last 3000): **241**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 8721 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 3288 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 4809 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 31301 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXWTIMAX-26DEC31-T180 | 180.01 or above | 16c | 4.5c | 453 | 188 | 5402 | 2110 | 228228 | $2220 | 30d+ |
| KXWTIMAX-26DEC31-T150 | 150.01 or above | 30c | 3.1c | 6 | 3 | 11 | 2825 | 179250 | $4809 | 30d+ |
| KXWTIMAX-26DEC31-T160 | 160.01 or above | 24c | 1.9c | 46 | 6 | 1097 | 1281 | 154207 | $1556 | 30d+ |
| KXWTIMAX-26DEC31-T140 | 140.01 or above | 32c | 3.0c | 11 | 7 | 56 | 119 | 129733 | $2474 | 30d+ |
| KXWTIMAX-26DEC31-T115 | 115.01 or above | 63c | 5.9c | 410 | 7 | 625 | 428 | 128539 | $7033 | 30d+ |
| KXWTIMAX-26DEC31-T120 | 120.01 or above | 55c | 2.9c | 1 | 37 | 1321 | 1049 | 122823 | $3888 | 30d+ |
| KXWTIMAX-26DEC31-T200 | 200.01 or above | 15c | 0.3c | 8 | 169 | 3748 | 3524 | 99677 | $3145 | 30d+ |
| KXWTIMAX-26DEC31-T130 | 130.01 or above | 45c | 0.4c | 4300 | 59 | 4300 | 871 | 90259 | $9356 | 30d+ |
| KXWTIMAX-26DEC31-T125 | 125.01 or above | 54c | 1.7c | 707 | 77 | 707 | 1061 | 82232 | $3973 | 30d+ |
| KXWTIMAX-26DEC31-T135 | 135.01 or above | 41c | 6.4c | 439 | 5 | 439 | 5 | 63564 | $2159 | 30d+ |
| KXWTI-26APR20-T101.99 | 102.0 or above | 20c | 9.0c | 20 | 100 | 20 | 100 | 25467 | $26865 | 1-3d |
| KXWTI-26APR20-T89.99 | 90.0 or above | 64c | 1.0c | 1 | 1076 | 1010 | 1167 | 23361 | $24484 | 1-3d |
| KXWTIW-26APR24-T90.99 | 91.0 or above | 58c | 2.0c | 87 | 85 | 524 | 1305 | 19668 | $26166 | 3-7d |
| KXWTI-26APR20-T87.99 | 88.0 or above | 72c | 3.0c | 113 | 3 | 334 | 313 | 18868 | $19940 | 1-3d |
| KXWTI-26APR20-T86.99 | 87.0 or above | 80c | 14.0c | 253 | 80 | 0 | 0 | 13143 | $13062 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXWTIMAX | WTI oil yearly high | annual | 10 | 10 | $43,845 | 1,276,608 | 3.4c |
| KXWTI | WTI oil on day | custom | 40 | 35 | $202,622 | 214,151 | 5.7c |
| KXBRENTMON | Brent Monthly | monthly | 20 | 18 | $5,059 | 78,114 | 13.0c |
| KXWTIW | WTI oil weekly range | weekly | 15 | 1 | $84,179 | 72,706 | 2.0c |
| KXWTIMINM | WTI oil monthly low | one_off | 12 | 4 | $22,031 | 64,230 | 61.0c |
| KXAAAGASMINTX | Texas lowest gas price yearly | annual | 6 | 5 | $625 | 19,612 | 9.0c |
| KXWTIMIN | WTI oil yearly low | annual | 8 | 5 | $4,530 | 19,272 | 24.3c |
| KXAAAGASMINCA | California lowest gas price yearly | annual | 4 | 1 | $136 | 15,251 | 4.0c |
| KXBRENTD | Brent Oil Daily | daily | 30 | 26 | $10,320 | 14,198 | 27.3c |
| KXAAAGASMINFL | Florida lowest gas price yearly | custom | 4 | 2 | $330 | 10,114 | 8.0c |

## Curated notes

<!-- KEEP-START -->
### Market structure
- Series covered: KXBRENTD (Brent daily), KXWTID (WTI daily; currently 0 open), KXWTIH (WTI hourly), KXNATGASW (Nat gas weekly), KXNATGASMON (Nat gas monthly).
- Resolution mechanism: official futures settlement price (ICE Brent, NYMEX WTI/NG).
- Frequency: daily (Brent), hourly (WTI-H), weekly/monthly (nat gas).
- Structure: **strike ladder** — for each day, multiple strikes like "$93 or above",
  "$95 or above", "$100 or above". Each strike is a separate binary market.
- Typical close time: 21:00 UTC (= 17:00 ET, roughly US cash close).

### Informed flow profile
- **Retail + professional mix.** Real hedgers and speculators trade these.
- **HFT presence: moderate.** Top-2 strikes near spot often 1-3c spread; shoulder
  strikes (10-30% OTM or ITM) stay 15-40c wide. This is our zone.
- Informed-flow sources:
  - Physical-traders (refiners, producers) on Brent especially.
  - CL/BZ futures arbers: will eat any mispricing > fees + gas vs the futures curve.
  - News traders around EIA inventory (US oil), OPEC, geopolitical shocks.

### Time windows (UTC)
- **SAFE**: 00:00 - 11:00 UTC (Asian session, US/EU oil markets quiet or closed).
- **QUIET**: 11:00 - 13:30 UTC (EU oil pickup, not yet chaotic).
- **DANGEROUS**: 13:30 - 14:00 UTC (US cash equities open; cross-flow into commodities).
- **VERY DANGEROUS**:
  - **Wed 14:30 UTC**: EIA Weekly Petroleum Status Report — crude/gasoline/distillate
    inventory data. Biggest single scheduled mover for oil.
  - **OPEC / OPEC+ announcements**: ad hoc but pre-scheduled meeting dates.
  - **FOMC days, 18:00-19:30 UTC**: USD moves drag on commodities.
- **DANGEROUS**: 20:00 - 21:00 UTC — close-hour convergence; informed flow spikes.

### Correlation / basket structure
- Strike ladder = monotone CDF per underlying. P(>$95) >= P(>$96) >= P(>$97)...
  Violations = direct arb. Fit a smooth CDF to all strikes; outliers are relative
  value. See `correlation_structure.md`.
- Brent and WTI correlate ~0.95 daily. If both markets are open we can cross-hedge.
- Natural gas decoupled from crude most of the time.

### Verdict
- **v0 target: YES — primary commodity target.**
- Why:
  - 15-40c spreads on shoulder strikes give real MM edge.
  - Strike-ladder structure = correlation opportunities (adjacent-strike arb, CDF fitting).
  - Well-defined dangerous windows (EIA, FOMC, US cash open).
- Caveats:
  - Underlying-arb risk: if someone hedges on futures, we could be picked off when
    Brent moves intraday without Kalshi-market liquidity catching up.
  - Position sizing must respect strike-ladder correlation (one "oil up" view
    positions us across many adjacent strikes).
- Path: paper trade the shoulder strikes for a week. Skip Wed 14:30 UTC entirely.
<!-- KEEP-END -->
