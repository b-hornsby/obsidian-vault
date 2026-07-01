---
id: 993319
source: GEMINI
date: 2026-02-26
tags: ['npm-global', 'npm-config', 'prefix', 'cachyos', 'claude-code-install']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was setting up a user-level npm global directory to avoid permission issues when installing Claude Code.
---
# so after these three what do i need to do? : ~/vc projects/immortal agent
❯ mkdir ~/.npm-global

~/vc projects/immortal agent
❯ npm config set prefix '~/.npm-global'

~/vc projects/immortal agent
❯ 

### USER
so after these three what do i need to do? : ~/vc projects/immortal agent
❯ mkdir ~/.npm-global

~/vc projects/immortal agent
❯ npm config set prefix '~/.npm-global'

~/vc projects/immortal agent
❯ 

### GEMINI
You are halfway through the "clean" fix. Now you need to make sure your computer actually knows where to look for the claude command once it's installed. 1. The Critical Step: Update your PATH Right now, you've told npm where to put the files, but your terminal doesn't know to check that new folder for executable programs. Since you are likely using Zsh (common on macOS and modern Linux), run this command to append the path to your configuration file: echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc Now, force the terminal to notice the change by running: source ~/.zshrc 2. The Installation Now that the pipes are connected, run the install command again. It should work without sudo and without errors: npm install -g @anthropic-ai/claude-code 3. The Activation Once that finishes, verify it by typing: claude It will prompt you to log in via your browser. Use your Claude Pro account here. Advisor's Reality Check: "Immortal Agent" Since you’re working on something called immortal agent, you are likely dealing with loops, state management, or long-running processes. The Strategy: When you start claude inside this project folder, it will index your files. Because you are on the Cursor Free Tier, do not waste your limited Cursor "Composer" uses on complex logic. Use Cursor for: Fast UI tweaks and "seeing" the code. Use Claude Code for: "Implement the memory persistence layer for the agent" or "Debug why the event loop is hanging." Would you like me to help you define the CLAUDE.md file now? This file acts as the "Brain" for Claude Code. Without it, Claude will guess your coding style. With it, it will know exactly how immortal agent is supposed to behave before it writes a single line.
