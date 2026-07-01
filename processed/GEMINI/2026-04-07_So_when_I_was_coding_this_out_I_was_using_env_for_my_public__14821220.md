---
category: crypto-web3
date: 2026-04-07
id: 614731
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking whether he still needs to use a .env file for his public
  wallet when converting his code into a reusable skill.
tags:
- env-file
- wallet-security
- skill-conversion
- solana-wallet
---
# So when I was coding this out I was using .env for my public wallet. Do I need to do that when I’m converting this to a skill?

### USER
So when I was coding this out I was using .env for my public wallet. Do I need to do that when I’m converting this to a skill?

### GEMINI
Yes, you still need an environment variable, but you’re moving it from your project’s .env file to the MCP Server’s configuration. In your old setup, your code was manually pulling the address to know where to send transactions. In the "Skill" model, the Phantom MCP server (the "hands") acts as the gatekeeper. Where the Wallet Address Lives Now Since you are using the official Phantom MCP server (launched Feb 2026), you don't put the wallet address inside your Obsidian Skill Node (for privacy). Instead, you define it in your MCP configuration file (likely claude_desktop_config.json or your Docker Compose file). Here is the standard setup for your Tiny11 machine: { "mcpServers": { "phantom": { "command": "npx", "args": ["-y", "@phantom/mcp-server"], "env": { "PHANTOM_APP_ID": "YOUR_APP_ID", "SOLANA_WALLET": "YOUR_PUBLIC_WALLET_ADDRESS", "RPC_URL": "https://api.mainnet-beta.solana.com" } } } } Why this is better for "Operation Immortal" Security: Your public wallet address isn't hardcoded in your "Second Me" brain or your GitHub logs. It stays in a local config file on your machine. The "Hands" are Fixed: By setting the SOLANA_WALLET variable here, the Phantom MCP tool will only interact with that address. When Hermes says "Check the balance," the MCP already knows which wallet to check. Session Persistence: The official Phantom MCP (v0.1.1+) uses a session.json file in your local directory. This means once you authenticate, the agent stays "Immortal" across reboots without you needing to sign in every time. Do you need a .env for the Skill? No. The Skill itself (in Obsidian) should just refer to the wallet abstractly. Your Strategy.md should say: "Check the primary wallet balance using the Phantom MCP. If profit > $20, move to savings." The AI is smart enough to know that "the primary wallet" is whatever the Phantom MCP is currently controlling. The "Operation Immortal" Checklist To pivot correctly today: [ ] Locate your Phantom App ID: You'll need this for the new MCP server. [ ] Update your Config: Put your public address in the env section of your MCP settings as shown above. [ ] Create the Ledger: In Obsidian, create Immortal_Ledger.md. This replaces your .env logs. One final piece of advice: Since you're dealing with $300 and a Mac Mini goal, I'd suggest keeping one "Secret" file in your vault called Vault/Private/Keys.md.encrypted (or just keep it out of Obsidian entirely). Only the Public Address should ever be visible to the AI's reasoning. Does that help clear up where the "connection" happens now? It's all about the MCP Config being the bridge.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
