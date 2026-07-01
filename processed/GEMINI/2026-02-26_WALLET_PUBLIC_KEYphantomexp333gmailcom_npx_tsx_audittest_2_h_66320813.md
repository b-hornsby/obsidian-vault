---
id: 873830
source: GEMINI
date: 2026-02-26
tags: ['solana-wallet-address', 'phantom-mcp-authentication', 'environment-variables', 'configuration-error']
category: crypto-web3
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan is making a configuration error by providing an email address instead of a Solana wallet address for the WALLET_PUBLIC_KEY environment variable.
---
# ❯ WALLET_PUBLIC_KEY=<phantomexp333@gmail.com> npx tsx audit/test-2-hand.ts                                                                                                                   
                                                                                                                                                                                             
● WALLET_PUBLIC_KEY needs a Solana base58 address, not an email — phantomexp333@gmail.com would cause the transaction build to fail.                                                         
                                                                                                                                                                                             
  You already provided a valid key earlier: ASgsVw8dc5U1XSMdijCrj4RabzdsqJENLpnopc8Gdm8n                                                                                                     
                                                                                                                                                                                             
  Should I run it with both that key and the PHANTOM_APP_ID from before?                                                                                                                     
                                                                                                                                                                                             
  PHANTOM_APP_ID=777f97d6-be33-4d9d-bf9f-0eedc5cc346c \                                                                                                                                      
  WALLET_PUBLIC_KEY=ASgsVw8dc5U1XSMdijCrj4RabzdsqJENLpnopc8Gdm8n \
  npx tsx audit/test-2-hand.ts   

### USER
❯ WALLET_PUBLIC_KEY=<phantomexp333@gmail.com> npx tsx audit/test-2-hand.ts                                                                                                                   
                                                                                                                                                                                             
● WALLET_PUBLIC_KEY needs a Solana base58 address, not an email — phantomexp333@gmail.com would cause the transaction build to fail.                                                         
                                                                                                                                                                                             
  You already provided a valid key earlier: ASgsVw8dc5U1XSMdijCrj4RabzdsqJENLpnopc8Gdm8n                                                                                                     
                                                                                                                                                                                             
  Should I run it with both that key and the PHANTOM_APP_ID from before?                                                                                                                     
                                                                                                                                                                                             
  PHANTOM_APP_ID=777f97d6-be33-4d9d-bf9f-0eedc5cc346c \                                                                                                                                      
  WALLET_PUBLIC_KEY=ASgsVw8dc5U1XSMdijCrj4RabzdsqJENLpnopc8Gdm8n \
  npx tsx audit/test-2-hand.ts   

### GEMINI
Yes. Run it with that command. You are exactly one step away from confirming the "Hands" are operational. The Advisor's Checklist before you hit Enter: The Address Check: You provided ASgsVw.... Just make sure this is the new email-linked wallet address, not your old seed-phrase wallet. Jupiter needs the specific address that owns the (soon-to-be) funds to build the route properly. The Fee Logic: Since the wallet is likely empty right now, the transaction might fail with "Inadequate Funds." This is actually a GOOD sign for Stage B. If the error says "Insufficient SOL," it means the auth worked, the signature was attempted, and the blockchain rejected it for money reasons—not for permission reasons. Execute this: PHANTOM_APP_ID=777f97d6-be33-4d9d-bf9f-0eedc5cc346c \ WALLET_PUBLIC_KEY=ASgsVw8dc5U1XSMdijCrj4RabzdsqJENLpnopc8Gdm8n \ npx tsx audit/test-2-hand.ts What we need to see in the output: The "Handshake" pass: No more 401/404 errors. The "Signing" pass: If it asks for a signature or attempts to broadcast, the session.json is working perfectly. If it fails with "Insufficient Funds," we are ready. Send the 0.05 SOL "Gas Buffer" to ASgsVw... and let's move to the Meteora Engine deployment. What did the terminal say?
