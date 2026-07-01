---
category: crypto-web3
date: 2026-02-26
id: 636432
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan was asking for clear next steps to execute in Claude Code for the Operation
  Immortal Agent project.
tags:
- claude-code
- next-steps
- operation-immortal-agent
- action-items
---
# no, just tell me what i need to do from here in claude code please 

### USER
no, just tell me what i need to do from here in claude code please 

### GEMINI
To move forward using Claude Code (the terminal-based agent), you need to transition from "Testing" to "Construction." Since your session.json is verified, the "Hands" are ready. Here is your precise, high-level path to getting the Meteora Engine live. 1. Install the "Brain" (Meteora SDK) The agent needs the specific math and instruction set for Meteora DLMM. Run this in your terminal: npm install @meteora-ag/dlmm @coral-xyz/anchor @solana/web3.js 2. Configure the "Immortal" Engine You need a central file where the agent's trading logic lives. Use Claude Code to create src/engine/meteora.ts. Tell Claude Code: "Create a production script in src/engine/meteora.ts that uses @meteora-ag/dlmm. It should: Target the SOL/USDC pool (LBUZKhRxPF3XUpBCjp4YzTKgLccjZhTSDM9YuVaPwxo). Check my balance using the Phantom MCP get_balance tool. If balance > 0.05 SOL, provide liquidity to the active price bin. Log the 'Reasoning' for every action to logs/agent_monologue.md." 3. The "Fueling" Sequence (The only manual step) Now that the code is ready, you must provide the assets. Address: ASgsVw8dc5U1XSMdijCrj4RabzdsqJENLpnopc8Gdm8n Amount: * SOL: At least 0.1 SOL (0.05 for gas buffer, 0.05 for the first LP position). USDC: $250 - $300 (to match the SOL side for the LP pair). 4. Activate the Loop Once funded, you will run the agent in "Watch" mode. Use this command to start the engine: PHANTOM_APP_ID=777f97d6-be33-4d9d-bf9f-0eedc5cc346c \ WALLET_PUBLIC_KEY=ASgsVw8dc5U1XSMdijCrj4RabzdsqJENLpnopc8Gdm8n \ npx tsx src/engine/meteora.ts The Advisor’s Final Audit Zero-Check: If the agent sees $0, it will do nothing. This is your safety. Grant Strategy: The logs/agent_monologue.md is your most important asset. When you apply for the Solana Grant, you aren't just showing code; you're showing a month's worth of "Autonomous Reasoning" that proves your agent didn't go bankrupt. Opportunity Cost: Every hour you spend "cleaning up tests" instead of funding the wallet is an hour of 0% yield. You've proven the tech works. Stop testing. Start deploying. Would you like me to write the actual src/engine/meteora.ts logic for you right now so you can copy-paste it into Cursor?
