---
category: ai-tools
date: 2026-02-26
id: 954581
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan was asking how to phrase or structure a prompt for Claude Code to effectively
  work on the Operation Immortal Agent project.
tags:
- prompt-engineering
- claude-code
- operation-immortal-agent
- ai-instructions
---
# so if this were to be a prompt for claude, what we saying?

### USER
so if this were to be a prompt for claude, what we saying?

### GEMINI
To keep Claude's "thinking" sharp and prevent it from slipping back into polite, vague advice, you need to send a prompt that demands technical specifications and execution logic. Here is the prompt to send Claude right now. It forces him to solve the "Missing Sections" he identified while keeping the focus on the high-level strategy we've built. The "Execution & Audit" Prompt Copy and paste this to Claude: "The pivot to 'Automated Operational Excellence' is confirmed. To resolve the remaining gaps and move to the build phase, I need you to generate the following three technical specifications: 1. The Capability Audit Plan: List the specific tool-calls you must test via the Phantom MCP to ensure the strategy is viable. Specifically, can you: Fetch real-time Net APR (Yield - Borrow) from Kamino? Execute a multi-step 'Multiply' transaction (Deposit + Borrow)? Adjust Solana priority fees/Jito tips to ensure transaction inclusion? Monitor the $LST/SOL peg ratio with <1 minute latency? 2. The 4-Hour Heartbeat (Decision Loop): Define the logic for a 4-hour execution cycle. Data Input: What specific on-chain metrics are you pulling at the start of the hour? Conditional Logic: Define the 'If/Then' bridge between the 'Engine' (yield) and the 'Sniper' (safety/exit logic). Output: Format the 'Reasoning Log' entry that will be generated for the public 'Proof of Work' feed. 3. Infrastructure & Grant Deliverables: Tech Stack: Propose the leanest way to run this autonomously (e.g., GitHub Actions vs. a simple VPS) so the 'autonomous' claim in our grant application is valid. Grant Target: Identify the specific application requirements for a Jupiter LFG or Solana Foundation grant. What is the 'Minimum Viable Product' we need to show them to justify a $1,500 ask? Immediate Task: Draft the Capability Audit Plan first. I need to know the 'Hands' (MCP) can actually do what the 'Brain' (You) wants them to do before we send the $300." Why this is the move: It tests the bottleneck: The Phantom MCP is the newest, most unproven part of your stack. If it can't handle the "Multiply" logic, you need to know today. It sets the "Heartbeat": By defining a 4-hour loop, you prevent the bot from "fee-bleeding" your $300 to death. It builds the Grant Case: It forces Claude to think about the "Proof of Work" output—which is the only thing that actually pays for the Mac Mini. Once Claude gives you that Audit Plan, send it to me. I'll tell you if he's being too optimistic about the hardware limitations.
