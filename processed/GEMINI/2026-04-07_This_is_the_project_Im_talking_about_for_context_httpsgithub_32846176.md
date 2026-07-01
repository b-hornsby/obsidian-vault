---
id: 197833
source: GEMINI
date: 2026-04-07
tags: ['self-sustained-agent', 'github-reference', 'open-source-agent', 'project-context']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan shared a GitHub link to the 'self_sustained_agent' project as context for what he was building.
---
# This is the project I’m talking about for context https://github.com/toastedmel0n/self_sustained_agent

### USER
This is the project I’m talking about for context https://github.com/toastedmel0n/self_sustained_agent

### GEMINI
I see exactly where you are now. By looking at the naming convention and your goal, it’s clear: Project Immortal was your attempt to solve the "AI overhead" problem by creating a closed-loop economy. The repo was meant to be the "financial organ" of your Second Me. It uses Meteora DLMM (Dynamic Liquidity Market Maker) because of the high capital efficiency and fee generation. The "Phantom MCP" was your bridge to allow an AI (like Claude) to sign transactions safely. The Pivot: From Repo to "Sustain Skill" Since you haven't finished the code, you should stop trying to build a standalone "Self-Sustained Agent" app and instead convert that repo's logic into a Skill Node in Obsidian. Here is how you do it: 1. The "Logic Transfer" (Don't lose the Alpha) The most valuable part of your repo isn't the TypeScript boilerplate; it’s the Strategy. You likely have logic for: Which pools to target (e.g., SOL/USDC vs. high-volatility memecoin pairs). The "Rebalance Trigger" (when to move liquidity to stay in range). The "Claim & Convert" loop (taking fees and turning them into API credits). Action: Take your main logic file from GitHub and paste it into Hermes. Tell it: "Summarize the financial strategy in this code into a set of 'If/Then' rules for an Obsidian Skill Node." 2. Swap "Custom Code" for "Standard MCP" You were building a custom Phantom MCP. To save time, don't finish it. Use a community-vetted Solana/Meteora MCP (like the one by fciaf420 mentioned in the search results). This gives Hermes the tools: get_pool_info, claim_fees, add_liquidity. The Skill Node in Obsidian then tells Hermes when and how to use those tools based on the logic you already started in your repo. 3. Security: The "Public Wallet" Issue You mentioned your public wallet is in that project. On GitHub: If your private key or sensitive info was ever committed, consider it burned. Rotate to a new wallet. In the Skill Node: In your Skills/Finance/Meteora_Sustain.md file, only include your Public Key. In Tiny11/Docker: Keep the Private Key in a .env file that the MCP server reads. Hermes uses the skill to decide to trade, but it never actually "sees" the key; it just sends the command to the MCP "harness." The New "Immortal" Blueprint Instead of a separate GitHub project, your "Self-Sustained" feature becomes a background task for your Second Me: The Memory: Obsidian stores the Meteora_Sustain.md (Strategy) and Wallet_Ledger.md (History). The Brain: Hermes checks the Meteora pools once a day via MCP. The Goal: It claims enough fees to top up your API credits, ensuring it can literally "pay its own rent" to keep existing on your Tiny11 machine. Why this is better: If you keep it as a GitHub project, it’s a separate tool you have to manage. If it’s a Skill, it is a part of you. Your "Second Me" becomes an entity that manages its own heart (the wallet) and lungs (the API credits). Does this help you see how to "harvest" the work you did on GitHub without having to actually finish the coding?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
