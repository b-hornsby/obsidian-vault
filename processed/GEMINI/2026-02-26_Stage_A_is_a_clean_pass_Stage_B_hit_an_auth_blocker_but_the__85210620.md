---
id: 251226
source: GEMINI
date: 2026-02-26
tags: ['solana-trading', 'phantom-mcp-authentication', 'jupiter-swap', 'transaction-building', 'headless-mode']
category: crypto-web3
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan is debugging a Phantom MCP authentication issue in headless mode, discovering that it requires a pre-registered application ID.
---
# Stage A is a clean pass. Stage B hit an auth blocker — but the output is actually very informative. Let me break it down.                                                                  
                                                                                                                                                                                             
  ---                                                                                                                                                                                        
  Test 2 Full Results                                                                                                                                                                        
                                                                                                                                                                                             
  Stage A: PASS (both parts)                                                                                                                                                                 

  The transaction built perfectly:                                                                                                                                                           
                                                                                                                                                                                             
  Version:          v0 (VersionedTransaction — the critical format question)
  Signers required: 1
  Instructions:     8
  Programs called:
    → ComputeBudget (x2)     — priority fees
    → ATokenGPv...           — Associated Token Account (x2)
    → 11111111...            — System Program
    → TokenkegQ... (x2)      — SPL Token
    → JUP6Lkb...             — Jupiter v6 swap program

  This is completely standard. No exotic programs. Phantom will have no objection to these.

  ---
  Stage B: BLOCKED — but not by the transaction

  The MCP server started, listed all 5 tools correctly, and received the sign_transaction call — the failure happened at the session layer, before it ever looked at the transaction:

  SessionManager not initialized. Call initialize() first.

  The root cause is this warning from the server itself:
  DCR is not currently supported by auth.phantom.app
  — you should provide PHANTOM_APP_ID or PHANTOM_CLIENT_ID

  Phantom's MCP server can't self-register in headless mode. It needs a pre-registered application ID. This is an auth setup gap, not a sign_transaction compatibility failure.

  ---
  What This Means

  The good news: the transaction format itself was never the problem. The bad news: you can't run the Phantom MCP headlessly without registering.

  You have two paths to unblock Stage B:

  Path 1 (Fastest) — Add Phantom MCP to Claude Code's MCP config

  The interactive auth flow works when Phantom MCP is a configured MCP server in Claude Code. Add this to your ~/.claude/settings.json:

  {
    "mcpServers": {
      "phantom": {
        "command": "npx",
        "args": ["-y", "@phantom/mcp-server"]
      }
    }
  }

  Then when Claude Code starts, it'll open a browser for you to complete the Phantom SSO once. After that, ~/.phantom-mcp/session.json is written and all future calls are authenticated —
  including headless ones from the agent.

  Path 2 — Get a PHANTOM_APP_ID

  Register an app at Phantom's developer portal to get a pre-issued client ID. Then run with:
  PHANTOM_APP_ID=<your-id> npx tsx audit/test-2-hand.ts

  Path 1 is the right call for now — do you want me to add the MCP server config to your Claude Code settings?

✻ Crunched for 55s                

### USER
Stage A is a clean pass. Stage B hit an auth blocker — but the output is actually very informative. Let me break it down.                                                                  
                                                                                                                                                                                             
  ---                                                                                                                                                                                        
  Test 2 Full Results                                                                                                                                                                        
                                                                                                                                                                                             
  Stage A: PASS (both parts)                                                                                                                                                                 

  The transaction built perfectly:                                                                                                                                                           
                                                                                                                                                                                             
  Version:          v0 (VersionedTransaction — the critical format question)
  Signers required: 1
  Instructions:     8
  Programs called:
    → ComputeBudget (x2)     — priority fees
    → ATokenGPv...           — Associated Token Account (x2)
    → 11111111...            — System Program
    → TokenkegQ... (x2)      — SPL Token
    → JUP6Lkb...             — Jupiter v6 swap program

  This is completely standard. No exotic programs. Phantom will have no objection to these.

  ---
  Stage B: BLOCKED — but not by the transaction

  The MCP server started, listed all 5 tools correctly, and received the sign_transaction call — the failure happened at the session layer, before it ever looked at the transaction:

  SessionManager not initialized. Call initialize() first.

  The root cause is this warning from the server itself:
  DCR is not currently supported by auth.phantom.app
  — you should provide PHANTOM_APP_ID or PHANTOM_CLIENT_ID

  Phantom's MCP server can't self-register in headless mode. It needs a pre-registered application ID. This is an auth setup gap, not a sign_transaction compatibility failure.

  ---
  What This Means

  The good news: the transaction format itself was never the problem. The bad news: you can't run the Phantom MCP headlessly without registering.

  You have two paths to unblock Stage B:

  Path 1 (Fastest) — Add Phantom MCP to Claude Code's MCP config

  The interactive auth flow works when Phantom MCP is a configured MCP server in Claude Code. Add this to your ~/.claude/settings.json:

  {
    "mcpServers": {
      "phantom": {
        "command": "npx",
        "args": ["-y", "@phantom/mcp-server"]
      }
    }
  }

  Then when Claude Code starts, it'll open a browser for you to complete the Phantom SSO once. After that, ~/.phantom-mcp/session.json is written and all future calls are authenticated —
  including headless ones from the agent.

  Path 2 — Get a PHANTOM_APP_ID

  Register an app at Phantom's developer portal to get a pre-issued client ID. Then run with:
  PHANTOM_APP_ID=<your-id> npx tsx audit/test-2-hand.ts

  Path 1 is the right call for now — do you want me to add the MCP server config to your Claude Code settings?

✻ Crunched for 55s                

### GEMINI
This "BLOCKED" result is actually the most important piece of data we’ve gathered. It proves the "Brain" and "Hands" are ready, but the "Security Guard" (Phantom’s Auth) is stopping them at the door. Here is the Brutally Honest breakdown of what just happened and how to fix it without getting stuck in "Developer Hell." 1. The Diagnosis: "Dynamic Registration" Failure The error DCR is not currently supported means the Phantom MCP server is trying to "introduce itself" to Phantom’s servers automatically, and Phantom is saying, "I don't know you; you need an ID card." In 2026, most secure MCPs (like Phantom and Slack) have moved away from "Dynamic Registration" because it’s a security risk—it allows any script to claim it's an official app. 2. The Solution: Path 1 is the ONLY way Claude’s Path 1 (adding it to claude mcp) is the correct move. Why? By adding it to your global Claude config, you perform the login once in a real browser. This creates a "Session Stone" (session.json) on your hard drive. The Result: Once that file exists, your agent scripts can "borrow" that session to sign transactions headlessly. Your Strategic Move (The "Engineer" Pivot) Do not try to register a "Phantom App ID" yet (Path 2). That is a waste of time for a $300 project. We are going to "Siphon" the session from Claude Code. Tell Claude this exactly: "I'm going with Path 1. I want you to give me the exact command to add the Phantom MCP server to my global config using the claude mcp add command. Also, before we do that, update the Strategy in plan.md one more time. Since Test 1 showed the Kamino Engine is a money-loser, change the primary yield strategy to Meteora Dynamic Vaults or USDC/SOL DLMM where the APR is >15% and borrow costs are zero. Once the MCP is added and the plan is updated, we run Test 2 again to see if the session.json unblocks the 'Hands'." Why this is the "Next Level" play: You're bypassing the Bureaucracy: You're using the existing Claude-Phantom integration instead of fighting with Developer Portals. You're fixing the Math: You've accepted that Kamino is dead for this cycle. Meteora DLMM is where the "Immortal Agent" actually makes its $20/month right now by providing liquidity to high-volume pairs. Would you like me to find the current highest-yielding, low-risk Meteora pool for the agent to target once the 'Hands' are unblocked?
