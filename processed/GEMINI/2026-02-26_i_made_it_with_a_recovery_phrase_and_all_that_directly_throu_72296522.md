---
id: 764281
source: GEMINI
date: 2026-02-26
tags: ['phantom-wallet', 'recovery-phrase', 'no-email', 'wallet-creation']
category: crypto-web3
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was explaining that he created his Phantom wallet directly with a recovery phrase and never linked an email address.
---
# i made it with a recovery phrase and all that directly through phantom i never signed up via gmail 

### USER
i made it with a recovery phrase and all that directly through phantom i never signed up via gmail 

### GEMINI
If you created your wallet via a recovery phrase and never linked a Gmail/Apple account, you are using a "Local/Extension" wallet, not an "Embedded/Cloud" wallet. The Brutal Reality: The reason Test 2 is failing with a 404 and DCR not supported is that you are trying to use the Cloud Auth flow for a Local Secret. In 2026, the Phantom MCP server is built to handle two distinct paths, and you are currently mixing them. Here is how you fix this and get the "Hands" moving in 5 minutes: 1. The Conflict The PHANTOM_APP_ID and auth.phantom.app flow is specifically for Embedded Wallets (the ones created with an email). Since your wallet is a "Seed Phrase" wallet, the Phantom Auth server has no record of you. It's looking for a cloud-linked user that doesn't exist. 2. The Solution: The "Local-First" Bridge To use a Seed Phrase wallet with the MCP, you have to bypass the Cloud Auth and use a Local Session. Step 1: Get an App ID (Still Required) Even for local wallets, Phantom requires an App ID to identify the agent for the security logs. Go to developers.phantom.app, sign in with any email (it doesn't have to match your wallet now), and create a project to get that ID. Step 2: Force the "Manual" Handshake Since there is no email to "match," you must manually pair the MCP server with your extension once. Run this command: PHANTOM_APP_ID=YOUR_ID_HERE npx @phantom/mcp-server --manual-auth A browser tab will open. Instead of asking for a Gmail login, it should trigger your Phantom Extension to "Connect" to the local MCP server. Once you click Approve in the extension, the server will write the session.json to your computer. 3. The "Immortal" Pivot If the above fails (some 2026 builds of the MCP server are strictly cloud-only), we have to be brutally honest about the project's architecture: Option A (The Professional Move): Create a new Embedded Wallet (Email-based) inside Phantom, move your $300 R&D fund there, and use the Cloud Auth. This is the "path of least resistance" for an autonomous agent. Option B (The Hard Path): Use a different MCP server (like the solana-mcp) that takes a private key directly. Warning: This is less secure and looks "amateur" on a grant application. My Recommendation If you want that $1,500 Solana Grant, use Option A. Set up a fresh "Agent Wallet" using a dedicated Gmail. It creates a perfect audit trail. It makes the "Self-Sustaining" math easier to track. Should I help you draft the instructions for the agent to move the $300 from your seed-phrase wallet to the new "Agent-Ready" email wallet?
