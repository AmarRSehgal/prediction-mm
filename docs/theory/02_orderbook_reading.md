# Reading the Orderbook

## Basic anatomy

A limit orderbook has levels: each level is (price, total size, number of orders). The **top of book** (TOB) is the best bid and best ask; the gap between them is the spread; depth is size stacked behind TOB.

Two numbers that matter more than most people realize:

- **Queue position**: at a given price level, you are Nth in line. FIFO fills in most venues. Being early in queue is a real asset, not an implementation detail.
- **Book imbalance** at TOB (or first K levels): `(bid_size - ask_size) / (bid_size + ask_size)`. Strongly predictive of next-tick direction on short horizons.

## Canonical book shapes and what they mean

### 1. Thin symmetric book
E.g., 10 @ bid, 10 @ ask, wide gap to next levels.
- Low liquidity; you may be the only MM.
- Each trade moves price a lot.
- Your quotes do not compete with much — you set the spread.
- Risk: if someone hits you with size, you sweep multiple levels when covering.

### 2. Stacked / deep book
Hundreds at every level close to TOB.
- Liquid, competitive.
- Hard to get to front of queue; stuck behind big players.
- Low per-trade PnL, high turnover required.
- Usually not where a small MM should play.

### 3. Lopsided book
E.g., 500 @ bid, 20 @ ask.
Two interpretations, opposite implications:
- **Real buying interest** (support): price will drift up; quote ask eagerly, raise bid cautiously.
- **Spoof** (fake wall to induce movement, then cancel): the large order is not real; do not lean on it.

How to tell them apart: does the large order **refresh after partial fills**? Real orders get filled or pulled; spoofs cancel instantly when price approaches. Track the order's lifetime and fill ratio over time.

### 4. Wall at a specific price
E.g., 10,000 @ 0.52 in a Kalshi market trading at 0.50. Candidates:
- Whale accumulating or exiting (real).
- Decoy to pin price (spoof — illegal in regulated markets but happens).
- Hedge from a structured product (real, price-indifferent).

MM response: do **not** put size between the wall and TOB unless you have a view. The wall dominates the fill dynamics.

### 5. Icebergs / hidden orders
Visible size is the tip; real size refills after each fill.
Signature: level keeps coming back to the same visible size after trades hit it.
These are **informed flow indicators** — someone wants to transact quietly. Widen or skew away.

### 6. Layering / order-book stuffing
Many small orders stacked at staggered prices.
Usually algorithmic; often HFT seeding levels.
Your quote has to compete on queue position or sit behind.

## Microstructure signals to compute

| Signal | Formula | Use |
|---|---|---|
| Book imbalance (BI) | `(Qb - Qa) / (Qb + Qa)` at TOB | Short-term drift predictor |
| Weighted mid | `(Qa*Pb + Qb*Pa) / (Qa + Qb)` | Fairer "true mid" than midpoint |
| Order flow imbalance (OFI) | sum of signed TOB size changes | Direction of pressure |
| Trade imbalance | `(buy_vol - sell_vol) / total_vol` | Toxic flow proxy |
| Cancel rate | `cancels / (cancels + fills)` at TOB | High = spoofy / noisy |
| Quote-to-trade ratio | quote updates per trade | High = HFT arms race |

## How book shape changes quoting

- **Thin + symmetric**: quote wider than microstructure implies — you are the liquidity provider of last resort; charge for it.
- **Lopsided (real)**: skew reservation price toward the weaker side. The book is telling you where fair value is heading.
- **Lopsided (spoof)**: ignore the wall; use weighted mid from smaller orders only.
- **Iceberg detected**: widen aggressively on that side. Pull and observe.
- **Large trade just printed**: wait. Price is about to move or revert; do not quote into it until the dust settles. The "quote-then-pull" reflex around big prints is a major source of PnL protection.
