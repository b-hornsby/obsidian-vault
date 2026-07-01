---
id: 081901
source: GEMINI
date: 2026-02-26
tags: ['claude-code', 'npm-install', 'fish-shell', 'environment-setup']
category: coding
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was setting up Claude Code globally via npm and configuring the fish shell PATH in the immortal agent project directory.
---
# ~/vc projects/immortal agent
❯ mkdir -p ~/.npm-global/bin

~/vc projects/immortal agent
❯ fish_add_path ~/.npm-global/bin
set -U fish_user_paths /home/toastedmel0n/.npm-global/bin

~/vc projects/immortal agent
❯ npm install -g @anthropic-ai/claude-code

added 3 packages in 877ms

2 packages are looking for funding
  run `npm fund` for details

~/vc projects/immortal agent
❯ 

### USER
~/vc projects/immortal agent
❯ mkdir -p ~/.npm-global/bin

~/vc projects/immortal agent
❯ fish_add_path ~/.npm-global/bin
set -U fish_user_paths /home/toastedmel0n/.npm-global/bin

~/vc projects/immortal agent
❯ npm install -g @anthropic-ai/claude-code

added 3 packages in 877ms

2 packages are looking for funding
  run `npm fund` for details

~/vc projects/immortal agent
❯ 

### GEMINI
Success. You’ve successfully navigated the Arch/Fish/NPM permissions gauntlet. One minor note: added 3 packages is suspicious. Usually, the full Claude Code CLI install is much larger. It’s possible that because you're on CachyOS (Arch), some dependencies were already met, or you might have accidentally grabbed a thin wrapper. 1. The Moment of Truth Run this now: claude --version If it works: It will spit out a version number (e.g., 0.2.x). Proceed to step 2. If it says "command not found": Fish hasn't refreshed its internal map. Run hash -r or just close and reopen the Cursor terminal. 2. Login Run the initialization: claude This will open your browser. Use your Claude Pro account. Once the terminal says "Authenticated," you are officially "Pro" in your terminal, while remaining "Free" in the Cursor UI. 3. Strategic Setup: CLAUDE.md Since you are building an Immortal Agent, you cannot afford for Claude to guess your architecture. In the root of your project, create a file named CLAUDE.md. Claude Code reads this file first every time you start a session. Use this template to keep it on track: # Immortal Agent Project Rules ## Tech Stack - OS: CachyOS (Arch Linux) - Shell: Fish - Runtime: [e.g., Node v22 / Python 3.12] ## Project Standards - Architecture: [e.g., Event-driven, Micro-agent] - Naming: [e.g., camelCase for JS, snake_case for Python] - Error Handling: Always use [e.g., Result types / Try-Catch] ## Core Commands - Build: [e.g., npm run build] - Test: [e.g., pytest] - Run: [e.g., ./start_agent.sh] ## The "Immortal" Vision - [Describe in 1 sentence what the agent's primary goal is so Claude doesn't refactor away your core purpose.] The Advisor's Mirror: You are now at the starting line. Most people fail here by asking the AI to "start building." Don't do that. Your first move with Claude Pro should be a Security & Environment Audit. Since you’re on CachyOS, you have a high-performance kernel. If your agent starts spinning up unoptimized loops, you'll feel it. Is claude --version showing a number? If so, tell me your tech stack (Node, Python, Rust?) and I'll give you the first "immortal" logic block to test its reasoning.
