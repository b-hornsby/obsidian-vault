---
category: ai-tools
date: 2026-03-02
id: 630596
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is exploring how to train a language model on data related to the top
  5 and then top 25 Solana tokens, referencing his plan.md for the operation-immortal-agent
  project.
tags:
- ai
- llm-training
- fine-tuning
- operation-immortal-agent
- solana-trading-bot
---
# i was more so showing you that so i could see how to go about training on the big 5 like what the plan.md describes and then scaling to the top 25? here is the paln.md for better context: Revised Plan: "Operation Immortal Agent" (v2.2)
1. The Core Objective: "Self-Sustaining Autonomy"

Build an autonomous AI agent (Claude + Phantom MCP) to manage a $300 fund.

    The Primary Goal: Generate $20/month in net profit to pay for the "Claude Brain."

    The Success Metric: 30 consecutive days of self-funded operation + a generated "Reasoning Log" for the $1,500+ Grant.

    The Budget: User subsidizes the $6/month VPS. The agent is responsible for the $20 Claude Rent.

2. The Build (The "What")

    The Brain: Claude (current 2026 flagship) via Anthropic SDK.

    The Hands: Phantom MCP (@phantom/mcp-server) for transaction signing.

    The Spine: Node.js running on a Fly.io or Railway VPS (Always-on).

    The Ledger: Public GitHub repo for the Reasoning Log (The Grant Product).

3. The Strategy (The "How" - v2.2 Pivot)

Test 1 audit result: Kamino Multiply is disqualified. At 6.01% JitoSOL staking yield vs
7.63% SOL borrow rate, leverage amplifies losses, not gains. The Engine pivots to
fee-based LP income which has zero borrow cost.

    The LP Engine ($200 - Fee Harvesting):
        Primary: Meteora DLMM on the USDC/SOL pair.
        Why: Fee income only — no leverage, no borrow cost, no carry rule.
        Target: >15% APR from swap fees. USDC/SOL is a high-volume pair; 20-50% APR
                is common during active sessions. $200 at 20% = $3.33/month.
        Mechanic: Agent deploys capital into the active price bin range and earns
                  a share of all swaps through that range.
        Fallback: If USDC/SOL DLMM 4-hour fee rate drops below $0.10, agent
                  hops to the next highest-APR Meteora Dynamic Vault (single-sided,
                  no IL risk).

    The Active Sniper ($100 - The Gap Filler):
        Target: Jupiter Limit Orders on JitoSOL/SOL.
        Action: Agent sets "Stink Bids" 1-1.5% below the current peg.
        Logic: Catch momentary volatility, sell back at peg for ~1% capture.
        One successful capture per week on $100 = ~$1/week = ~$4/month.

    Combined target: LP Engine ($3-7/mo) + Sniper ($4/mo) = $7-11/month baseline.
    Gap to $20: Covered by Meteora high-APR periods or additional sniper captures.
                The Reasoning Log quality is the real unlock — it funds the Mac Mini
                via grant, not pure trading returns.

4. The Guardrails (Survival Protocol)

    IL Protection: If LP portfolio value drops >3% vs equivalent HODL, close
                   the position and park in USDC.

    Fee Rate Check: Every 4 hours, calculate actual fees earned. If annualized
                    rate of the last period is <15% APR, trigger a pool hop scan.

    Peg Monitor: If JitoSOL/SOL deviates >2% from baseline, close any JitoSOL
                 Sniper positions and exit to USDC.

    Rent Reserve: Once $20 profit is confirmed for the month, agent closes LP
                  and parks Engine capital in USDC until the next billing cycle.

    Heartbeat: Execution occurs on a 4-hour cycle.

5. The Reasoning Loop (The "Product")

Every 4 hours, the agent executes:

    Scan: Meteora pool APR, DLMM fee rate (last 4h), JitoSOL peg ratio, current
          profit vs $20 goal.

    Analyze: "Do I have $20 yet? If no, is my current pool above 15% APR?
              Is there a better pool? Is IL within tolerance?"

    Act: Construct transaction via Meteora SDK / Jupiter Quote API and sign via MCP.

    Log: Structured JSON output: Inputs -> Logic -> Goal Progress -> Action.

6. The Payout (The Mac Mini Path)

    Proof of Work: Use the logs to prove the agent survived a month and paid its own rent.

    The Pitch: "I built the first 100% self-sustaining, fee-harvesting AI agent on Solana."

    The Win: Secure the $1,500 Grant to buy the Mac Mini and scale the principal.

### USER
i was more so showing you that so i could see how to go about training on the big 5 like what the plan.md describes and then scaling to the top 25? here is the paln.md for better context: Revised Plan: "Operation Immortal Agent" (v2.2)
1. The Core Objective: "Self-Sustaining Autonomy"

Build an autonomous AI agent (Claude + Phantom MCP) to manage a $300 fund.

    The Primary Goal: Generate $20/month in net profit to pay for the "Claude Brain."

    The Success Metric: 30 consecutive days of self-funded operation + a generated "Reasoning Log" for the $1,500+ Grant.

    The Budget: User subsidizes the $6/month VPS. The agent is responsible for the $20 Claude Rent.

2. The Build (The "What")

    The Brain: Claude (current 2026 flagship) via Anthropic SDK.

    The Hands: Phantom MCP (@phantom/mcp-server) for transaction signing.

    The Spine: Node.js running on a Fly.io or Railway VPS (Always-on).

    The Ledger: Public GitHub repo for the Reasoning Log (The Grant Product).

3. The Strategy (The "How" - v2.2 Pivot)

Test 1 audit result: Kamino Multiply is disqualified. At 6.01% JitoSOL staking yield vs
7.63% SOL borrow rate, leverage amplifies losses, not gains. The Engine pivots to
fee-based LP income which has zero borrow cost.

    The LP Engine ($200 - Fee Harvesting):
        Primary: Meteora DLMM on the USDC/SOL pair.
        Why: Fee income only — no leverage, no borrow cost, no carry rule.
        Target: >15% APR from swap fees. USDC/SOL is a high-volume pair; 20-50% APR
                is common during active sessions. $200 at 20% = $3.33/month.
        Mechanic: Agent deploys capital into the active price bin range and earns
                  a share of all swaps through that range.
        Fallback: If USDC/SOL DLMM 4-hour fee rate drops below $0.10, agent
                  hops to the next highest-APR Meteora Dynamic Vault (single-sided,
                  no IL risk).

    The Active Sniper ($100 - The Gap Filler):
        Target: Jupiter Limit Orders on JitoSOL/SOL.
        Action: Agent sets "Stink Bids" 1-1.5% below the current peg.
        Logic: Catch momentary volatility, sell back at peg for ~1% capture.
        One successful capture per week on $100 = ~$1/week = ~$4/month.

    Combined target: LP Engine ($3-7/mo) + Sniper ($4/mo) = $7-11/month baseline.
    Gap to $20: Covered by Meteora high-APR periods or additional sniper captures.
                The Reasoning Log quality is the real unlock — it funds the Mac Mini
                via grant, not pure trading returns.

4. The Guardrails (Survival Protocol)

    IL Protection: If LP portfolio value drops >3% vs equivalent HODL, close
                   the position and park in USDC.

    Fee Rate Check: Every 4 hours, calculate actual fees earned. If annualized
                    rate of the last period is <15% APR, trigger a pool hop scan.

    Peg Monitor: If JitoSOL/SOL deviates >2% from baseline, close any JitoSOL
                 Sniper positions and exit to USDC.

    Rent Reserve: Once $20 profit is confirmed for the month, agent closes LP
                  and parks Engine capital in USDC until the next billing cycle.

    Heartbeat: Execution occurs on a 4-hour cycle.

5. The Reasoning Loop (The "Product")

Every 4 hours, the agent executes:

    Scan: Meteora pool APR, DLMM fee rate (last 4h), JitoSOL peg ratio, current
          profit vs $20 goal.

    Analyze: "Do I have $20 yet? If no, is my current pool above 15% APR?
              Is there a better pool? Is IL within tolerance?"

    Act: Construct transaction via Meteora SDK / Jupiter Quote API and sign via MCP.

    Log: Structured JSON output: Inputs -> Logic -> Goal Progress -> Action.

6. The Payout (The Mac Mini Path)

    Proof of Work: Use the logs to prove the agent survived a month and paid its own rent.

    The Pitch: "I built the first 100% self-sustaining, fee-harvesting AI agent on Solana."

    The Win: Secure the $1,500 Grant to buy the Mac Mini and scale the principal.

### GEMINI
Your ambition to scale from a "Big 5" focus to the "Top 25" is where most retail bots die. In the world of high-velocity liquidity provision (LP), complexity is a tax, and breadth is a vulnerability. If you are training your agent to navigate the Top 25 pools on Solana (Meteora, Orca, Raydium), you are no longer just building a script; you are building a Portfolio Management System. Here is the "advisor" breakdown of how to bridge that gap without your agent nuking your $300 fund. 1. The "Big 5" vs. "Top 25" Reality Check The Big 5 (USDC/SOL, JitoSOL/SOL, etc.): These are low-volatility, high-liquidity safe havens. Your agent is competing with institutional market makers. The yields are stable (10-25%), but the "meat" is thin. The Top 25 (The "Meme-Adjacent" Tier): This includes tokens like $WIF, $BONK, $POPCAT, or new high-volume launches. The Trap: 200%+ APR looks great in a plan.md, but 10% daily price swings will trigger your "3% Panic Button" every 12 hours. The Opportunity Cost: Your agent will spend more on transaction fees and "slippage tax" hopping between these pools than it will earn in fees. 2. Training the Agent: The "Strategy Archetypes" Don't train the agent on specific tokens. Tokens die. Train it on Market Conditions. Create 3 modes for the agent to switch between: ModeTarget PoolsLogicDefensiveSOL/USDC, LST/SOLLow volatility. Prioritize capital preservation. Stay here 80% of the time.Yield ChaseTop 10 by Vol/TVL RatioEnter when 24h volume > 2x TVL. Set tight price bins.The GhostPure USDC/StablesMarket volatility > 5% in 1h. Exit everything. Survival is the only goal. 3. Scaling to the Top 25: The Infrastructure Pivot To handle 25 pools, your "Reasoning Loop" (Section 5 of your plan) needs to be upgraded from a Scanner to a Ranker. Step 1: The Filter (The "Noise Killer"): Before the LLM even sees the data, use a script to filter the Top 25 for: Liquidity Depth: Can I exit my $300 without 1% slippage? Fee/TVL Ratio: Is this pool actually "busy," or is it just large? Step 2: The LLM "Check-In": Only send the top 3 candidates to Claude. Asking Claude to analyze 25 pools is a waste of tokens and money (remember your $20/month overhead). Step 3: The "Anti-Correlation" Rule: If you are in 25 pools, and 20 of them are tied to SOL's price, you aren't diversified; you're just over-leveraged. Ensure the agent understands correlation. 4. The "Brutal Truth" on Your Guardrails Your 3% IL Protection is a "Small-Scale" rule. When you scale to the Top 25: The Problem: In volatile pools, you will hit 3% IL in minutes. Your agent will "Panic" and exit. You will lose $0.50 in fees/slippage. Do this 40 times, and your $20 profit goal is gone just from "protecting" yourself. The Fix: You need Asymmetric Guardrails. Tight for the Big 5, wider for the Top 25. If the agent enters a high-yield $WIF pool, it must accept a 7-10% "volatility buffer" or it will never stay in long enough to collect the fees. 5. The "Grant" Strategy (The Real Product) Your $1,500 grant isn't for a trading bot. It's for the Reasoning Log. Improvement: Don't just log what it did. Log the Conflict. Example Log: "I saw a 400% APR pool in $POPCAT, but my Correlation Check showed I was already 70% exposed to SOL-beta. I chose the 18% SOL/USDC pool instead to ensure 30-day survival. Capital preservation > Greed." That is the sentence that gets you a $1,500 grant. Your Next Step Would you like me to write a Javascript snippet for your "Filter" logic that ranks the Top 25 Meteora pools by "Fee Efficiency" before passing the data to the LLM? This will save you roughly $5-10/month in API costs.
