---
id: 066870
source: GEMINI
date: 2026-02-26
tags: ['solana-trading', 'jupiter-swap', 'phantom-mcp-authentication', 'transaction-signing']
category: crypto-web3
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan is testing the quoting stage of his Solana trading bot and needs his wallet public key and Phantom MCP authentication to proceed to the transaction building and signing stages.
---
# Stage A (Quote) is live and working:   

  Input:        0.01 SOL                                                                                                                                                                     
  Output:       0.00791759 JitoSOL
  Implied peg:  1.263010 SOL per JitoSOL                                                                                                                                                     
  Price impact: 0.0000%                                                                                                                                                                    
  Route hops:   3  (PancakeSwap → Stabble → Whirlpool)

  To run Stage A (transaction build) and Stage B (MCP signing), I need two things from you:

  1. Your Solana wallet public key — this is your wallet address, not your seed phrase or private key. It looks like 7xKX... — safe to share. Jupiter needs it to build the correct token
  accounts in the transaction.

  2. Phantom MCP auth — when Stage B runs, it will launch npx @phantom/mcp-server which will open a browser window for you to authenticate with your Phantom wallet via Google/Apple SSO. You
   just need to be ready to approve it.

  Once you share the public key, run:
  WALLET_PUBLIC_KEY=<your-pubkey> npx tsx audit/test-2-hand.ts

  Or just drop the key here and I'll run it for you.

### USER
Stage A (Quote) is live and working:   

  Input:        0.01 SOL                                                                                                                                                                     
  Output:       0.00791759 JitoSOL
  Implied peg:  1.263010 SOL per JitoSOL                                                                                                                                                     
  Price impact: 0.0000%                                                                                                                                                                    
  Route hops:   3  (PancakeSwap → Stabble → Whirlpool)

  To run Stage A (transaction build) and Stage B (MCP signing), I need two things from you:

  1. Your Solana wallet public key — this is your wallet address, not your seed phrase or private key. It looks like 7xKX... — safe to share. Jupiter needs it to build the correct token
  accounts in the transaction.

  2. Phantom MCP auth — when Stage B runs, it will launch npx @phantom/mcp-server which will open a browser window for you to authenticate with your Phantom wallet via Google/Apple SSO. You
   just need to be ready to approve it.

  Once you share the public key, run:
  WALLET_PUBLIC_KEY=<your-pubkey> npx tsx audit/test-2-hand.ts

  Or just drop the key here and I'll run it for you.

### GEMINI
Sharing your Public Key is perfectly safe—it is your "username" on the blockchain. Without your private key or seed phrase, no one (including an AI) can take your funds. However, since Test 1 showed that Kamino Multiply is currently a money-loser, we are in a high-stakes pivot. Test 2 is no longer just a "hand check"; it is the "survival check." If this swap works, we can move to more aggressive yield-harvesting on Meteora. Here is what you do: Get your Public Key: Open Phantom, click on your account name/address at the top, and copy the string (e.g., 7xKX...). Paste it into your terminal like this: WALLET_PUBLIC_KEY=PASTE_YOUR_KEY_HERE npx tsx audit/test-2-hand.ts The SSO Moment: A browser window will pop up. This is the Phantom MCP SSO. You are granting Claude the right to ask for signatures. Crucial: This does not give Claude a blank check. For this test, it should still trigger a Phantom "Approve" notification on your phone or browser for the $1.50 swap. What to watch for in the terminal output: When you run the script, Claude is going to show you a "Transaction Payload." Look for these two things before you hit approve in your wallet: Priority Fees: Ensure you see something like setComputeUnitPrice. If the network is busy and this is missing, the transaction will hang, and you'll waste SOL on "lost" gas. The Error Code: If the terminal says Unauthorized Program ID, it means the Phantom MCP is "locked" to only allow simple transfers and Phantom's internal swap. Drop your Public Key here if you want me to double-check the "Test 2" script logic for safety before you run it, or just let me know the result of the swap! If Test 2 passes, are you ready to look at Meteora Dynamic Vaults as the new "Engine"? (They are currently yielding 15-40% on stables/SOL pairs, which would cover the $20 rent).
