# Avellaneda-Stoikov — Deep Dive

Reference: Avellaneda & Stoikov (2008), *"High-frequency trading in a limit order book"*.

The canonical academic MM model. Solves the inventory-vs-spread tradeoff in closed form under specific assumptions. Still the reference point; every modern MM paper either extends it or argues against one of its assumptions.

## Setup — the assumptions

### Price process
Arithmetic Brownian motion, no drift:
```
dS_t = sigma * dW_t
```
No drift =>  MM has no directional view (realistic: if you could predict, you would take directionally, not MM).

### MM state
- `q_t` = inventory (positive = long, negative = short)
- `X_t` = cash balance
- Mark-to-market wealth: `W_t = X_t + q_t * S_t`

### Quoting
MM posts bid at distance `delta_b` below mid, ask at distance `delta_a` above mid:
```
p_bid = S_t - delta_b
p_ask = S_t + delta_a
```

### Order arrival — the key empirical claim
Probability of a market order hitting your quote falls exponentially with distance from mid:
```
lambda_a(delta_a) = A * exp(-k * delta_a)
lambda_b(delta_b) = A * exp(-k * delta_b)
```
- `A` = base arrival rate (how busy the market is).
- `k` = price sensitivity of flow (how fast arrival decays as you quote further).

Quote at mid => many fills. Quote far out => few fills. `k` controls the steepness.
**Thin / illiquid markets have low `A` and low `k`.**

### Objective
Maximize expected exponential utility of terminal wealth at horizon `T`:
```
U(W_T) = -exp(-gamma * W_T)
```
- `gamma` = risk aversion. Higher = more inventory-averse.
- `T` = horizon. Trading day end for equities; **resolution time for prediction markets** — natural fit.

## The solution — two equations to remember

Solving the Hamilton-Jacobi-Bellman PDE (messy derivation, skip), two clean results:

### 1. Reservation price (inventory-adjusted indifference price)
```
r(s, q, t) = s - q * gamma * sigma^2 * (T - t)
```

**This is the central insight. Quotes should be symmetric around `r`, not around mid `s`.**

Interpretation:
- `q > 0` (long) => `r < s`. Lower both bid AND ask. Ask becomes more attractive (want to sell); bid becomes less competitive (do not want more).
- `q < 0` (short) => `r > s`. Raise both.
- Skew magnitude `q * gamma * sigma^2 * (T - t)` scales with:
  - **Inventory** `q` — more inventory, more skew.
  - **Risk aversion** `gamma`.
  - **Variance** `sigma^2` — riskier price => stronger urge to flatten.
  - **Remaining horizon** `(T - t)` — more time left => more chance of adverse move => more skew. As `t -> T`, skew vanishes.

### 2. Optimal spread
Total spread `delta_a + delta_b`:
```
delta_a + delta_b = gamma * sigma^2 * (T - t) + (2/gamma) * ln(1 + gamma/k)
```

Two components:
- `gamma * sigma^2 * (T - t)` — **inventory risk premium**. Charge more when volatile / more time left.
- `(2/gamma) * ln(1 + gamma/k)` — **microstructure spread**. Depends only on `k` and `gamma`. In illiquid markets (low `k`), this is large. Your "monopoly rent" for being the only liquidity provider.

Then:
```
p_ask = r + (delta_a + delta_b) / 2
p_bid = r - (delta_a + delta_b) / 2
```
Quoting symmetrically around the **reservation price**, not mid.

## Worked intuition

Prediction market contract: mid = 0.40, resolution in 1 hour, `sigma = 0.02/sqrt(hour)`, `gamma = 10`, `A = 5`, `k = 50`.

Start with `q = 0`:
- `r = 0.40` (no skew).
- Inventory premium: `10 * 0.0004 * 1 = 0.004`.
- Microstructure: `(2/10) * ln(1 + 10/50) = 0.2 * 0.182 = 0.036`.
- Total spread: `0.040`.
- Quote: bid 0.380, ask 0.420.

After buying 5 contracts, `q = 5`:
- `r = 0.40 - 5 * 10 * 0.0004 * 1 = 0.38`.
- Same spread: 0.040.
- New quote: bid 0.360, ask 0.400. Ask is now at the old mid — you really want to unload.

As `t -> T` (last 5 minutes):
- Inventory premium shrinks (term goes to zero): spread tightens to just microstructure component.
- Skew shrinks: the model stops worrying about inventory because "mark-out" is imminent.

**In prediction markets this last property is wrong** — see adaptations below. Resolution is *not* a mark-out at fair value; it is a binary payoff.

## Adapting AS to prediction markets

AS is built for unbounded Gaussian prices. Prediction markets have [0,1] bounded prices and binary resolution. Required adjustments:

### 1. Heteroskedastic, price-dependent volatility
A contract at 0.5 has maximum volatility; at 0.01 or 0.99 volatility is tiny. Use a Beta-process or logistic-Brownian model. Practically: estimate local `sigma` from rolling realized vol.

### 2. Resolution risk dominates inventory risk near `T`
In AS, horizon `T` is a soft constraint. In prediction markets, `T` is resolution — inventory pays $0 or $1. You should actually **widen and lean harder to flatten** as resolution nears, not tighten. Replace AS's linear-in-time inventory term with a term that explodes near resolution if `q != 0`.

### 3. Calibrate `k` per contract
Thin political markets have very different `k` than liquid weather markets. Fit from fill data: regress `log(arrival_rate)` on quote distance.

### 4. Bounded quote truncation
AS can suggest quotes `< 0` or `> 1`. Clip. When clipped, skew is bounded and strategy degrades — signal that inventory is too large for the market; stop quoting that side.

### 5. Jump-aware extension
Prediction markets jump on news. Vanilla AS under-prices jump risk. Either add Merton-jump-diffusion (complex) or implement a news-pull overlay (simpler): widen or pull around pre-known event times. See `../strategy/safe_windows.md`.

## Key limitations of vanilla AS

1. **No order flow information.** AS treats arrivals as exogenous Poisson; real markets have predictive OFI. Extensions: Cartea-Jaimungal.
2. **No queue priority.** AS assumes instant fill conditional on price; real venues are FIFO.
3. **No adverse selection.** Arrivals are symmetric noise. Real trades are asymmetric: you get hit more when price is about to move against you. Glosten-Milgrom addresses this.
4. **Constant parameters.** `sigma`, `A`, `k`, `gamma` treated as constants; in practice all time-varying.
5. **Single contract.** No cross-market hedging. For prediction markets with complementary YES/NO or basket contracts, need multi-asset extensions (Gueant 2015).

## What to actually implement in v0

Practical prediction-market quoter skeleton:

```
mid = weighted_mid_from_book()
sigma = realized_vol(window=30min)
T_minus_t = seconds_to_resolution / scale
q = current_inventory

# AS core
r = mid - q * gamma * sigma^2 * T_minus_t
spread = gamma * sigma^2 * T_minus_t + (2/gamma) * ln(1 + gamma/k)

# Prediction-market clamps
bid = clip(r - spread/2, 0.01, 0.99)
ask = clip(r + spread/2, 0.01, 0.99)

# Overlays
if in_news_event_window():
    pull_quotes()
if abs(q) > inventory_cap:
    quote_only_reducing_side()
if seconds_to_resolution < 300 and q != 0:
    aggressive_unwind()
```

**`gamma` is the main tuning knob.** Start high (strong inventory aversion, wide spread, few fills, low risk). Tune down after validating.

## Extensions worth reading later

- **Cartea-Jaimungal** (2014) — adds order flow imbalance to AS.
- **Gueant-Lehalle-Fernandez-Tapia** (2013) — closed-form approximation; widely used in practice.
- **Gueant** (2015) — multi-asset / basket MM.
- **Stoikov-Saglam** (2009) — adverse selection in AS framework.
- RL-based MM (various 2018+) — learn the quoting policy directly from market simulation.
