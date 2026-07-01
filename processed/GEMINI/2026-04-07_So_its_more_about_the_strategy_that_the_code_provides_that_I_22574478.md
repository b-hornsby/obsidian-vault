---
id: 593847
source: GEMINI
date: 2026-04-07
tags: ['solana-wallet', 'agent-skills-vs-agents', 'phantom-mcp', 'public-wallet-security']
category: crypto-web3
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was clarifying the difference between building agents versus reusable skills, and asking how to ensure his public Solana wallet address is the one used for interactions.
---
# So it’s more about the strategy that the code provides that I can use as a skill rather than designing an entire agent to do that same action? How do I ensure that my public facing solana wallet address is the one that is interacted with

### USER
So it’s more about the strategy that the code provides that I can use as a skill rather than designing an entire agent to do that same action? How do I ensure that my public facing solana wallet address is the one that is interacted with

### GEMINI
This is the critical "security bridge" where the Skill (the brain) meets the Wallet (the money). You are exactly right: you don't want to design an entire agent "harness" just to handle one specific wallet. Instead, you configure the MCP Server to point to your public address, and the Skill tells the agent how to interact with that specific instance. 1. How to lock it to your Wallet When you use the official Phantom MCP, you don't hardcode the wallet in your strategy. You set it in your MCP Config File (usually claude_desktop_config.json or your Docker environment variables). The Config (The "Harness" level): In your Tiny11 setup, your config for the Phantom MCP looks like this: { "mcpServers": { "phantom": { "command": "npx", "args": ["-y", "@phantom/mcp-server"], "env": { "SOLANA_WALLET": "YOUR_PUBLIC_WALLET_ADDRESS_HERE", "RPC_URL": "https://api.mainnet-beta.solana.com" } } } } By putting your address here, you ensure that every time Hermes calls a "phantom" tool, it is only interacting with that specific wallet. It can't wander off to another address unless you change this master config. 2. Strategy vs. Action (The Skill's Job) The reason the Skill is better than the Agent is about "Logic Portability." The Code (What you were building): You were writing signTransaction() and checkBalance() logic. This is "Plumbing." The Skill (What you have now): You write Rules. "If the balance in the SOLANA_WALLET (defined in MCP) drops below 0.1 SOL, alert me. If profit > $20, swap to USDC." The Skill doesn't need to know how to talk to the blockchain; it just needs to know what you want to happen. The Phantom MCP handles the "How." 3. The "Immortal" Security Protocol To ensure your public wallet is the only one used, and used safely, you add Safety Guardrails directly into your Obsidian Skill Node: Identity Verification: "Before any swap, call get_address and verify it matches [Your_Public_Address]. If it doesn't, ABORT." Spend Limits: "You are authorized to move a maximum of $50 per day without a manual 'Checkpoint' file being signed by me in Obsidian." The "Phantom" Gatekeeper: Since you're using Phantom, you can set it to "Manual Confirmation" mode. Hermes proposes the trade, but your Phantom extension pops up on your screen for the final click. This is the ultimate "Immortal" safety net—the AI manages the strategy, but you keep the keys. Summary: Why this wins By moving to a Skill, you've effectively "outsourced" the hardest parts (Security, API updates, and Signing) to the Phantom team. You are left with the Pure Strategy: Input: Your $300 seed. Logic: Your Kamino/Meteora math. Output: The $20 "Claude Rent" and the Mac Mini fund. Ready to try this? Your first step is to move that "Target Address" into your MCP environment variables. Once that's done, Hermes will "see" your wallet as its only financial world. Should we write the "Verification" section of your Skill Node next to make sure Hermes always double-checks the address before trading?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/crypto-web3|Crypto Web3]]
