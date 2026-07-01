---
category: coding
date: 2026-04-07
id: 840269
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is confused about how to achieve the same results when converting an
  agent-based system into a skill.
tags:
- skill-development
- ai-agent-refactoring
- workflow-optimization
---
# I’m confused tho like I was building out the system for an agent to do that action utilizing those tools but now how would I achieve that result if I turn this into a skill

### USER
I’m confused tho like I was building out the system for an agent to do that action utilizing those tools but now how would I achieve that result if I turn this into a skill

### GEMINI
I understand the confusion—it feels like I’m telling you to swap a running machine for a text document. But in the 2026 agent architecture, a Skill isn't just a "note." It is a Runtime Logic Module. Think of the Standalone Agent you were building as a "Hardwired Circuit," and a Skill as "Software" running on a pre-existing "CPU" (Hermes). Here is exactly how turning it into a skill achieves the same result, but more reliably: 1. The "Logic" vs. The "Labor" In your GitHub project, you were writing code to handle both the Thinking (Decision Logic) and the Doing (API calls). The Problem: If you code a standalone agent, you have to build the loop, the error handling, and the connection to the wallet yourself. The Skill Solution: You let Hermes (the brain) and Phantom MCP (the hands) handle the labor. The Skill is the specific "Business Logic" that connects them. 2. How the Result is Achieved (The "Handover") Instead of a script running in a terminal, here is how the "Skill" version of Operation Immortal Agent actually performs the action: ComponentWhat it does in the Skill modelTriggerA cron job or a command like "Hermes, check the yield" wakes the agent up.DiscoveryHermes looks at your /Skills folder, sees Immortal_Yield.md, and says: "I know how to do this."LogicHermes reads your Kamino/Meteora math from that Markdown file. It now "knows" your $200/$100 split.ExecutionHermes calls the Phantom MCP tool get_balance. If it sees profit, it calls the transfer or swap tool.PersistenceHermes writes the result into an Obsidian Ledger. Next time it wakes up, it reads that ledger to see its progress. 3. Why this is superior to your GitHub project If your GitHub code has a bug in the "Loop," the whole thing crashes and you have to debug TypeScript. If the market shifts and your Kamino Strategy needs to change: Standalone Agent: You have to re-code, re-compile, and re-deploy your bot. Skill: You just edit the Markdown text in Obsidian. The next time Hermes checks the yield, he's instantly following the new rules. The "How-To" Summary You aren't losing the "Action"—you are delegating the "Boring Code" to the MCP Protocol so you can focus on the Alpha Strategy. How to make it happen today: Stop writing "Harness" code. Define the "Flow" in Obsidian: Write out exactly what the agent should check first, second, and third. The "Act": Tell Hermes: "Your job is to follow the instructions in Immortal_Yield.md. Use the Phantom MCP tools to make it happen. Report back to the Ledger when you're done." Think of it this way: You were trying to build a robot that could cook. I'm telling you to just give the Recipe (The Skill) to a Professional Chef (Hermes) who already has the Kitchen (Phantom MCP). Which part of the original code are you most worried about losing if you move to this "Recipe" model? (e.g., the specific way it calculated the yield or a custom API call?)
