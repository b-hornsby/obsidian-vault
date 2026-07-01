---
category: coding
date: 2026-04-07
id: 400824
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
- second-brain-vault
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to convert a work-in-progress project into a skill instead of
  building it as an agent.
tags:
- skill-development
- ai-agent-refactoring
- project-pivot
---
# No I mean like that project is still a work in progress but I want it to be a skill rather than building it out as an agent

### USER
No I mean like that project is still a work in progress but I want it to be a skill rather than building it out as an agent

### GEMINI
That is a smart pivot. Since "Project Immortal" is about state-persistence and longevity, trying to build it as a standalone agent is essentially trying to code a "ghost in the machine." Instead, treat it as a "System Skill"—a set of rules and protocols that any model (the harness) uses to ensure it never loses its place. The Architecture: "Skill" vs. "Agent" The Agent (Harness): The reasoning loop that runs in Docker. The Skill (Immortal Agent): A dedicated folder in Obsidian that defines how the agent should manage its own "consciousness" and session history. Step 1: The Skill Node Structure Create a folder in your Obsidian vault called Skills/System/Immortal_Protocol/. Inside, create a main file called SKILL.md. This isn't just a prompt; it's a Standard Operating Procedure (SOP). # Skill: Immortal Protocol (v1.0) **Description:** A persistence layer for maintaining context and task state across session resets. ## 1. Initial Handshake (Bootup) On start, the harness MUST: 1. Use Obsidian MCP to list files in `Memory/Current_State/`. 2. Read `Last_Session_Summary.md` and `Active_Goals.json`. 3. Set the internal "Task Pointer" to the last recorded step. ## 2. The Persistence Loop (Shutdown/Pause) Before any pause or on user command "Snapshot": 1. Summarize the current conversation's progress. 2. Update `Memory/Current_State/Checkpoints/` with a timestamped log. 3. Update the global `Project_Status_Board.md`. ## 3. Error Recovery If a "Context Overflow" or "Crash" occurs: 1. Discard current working memory. 2. Re-initialize from the last verified Checkpoint. Step 2: Connect via MCP Since you're using the Model Context Protocol, you don't need to write new code for the "Immortal" part. You just tell Hermes (the harness) how to use the MCP tools to interact with this skill. In your Harness System Prompt, add this instruction: "You have access to a library of Skills in your Obsidian vault. If the user refers to 'Project Immortal' or requests persistence, load and strictly follow the protocol defined in Skills/System/Immortal_Protocol/SKILL.md." Step 3: Why This Saves You Time Stop Coding, Start Documenting: You no longer have to worry about how the agent saves its state in Python. You just define where it should write the file in Obsidian using the MCP tool it already has. Model Agnostic: If Hermes v0.6.0 crashes or gets replaced by Gemma 4, the Immortal Skill stays in your vault. The new model just reads the "Initial Handshake" and picks up exactly where the last one left off. Scalability: If you want to add a "Recall" feature later, you don't rebuild the agent. You just update the SKILL.md file with a new section on "Memory Retrieval Logic." The Immediate Action Take whatever you've brainstormed for "Immortal Agent" so far and dump it into that SKILL.md file. Don't worry about it being "done"—the beauty of a Skill Node is that the agent can help you finish it once it has the file in its context. Does this feel like it clears the "work in progress" hurdle for you, or is there a specific technical feature of the Immortal Agent (like a specific script or DB) that you're worried about losing?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
