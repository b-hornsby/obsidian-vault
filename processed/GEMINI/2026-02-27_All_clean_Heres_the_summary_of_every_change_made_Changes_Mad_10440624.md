---
id: 756178
source: GEMINI
date: 2026-02-27
tags: ['solana-trading-bot', 'dlmm', 'risk-management', 'phantom-mcp', 'code-summary']
category: crypto-web3
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan is reviewing a summary of changes made to his Solana trading bot, including on-chain position checks, EXIT directives, and Phantom MCP testing.
---
# All clean. Here's the summary of every change made.                                                                                                                                                                 
                                                                                                                                                                                                                      
  ---                                                                                                                                                                                                                 
  Changes Made
                                                                                                                                                                                                                      
  1. Scan Phase — On-chain Position Check (scanExistingPositions)                                                                                                                                                   

  New function that calls dlmmPool.getPositionsByUserAndLbPair(walletPubkey) directly from the chain every cycle — not from agent_state.json. It:
  - Returns all LbPosition[] in the USDC/SOL pool for your wallet
  - Converts totalXAmount (USDC) to SOL-equivalent using activeBin.pricePerToken
  - Calculates retentionRatio and ilPercent vs state.initialDepositSol
  - The DLMM pool is now created once per cycle and shared between the scan and any transaction building (removed the duplicate DLMM.create call)
  - state.initialDepositSol accumulates with each deploySol on open, resets to 0 on EXIT

  2. Brain Prompt — EXIT Directive

  BrainDecision.decision is now "GO" | "NO_GO" | "EXIT". The prompt has an explicit ⚠️  EMERGENCY EXIT DIRECTIVE section that:
  - Shows the current retentionRatio and whether EXIT is required
  - States clearly it overrides APR and all other factors
  - Is pre-evaluated inline: EXIT required: YES/NO so the model sees the answer it should give

  Defense-in-depth: A hardcoded IL guardrail also fires before the Brain call. If retentionRatio < 0.97 and a position exists, executeExit() is called immediately — the Brain never gets consulted. This ensures the
  IL trip works even if the Anthropic API is down.

  3. Phantom MCP Test Command

  npx tsx scripts/test-phantom.ts

  The script:
  1. Resolves @phantom/mcp-server locally — fails fast with a clear message if not installed
  2. Connects via StdioClientTransport, lists available tools, and checks for sign_transaction and get_wallet_addresses
  3. Calls get_wallet_addresses (read-only — no transaction is sent or signed)
  4. Cross-checks the returned Solana address against your WALLET_PUBLIC_KEY env var

  This confirms your env vars are wired correctly before you risk any real capital.

✻ Baked for 6m 22s                     

### USER
All clean. Here's the summary of every change made.                                                                                                                                                                 
                                                                                                                                                                                                                      
  ---                                                                                                                                                                                                                 
  Changes Made
                                                                                                                                                                                                                      
  1. Scan Phase — On-chain Position Check (scanExistingPositions)                                                                                                                                                   

  New function that calls dlmmPool.getPositionsByUserAndLbPair(walletPubkey) directly from the chain every cycle — not from agent_state.json. It:
  - Returns all LbPosition[] in the USDC/SOL pool for your wallet
  - Converts totalXAmount (USDC) to SOL-equivalent using activeBin.pricePerToken
  - Calculates retentionRatio and ilPercent vs state.initialDepositSol
  - The DLMM pool is now created once per cycle and shared between the scan and any transaction building (removed the duplicate DLMM.create call)
  - state.initialDepositSol accumulates with each deploySol on open, resets to 0 on EXIT

  2. Brain Prompt — EXIT Directive

  BrainDecision.decision is now "GO" | "NO_GO" | "EXIT". The prompt has an explicit ⚠️  EMERGENCY EXIT DIRECTIVE section that:
  - Shows the current retentionRatio and whether EXIT is required
  - States clearly it overrides APR and all other factors
  - Is pre-evaluated inline: EXIT required: YES/NO so the model sees the answer it should give

  Defense-in-depth: A hardcoded IL guardrail also fires before the Brain call. If retentionRatio < 0.97 and a position exists, executeExit() is called immediately — the Brain never gets consulted. This ensures the
  IL trip works even if the Anthropic API is down.

  3. Phantom MCP Test Command

  npx tsx scripts/test-phantom.ts

  The script:
  1. Resolves @phantom/mcp-server locally — fails fast with a clear message if not installed
  2. Connects via StdioClientTransport, lists available tools, and checks for sign_transaction and get_wallet_addresses
  3. Calls get_wallet_addresses (read-only — no transaction is sent or signed)
  4. Cross-checks the returned Solana address against your WALLET_PUBLIC_KEY env var

  This confirms your env vars are wired correctly before you risk any real capital.

✻ Baked for 6m 22s                     

### GEMINI
The system now has integrity. You’ve moved from a brittle, file-dependent script to a chain-aware protocol with a "Dead Man's Switch." However, as your advisor, I need to point out the tactical transition you are about to make. You are moving from the "Design" phase to the "Execution" phase. In this transition, the greatest risk is no longer the code—it's environment friction. The Reality Check The "Exit" is the hardest part: It's easy to code an executeExit(). It's much harder to execute it during a period of high network congestion (which usually happens when the price is crashing). If the RPC is lagging, your "3% IL Guardrail" could slip to 10% before a transaction lands. The Silent Killer: Your script uses setInterval for a 4-hour heartbeat. If the process crashes due to a memory leak or a transient Fly.io error, it doesn't "restart" unless you have a process manager (like Docker's restart policy) watching it. Final Pre-Flight Verification Before you run that test-phantom.ts script, verify these two "hidden" assumptions in your setup: Priority Fees: Does your executeExit() function include a dynamic priority fee? If you are trying to exit a losing position during a SOL sell-off without a priority fee, your transaction will sit in the mempool while your 3% loss turns into a 6% loss. The RPC Tier: If you are using a public or "Free Tier" RPC, the getTransaction() call in the Verify stage will likely be rate-limited or return null because the data hasn't indexed yet. This will make the agent think the transaction failed when it actually succeeded (the "Double Spend" risk). The Precision Plan for the Next 60 Minutes 1. Run the Phantom Test Run npx tsx scripts/test-phantom.ts. If it fails: Do not pass go. Usually, this is a PATH issue or a missing env var. If it passes: Move to the "Tiny Capital" test. 2. The "Dust" Transaction Do not deploy to Fly.io yet. Run the agent locally with 0.01 SOL. Manually set your initialDepositSol in the JSON to a value higher than your current balance to trigger a forced EXIT. Observe the agent: Does it recognize the "loss," skip the Brain, call the MCP, and successfully broadcast? 3. Monitor the Monologue Open logs/agent_monologue.md. If it’s just a wall of text, it’s useless. It should look like a flight recorder. What I can do for you now: I can help you harden the transaction logic. Specifically, would you like me to show you how to add a Priority Fee instruction to the Meteora transaction? This ensures that when the "Emergency Exit" fires, it actually gets through the Solana network congestion. Shall we add the "Gas Pedal" (Priority Fees) to your Exit logic?
