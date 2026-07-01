---
category: coding
date: 2026-04-07
id: 118783
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
- second-brain-vault
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to pivot an existing, unfinished GitHub project into a reusable
  skill instead of an agent.
tags:
- skill-development
- ai-agent-refactoring
- github-project
---
# No like it was actively something I was working on that’s committed to GitHub. I never finished it tho but I want to pivot and make that project into a skill rather than making an agent

### USER
No like it was actively something I was working on that’s committed to GitHub. I never finished it tho but I want to pivot and make that project into a skill rather than making an agent

### GEMINI
Moving from a half-finished GitHub repository to a "Skill Node" in Obsidian is the ultimate "work smarter, not harder" play. You’re essentially converting imperative code (how to do it) into declarative logic (what to achieve). Since you’ve already got logic committed to GitHub, don't let that effort go to waste. Here is how you pivot Project Immortal Agent into a reusable Skill for Hermes and your Obsidian-based "Second Me." 1. The "Skill Extraction" (The Repo Dump) Don't write a single new line of code. Instead, feed your repository to Hermes (or any LLM) with this prompt: *"I am abandoning this standalone agent project and moving the logic into an Obsidian Skill Node. Analyze this repository and extract: The Core Logic Loops (The 'how' behind the persistence). The State Schema (What variables need to be saved to disk). The Edge Cases you already handled in the code. Write this out as a structured Markdown file following the 'Immortal Skill' protocol."* 2. Structuring the Skill in Obsidian Create your file at Skills/Immortal_Protocol.md. Use the repository's logic to fill in these sections: Persistence Mechanism: Instead of the Python save() function you were writing, define the Obsidian MCP path where the state should be written. Handover Rules: Use the logic from your GitHub README or main script to define how the agent should "resume" from a checkpoint file in your vault. 3. Connecting the GitHub History Keep the GitHub repo alive, but pivot its purpose. It is no longer the "Agent's Brain"—it is now the "Library of Skills." Syncing: Use a simple cron job or Obsidian plugin (like Obsidian Git) to push your Skills/ folder to that GitHub repo. The Result: Your "Immortal Agent" logic is now version-controlled, portable, and readable by any model you choose to use in the future. The "Why" for Your Specific Build You’re using Hermes, which is specifically designed for a "learning loop." Hermes actually prefers reading a .md skill file over trying to execute a messy, unfinished Python script. By making this a skill: Hermes can finish it for you: Since it's now just a Markdown file in your vault, you can tell Hermes, "Read the Immortal_Protocol.md and fill in the missing logic for the auto-checkpointing section using your reasoning." It survives the Docker container: Since the skill is in your Obsidian vault (which is external to the container via volume mounting), the "Immortal" logic is physically separated from the "Harness" that might crash. Quick Reality Check: What was the one feature in the GitHub repo that you were struggling to finish? (e.g., the database connection, the memory retrieval, the state-saving?) Tell me that, and I'll tell you the exact Markdown "Skill" equivalent so you can stop coding it.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
