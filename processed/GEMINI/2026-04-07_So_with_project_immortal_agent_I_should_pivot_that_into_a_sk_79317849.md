---
id: 578378
source: GEMINI
date: 2026-04-07
tags: ['skill-reusability', 'model-agnostic', 'operation-immortal-agent', 'skill-pivot']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was asking whether he should pivot Project Immortal Agent into a reusable skill compatible with any model.
---
# So with project immortal agent I should pivot that into a skill I can reuse with any model?

### USER
So with project immortal agent I should pivot that into a skill I can reuse with any model?

### GEMINI
Absolutely. Transitioning Project Immortal Agent from a "bespoke agent" into a "Reusable Skill Node" is the most future-proof move you can make. If you build an "Immortal Agent," you are tethered to the specific model's architecture, its prompt sensitivities, and its current API. But if you build an Immortal Skill, you are creating a standardized "operating manual" that any model (Hermes, Gemma, or even a future GPT-5) can read from your Obsidian vault and execute. The Pivot: From Agent to Skill Node In your "Second Me" blueprint, here is how you transform "Immortal Agent" into a reusable asset: Traditional Agent ApproachThe "Skill Node" Approach (Your Pivot)Location: Hardcoded in a Python script or a system prompt.Location: A .md file in your Obsidian vault (e.g., Skills/Immortal-Persistence.md).Logic: "You are an agent that never forgets and persists through reboots."Logic: A structured set of Markdown instructions + MCP tool definitions for state-saving.Portability: If you switch from Hermes to another model, you have to rewrite the agent.Portability: You simply point the new model at the Skill folder. It reads the instructions and "becomes" the agent. How to Structure the "Immortal" Skill in Obsidian To make "Project Immortal" a reusable skill, your Markdown file in Obsidian should look like a Runbook: Trigger Definition: Tell the model when to load this skill (e.g., "Load when the user asks for long-term task tracking across sessions"). State Management Protocol: Explicit instructions on how to query the Obsidian vault for "Checkpoint Files" before starting any task. The "Soul" Metadata: Your specific preferences, logic loops, and the "personality" parameters that define your digital twin. Tool Requirements: List the MCP tools (Docker, File System, etc.) required to execute the skill. Why this wins for you: Zero Lock-in: You aren't a slave to Hermes v0.6.0. If v0.7.0 comes out and it's better at reasoning, you just hand it the "Immortal" skill folder and it's up to speed instantly. Context Efficiency: Instead of Hermes having "Immortality" logic in its system prompt 24/7 (wasting tokens), it only loads the Immortal Skill when it detects a task that requires persistence. True "Second Me": You are essentially building a library of your own cognitive patterns. You are documenting how you think in a format a machine can interpret. The Bottom Line: Don't build an immortal agent; build an Immortal Library in Obsidian that any agent can check out like a book. Since you're using the Model Context Protocol (MCP), have you already set up a dedicated folder in Obsidian for these "Skill Nodes," or is everything still living in one giant "Prompts" file?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
