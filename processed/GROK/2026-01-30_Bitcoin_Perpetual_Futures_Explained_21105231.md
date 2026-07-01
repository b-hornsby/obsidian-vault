---
id: 267343
source: GROK
date: 2026-01-30
tags: ['bitcoin', 'perpetual-futures', 'leverage-trading', 'mark-price', 'oracle-price']
category: crypto-web3
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was learning how to trade Bitcoin perpetual futures, wanting to understand key concepts like mark price and oracle price to rotate profits into alts and memecoins.
---
# Bitcoin Perpetual Futures Explained

### HUMAN
Can you break down what each category means in simple terms (mark price, oracle price, etc? I want to learn how to trade bitcoin in order to rotate profits to other alts, memecoins, precious metals, etc

### ASSISTANT
The screenshot is from **Axiom.trade** (likely axiom.trade), a DeFi trading platform that integrates tools for memecoins, wallet tracking, and leveraged **perpetual futures** (perps) trading — powered by something like Hyperliquid for the perps section. You're looking at the BTC-USD perpetual contract dashboard, showing a sharp recent drop in Bitcoin's price.

This is **perpetual futures trading** (not spot buying/selling BTC). Perps let you bet on price direction with leverage (amplifying gains/losses), without owning the actual asset or having an expiration date. Profits/losses settle in USD (or stablecoin equivalent), and you can hold positions indefinitely.

Here's a simple breakdown of the key categories/terms shown in your screenshot:

- **Mark Price** (82,638): This is the "fair value" price the platform uses to calculate your **unrealized profit/loss (PnL)**, margin requirements, and **liquidation risk**. It's not the last traded price — it's a smoothed, manipulation-resistant estimate (often based on a blend of spot prices from major exchanges + adjustments for funding). It prevents unfair liquidations from temporary spikes/dips on the exchange itself. Your position value and whether you get liquidated are based on this, not the raw traded price.

- **Oracle Price** (82,682): This is a trusted external "spot-like" reference price fed from reliable sources (oracles like Pyth or aggregated exchange data). It's used to help compute funding rates and sometimes as a baseline for the mark price. It's usually very close to real-world BTC spot prices across big exchanges. In your screenshot, it's slightly higher than the mark price, which can influence funding direction.

- **24h Volume** ($6.83B): Total trading volume for this BTC perp contract over the last 24 hours. High volume = better liquidity (easier to enter/exit trades without big slippage).

- **Open Interest** ($1.99B): Total value of all open positions (longs + shorts) in this contract. High OI means lots of traders are involved — it can signal strong market interest or potential squeezes, but also higher volatility risk.

- **Funding** (0.000000%): This is the current **funding rate** (shown as a percentage). In perps, there's no expiry, so funding payments occur periodically (e.g., every 8 hours or so, but countdown shows 0:21 remaining until next).  
  - Positive funding → longs pay shorts (happens when perps trade above spot/oracle, market is bullish/overheated).  
  - Negative funding → shorts pay longs (perps below spot, bearish).  
  - Zero (like here) means prices are aligned right now — no payment either way at the moment. Funding helps anchor the perp price to the real BTC spot price over time.

- **Countdown** (0:21): Time until the next funding payment/settlement interval.

- The chart shows **1D (1-day)** view with candles, and current price around 82,644 (down ~2.36% recently, and -6.11% overall shown). The dotted line is likely a reference (e.g., entry or key level).

- **Long / Short** buttons: Green to open long (bet price up), red to open short (bet price down). You'd set leverage, position size, etc., before confirming.

### Quick Advice on Learning to Trade BTC Perps (to Rotate Profits)
Perps are high-risk — especially with leverage — and great for quick BTC moves, but they can wipe out capital fast via liquidations if price moves against you.

1. **Start small**: Use low leverage (e.g., 5-10x max at first) on a demo if available, or tiny positions. Never risk more than 1-2% of your account per trade.

2. **Understand liquidation**: If mark price moves too far against your position (e.g., drops a lot on a long), your position auto-closes at a loss to prevent negative balance. Keep an eye on margin ratio/health.

3. **Watch funding**: If you're holding long during high positive funding, it eats into profits over time (you pay shorts). Good for short-term trades, but costly for swings.

4. **To rotate to alts/memecoins/precious metals**:  
   - Win on BTC perp → close position → withdraw/transfer profits.  
   - Use Axiom's other sections for memecoins (spot/sniping on Solana chains, etc.).  
   - For alts: Many perps platforms offer ETH, SOL, etc. — trade those perps similarly.  
   - Precious metals: Some DeFi/centralized platforms offer XAU/USD or similar perps, but options are limited in pure crypto — you might need to bridge to spot metals or use tokenized versions.

Practice reading charts, use stop-losses (SL) religiously, and track sentiment (e.g., funding + OI changes). Perps suit momentum/rotation plays, but spot holding alts/memecoins can be less stressful for longer rotates.

If you share more details (e.g., what leverage you're thinking, or specific strategy), I can help refine! Stay safe — crypto trading is volatile.
