---
category: crypto-web3
date: 2026-02-26
id: 957470
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan created a new Phantom wallet using email signup and was asking what
  to do next.
tags:
- phantom-wallet
- new-wallet
- email-signup
- solana
---
# okay so i made a new wallet via email this time. now what? 

### USER
okay so i made a new wallet via email this time. now what? 

### GEMINI
This is the "Point of No Return." By moving to an Email Wallet, you’ve just upgraded from a "Local Script" to a "Cloud-Ready Agent." In the 2026 Solana ecosystem, this is how the big players do it. It provides the Stamper Key security that grant committees love to see. Step 1: Get the "Identity Card" (App ID) Go to developers.phantom.app. Sign in with the same Google/Apple account you just used to create your new wallet. Create a new project (e.g., "Immortal_Agent_v2"). Copy the App ID. Step 2: The "Handshake" (Auth) Now, we need to generate that session.json file. Run this command in your terminal: PHANTOM_APP_ID=YOUR_APP_ID_HERE npx -y @phantom/mcp-server The Pop-up: A browser window will open. The Selection: Select the exact same email you used for the wallet and the developer portal. The Result: The terminal should eventually say: Session saved to ~/.phantom-mcp/session.json. Step 3: Verify the "Hands" Once you see that "Session saved" message, run the Test 2 script one last time. It should now bypass the 404/401 errors and actually build/sign the swap. WALLET_PUBLIC_KEY=<your-new-email-wallet-address> npx tsx audit/test-2-hand.ts The Brutal Advice: The "Transition" You now have two wallets: your old Seed Phrase wallet and your new Email Agent wallet. Fund the Agent: Send $300 worth of SOL/USDC from your old wallet to the new Email Wallet address. Keep a "Gas Buffer": Make sure the new wallet has at least 0.05 SOL purely for transaction fees. Meteora DLMM rebalances can be frequent; don't let the agent "starve" on gas. Delete the Old Config: Once Test 2 passes, we are going to delete the audit/ folder and move into src/engine/. We don't want "Test" code anywhere near your real $300. Once Test 2 gives you a Transaction Signature (TxID), paste it here. I will then give you the "Meteora Deployment" code to start earning that $20/month. Are we clear for take-off?
