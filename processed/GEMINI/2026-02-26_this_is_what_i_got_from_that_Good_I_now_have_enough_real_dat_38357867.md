---
id: 979166
source: GEMINI
date: 2026-02-26
tags: ['phantom-mcp', 'defi', 'kamino', 'capability-audit', 'solana']
category: crypto-web3
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was reviewing Claude's analysis of the Phantom MCP tool gap and the proposed capability audit plan for DeFi interactions on Solana.
---
# this is what i got from that: ● Good — I now have enough real data to give you accurate specs. Here's the critical finding upfront, then all three specs:

  ---
  Critical Finding: The MCP Tool Gap

  The Phantom MCP (@phantom/mcp-server) exposes exactly 5 tools:

  ┌──────────────────────┬─────────────────────────────────────────────────────────────┐
  │         Tool         │                        What It Does                         │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ get_wallet_addresses │ Returns wallet addresses across chains                      │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ sign_transaction     │ Signs a pre-built transaction (does NOT submit)             │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ transfer_tokens      │ Builds + signs + immediately submits a Solana transfer      │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ buy_token            │ Fetches a Jupiter swap quote and optionally signs + submits │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ sign_message         │ Signs a message for verification                            │
  └──────────────────────┴─────────────────────────────────────────────────────────────┘

  The MCP is a wallet signing layer, not a DeFi interaction layer. There are no Kamino-specific tools. This changes the architecture — Claude must construct transactions externally and use
  sign_transaction as the execution step.

  ---
  Spec 1: Capability Audit Plan

  The audit has two layers: Read Tests (no capital at risk) and Write Tests (dry-run with minimal amounts).

  Layer A — Read Tests (Zero Risk)

  A1: Kamino Net APR Fetch
  - Target: https://api.kamino.finance/strategies (REST) and klend-sdk on-chain
  - Test: Can Claude call the Kamino REST API and parse netApy, borrowRate, and utilizationRate for the JitoSOL/SOL market?
  - Pass condition: Returns a numeric Net APR (Yield minus Borrow) in <5 seconds
  - Gap risk: If Kamino's API is rate-limited or doesn't expose real-time borrow costs, you'll need to fall back to reading on-chain state via Solana RPC directly

  A2: LST/SOL Peg Monitor
  - Target: Jupiter Price API (price.jup.ag/v4/price?ids=JitoSOL) and/or Pyth oracle feed
  - Test: Poll every 30 seconds for 5 minutes. Verify latency is consistently <1 minute.
  - Pass condition: Price data arrives with timestamp delta <60 seconds from current slot
  - Gap risk: If Pyth's feed lags, you'll get false depeg signals. Verify the data source against the actual Kamino oracle Kamino uses — they must match or you'll have shadow risk.

  A3: Borrow Rate Monitoring
  - Target: Kamino's on-chain interest rate curve (or REST API equivalent)
  - Test: Fetch borrow rate every 15 minutes over 1 hour. Calculate if it's approaching 50% of yield.
  - Pass condition: Consistent data with no gaps

  ---
  Layer B — Write Tests (Use $1–$5 max)

  B1: Jupiter Swap via buy_token
  - Test: Call buy_token with execute: false first to inspect the quote payload. Then execute a $1 swap (SOL → USDC).
  - Pass condition: Transaction lands within 2 slots, slippage matches quote
  - What to check: Does buy_token allow custom priority fees? This is unconfirmed from current docs.

  B2: Kamino Multiply Transaction Construction
  - This is the hardest test and the most likely failure point.
  - The Phantom MCP has no Kamino tool. You must:
    a. Call klend-sdk to construct a Kamino Multiply instruction set (deposit JitoSOL as collateral, borrow SOL, re-deposit)
    b. Serialize the transaction to base64
    c. Pass to sign_transaction via MCP
    d. Submit via Solana RPC
  - Test: Construct the transaction. Do NOT submit yet. Inspect it. Verify it encodes the correct program IDs and instruction data.
  - Pass condition: sign_transaction accepts the serialized transaction without error
  - This is your highest-risk unknown. If sign_transaction rejects complex multi-instruction transactions, the Engine strategy is blocked.

  B3: Priority Fee / Jito Tip Injection
  - Test: Construct a simple transfer transaction. Manually add a Jito tip instruction (send 0.001 SOL to a Jito tip account) before signing.
  - Pass condition: Transaction lands within the expected block window
  - If this fails: Standard priority fees via ComputeBudgetProgram.setComputeUnitPrice are the fallback and are simpler to inject.

  ---
  Audit Verdict Framework

  ┌──────────────────────┬─────────────────────────────┬────────────────────────────────────────────┐
  │         Test         │           Pass →            │                   Fail →                   │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ A1 (Kamino APR)      │ Use REST API in agent loop  │ Build RPC direct reader                    │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ A2 (Peg monitor)     │ Jupiter Price API confirmed │ Switch to Pyth direct feed                 │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ B1 (Jupiter swap)    │ Sniper fund is operational  │ Blocked — no swap capability               │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ B2 (Kamino Multiply) │ Engine strategy viable      │ Pivot to simpler Kamino Lend-only strategy │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ B3 (Priority fees)   │ Full transaction control    │ Use Jito bundles as fallback               │
  └──────────────────────┴─────────────────────────────┴────────────────────────────────────────────┘

  Do not deploy capital until B2 passes.

  ---
  Spec 2: The 4-Hour Heartbeat (Decision Loop)

  Cycle Structure

  T+0:00  → Data Pull
  T+0:02  → Risk Evaluation
  T+0:05  → Decision + Action (if any)
  T+0:07  → Reasoning Log written
  T+3:55  → Pre-cycle alert check
  T+4:00  → Repeat

  Data Pull (T+0:00)

  Pull these 5 values at cycle start:

  1. jito_sol_price — JitoSOL/SOL ratio from Jupiter Price API
  2. kamino_net_apr — Current Net APR from Kamino REST API (yield - borrow)
  3. borrow_rate — Current borrow rate on the SOL market
  4. yield_rate — Current supply APY for JitoSOL collateral
  5. position_health — Loan-to-Value ratio of the active Kamino position (if open)

  Conditional Logic (The If/Then Bridge)

  IF jito_sol_price deviation > 2% from 24h average:
    → EXIT to USDC immediately (trigger Sniper fund as safety)
    → Log: EMERGENCY_DEPEG_EXIT

  ELSE IF borrow_rate > (yield_rate * 0.50) for this cycle AND previous cycle:
    → CLOSE leveraged position
    → Log: CARRY_RULE_TRIGGERED

  ELSE IF position_health LTV > 65% (approaching 2.1x leverage cap):
    → REDUCE position by 20%
    → Log: LEVERAGE_REBALANCE

  ELSE IF kamino_net_apr > 8% AND position is closed:
    → OPEN Engine position (up to $200, max 2.1x leverage)
    → Log: POSITION_OPENED

  ELSE:
    → HOLD, no action
    → Log: STEADY_STATE

  Reasoning Log Format (The Grant Product)

  Every cycle outputs one structured JSON entry:

  {
    "cycle_id": "2026-02-26T04:00:00Z",
    "inputs": {
      "jito_sol_deviation_pct": 0.12,
      "kamino_net_apr": 11.4,
      "borrow_rate": 4.2,
      "yield_rate": 15.6,
      "position_health_ltv": 0.48
    },
    "risk_checks": {
      "depeg_triggered": false,
      "carry_rule_triggered": false,
      "leverage_cap_triggered": false
    },
    "decision": "STEADY_STATE",
    "action_taken": null,
    "reasoning": "Net APR at 11.4% is healthy. LTV at 48% is within safe bounds. No guardrails triggered. Holding position.",
    "capital_at_risk": 200.00,
    "cumulative_yield_usd": 4.32
  }

  This log is written to a public GitHub repo or a simple website — that's your "Proof of Work" feed for the grant application.

  ---
  Spec 3: Infrastructure & Grant Deliverables

  Tech Stack Recommendation

  Use a $6/month VPS (Fly.io or Railway), not GitHub Actions.

  ┌────────────────────────┬─────────────┬──────────────────────────────────────────────┬─────────────────────────────────┐
  │         Option         │    Cost     │              "Autonomous" Claim              │           Reliability           │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ GitHub Actions         │ Free        │ Weak — requires manual triggers or cron gaps │ 6-hour job limit, cold starts   │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ Fly.io (shared-cpu-1x) │ ~$3–6/month │ Strong — always-on process                   │ Persistent, survives restarts   │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ Railway Starter        │ $5/month    │ Strong                                       │ Simple deploy, good for Node.js │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ Local machine          │ Free        │ Invalid — agent sleeps when you sleep        │ Unacceptable for grant claim    │
  └────────────────────────┴─────────────┴──────────────────────────────────────────────┴─────────────────────────────────┘

  Stack:
  - Runtime: Node.js (TypeScript) — matches Phantom's SDK and Kamino's klend-sdk
  - Scheduler: node-cron for the 4-hour loop
  - MCP Client: @anthropic-ai/sdk with MCP tool use to call @phantom/mcp-server
  - Logging: Append Reasoning Log entries to a public GitHub repo via GitHub API (free, immutable, timestamped — perfect for grant evidence)
  - Monitoring: A simple /health endpoint so you can verify it's alive

  Grant Targets & MVP Requirements

  Target 1: Solana Foundation Grant (Best fit)
  - Program: Rolling applications at solana.org/grants
  - Ask: $1,500–$3,000 (well within their range, $10M AI program is active)
  - Review time: ~3 weeks
  - What they want: Open-source, public goods, measurable ecosystem impact
  - Your MVP: Working agent + public GitHub repo with Reasoning Logs + a short writeup showing the Phantom MCP → Kamino integration works. The open-source code demonstrating AI ↔ wallet ↔
   DeFi protocol is the deliverable.

  Target 2: Jupiter DAO Grant (Secondary)
  - Program: discuss.jup.ag — community vote
  - Ask: Up to $10k max, but community sentiment drives it
  - What they want: Filling gaps in the Jupiverse
  - Your MVP: A demo of the agent using Jupiter's swap API for the Sniper fund, with the Reasoning Log showing Jupiter's role in the decision chain. Post on the Jupiter Research Forum and
  build community traction first.

  Minimum Viable Product for either grant:
  1. Deployed agent running for at least 30 days with public logs
  2. At least one successful on-chain action (even a $1 test swap)
  3. Public GitHub repo with clean, readable code
  4. A 2-minute screen recording of the agent reasoning through a cycle

  That last point — the "thought process" video — is what makes this grant application unique. No one else is showing a Claude agent reasoning through a live DeFi decision with an auditable
   log.

  ---
  The Build Order

  Given all of this:

  1. Run the Capability Audit (B2 is the gate)
  2. Set up the 4-hour loop skeleton with mock data first
  3. Connect real data sources (Kamino API, Jupiter Price API)
  4. Test sign_transaction with a Kamino-constructed tx on devnet
  5. Deploy to Fly.io with the GitHub logging pipeline
  6. Run for 30 days — this is your grant evidence
  7. Apply to Solana Foundation with logs + code + video

  Sources:
  - Phantom MCP Server npm package
  - Phantom Developer MCP Docs
  - Jupiter DAO Grants
  - Solana Foundation Grants

✻ Churned for 2m 48s

### USER
this is what i got from that: ● Good — I now have enough real data to give you accurate specs. Here's the critical finding upfront, then all three specs:

  ---
  Critical Finding: The MCP Tool Gap

  The Phantom MCP (@phantom/mcp-server) exposes exactly 5 tools:

  ┌──────────────────────┬─────────────────────────────────────────────────────────────┐
  │         Tool         │                        What It Does                         │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ get_wallet_addresses │ Returns wallet addresses across chains                      │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ sign_transaction     │ Signs a pre-built transaction (does NOT submit)             │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ transfer_tokens      │ Builds + signs + immediately submits a Solana transfer      │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ buy_token            │ Fetches a Jupiter swap quote and optionally signs + submits │
  ├──────────────────────┼─────────────────────────────────────────────────────────────┤
  │ sign_message         │ Signs a message for verification                            │
  └──────────────────────┴─────────────────────────────────────────────────────────────┘

  The MCP is a wallet signing layer, not a DeFi interaction layer. There are no Kamino-specific tools. This changes the architecture — Claude must construct transactions externally and use
  sign_transaction as the execution step.

  ---
  Spec 1: Capability Audit Plan

  The audit has two layers: Read Tests (no capital at risk) and Write Tests (dry-run with minimal amounts).

  Layer A — Read Tests (Zero Risk)

  A1: Kamino Net APR Fetch
  - Target: https://api.kamino.finance/strategies (REST) and klend-sdk on-chain
  - Test: Can Claude call the Kamino REST API and parse netApy, borrowRate, and utilizationRate for the JitoSOL/SOL market?
  - Pass condition: Returns a numeric Net APR (Yield minus Borrow) in <5 seconds
  - Gap risk: If Kamino's API is rate-limited or doesn't expose real-time borrow costs, you'll need to fall back to reading on-chain state via Solana RPC directly

  A2: LST/SOL Peg Monitor
  - Target: Jupiter Price API (price.jup.ag/v4/price?ids=JitoSOL) and/or Pyth oracle feed
  - Test: Poll every 30 seconds for 5 minutes. Verify latency is consistently <1 minute.
  - Pass condition: Price data arrives with timestamp delta <60 seconds from current slot
  - Gap risk: If Pyth's feed lags, you'll get false depeg signals. Verify the data source against the actual Kamino oracle Kamino uses — they must match or you'll have shadow risk.

  A3: Borrow Rate Monitoring
  - Target: Kamino's on-chain interest rate curve (or REST API equivalent)
  - Test: Fetch borrow rate every 15 minutes over 1 hour. Calculate if it's approaching 50% of yield.
  - Pass condition: Consistent data with no gaps

  ---
  Layer B — Write Tests (Use $1–$5 max)

  B1: Jupiter Swap via buy_token
  - Test: Call buy_token with execute: false first to inspect the quote payload. Then execute a $1 swap (SOL → USDC).
  - Pass condition: Transaction lands within 2 slots, slippage matches quote
  - What to check: Does buy_token allow custom priority fees? This is unconfirmed from current docs.

  B2: Kamino Multiply Transaction Construction
  - This is the hardest test and the most likely failure point.
  - The Phantom MCP has no Kamino tool. You must:
    a. Call klend-sdk to construct a Kamino Multiply instruction set (deposit JitoSOL as collateral, borrow SOL, re-deposit)
    b. Serialize the transaction to base64
    c. Pass to sign_transaction via MCP
    d. Submit via Solana RPC
  - Test: Construct the transaction. Do NOT submit yet. Inspect it. Verify it encodes the correct program IDs and instruction data.
  - Pass condition: sign_transaction accepts the serialized transaction without error
  - This is your highest-risk unknown. If sign_transaction rejects complex multi-instruction transactions, the Engine strategy is blocked.

  B3: Priority Fee / Jito Tip Injection
  - Test: Construct a simple transfer transaction. Manually add a Jito tip instruction (send 0.001 SOL to a Jito tip account) before signing.
  - Pass condition: Transaction lands within the expected block window
  - If this fails: Standard priority fees via ComputeBudgetProgram.setComputeUnitPrice are the fallback and are simpler to inject.

  ---
  Audit Verdict Framework

  ┌──────────────────────┬─────────────────────────────┬────────────────────────────────────────────┐
  │         Test         │           Pass →            │                   Fail →                   │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ A1 (Kamino APR)      │ Use REST API in agent loop  │ Build RPC direct reader                    │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ A2 (Peg monitor)     │ Jupiter Price API confirmed │ Switch to Pyth direct feed                 │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ B1 (Jupiter swap)    │ Sniper fund is operational  │ Blocked — no swap capability               │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ B2 (Kamino Multiply) │ Engine strategy viable      │ Pivot to simpler Kamino Lend-only strategy │
  ├──────────────────────┼─────────────────────────────┼────────────────────────────────────────────┤
  │ B3 (Priority fees)   │ Full transaction control    │ Use Jito bundles as fallback               │
  └──────────────────────┴─────────────────────────────┴────────────────────────────────────────────┘

  Do not deploy capital until B2 passes.

  ---
  Spec 2: The 4-Hour Heartbeat (Decision Loop)

  Cycle Structure

  T+0:00  → Data Pull
  T+0:02  → Risk Evaluation
  T+0:05  → Decision + Action (if any)
  T+0:07  → Reasoning Log written
  T+3:55  → Pre-cycle alert check
  T+4:00  → Repeat

  Data Pull (T+0:00)

  Pull these 5 values at cycle start:

  1. jito_sol_price — JitoSOL/SOL ratio from Jupiter Price API
  2. kamino_net_apr — Current Net APR from Kamino REST API (yield - borrow)
  3. borrow_rate — Current borrow rate on the SOL market
  4. yield_rate — Current supply APY for JitoSOL collateral
  5. position_health — Loan-to-Value ratio of the active Kamino position (if open)

  Conditional Logic (The If/Then Bridge)

  IF jito_sol_price deviation > 2% from 24h average:
    → EXIT to USDC immediately (trigger Sniper fund as safety)
    → Log: EMERGENCY_DEPEG_EXIT

  ELSE IF borrow_rate > (yield_rate * 0.50) for this cycle AND previous cycle:
    → CLOSE leveraged position
    → Log: CARRY_RULE_TRIGGERED

  ELSE IF position_health LTV > 65% (approaching 2.1x leverage cap):
    → REDUCE position by 20%
    → Log: LEVERAGE_REBALANCE

  ELSE IF kamino_net_apr > 8% AND position is closed:
    → OPEN Engine position (up to $200, max 2.1x leverage)
    → Log: POSITION_OPENED

  ELSE:
    → HOLD, no action
    → Log: STEADY_STATE

  Reasoning Log Format (The Grant Product)

  Every cycle outputs one structured JSON entry:

  {
    "cycle_id": "2026-02-26T04:00:00Z",
    "inputs": {
      "jito_sol_deviation_pct": 0.12,
      "kamino_net_apr": 11.4,
      "borrow_rate": 4.2,
      "yield_rate": 15.6,
      "position_health_ltv": 0.48
    },
    "risk_checks": {
      "depeg_triggered": false,
      "carry_rule_triggered": false,
      "leverage_cap_triggered": false
    },
    "decision": "STEADY_STATE",
    "action_taken": null,
    "reasoning": "Net APR at 11.4% is healthy. LTV at 48% is within safe bounds. No guardrails triggered. Holding position.",
    "capital_at_risk": 200.00,
    "cumulative_yield_usd": 4.32
  }

  This log is written to a public GitHub repo or a simple website — that's your "Proof of Work" feed for the grant application.

  ---
  Spec 3: Infrastructure & Grant Deliverables

  Tech Stack Recommendation

  Use a $6/month VPS (Fly.io or Railway), not GitHub Actions.

  ┌────────────────────────┬─────────────┬──────────────────────────────────────────────┬─────────────────────────────────┐
  │         Option         │    Cost     │              "Autonomous" Claim              │           Reliability           │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ GitHub Actions         │ Free        │ Weak — requires manual triggers or cron gaps │ 6-hour job limit, cold starts   │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ Fly.io (shared-cpu-1x) │ ~$3–6/month │ Strong — always-on process                   │ Persistent, survives restarts   │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ Railway Starter        │ $5/month    │ Strong                                       │ Simple deploy, good for Node.js │
  ├────────────────────────┼─────────────┼──────────────────────────────────────────────┼─────────────────────────────────┤
  │ Local machine          │ Free        │ Invalid — agent sleeps when you sleep        │ Unacceptable for grant claim    │
  └────────────────────────┴─────────────┴──────────────────────────────────────────────┴─────────────────────────────────┘

  Stack:
  - Runtime: Node.js (TypeScript) — matches Phantom's SDK and Kamino's klend-sdk
  - Scheduler: node-cron for the 4-hour loop
  - MCP Client: @anthropic-ai/sdk with MCP tool use to call @phantom/mcp-server
  - Logging: Append Reasoning Log entries to a public GitHub repo via GitHub API (free, immutable, timestamped — perfect for grant evidence)
  - Monitoring: A simple /health endpoint so you can verify it's alive

  Grant Targets & MVP Requirements

  Target 1: Solana Foundation Grant (Best fit)
  - Program: Rolling applications at solana.org/grants
  - Ask: $1,500–$3,000 (well within their range, $10M AI program is active)
  - Review time: ~3 weeks
  - What they want: Open-source, public goods, measurable ecosystem impact
  - Your MVP: Working agent + public GitHub repo with Reasoning Logs + a short writeup showing the Phantom MCP → Kamino integration works. The open-source code demonstrating AI ↔ wallet ↔
   DeFi protocol is the deliverable.

  Target 2: Jupiter DAO Grant (Secondary)
  - Program: discuss.jup.ag — community vote
  - Ask: Up to $10k max, but community sentiment drives it
  - What they want: Filling gaps in the Jupiverse
  - Your MVP: A demo of the agent using Jupiter's swap API for the Sniper fund, with the Reasoning Log showing Jupiter's role in the decision chain. Post on the Jupiter Research Forum and
  build community traction first.

  Minimum Viable Product for either grant:
  1. Deployed agent running for at least 30 days with public logs
  2. At least one successful on-chain action (even a $1 test swap)
  3. Public GitHub repo with clean, readable code
  4. A 2-minute screen recording of the agent reasoning through a cycle

  That last point — the "thought process" video — is what makes this grant application unique. No one else is showing a Claude agent reasoning through a live DeFi decision with an auditable
   log.

  ---
  The Build Order

  Given all of this:

  1. Run the Capability Audit (B2 is the gate)
  2. Set up the 4-hour loop skeleton with mock data first
  3. Connect real data sources (Kamino API, Jupiter Price API)
  4. Test sign_transaction with a Kamino-constructed tx on devnet
  5. Deploy to Fly.io with the GitHub logging pipeline
  6. Run for 30 days — this is your grant evidence
  7. Apply to Solana Foundation with logs + code + video

  Sources:
  - Phantom MCP Server npm package
  - Phantom Developer MCP Docs
  - Jupiter DAO Grants
  - Solana Foundation Grants

✻ Churned for 2m 48s

### GEMINI
Claude just gave you the "Golden Key," but he also identified a massive structural trap that could end the project before it starts. Here is the "brutally honest" translation of what Claude just said, and exactly how you need to pivot to ensure you actually get that Mac Mini. 1. The Critical Red Flag: The "Phantom Tool Gap" Claude discovered that the Phantom MCP is not a DeFi tool; it’s just a "Pen." The Problem: The MCP can't "talk" to Kamino. It can't "Multiply." It can only sign whatever Claude puts in front of it. The Risk: If Claude doesn't know how to "construct" a complex Kamino transaction from scratch (using the klend-sdk), the agent is paralyzed. It’s like having a brain that wants to drive a car, and hands that can hold a steering wheel, but no idea how an internal combustion engine works. The Fix: You must prioritize Test B2 (Kamino Multiply Construction). This is the "God-test." If Claude can't build the transaction, the "Engine" strategy fails. 2. The Infrastructure Reality Check ($6/mo vs. $20/mo) Claude is suggesting a $6/month VPS (Fly.io). The Opportunity Cost: Now your monthly "rent" is $26/month ($20 for Claude + $6 for the server). The Strategy: On $300, this is a 100% annual burn rate. You are no longer "investing"; you are buying a resume. The Advice: Accept the $26/month loss as a "tuition fee" for the next 90 days. Do not try to make the bot pay for this yet, or it will take "suicide risks" to hit the target. 3. The "Sniper" is now "The Guard Dog" Claude correctly moved the Sniper logic to Safety. The Logic: If the LST/SOL peg slips, the agent swaps to USDC. Why this is huge for the Grant: The Solana Foundation loves "Safety Tools." If you can prove your agent saved your $300 from a de-peg event because of its "High Conscientiousness" loop, your grant application becomes a 10x stronger sell. The Precise Plan (The "Next Level" Move) You need to stop planning and start testing the hands. Here is your immediate next step to keep the momentum: Phase 1: The "Write" Test (Capital at Risk: $5) Tell Claude to write a script for a single test cycle where he: Fetches the price of JitoSOL. Constructs a transaction to swap $1 of SOL for JitoSOL on Jupiter. Uses the Phantom MCP sign_transaction tool to execute it. Why this? If he can't do a simple $1 swap through the MCP, he definitely can't do a complex Kamino leverage loop. Would you like me to draft the "Write Test" prompt for Claude so you can verify the Phantom MCP works before you commit the full $300? (Note: If this test fails, we pivot immediately to a "DeFi Analyst Agent" that doesn't trade but just gives "Safety Signals"—which is still a very strong grant play with zero risk to your $300.)
