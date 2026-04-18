# Venue Comparison

Short, opinionated overview. Full API specs live elsewhere; this doc is about the strategic tradeoffs.

## Kalshi — recommended v0

- **Status**: US-regulated (CFTC DCM), designated contract market.
- **Asset class**: event contracts (economic, weather, politics, culture, climate).
- **API**: clean REST + WebSocket, documented, stable. Supports read-only keys.
- **Fees**: taker fees; maker generally free (check current schedule). Position limits per-contract.
- **Order book**: real CLOB; honest FIFO; no on-chain weirdness.
- **Liquidity**: moderate on headline markets, thin on niche (which is what we want).
- **Pros**: cleanest API, clearest rules, regulated (low platform-death risk), easy paper->live path.
- **Cons**: lower volume ceiling than Polymarket; position caps can constrain sizing; US-person KYC required.

**Use as v0.**

## Polymarket

- **Status**: on-chain CLOB on Polygon; off-limits to US persons (ongoing CFTC dispute, recently resolved for some markets).
- **Asset class**: much broader — crypto, politics, culture, sports, anything.
- **API**: public CLOB REST / WS, well-documented. Wallet-signed orders.
- **Fees**: gas (cheap on Polygon but non-zero); protocol fees vary.
- **Order book**: hybrid — CLOB matching, on-chain settlement.
- **Liquidity**: highest of any prediction venue on headline markets.
- **Pros**: deepest markets, broadest coverage, no position caps.
- **Cons**: on-chain complexity; private-key handling (real risk); gas is a per-fill tax; US regulatory uncertainty persists; no read-only key concept (address + signer).

**Consider in Phase 4+ after Kalshi is stable.**

## Manifold

- **Status**: play-money; no real capital.
- **Asset class**: anything users create.
- **API**: REST, simple.
- **Use**: strategy validation, testing the quoting logic against real (if play-money) order flow before moving to real capital.
- **Cons**: play money means incentives are different; participants are not representative.

**Use as a sandbox in Phase 3 alongside Kalshi paper trading.**

## Others

- **PredictIt**: US-regulated but limited universe, $850 per-contract cap, in decline. Skip.
- **Betfair**: sports-heavy; UK-regulated; separate ecosystem. Not a v0 target.
- **Smarkets**: similar to Betfair. Not a v0 target.

## Decision

Start with Kalshi. Read-only key first. Migrate paper-trading logic to Polymarket only after Kalshi strategy is profitable and the architecture is clean enough to swap the venue adapter.
