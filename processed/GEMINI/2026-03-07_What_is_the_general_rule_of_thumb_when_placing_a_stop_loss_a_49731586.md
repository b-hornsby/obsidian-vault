---
category: crypto-web3
date: 2026-03-07
id: 145790
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to understand general rules for setting stop-loss and take-profit
  levels when trading wrapped Bitcoin perpetuals.
tags:
- perp-trading
- stop-loss
- take-profit
- wrapped-bitcoin
- trading-strategy
---
# What is the general rule of thumb when placing a stop loss and your take profit when trading perps? Specifically wrapped bitcoin?

### USER
What is the general rule of thumb when placing a stop loss and your take profit when trading perps? Specifically wrapped bitcoin?

### GEMINI
When trading perpetual futures (perps), specifically Wrapped Bitcoin (WBTC), the rules of thumb aren't about "safe" numbers, but about mathematical expectancy. If you are looking for a standard starting point, here is how the mechanics actually work: 1. The Risk-Reward Ratio (The "Gold Standard") The most common rule of thumb is a 1:2 or 1:3 ratio. 1:2 Ratio: If you risk $100 on your Stop Loss (SL), your Take Profit (TP) should be at least $200 away. Why? This allows you to be wrong more than half the time and still remain profitable. At a 1:3 ratio, you only need to be "right" 30% of the time to break even. 2. Stop Loss Placement: Structure over Percentages In crypto perps, a "5% stop loss" is often useless because WBTC volatility can wick 5% in minutes just to hunt liquidity. Structural SL: Place your stop below the recent swing low (for a long) or above the recent swing high (for a short). Volatility-Adjusted (ATR): Use the Average True Range (ATR) indicator. A common rule is to set your SL at 1.5x or 2x the ATR from your entry. This ensures your stop is outside the "noise" of normal price action. 3. Take Profit: Resistance and Scaling Don't just pick a random number. Level-to-Level: Place your TP just below a major resistance level (for longs) or just above major support (for shorts). Scaling Out: A professional rule of thumb is to close 50% of the position at 1:1 or 1:1.5, move your SL to entry ("Break Even"), and let the remaining 50% ride to a 1:3 target. This "locks in" the trade and removes the risk of a total loss if the market reverses. 4. The "WBTC Specific" Factor Since WBTC is an ERC-20 token on Ethereum, you must account for: Liquidity Wicks: WBTC can sometimes experience slight de-pegs or "fat finger" wicks on specific DEXs that don't happen on centralized BTC exchanges. Ensure your stop loss is triggered by the Mark Price (the global average) rather than the Last Price (the specific price on that one exchange) to avoid getting "scammed" out of a position by a localized spike. MetricRule of ThumbMin. Risk/Reward1:2Stop Loss BasisPrevious Swing High/Low + small bufferMax Risk per Trade1% to 3% of your total account balanceTake Profit BasisNext major structural resistance/support Would you like me to calculate specific entry, SL, and TP levels for a WBTC trade based on the current market price?
