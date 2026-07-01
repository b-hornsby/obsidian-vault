---
id: 721373
source: GEMINI
date: 2026-02-26
tags: ['claude-code', 'project-initiation', 'plan-md', 'self-sustaining-agent']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was trying to figure out how to prompt Claude Code to start working on his self-sustaining agent project based on his plan.md.
---
# so now that this is in my plan.md what do i tell claude to get this started? 

### USER
so now that this is in my plan.md what do i tell claude to get this started? 

### GEMINI
To get Claude started, you need to move him from "Advisor Mode" to "Engineer Mode." Since the Phantom MCP is the newest and most restricted part of the stack, you must force Claude to prove he can actually drive the "Hands." Copy and paste this exact prompt. It uses the specific technical terminology for the February 2026 stack to ensure he doesn't give you a generic response. The "Phase 1: Tool-Check" Prompt Copy and paste this to Claude: "I have updated plan.md to v2.1. The mission is now Self-Sustaining Autonomy: $20/month profit target to cover your own subscription. To achieve this, we are using the High-Efficiency Pivot (Kamino Yield-Hopping + Jupiter Limit Order Sniper). Before we write any core logic, we must pass the Capability Audit. I need you to act as the lead engineer and perform the following three 'Hand-Eye Coordination' tests using the Phantom MCP tools: 1. The 'Eye' Test (Data Retrieval): Fetch the current JitoSOL/SOL price ratio from the Jupiter Price API and the current 'Net APR' for the JitoSOL Multiply market on Kamino. Goal: Verify you can parse these and calculate if the 'Net Carry' is positive. 2. The 'Hand' Test (Transaction Construction): Draft the code for a $1 Test Swap (SOL to JitoSOL) using the Jupiter Swap API. Constraint: You must show me how you will take the swapTransaction (base64) from Jupiter and pass it to the Phantom MCP sign_transaction tool. 3. The 'Sniper' Test (Limit Order Logic): Show me the JSON payload for creating a Jupiter Limit Order at 1% below the current JitoSOL peg. Critical: Confirm if the Phantom MCP sign_transaction tool can handle the complex instructions required for a limit-orders/create call, or if we need to use a simpler swap-based strategy. Do not write the whole agent yet. Provide the specific code snippets for these three tests so we can verify the 'Hands' are functional. Once these pass, we deploy the $300." Why this prompt works: Forces Technical Specificity: By asking for the "base64" handling and "JSON payload," you prevent him from being "helpful" and vague. Validates the "Self-Sustaining" Math: By making him check the "Net Carry," you're making him do the math on the $20/month target immediately. Identifies the Bottleneck: If he struggles to explain how sign_transaction handles a Limit Order, you know your "Sniper" strategy needs to be simplified before you lose money on failed transactions. When he replies, look for the code. If he gives you more "advice" without code, tell him: "Stop advising. Show me the TypeScript implementation for the sign_transaction call." Would you like me to review his code once he generates it to make sure he isn't missing a 'Priority Fee' instruction that will cause your trades to fail?
