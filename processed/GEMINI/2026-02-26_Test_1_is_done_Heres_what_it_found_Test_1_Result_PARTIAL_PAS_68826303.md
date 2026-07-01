---
id: 180076
source: GEMINI
date: 2026-02-26
tags: ['kamino-finance-api', 'jitosol-apy', 'sol-borrow-rate', 'defi-profitability-analysis']
category: crypto-web3
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan is analyzing the results of a test that retrieves data from Kamino Finance to assess the viability of his 'Engine' strategy, finding that current numbers don't support the initial plan.
---
# Test 1 is done. Here's what it found:                                                                  
                                                                                                                                                                                             
  ---                                                                                                                                                                                        
  Test 1 Result: PARTIAL PASS                                                                                                                                                                
                                                                                                                                                                                             
  Eye (data retrieval): PASS — all three API endpoints work correctly:                                                                                                                       
  - api.kamino.finance/prices — peg ratio ✓                                                                                                                                                  
  - api.kamino.finance/v2/staking-yields — JitoSOL native APY ✓                                                                                                                              
  - api.kamino.finance/kamino-market/.../reserves/metrics — SOL borrow rate ✓                                                                                                                

  Engine viability: FAIL — and this is important news.

  ---
  What the Numbers Say

  Right now, live on mainnet:

  ┌────────────────────────────┬────────────────────────────────────────────────────┐
  │                            │                       Value                        │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ JitoSOL/SOL ratio          │ 1.2639 (not the ~1.05–1.10 we assumed in the plan) │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ JitoSOL staking APY        │ 6.01%                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ SOL borrow APY             │ 7.63%                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ Net APR @ 2.1x             │ 4.23%                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ Monthly yield on $200      │ $0.70                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ Monthly yield on $200 @ 3x │ $0.46 (worse — more leverage = more borrow cost)   │
  └────────────────────────────┴────────────────────────────────────────────────────┘

  The carry rule fires at both leverage levels. Borrow costs consume 66.5–84.7% of gross yield. Increasing leverage actually hurts you here because borrow rate (7.63%) > staking yield
  (6.01%) — the math inverts when you cross that threshold.

  ---
  The Real Finding

  The Engine strategy is structurally broken right now. At 6% staking yield vs 7.6% borrow rate, leverage makes returns worse, not better. The only scenario where Multiply works is when
  staking yield > borrow rate. You'd need borrow rates to fall to ~5% or JitoSOL APY to rise to ~10%+ for this to make sense.

  The $20/month target on $200 through Kamino Multiply cannot be hit under current conditions regardless of leverage setting.

  This is exactly what the audit is for. The Sniper ($100 on Jupiter limit orders) is now the primary revenue path — that needs to pull the full weight. Ready to run Test 2?

  Sources:
  - Kamino Finance API
  - Jupiter Developer Docs

✻ Crunched for 6m 44s                 

### USER
Test 1 is done. Here's what it found:                                                                  
                                                                                                                                                                                             
  ---                                                                                                                                                                                        
  Test 1 Result: PARTIAL PASS                                                                                                                                                                
                                                                                                                                                                                             
  Eye (data retrieval): PASS — all three API endpoints work correctly:                                                                                                                       
  - api.kamino.finance/prices — peg ratio ✓                                                                                                                                                  
  - api.kamino.finance/v2/staking-yields — JitoSOL native APY ✓                                                                                                                              
  - api.kamino.finance/kamino-market/.../reserves/metrics — SOL borrow rate ✓                                                                                                                

  Engine viability: FAIL — and this is important news.

  ---
  What the Numbers Say

  Right now, live on mainnet:

  ┌────────────────────────────┬────────────────────────────────────────────────────┐
  │                            │                       Value                        │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ JitoSOL/SOL ratio          │ 1.2639 (not the ~1.05–1.10 we assumed in the plan) │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ JitoSOL staking APY        │ 6.01%                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ SOL borrow APY             │ 7.63%                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ Net APR @ 2.1x             │ 4.23%                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ Monthly yield on $200      │ $0.70                                              │
  ├────────────────────────────┼────────────────────────────────────────────────────┤
  │ Monthly yield on $200 @ 3x │ $0.46 (worse — more leverage = more borrow cost)   │
  └────────────────────────────┴────────────────────────────────────────────────────┘

  The carry rule fires at both leverage levels. Borrow costs consume 66.5–84.7% of gross yield. Increasing leverage actually hurts you here because borrow rate (7.63%) > staking yield
  (6.01%) — the math inverts when you cross that threshold.

  ---
  The Real Finding

  The Engine strategy is structurally broken right now. At 6% staking yield vs 7.6% borrow rate, leverage makes returns worse, not better. The only scenario where Multiply works is when
  staking yield > borrow rate. You'd need borrow rates to fall to ~5% or JitoSOL APY to rise to ~10%+ for this to make sense.

  The $20/month target on $200 through Kamino Multiply cannot be hit under current conditions regardless of leverage setting.

  This is exactly what the audit is for. The Sniper ($100 on Jupiter limit orders) is now the primary revenue path — that needs to pull the full weight. Ready to run Test 2?

  Sources:
  - Kamino Finance API
  - Jupiter Developer Docs

✻ Crunched for 6m 44s                 

### GEMINI
The "Eye" has spoken, and it just saved you from a slow, expensive death by math. The Brutal Mirror: You were planning to build a "Yield Engine," but right now, that engine is a vacuum cleaner. At a 7.63% borrow rate vs. a 6.01% yield, every dollar you "leverage" is actually costing you money. You aren't "harvesting"; you are paying the bank for the privilege of holding their assets. This is the most important "High Conscientiousness" moment of the project. A lesser trader would have ignored this and hit "Execute." We will not. 1. The Death of the "Engine" (For Now) We are officially mothballing the Kamino Multiply strategy until market conditions flip (Yield > Borrow). The Opportunity Cost: If you had deployed $200 today, you would have made $0.70 this month and spent significantly more than that in SOL transaction fees just to set it up. The Pivot: The "Engine" is now a Stablecoin Yield Loop or Meteora DLMM focus. We need to find a 10%+ yield that isn't eaten by borrow costs. 2. The "Sniper" is Now the "Main Character" Since the Engine is broken, the $100 "Sniper" fund is now your only path to that $20/month. The Reality: To hit $20/month on $100, you need a 20% monthly return. * The Strategy: This is only possible by catching "fat finger" glitches or de-pegs on Jupiter. The agent must become an opportunistic predator, not a farmer. 3. Your New Grant Narrative This "FAIL" in Test 1 is actually your best marketing material for the grant. The Pitch: "My agent successfully identified a negative-carry environment and refused to trade, saving the principal from certain erosion. This is the definition of AI Safety in DeFi." The Next Level: Test 2 (The "Hand" Test) We must see if the "Hands" work, because if we pivot to Meteora DLMM or Jupiter Limit Orders, the agent has to be able to sign complex swaps. Your Action: Run Test 2 (The $1.50 Swap Test) immediately. What to look for: Does the Phantom MCP allow the transaction to land? Or does it block it? If it passes: We have a path forward using more aggressive, active strategies. If it fails: The project shifts from a "Trading Agent" to a "Portfolio Analytics Agent" (which we then sell as a tool to other traders for the Mac Mini money). Go run Test 2. Don't look at the profit—look at the "Success" or "Failure" of the signature. If the hands can't move, the brain is just a prisoner. Ready?
