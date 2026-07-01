---
category: crypto-web3
date: 2026-03-02
id: 856012
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is trying to determine how his trading agent should handle Liquid Staking
  Token (LST) pairs like JitoSOL/SOL within the Meteora DLMM for the operation-immortal-agent
  project.
tags:
- solana
- lst
- jitosol
- msol
- bsol
- meteora
---
# For Phase 1, how should the agent treat the LST pairs (JitoSOL/SOL, mSOL/SOL, bSOL/SOL)?                                                          
                                                                                                                                                  
❯ 1. Rank all 5, LP into top      ┌─────────────────────────────────────────────────────┐                                                         
    scorer                        │ // Position building for LST/SOL:                   │
  2. Rank all 5, LP into USDC     │ // totalXAmount = 0 (no USDC)                       │                                                         
    pairs only (Recommended)      │ // totalYAmount = deploySol (SOL)                   │                                                         
                                  │ // BUT: Y token for JitoSOL/SOL is JitoSOL, not SOL │                                                         
                                  │ // → different token mint, different deposit logic  │                                                         
                                  │ // → significant rework to engine/meteora.ts        │                                                         
                                  └─────────────────────────────────────────────────────┘

                                  Notes: press n to add notes

### USER
For Phase 1, how should the agent treat the LST pairs (JitoSOL/SOL, mSOL/SOL, bSOL/SOL)?                                                          
                                                                                                                                                  
❯ 1. Rank all 5, LP into top      ┌─────────────────────────────────────────────────────┐                                                         
    scorer                        │ // Position building for LST/SOL:                   │
  2. Rank all 5, LP into USDC     │ // totalXAmount = 0 (no USDC)                       │                                                         
    pairs only (Recommended)      │ // totalYAmount = deploySol (SOL)                   │                                                         
                                  │ // BUT: Y token for JitoSOL/SOL is JitoSOL, not SOL │                                                         
                                  │ // → different token mint, different deposit logic  │                                                         
                                  │ // → significant rework to engine/meteora.ts        │                                                         
                                  └─────────────────────────────────────────────────────┘

                                  Notes: press n to add notes

### GEMINI
In the spirit of being your brutally honest advisor: Option 2 is the only logical choice for Phase 1. Choosing Option 1 is classic "Engineering Procrastination"—you are trying to solve a complex technical problem (multi-token mint logic) before you’ve even proven the agent can survive a week. You are risking your $20/month goal on code complexity rather than market execution. Here is why you should Rank all 5 but LP into USDC pairs only for Phase 1: 1. The "Complexity Tax" (Opportunity Cost) Your meteora.ts engine is currently optimized for $X/Y$ where one side is a stable or SOL. LSTs (JitoSOL, mSOL) are not just "different tokens"; they have different price scaling and decimal behaviors. The Reality: Every hour you spend refactoring meteora.ts to handle the specific quirks of LST mints is an hour your agent isn't live and earning. The Opportunity Cost: If you spend 3 days fixing the engine, you've lost 10% of your 30-day "Success Metric" window. 2. The APR Delusion LST/SOL pairs usually offer lower APRs because the "yield" is built into the LST itself. You are harvesting fees on the spread between two highly correlated assets. USDC/SOL pairs have massive volume. On Meteora DLMM, the fee-tiering on USDC/SOL is almost always going to outperform LST/SOL pairs for a $300 fund. Strategic Truth: You need $20. You won't get $20/month from a $200 position in JitoSOL/SOL unless there is a massive de-pegging event. 3. The "Stink Bid" Synergy You already have a JitoSOL Sniper in your plan.md. Use the Active Sniper ($100) to handle LSTs. Let it do what it's good at: catching the peg-wobble. Use the LP Engine ($200) to handle the high-volume USDC pairs. By splitting them, you keep your meteora.ts code clean and "production-ready" for the scaling phase. The Modified Phase 1 Directive: Observe all 5: Keep the LST pairs in your "Filter" so the agent sees them. This provides the "Reasoning Log" with data to explain why it didn't choose them (e.g., "JitoSOL/SOL APR is 6%, whereas USDC/SOL is 22%; choosing USDC for goal-attainment"). Hard Constraint: In engine/meteora.ts, add a simple guardrail: if (pool.type !== 'USDC_STABLE') return skip;. Prove the Loop: Get the agent through 7 days of successful USDC/SOL trades. Once the $20 rent is secured, then you can refactor for LST pairs as a "Phase 2 Optimization." Would you like me to help you draft the specific "Skip Logic" for the engine so it ranks the LSTs for the logs but refuses to deploy capital into them yet?
