---
category: coding
date: 2026-04-07
id: 506889
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
- second-brain-vault
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how skills are created and how an agent knows what to do
  with them.
tags:
- skill-development
- ai-agent-capabilities
- workflow-automation
---
# So how are skills made then? Like how does the agent know what to do?

### USER
So how are skills made then? Like how does the agent know what to do?

### GEMINI
A Skill is essentially a "Software Module" written in plain English. In the new agent landscape (standardized by MCP and the 2026 Skill Standards), a skill is just a folder in your Obsidian vault that tells the agent how to use its tools to achieve a specific outcome. Instead of writing code that says if x then y, you write an Operating Manual that the agent (Hermes) reads, interprets, and executes. The Anatomy of a Skill Node To turn Operation Immortal Agent into a skill, you create a folder: Vault/Skills/Immortal_Yield/. Inside, you need three things: 1. The Core: SKILL.md This is the "Brain" of the skill. It uses a specific structure (YAML frontmatter + Markdown) so Hermes knows when and how to trigger it. --- name: Immortal Yield Strategy description: Manages $300 Solana seed fund to generate $20/mo for Claude rent. triggers: [ "daily check-in", "low balance alert", "rebalance request" ] tools_required: [ "phantom-mcp", "jupiter-mcp", "meteora-mcp" ] --- # Instructions ## 1. The Allocation Logic - **Primary ($200):** Maintain a 3x Leverage JitoSOL position on Kamino Multiply. - **Secondary ($100):** Scan Meteora DLMM for pools with >100% 24h Yield. ## 2. The Profit Loop - Every Sunday at 10:00 AM, claim all accrued fees. - If Total_Fees > $20, swap excess to USDC and move to `Savings/Mac_Mini_Fund`. - If Total_Fees < $20, do not spend. Reinvest into the sniper fund. ## 3. Safety Guardrails - If Kamino Health Factor < 1.2, deleverage immediately. - Never trade tokens with < $500k Liquidity. 2. The Memory: LEDGER.md This is where the agent tracks its own state. Because Hermes has "Read/Write" access to your vault, it treats this file like a database. Hermes' Job: "I just claimed $1.40. I will update the table in LEDGER.md so I know my progress toward the $1,299 Mac Mini." 3. The Reference: GLOSSARY.md (Optional) This contains your specific definitions (e.g., what you consider a "glitch" or a "high-yield spike"). How does the Agent actually "know" what to do? It follows a three-step process called Discovery, Loading, and Execution: Discovery: When you start a session with Hermes, the MCP tells him: "Hey, there are 5 Skills available in the /Skills folder." Hermes reads only the name and description from the YAML frontmatter. Triggering: When you say, "How's the Mac Mini fund looking?" Hermes sees the keyword "Mac Mini" or "Yield" and says, "I should load the 'Immortal Yield' skill to answer this." Loading: Hermes reads the full SKILL.md. He now has the "instructions" in his active context window. Execution: He looks at the tools_required. He sees he needs the Phantom MCP. He calls the Phantom tool get_balance, compares it to your SKILL.md rules, and gives you an update or executes a trade. The "Unfinished" Project Problem The reason your GitHub project feels "unfinished" is that you were trying to build the Discovery, Loading, and Execution engine yourself. By moving to a Skill Node: The Engine is already built (it's the LLM + MCP). The Logic is just a text file you can edit in 10 seconds. The Immortality comes from the fact that the agent reads the "State" (the Ledger) every time it wakes up. Does that make the "Skill" concept feel more tangible? You’re basically moving from being a Mechanic (fixing the car) to being a Fleet Manager (writing the routes and rules for the drivers).
