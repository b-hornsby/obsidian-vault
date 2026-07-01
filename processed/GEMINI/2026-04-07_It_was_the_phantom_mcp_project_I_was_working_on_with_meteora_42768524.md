---
id: 249713
source: GEMINI
date: 2026-04-07
tags: ['phantom-mcp', 'meteora-dlmm', 'solana-trading-bot', 'claude-api-costs']
category: crypto-web3
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan explains that the Phantom MCP project with Meteora DLMM pools was intended to make Claude code pay for itself.
---
# It was the phantom mcp project I was working on with meteora dlmm pools. It was supposed to allow Claude code to pay for itself so I could keep using it

### USER
It was the phantom mcp project I was working on with meteora dlmm pools. It was supposed to allow Claude code to pay for itself so I could keep using it

### GEMINI
That explains the GitHub commit perfectly. You weren't just building a bot; you were building a Self-Sustaining Infrastructure—an AI that yields its own "rent" via DeFi. The "Immortal" part now makes total sense: if the agent stops, the DLMM positions aren't being managed, the fees aren't being claimed, and the funding for the Claude API keys dries up. The project literally "dies." Here is how you pivot that specific Phantom/Meteora repo into a Skill Node for your Hermes/Obsidian setup: 1. The "Skill" is the Strategy, not the Script Instead of trying to finish the TypeScript/Bun process that manages the Meteora pools, you move the Decision Logic to Obsidian. Your new Skill Node (Skills/Finance/Meteora_Sustain.md) should contain: Pool Selection Logic: The specific parameters (Bin Step, Fee Tier, Volatility) you were hardcoding. The "Claude Rent" Threshold: A rule that says: "When unclaimed fees reach $25, execute meteora_claim_fees and swap to USDC to cover next month's API limit." Active Rebalancing: Rules for when a DLMM position goes "Out of Range" (OOR). Instead of code, use logic: "If price > max_bin, shift liquidity 5% higher." 2. Use Existing MCP Tools (Don't Rebuild) You don't need to finish your custom Phantom MCP if you use what’s already out there. There are now robust Meteora DLMM MCP servers (like the fciaf420 one) that already have tools like meteora_add_liquidity and meteora_claim_fees. The Pivot: Delete your unfinished "harness" code. The New Flow: Hermes (the agent) reads your Meteora Sustain Skill from Obsidian, then uses a standardized Meteora MCP to execute the trades. 3. Handling the Wallet Securely Since you mentioned your public wallet was in the project: The Skill Node should only reference your Public Key for balance checks. The Private Key should live in your Docker .env file or a local keypair.json that the MCP server points to. Never let the skill logic "know" the private key; it only knows it has the permission to ask the MCP to "Sign & Send." The "Project Immortal" Vision (v2.0) By making this a skill, you’ve actually achieved "Immortality" better than a GitHub repo could: Persistence: Your strategy is stored in Markdown. Even if Meteora’s API changes, you just update the text of the skill. Self-Correction: Because Hermes can reason, it can look at the DLMM pool and say, "Hey, the volume on this pair dropped, this won't pay for Claude this month. Should I move to the SOL/USDC high-fee pool?" Low Overhead: You aren't running a heavy background process. You just have a cron job (or an Obsidian reminder) that wakes Hermes up once a day to "Check Sustainability." Does this pivot feel like it saves the core "dream" of the project without the headache of finishing the custom code? (Also, quick tip: If you're using Meteora DLMM, make sure your skill includes a "Jito Tip" rule so your rebalancing transactions actually land during high volatility!)


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/operation-immortal-agent|Operation Immortal Agent]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/crypto-web3|Crypto Web3]]
