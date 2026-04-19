# comm_energy

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **22** (22 with open markets)
- Open markets: **436** (271 contested)
- Total 24h volume: **$385,928**
- Total open interest: **1,865,307**
- Top-OI mean spread (median across series): **8.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **9.0c**
- Median TOB bid / ask size: **30 / 70** contracts
- Median depth within 5c of best bid / ask — **192 / 250** contracts
- Median depth within 10c of best bid / ask — **274 / 399** contracts
- Median depth within 5c of midpoint — bid: **4** / ask: **6** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **148**
- Mean informed-signal proxy: **-1.730** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **5.37c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 9226 | 3.28 | -0.707 | 15.00 | 26.1 |
| 3-7d | 3274 | 2.51 | -0.695 | 11.00 | 44.3 |
| 7-30d | 4827 | 4.18 | -0.540 | 18.00 | 40.0 |
| 30d+ | 12206 | 1.81 | -0.719 | 8.00 | 52.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXWTIMAX-26DEC31-T180 | 180.01 or above | 16c | 4.5c | 453 | 132 | 6683 | 4541 | 23286 | 4927 | 228228 | $2276 | 30d+ |
| KXWTIMAX-26DEC31-T150 | 150.01 or above | 30c | 3.1c | 6 | 3 | 1777 | 3344 | 5069 | 3880 | 179250 | $4809 | 30d+ |
| KXWTIMAX-26DEC31-T160 | 160.01 or above | 24c | 1.9c | 5 | 3 | 1323 | 1469 | 2938 | 2707 | 154207 | $1559 | 30d+ |
| KXWTIMAX-26DEC31-T140 | 140.01 or above | 32c | 3.0c | 11 | 7 | 56 | 1195 | 548 | 5901 | 129733 | $2474 | 30d+ |
| KXWTIMAX-26DEC31-T115 | 115.01 or above | 61c | 1.9c | 50 | 166 | 960 | 196 | 1965 | 3182 | 128519 | $6071 | 30d+ |
| KXWTIMAX-26DEC31-T120 | 120.01 or above | 55c | 3.7c | 226 | 37 | 1330 | 1149 | 1951 | 1649 | 122823 | $3640 | 30d+ |
| KXWTIMAX-26DEC31-T200 | 200.01 or above | 15c | 0.1c | 8 | 0 | 3661 | 3819 | 4779 | 12131 | 99677 | $3145 | 30d+ |
| KXWTIMAX-26DEC31-T130 | 130.01 or above | 45c | 0.4c | 4291 | 59 | 4291 | 871 | 5698 | 932 | 90268 | $9366 | 30d+ |
| KXWTIMAX-26DEC31-T125 | 125.01 or above | 54c | 1.7c | 717 | 68 | 1065 | 1052 | 1223 | 3616 | 82241 | $2766 | 30d+ |
| KXWTIMAX-26DEC31-T135 | 135.01 or above | 41c | 5.7c | 439 | 5 | 459 | 471 | 697 | 1384 | 63564 | $1956 | 30d+ |
| KXWTI-26APR20-T101.99 | 102.0 or above | 15c | 4.0c | 99 | 1 | 1199 | 11 | 1976 | 1135 | 25495 | $27006 | 1-3d |
| KXWTI-26APR20-T89.99 | 90.0 or above | 55c | 6.0c | 62 | 589 | 965 | 880 | 1560 | 886 | 23315 | $24703 | 1-3d |
| KXWTIW-26APR24-T90.99 | 91.0 or above | 59c | 2.0c | 43 | 117 | 431 | 1205 | 1385 | 1289 | 20306 | $20855 | 3-7d |
| KXWTI-26APR20-T87.99 | 88.0 or above | 70c | 3.0c | 188 | 3 | 660 | 156 | 660 | 608 | 18897 | $19253 | 1-3d |
| KXWTI-26APR20-T86.99 | 87.0 or above | 78c | 9.0c | 48 | 164 | 224 | 244 | 244 | 485 | 13148 | $12680 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXWTIMAX | WTI oil yearly high | annual | 10 | 10 | $38,919 | 1,278,511 | 3.2c |
| KXWTI | WTI oil on day | custom | 40 | 36 | $209,623 | 223,163 | 5.3c |
| KXWTIW | WTI oil weekly range | weekly | 15 | 1 | $78,356 | 84,410 | 4.0c |
| KXBRENTMON | Brent Monthly | monthly | 20 | 20 | $5,184 | 78,422 | 9.7c |
| KXWTIMINM | WTI oil monthly low | one_off | 12 | 5 | $18,433 | 65,051 | 34.0c |
| KXAAAGASMINTX | Texas lowest gas price yearly | annual | 6 | 5 | $625 | 19,612 | 9.0c |
| KXWTIMIN | WTI oil yearly low | annual | 8 | 4 | $4,470 | 19,272 | 28.7c |
| KXAAAGASMINCA | California lowest gas price yearly | annual | 4 | 1 | $136 | 15,251 | 4.0c |
| KXBRENTD | Brent Oil Daily | daily | 30 | 25 | $9,933 | 14,760 | 7.0c |
| KXBRENTW | Brent Oil | weekly | 20 | 15 | $10,832 | 11,632 | 6.0c |

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
