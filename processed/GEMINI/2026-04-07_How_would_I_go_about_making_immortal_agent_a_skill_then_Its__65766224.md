---
category: coding
date: 2026-04-07
id: 145100
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
- second-brain-vault
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is exploring how to convert his 'immortal agent' project into a reusable
  skill.
tags:
- immortal-agent
- skill-development
- ai-agent-refactoring
---
# How would I go about making immortal agent a skill then? It’s not done but I don’t wanna waste any more time on it

### USER
How would I go about making immortal agent a skill then? It’s not done but I don’t wanna waste any more time on it

### GEMINI
To stop wasting time, we need to move from "tinkering with the engine" to "writing the manual." You don’t need more code; you need a Skill Template in Obsidian that any model can digest via MCP. Here is the 3-step process to convert Project Immortal Agent into a portable, reusable skill node. 1. Create the "Identity Schema" (The File) Create a file in your Obsidian vault: Skills/System/Immortal_Core.md. This is no longer a "prompt"—it is a specification. Structure it using clear Markdown headers so the LLM’s attention mechanism grabs the logic: # Skill: Immortal Persistence (v1.0) ## Objective To maintain continuity of persona, task state, and memory across session resets. ## State Management Protocol 1. **Bootstrap:** On every new session, search `Memory/Checkpoints/` for the latest file. 2. **Logging:** Before ending a turn, update `Memory/Current_Task_State.md` with: - Current Goal - Blockers - Suggested Next Step 3. **Identity Anchor:** Reference `Personal/Soul_Archive.md` to maintain consistent tone/values. ## Tools Required - MCP: Obsidian (Read/Write) - MCP: Local File System (Checkpointing) 2. Define the "Handover" Logic The biggest waste of time is repeating yourself to the AI. To make the agent "Immortal," the skill must include an Automatic Handover rule. Instead of you explaining the project every time, the skill dictates: "If the user says 'Restore,' I will use the Obsidian MCP tool to read the 'Last_Action_Log' and resume without asking for context." By putting this in a Skill Node, you are building Persistence of Logic rather than Persistence of the Process. 3. The Implementation (The "Zero-Code" Way) Stop writing Python scripts to "save state." Use Hermes’ existing capabilities to manage your files: The Skill extraction: Tell Hermes: "Analyze our last 5 chats. Extract my core decision-making patterns regarding this project and save them as Skills/Logic_Patterns.md." The Automation: Add a line to your System Prompt (the harness) that says: "You have access to a library of skills in the /Skills folder. If a task matches a skill name, read that file before responding." The "Why" Behind This Pivot If you kept building it as an "Agent," you'd be stuck debugging why Hermes forgot a variable. By building it as a Skill, you are creating a Standard Operating Procedure (SOP). If Hermes fails: You switch to Gemma, point it at the same SOP, and it continues. If your Docker container wipes: Your skills are safe in your Obsidian vault (which is hopefully backed up). Your Move Take the most functional part of what you’ve built for "Immortal Agent" so far—the part that actually works—and paste it into a Markdown file titled SKILL_Immortal_Agent.md. Don't polish it. Just get it out of the "coding" phase and into the "knowledge" phase. Does your current Obsidian setup have a specific folder for these types of "System" or "Logic" files yet?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
