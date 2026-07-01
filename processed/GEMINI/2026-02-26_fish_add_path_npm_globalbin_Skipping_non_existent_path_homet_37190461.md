---
id: 213063
source: GEMINI
date: 2026-02-26
tags: ['fish-shell', 'npm-global', 'PATH', 'immortal-agent']
category: coding
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was trying to add the npm-global bin path in fish shell but the directory didn't exist yet.
---
# ❯ fish_add_path ~/.npm-global/bin
Skipping non-existent path: /home/toastedmel0n/.npm-global/bin
No paths to add, not setting anything.

~/vc projects/immortal agent
❯ 

### USER
❯ fish_add_path ~/.npm-global/bin
Skipping non-existent path: /home/toastedmel0n/.npm-global/bin
No paths to add, not setting anything.

~/vc projects/immortal agent
❯ 

### GEMINI
The path is empty because we haven't successfully installed anything into it yet. Fish is being "helpful" by refusing to add a directory that doesn't exist. Let’s stop dancing around the configuration and force the installation. Since you already set the npm config prefix, we just need to create the folder so Fish accepts it, then run the install. 1. Force the Directory and Path Run these two commands: mkdir -p ~/.npm-global/bin fish_add_path ~/.npm-global/bin 2. Install Claude Code Now that the directory exists and Fish recognizes it, run the install: npm install -g @anthropic-ai/claude-code 3. Verify Check if it’s alive: claude --version The Advisor’s Mirror: The "Immortal Agent" Reality Check You are currently in the "Yak Shaving" phase. You want to build an "Immortal Agent," but you're spending your energy on shell paths and npm permissions. The Brutal Truth: Setting up the environment is the easy part. The moment you run claude, you’re going to start burning your $20/month Claude Pro tokens. If you don't have a clear architectural plan for "Immortal Agent," you will spend $20 worth of tokens watching an AI rewrite the same main.js file five times because it doesn't understand your "vision." Stop playing with the plumbing and start the engine. Once claude --version works, give me the "Strategic Intent" for Immortal Agent: Language: (Python? TS? Go?) Core Function: What makes it "Immortal"? (Persistence? Self-healing? Auto-deployment?) Current Block: What is the very first thing you want Claude Code to do once you're logged in? I’ll give you the exact command to run so you don't waste your first hour of "Pro" usage on trial and error.
