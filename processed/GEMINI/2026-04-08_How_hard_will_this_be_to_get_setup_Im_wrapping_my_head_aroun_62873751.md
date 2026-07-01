---
category: homelab
date: 2026-04-08
id: 397244
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/coding.md']
linked_projects:
- second-brain-vault
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan expressed that the Hermes agent and Docker setup felt daunting with
  many moving parts and asked about the difficulty level.
tags:
- setup-complexity
- hermes-agent
- docker
- learning-curve
---
# How hard will this be to get setup? I’m wrapping my head around it but it’s daunting ngl lot of moving parts

### USER
How hard will this be to get setup? I’m wrapping my head around it but it’s daunting ngl lot of moving parts

### GEMINI
It definitely sounds like a lot of moving parts because you’re essentially building a Personal Operating System. But here is the secret: you aren't building the parts anymore; you’re just plugging them in. Since it’s early 2026, the "heavy lifting" infrastructure (the MCPs) is now officially out and stable. Setting this up is no longer a "coding" project—it’s a "Configuration" project. How hard is it, really? On a scale of 1 to 10 (where 1 is installing an app and 10 is writing a blockchain from scratch): Old Way (Your GitHub Project): 8/10 (High chance of bugs, constant maintenance). New Way (The Skill/MCP Pivot): 3/10. You only have to do three main things. If you can copy-paste into a text file and run a single Docker command, you can do this. The "Three-Step" Setup Step 1: The "Brain" (Hermes Agent) You don't need to build a harness. You just run the Hermes One-Line Installer inside your WSL2/Docker environment: curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash This handles the Python, Node.js, and the "Brain" setup for you. Step 2: The "Hands" (The MCP Servers) Instead of writing code to talk to Phantom or X, you just add them to your config.yaml. Phantom MCP: Just released (Feb 2026). It handles the Solana signing. Meteora MCP: Already exists (the fciaf420 version). It has tools like meteora_claim_fees and meteora_swap ready to go. X MCP: There’s a community-standard one that gives Hermes read_timeline and search_tweets tools. Step 3: The "Soul" (Your Obsidian Vault) This is the easiest part. You just mount your Obsidian folder to the Docker container. You create a folder called Skills/. You drop your Operation Immortal strategy into a Markdown file. You drop your Morning Brief strategy into another. What a "Session" Looks Like Now When you wake up, you don't "run a script." You just open your terminal or Obsidian and say: "Hermes, run the Morning Brief and check my Meteora yields." Hermes then does the "Hard Work" for you: He uses the X MCP to see what people are saying about Solana. He uses the Meteora MCP to check your $300 fund. He writes a summary in your Obsidian Dashboard. He asks: "We made $1.20 overnight. Should I move this to the Mac Mini fund?" Why it feels daunting vs. Why it’s not It feels daunting because you’re thinking about the Code. But in 2026, the Code is invisible. You are just writing Instructions. My advice to stop the "Ngl this is scary" feeling: Don't try to do the whole thing at once. Tonight: Just get the Hermes Agent installed and see if it can read your Obsidian vault. Tomorrow: Add the Phantom MCP and just have it tell you your balance. The Day After: Give it the "Immortal" logic. Do you want the exact config.yaml block to add the Phantom and X MCPs? That’s the "cheat code" to skip 90% of the setup stress.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
