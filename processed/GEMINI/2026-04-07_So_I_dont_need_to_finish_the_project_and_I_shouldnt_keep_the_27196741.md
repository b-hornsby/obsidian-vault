---
category: coding
date: 2026-04-07
id: 379633
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
- second-brain-vault
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is asking if he should abandon the 'immortal agent' project and its
  files in favor of a skill-based approach.
tags:
- project-abandonment
- skill-development
- immortal-agent
---
# So I don’t need to finish the project and I shouldn’t keep the immortal agent file anymore?

### USER
So I don’t need to finish the project and I shouldn’t keep the immortal agent file anymore?

### GEMINI
Exactly. Kill the project, save the logic. If you keep trying to "finish" it as a standalone Python/TypeScript project, you are fighting a battle on two fronts: you're trying to be a Software Developer (debugging environments, handling API breaking changes, managing dependencies) and a Knowledge Architect (building the "Second Me"). By pivoting that file into a Skill Node in Obsidian, you win back your time. Here is the final "clean-up" strategy: 1. The "Immortal Agent" File: Delete or Archive? Don't just delete it—harvest it first. * Open that file one last time. Copy the core logic (the "if price moves X, do Y" or "claim fees at Z threshold"). Paste that logic into a new Obsidian note: Vault/Skills/Finance/Meteora_Strategy.md. Then delete the file from the repo. ### 2. Why you shouldn't keep it as an "Agent" file An "Agent file" is a rigid script. A "Skill Node" is a dynamic instruction. Scripts break: If Meteora changes their SDK, your "Immortal Agent" file is dead code. Skills adapt: If the SDK changes, you just update the MCP server you're using. Hermes will read the same "Skill Node" in Obsidian and use the new tools to achieve the same goal. 3. The "Immortal" Rebrand "Project Immortal Agent" shouldn't be a file on GitHub; it should be a State of Being for your "Second Me." Instead of a script that runs, you have a Requirement in your Hermes system prompt: "Once a day, check Skills/Finance/Meteora_Strategy.md and ensure the self-sustainment loop is healthy." Summary of the Pivot Old Way (GitHub Project)New Way (The Skill Pivot)Effort: Debugging code and MCP connections.Effort: Refining the strategy in Markdown.Risk: Wallet keys in code; project goes "stale."Risk: None. Strategy is private; keys are in .env.Outcome: A bot that might work for a week.Outcome: A permanent financial "skill" for your AI. The Bottom Line: You’ve already done the hard part—you figured out the DLMM strategy. Don't let "finishing the code" get in the way of "using the strategy." Are you comfortable moving your wallet details into a local .env and letting a pre-built MCP handle the heavy lifting, or were you really attached to the custom code you were writing?
