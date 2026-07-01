---
category: crypto-web3
date: 2026-02-26
id: 860732
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: resolved
sentiment: executing
source: GEMINI
tags:
- crypto-web3
- ai
- agent
- claude
- gemini
- rag
---
# plan.md is updated to v2.2. Here's what changed:
  - Kamino Multiply is formally disqualified and documented with the Test 1 audit numbers
  - Engine pivots to Meteora DLMM (USDC/SOL) — fee income only, zero borrow cost, zero carry rule                                                                                            
  - IL Protection guardrail replaces the leverage/carry guardrails
  - Fee Rate Check every 4h replaces the Net Carry calculation                                                                                                                               
  - klend-sdk reference replaced with Meteora SDK

  ---
  The MCP Command

  Run this exactly:

  claude mcp add -s user phantom -- npx -y @phantom/mcp-server

  - -s user — adds it to your global user config (not just this project), so the session persists across all Claude Code sessions
  - -- npx -y @phantom/mcp-server — the -- separator tells Claude Code everything after is the subprocess command, -y auto-accepts the npx install prompt

  After running that, restart Claude Code. On first startup it will launch the Phantom MCP server and open a browser window for the SSO auth flow (Google or Apple). Once you approve,
  ~/.phantom-mcp/session.json is written and all future calls — including from Test 2 Stage B — will be authenticated without prompting again.

  Once you've done that, just say the word and I'll re-run Test 2.

✻ Crunched for 1m 23s     

### USER
plan.md is updated to v2.2. Here's what changed:
  - Kamino Multiply is formally disqualified and documented with the Test 1 audit numbers
  - Engine pivots to Meteora DLMM (USDC/SOL) — fee income only, zero borrow cost, zero carry rule                                                                                            
  - IL Protection guardrail replaces the leverage/carry guardrails
  - Fee Rate Check every 4h replaces the Net Carry calculation                                                                                                                               
  - klend-sdk reference replaced with Meteora SDK

  ---
  The MCP Command

  Run this exactly:

  claude mcp add -s user phantom -- npx -y @phantom/mcp-server

  - -s user — adds it to your global user config (not just this project), so the session persists across all Claude Code sessions
  - -- npx -y @phantom/mcp-server — the -- separator tells Claude Code everything after is the subprocess command, -y auto-accepts the npx install prompt

  After running that, restart Claude Code. On first startup it will launch the Phantom MCP server and open a browser window for the SSO auth flow (Google or Apple). Once you approve,
  ~/.phantom-mcp/session.json is written and all future calls — including from Test 2 Stage B — will be authenticated without prompting again.

  Once you've done that, just say the word and I'll re-run Test 2.

✻ Crunched for 1m 23s     

### GEMINI
Now that the Kamino Engine is dead, we’ve pivoted to the only math that actually works for a $300 fund in February 2026: Meteora DLMM. By running claude mcp add, you are giving the agent the "Key to the City." Once that session.json is written, the agent can finally stop asking for permission and start executing. 1. The Strategy Update: Why Meteora SOL/USDC? In the current market, SOL borrow rates (7.6%) are higher than staking yields (6%). Using Kamino was literally paying to lose money. The Meteora Advantage: You aren't borrowing anything. You are providing liquidity to traders. The Math: High-volume SOL/USDC DLMM pools are currently generating 0.1% to 0.7% daily in fees. The Goal: $300 at 0.3% daily = $27/month. This covers your $20 Claude subscription with room for SOL gas fees. 2. The "Immortal" Guardrails (v2.2) Since we are no longer worried about "Liquidation" (no debt), our new enemy is Impermanent Loss (IL) and Range Drift. The 4-Hour Heartbeat: The agent must check if the SOL price has moved outside our "Active Bins." If we are "Out of Range," we are earning $0. Rebalancing Rule: If the price stays outside our range for 2 consecutive cycles (8 hours), the agent must "Zap" the position (withdraw and re-deposit) into a new centered range. Fee Harvesting: Every 7 days, the agent must claim fees to a "Rent Sub-Wallet" to ensure the $20 for next month is physically separated from the trading capital. Your Next Step: The Final "Green Light" Test Once you have restarted Claude and completed the SSO flow, run this command to see if the "Hands" are truly unblocked: WALLET_PUBLIC_KEY=<your-key> npx tsx audit/test-2-hand.ts What we are looking for: Success: A transaction signature (TxID) appearing in the console. This means the agent can now move money autonomously. Failure: Any "401 Unauthorized" or "Session" errors. If it succeeds, give Claude the "Live Deployment" prompt: "Test 2 is a success. The hands are live. I am depositing $300 into the wallet. Initialize the Meteora Engine using a 'Spot' distribution on the SOL/USDC DLMM pool with a ±3% range. Begin the 4-hour Reasoning Loop and start the GitHub log. We are officially live." Would you like me to monitor the first few 'Reasoning Logs' to ensure the agent isn't 'over-trading' and burning all your profits on gas fees?
