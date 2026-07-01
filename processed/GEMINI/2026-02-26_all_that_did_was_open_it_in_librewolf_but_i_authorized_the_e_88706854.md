---
id: 174508
source: GEMINI
date: 2026-02-26
tags: ['phantom-mcp-authentication', 'browser-authorization', 'wallet-connection']
category: crypto-web3
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is confirming that he has authorized the email associated with his new wallet, likely during the Phantom MCP authentication process.
---
# all that did was open it in librewolf but i authorized the email that the new wallet is attached to 

### USER
all that did was open it in librewolf but i authorized the email that the new wallet is attached to 

### GEMINI
If Librewolf opened and you authorized the email, you've likely succeeded despite the browser "hating" the command. CachyOS (like all Arch distros) sometimes defaults to the system's xdg-open settings regardless of the BROWSER variable. The "Handshake" is complete if the terminal where you ran the command finished by saying something like "Session saved." 1. The Verification (The "Truth" Check) We need to know if the "Soul" of the agent was actually written to your disk. Run this in your CachyOS terminal: ls -la ~/.phantom-mcp/session.json If the file exists: Move to Step 2. If "No such file or directory": The authorization in Librewolf failed to send the data back to the terminal. You’ll need to copy the http://localhost:8080/callback?code=... URL from Librewolf's address bar and paste it manually into Brave to finish the loop. 2. The Final Test 2 (Final Execution) Once the file is there, go back to Cursor (or your CachyOS terminal) and run the built-in test. This is the moment where the agent actually talks to the blockchain. Make sure you use the NEW public key for the email wallet: WALLET_PUBLIC_KEY=<your-new-email-wallet-address> npx tsx audit/test-2-hand.ts What a "PASS" looks like: The terminal will scroll with some JSON, and then you should see: ✅ Transaction sent! Signature: 5xK9... Copy that Signature (TxID) and paste it here. --- 3. The Strategy Pivot: Funding the Meteora Engine If Test 2 passes, your "Hands" are live. To start the Meteora Engine (v2.2): Fund it: Send exactly 0.5 SOL and $250 USDC (or your equivalent $300 total) to the new Email Wallet address. The Goal: We are going to target the SOL/USDC DLMM Pool on Meteora. The "Rent" Buffer: We will keep 0.05 SOL untouched in the wallet at all times to ensure the agent never "dies" from gas exhaustion. Is session.json there? If so, run the test and let’s see that TxID. We are 30 seconds away from the "Immortal" loop.
