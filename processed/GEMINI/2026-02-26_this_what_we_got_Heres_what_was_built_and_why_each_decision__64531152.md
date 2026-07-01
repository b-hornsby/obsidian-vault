---
id: 089201
source: GEMINI
date: 2026-02-26
tags: ['phantom-mcp', 'jupiter-api', 'kamino', 'testing-pipeline', 'defi-agent']
category: crypto-web3
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was reviewing the three-test pipeline built for the DeFi agent and the critical unknown around Phantom MCP's program allowlist.
---
# this what we got: Here's what was built and why each decision was made:
                                                                      
  ---
  The Three Tests                                                                                                                                                                            
   
  Test 1 (test-1-eye.ts) — Zero risk                                                                                                                                                         
  Hits the Jupiter Price API and Kamino REST API, calculates Net Carry, and runs the Net Carry Rule check. It also includes the klend-sdk fallback (commented out) if the REST endpoint 404s.
   Run this first — if Net Carry is negative today, the Engine strategy needs to wait.

  Test 2 (test-2-hand.ts) — $1.50 max risk
  Shows the full pipeline: Jupiter Quote → buildSwapTransaction → base64 tx → Phantom MCP sign_transaction. The EXECUTE = false gate at the top is critical — review the dry-run output
  before flipping it. Also includes the direct MCP client approach (commented out) which bypasses Claude entirely and tests the raw tool I/O — this is the cleanest audit method.

  Test 3 (test-3-sniper.ts) — Zero risk (dry run only)
  Constructs the limit order payload, fetches the unsigned transaction from Jupiter's Limit Order v2 API, and runs a compatibility check on the transaction type. The decision tree at the
  bottom covers all three failure modes with explicit pivots.

  ---
  The Critical Unknown

  The biggest risk is whether Phantom MCP has a program allowlist. The buy_token tool uses Phantom's own quote API (guaranteed to work). But sign_transaction with an arbitrary program —
  like the Jupiter Limit Order program (jupoNjAxXgZ4rjzxHtggB2rBE4B8R2KMqYNYBNYdFBM7) or Kamino's lending program — may get rejected if Phantom gates which programs can be signed for.

  Test 2 will answer this. If it rejects with an "unauthorized program" error, the sniper pivots to buy_token with tight slippage, and Kamino Multiply requires the raw Solana RPC approach.

  ---
  Leverage Flag

  Plan v2.1 says 3x. idk.md guardrail says 2.1x. Test 1 calculates Net Carry at 2.1x — the safer number. You should resolve this before the Engine goes live.

✻ Churned for 3m 41s                       
                                                                      
────────────────────────────────────────────────────────────────────────────────────────────────────────────                                                                                                                                                                  
                                                                                                                                                                                             

### USER
this what we got: Here's what was built and why each decision was made:
                                                                      
  ---
  The Three Tests                                                                                                                                                                            
   
  Test 1 (test-1-eye.ts) — Zero risk                                                                                                                                                         
  Hits the Jupiter Price API and Kamino REST API, calculates Net Carry, and runs the Net Carry Rule check. It also includes the klend-sdk fallback (commented out) if the REST endpoint 404s.
   Run this first — if Net Carry is negative today, the Engine strategy needs to wait.

  Test 2 (test-2-hand.ts) — $1.50 max risk
  Shows the full pipeline: Jupiter Quote → buildSwapTransaction → base64 tx → Phantom MCP sign_transaction. The EXECUTE = false gate at the top is critical — review the dry-run output
  before flipping it. Also includes the direct MCP client approach (commented out) which bypasses Claude entirely and tests the raw tool I/O — this is the cleanest audit method.

  Test 3 (test-3-sniper.ts) — Zero risk (dry run only)
  Constructs the limit order payload, fetches the unsigned transaction from Jupiter's Limit Order v2 API, and runs a compatibility check on the transaction type. The decision tree at the
  bottom covers all three failure modes with explicit pivots.

  ---
  The Critical Unknown

  The biggest risk is whether Phantom MCP has a program allowlist. The buy_token tool uses Phantom's own quote API (guaranteed to work). But sign_transaction with an arbitrary program —
  like the Jupiter Limit Order program (jupoNjAxXgZ4rjzxHtggB2rBE4B8R2KMqYNYBNYdFBM7) or Kamino's lending program — may get rejected if Phantom gates which programs can be signed for.

  Test 2 will answer this. If it rejects with an "unauthorized program" error, the sniper pivots to buy_token with tight slippage, and Kamino Multiply requires the raw Solana RPC approach.

  ---
  Leverage Flag

  Plan v2.1 says 3x. idk.md guardrail says 2.1x. Test 1 calculates Net Carry at 2.1x — the safer number. You should resolve this before the Engine goes live.

✻ Churned for 3m 41s                       
                                                                      
────────────────────────────────────────────────────────────────────────────────────────────────────────────                                                                                                                                                                  
                                                                                                                                                                                             

### GEMINI
Claude has delivered the blueprints, and they are high-quality, but Test 2 is a minefield. Here is the "brutally honest" breakdown of where your $300 is actually at risk and how to interpret the results Claude is about to give you. 1. The "Unauthorized Program" Trap (Test 2) As of early 2026, the Phantom MCP is designed for "Safe" interactions. The Problem: If you try to sign a transaction for Kamino or Jupiter Limit Orders, Phantom might throw a "Program Not Allowed" error because it hasn't white-listed those specific smart contracts for AI signing. The Reality: If Test 2 fails, you cannot do the "Engine" (Kamino) or the "Sniper" (Limit Orders) automatically. You would be forced to use the buy_token tool only, which limits you to simple swaps. The Fix: If Test 2 fails, we pivot the plan to a "Meteora Yield Strategy" because the buy_token tool usually routes through Jupiter, which includes Meteora pools. 2. The Leverage Conflict (3x vs 2.1x) Claude noticed a contradiction in your instructions. My Advisory: Stick to 2.1x. Why? To hit $20/month on $300 at 2.1x leverage, you need the "Sniper" (Limit Orders) to work. If you jump to 3x leverage, one bad day on Solana (a 5% de-peg) will wipe out your $300 principal before the agent can even log the error. The Mac Mini is more important than the $20 rent. 3. Priority Fee Management The documentation shows that Phantom defaults to "Auto" for priority fees. The Danger: In 2026, "Auto" often isn't enough to beat the other bots during a de-peg. The Demand: If Claude's code in Test 2 doesn't explicitly include a ComputeBudgetProgram.setComputeUnitPrice instruction, your "Emergency Exit" will fail when you need it most. Your Immediate Action Plan Run the three tests Claude provided. Do not put the full $300 in the wallet yet. Put in $5 worth of SOL. Run Test 1: Does he get the APR data? (If yes, the "Brain" works). Run Test 2: Try to swap $1 of SOL for JitoSOL. If this fails, STOP. It means the "Hands" are tied. Run Test 3: Check the payload. Once you have the output from Test 2 (the swap test), paste it here. I need to see if the Phantom MCP gave you a "Success" or a "Signature Restricted" error. That error code determines whether we are building a "Trading God" or just a "Price Alerter." Should I give you a 'Troubleshooting Guide' for the most common MCP connection errors now, or are you ready to run the scripts?
