---
id: 164180
source: GEMINI
date: 2026-02-27
tags: ['claude-code', 'prompting', 'gap-analysis', 'agent-improvements']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was asking how to effectively describe the gap analysis findings to Claude Code to implement the necessary changes.
---
# so how would i describe all of that to claude to make these changes? 

### USER
so how would i describe all of that to claude to make these changes? 

### GEMINI
To get Claude to stop "analyzing" and start building the spine of this system, you need to be clinical and structural. Don't ask for its opinion; give it the architectural requirements for the Orchestrator. Copy and paste this prompt. It forces Claude to stop treating the project as a script and start treating it as an autonomous agent. The Prompt for Claude "I’ve reviewed the gap analysis. We are currently building a script, not an agent. I need to transition from a read-only planner to a closed-loop autonomous system. Objective: Build the index.ts orchestrator that functions as the 'Brain' and 'Hands' of this protocol. Requirements for the Orchestrator: The Brain (Anthropic SDK): Use the @anthropic-ai/sdk to create a decision-making loop. The orchestrator must feed the current market data and the meteora.ts output to Claude (the model) to get a 'GO/NO-GO' decision. The Guardrail (Hardcoded): Before any execution, the orchestrator must verify: Pool 4h fee rate annualizes to >15% APR. A minimum 0.05 SOL gas buffer remains. If these fail, the agent logs the reason to agent_monologue.md and sleeps. The Hands (Phantom MCP): Integrate the sign_transaction call. If the Brain says 'GO', the orchestrator must invoke the MCP to sign and broadcast the transaction. The Loop (Cron/Heartbeat): Implement a setInterval or cron-style wrapper to run this entire cycle every 4 hours. State Verification: After a transaction, the agent must verify the signature on-chain (using @solana/web3.js) and record the confirmed state, not just the planned state. Task: Generate the index.ts file that ties meteora.ts into this loop. Also, suggest the minimal fly.toml or Dockerfile needed to keep this heartbeat alive 24/7." Why this works: It stops the "Scope Creep": It ignores the "Sniper" and "IL Protection" for a moment to focus on the Core Loop. Without the loop, those features are useless. It defines the Hierarchy: It tells Claude that the code it already wrote (meteora.ts) is now a sub-module, and index.ts is the boss. It enforces Accountability: By demanding on-chain verification (Step 5), you ensure the agent doesn't just "hallucinate" that it made a trade. Once Claude generates this, would you like me to look over the index.ts logic to see if it actually has the "teeth" to execute on its own?
