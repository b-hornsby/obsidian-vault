---
id: 982741
source: GEMINI
date: 2026-03-06
tags: ['jupiter-api', 'api-migration', 'limit-orders', 'trigger-api', 'defi-agent']
category: crypto-web3
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was reviewing a summary of the Jupiter API migration from /limit/v2 to /trigger/v1 and what it meant for his DeFi agent.
---
# what does this mean?  All done. Here's a summary:                                                                                                                                                   
                                                                                                                                                                                
  Jupiter API Migration: /limit/v2 → /trigger/v1                                                                                                                                
                                                                                                                                                                              
  What changed in the API:                                                                                                                                                      
                                                                                                                                                                              
  ┌───────────────────────┬───────────────────────────────────────────┬────────────────────────────────────────────┐
  │                       │              Old (limit/v2)               │              New (trigger/v1)              │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Base URL              │ /limit/v2                                 │ /trigger/v1                                │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Fetch orders          │ /openOrders?wallet=                       │ /getTriggerOrders?user=&orderStatus=active │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Orders response       │ Root array []                             │ { orders: [], totalPages, page }           │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Order key field       │ account                                   │ orderKey                                   │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Order amount fields   │ inAmount, outAmount                       │ makingAmount, takingAmount                 │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ createOrder response  │ data.order || data.tx || data.transaction │ data.transaction (+ data.order = orderKey) │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ cancelOrders response │ data.txs                                  │ data.transactions                          │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Auth                  │ None                                      │ x-api-key header (all endpoints)           │
  └───────────────────────┴───────────────────────────────────────────┴────────────────────────────────────────────┘

  Bonus fix: The old code stored txid as orderAccount (a proxy) because the v2 API didn't clearly return the order key. With trigger/v1, createOrder returns order (the real
  account pubkey) directly — so LstOrder.orderAccount is now populated correctly on placement, making settle reconciliation actually work.

  One thing you still need to do: Add JUPITER_API_KEY=your_key_here to your .env file. Get a free key at portal.jup.ag. Without it the requests will be sent without auth and
  may get rejected.

  Updated pre-live checklist:
  1. ~~Set lstIntrinsicValues correctly~~ ✓
  2. ~~Verify Jupiter API schema~~ ✓ (and migrated to trigger/v1)
  3. Add JUPITER_API_KEY to .env ← remaining
  4. Confirm wallet is funded + private RPC endpoint set

  Sources:
  - Create Order | Jupiter Developer Docs
  - Get Trigger Orders | Jupiter Developer Docs

✻ Crunched for 7m 6s                  

### USER
what does this mean?  All done. Here's a summary:                                                                                                                                                   
                                                                                                                                                                                
  Jupiter API Migration: /limit/v2 → /trigger/v1                                                                                                                                
                                                                                                                                                                              
  What changed in the API:                                                                                                                                                      
                                                                                                                                                                              
  ┌───────────────────────┬───────────────────────────────────────────┬────────────────────────────────────────────┐
  │                       │              Old (limit/v2)               │              New (trigger/v1)              │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Base URL              │ /limit/v2                                 │ /trigger/v1                                │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Fetch orders          │ /openOrders?wallet=                       │ /getTriggerOrders?user=&orderStatus=active │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Orders response       │ Root array []                             │ { orders: [], totalPages, page }           │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Order key field       │ account                                   │ orderKey                                   │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Order amount fields   │ inAmount, outAmount                       │ makingAmount, takingAmount                 │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ createOrder response  │ data.order || data.tx || data.transaction │ data.transaction (+ data.order = orderKey) │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ cancelOrders response │ data.txs                                  │ data.transactions                          │
  ├───────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Auth                  │ None                                      │ x-api-key header (all endpoints)           │
  └───────────────────────┴───────────────────────────────────────────┴────────────────────────────────────────────┘

  Bonus fix: The old code stored txid as orderAccount (a proxy) because the v2 API didn't clearly return the order key. With trigger/v1, createOrder returns order (the real
  account pubkey) directly — so LstOrder.orderAccount is now populated correctly on placement, making settle reconciliation actually work.

  One thing you still need to do: Add JUPITER_API_KEY=your_key_here to your .env file. Get a free key at portal.jup.ag. Without it the requests will be sent without auth and
  may get rejected.

  Updated pre-live checklist:
  1. ~~Set lstIntrinsicValues correctly~~ ✓
  2. ~~Verify Jupiter API schema~~ ✓ (and migrated to trigger/v1)
  3. Add JUPITER_API_KEY to .env ← remaining
  4. Confirm wallet is funded + private RPC endpoint set

  Sources:
  - Create Order | Jupiter Developer Docs
  - Get Trigger Orders | Jupiter Developer Docs

✻ Crunched for 7m 6s                  

### GEMINI
This summary indicates a critical technical upgrade to a trading bot or application that interacts with Jupiter (the Solana-based decentralized exchange). Essentially, the code was rewritten to stop using an outdated, likely deprecated "Limit Order" system and move to a newer, more robust "Trigger Order" system. Here is the "brutally honest" breakdown of what this actually means for your operations: 1. You were using a "Legacy" system (and it was probably buggy) The "Old" version (/limit/v2) was less sophisticated. The note about the "Bonus fix" reveals that the previous code was using a "proxy" (a guess or a temporary ID) for order accounts because the old API didn't return clear data. The Reality: Your old setup likely had issues reconciling settled trades or tracking whether an order actually filled. Moving to /trigger/v1 means the bot now gets the real account address immediately. It's much more stable. 2. The Infrastructure has changed The table shows a complete overhaul of how the bot "talks" to Jupiter: Data Structure: Instead of getting a simple list of orders, the bot now handles paginated data (pages). This is better for performance if you have many orders. Naming Conventions: Fields like inAmount are now makingAmount. If you have custom scripts relying on the old names, they are now broken. Authentication: This is the biggest hurdle. The old system was "open." The new system requires an API key. 3. Your "To-Do" List is the bottleneck The summary is telling you that the code is ready, but the bot will not work yet. The API Key: You must go to portal.jup.ag, get a key, and put it in your .env file as JUPITER_API_KEY. Without this, Jupiter will reject your bot's requests. The RPC: The checklist mentions a "private RPC endpoint." If you are still using a public Solana RPC, your transactions will likely fail or be "front-run" (exploited) during high volatility. 4. Strategic Assessment The fact that it took 7 minutes and 6 seconds to "crunch" this suggests an AI or a highly automated developer tool performed a complex refactor of your codebase. The Risk: Whenever you migrate API versions, there is a risk of "edge case" failures (e.g., how the bot handles a partially filled order under the new schema). The Opportunity: This migration was necessary. Staying on v2 would have eventually resulted in total service failure when Jupiter turned off the old endpoint. You are now on the "modern" stack, which should be faster and more accurate. Would you like me to help you generate the .env file structure or explain how to verify if the new orderKey logic is working correctly?
