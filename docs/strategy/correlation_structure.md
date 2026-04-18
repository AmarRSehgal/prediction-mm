# Correlation Structure

## Thesis

Prediction markets do not exist in isolation. Many come in families where outcomes are mathematically related, and the market prices often violate the implied bounds. Two distinct opportunities:

1. **Hedging**: reduce inventory risk by offsetting a position in one contract with a correlated one.
2. **Relative-value / arbitrage**: when prices violate no-arbitrage bounds between related contracts, take the free edge directly.

Both require mapping the correlation / dependency structure per market family.

## Types of correlation structure

### 1. Adjacent-strike monotone (deterministic)
Example: Kalshi temperature markets on the same day / location:
- "High temp at LGA > 68F" = P68
- "High temp at LGA > 69F" = P69
- "High temp at LGA > 70F" = P70

By construction: `P68 >= P69 >= P70`. This is a hard no-arb constraint.

Implied fair values:
- `P(68 < T <= 69) = P68 - P69` must be >= 0.
- The full set of strikes implies a **CDF** for the underlying.

Opportunities:
- If `P69 > P68` at some point, that is a direct arbitrage (buy the cheaper, sell the more expensive, guaranteed value at resolution).
- Even without arb, you can fit a smooth CDF to all strikes; strikes that deviate from the fit are relative-value opportunities.
- Hedging: long P69 hedges short P68 in expectation; the difference has defined max payoff.

### 2. Exclusive / exhaustive (deterministic)
Example: "Which candidate wins X primary?" — a mutually exclusive, collectively exhaustive set.

By construction: `sum(P_i) = 1` (minus fee / spread drag, often `sum(P_i)` trades at ~0.98-1.02).

Opportunities:
- If `sum > 1.02` meaningfully, sell the whole basket (short every outcome).
- If `sum < 0.98`, buy the whole basket.
- The fee structure gives a natural bound; real arbs are rare on liquid venues but do appear on thin ones.
- Hedging: inventory on any one contract partially offset by opposite position in the sum of the others.

### 3. Complementary binary (deterministic)
`YES + NO = 1` minus fees.
Almost always tight on well-functioning venues, but occasionally drifts on thin ones.

### 4. Statistical correlation (stochastic)
Example: CPI headline vs CPI core. NFP vs unemployment rate. Weather at LGA vs JFK. Different elections on same day.

No hard bound, but historical correlation is strong. You can:
- Use one contract's move as a signal for the other's fair value.
- Partial hedge using historical beta.
- Risk: correlation breaks exactly when it matters (tail events).

### 5. Semantic / event correlation
Events on the same underlying theme: "Fed cuts in March" vs "Fed cuts by June". "Oscar Best Picture" vs "Oscar Best Director" (correlated when a film sweeps).

Usually weaker than statistical, but worth knowing for risk concentration limits.

## How to use correlation structure in the MM strategy

### A. No-arb monitor (lowest-hanging fruit)
Per market family, compute:
- Monotonicity violation flags (adjacent strikes out of order).
- Sum-to-one violations (mutually exclusive basket).
- Complementary YES/NO deviation from 1.

When violation > fee buffer, take directly. This is not MM; it is arb. But the infrastructure to monitor is identical, so build it alongside.

### B. Curve-fitted fair values
Fit a parametric CDF (Gaussian, skew-normal, or non-parametric isotonic) to all strikes in a strike family. Use fitted values as the anchor for individual-contract fair-value estimates, not raw mid.

Benefits:
- Smoother fair values, less whipsaw.
- Natural outlier detection (quote at a strike that disagrees with the curve by > K stddev: quote wider, or pull).
- Per-contract variance estimate from the curve fit.

### C. Basket inventory limits
Track inventory at the **family** level, not just per-contract. Long $X worth of "temp > 68" + long $X of "temp > 69" is not two independent exposures; it is roughly `2X` on the same underlying.
- Per-family dollar inventory cap.
- Per-family vega-equivalent cap if using CDF fit.

### D. Hedge routing
When inventory on contract A exceeds threshold and A has a correlated contract B with liquidity, take a partial hedge in B instead of aggressively unwinding A. Leaves the MM position on A intact; reduces net exposure faster and cheaper.

## Practical family-detection for Phase 1

Kalshi exposes market metadata with series / event structure that makes families explicit for strike ladders (weather, economic data). For less structured families:
- Group by event ID / series ID in the API response.
- Manually tag cross-family correlations (e.g., CPI headline and CPI core are in different series but related).

Deliverable for Phase 1:
- For each target market category, enumerate the family structure (how many related contracts, which constraints bind).
- For each family, measure historical no-arb violation frequency and magnitude.
- Decide whether an arb monitor is worth building on top of the MM stack (short answer: probably yes; cost is low).
