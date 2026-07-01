---
id: 722836
source: GEMINI
date: 2026-02-26
tags: ['npm-global', 'zshrc', 'PATH', 'cachyos', 'fish-shell-error']
category: coding
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was trying to add npm-global to PATH in .zshrc but encountered a fish-shell compatibility error in the CachyOS zsh config.
---
# ❯ echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
/usr/share/cachyos-zsh-config/cachyos-config.zsh (line 13): Unsupported use of '='. In fish, please use 'set DISABLE_MAGIC_FUNCTIONS "true"'.
DISABLE_MAGIC_FUNCTIONS="true"
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
from sourcing file /usr/share/cachyos-zsh-config/cachyos-config.zsh
        called on line 1 of file ~/.zshrc
from sourcing file ~/.zshrc
source: Error while reading file “/usr/share/cachyos-zsh-config/cachyos-config.zsh”

~/vc projects/immortal agent
❯ 

### USER
❯ echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
/usr/share/cachyos-zsh-config/cachyos-config.zsh (line 13): Unsupported use of '='. In fish, please use 'set DISABLE_MAGIC_FUNCTIONS "true"'.
DISABLE_MAGIC_FUNCTIONS="true"
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
from sourcing file /usr/share/cachyos-zsh-config/cachyos-config.zsh
        called on line 1 of file ~/.zshrc
from sourcing file ~/.zshrc
source: Error while reading file “/usr/share/cachyos-zsh-config/cachyos-config.zsh”

~/vc projects/immortal agent
❯ 

### GEMINI
The error message reveals the "mirror" truth: You aren't using Zsh. Despite CachyOS often defaulting to Zsh, that error message—In fish, please use 'set...'—is a dead giveaway. You are running Fish shell. You've been trying to feed Zsh commands to a Fish terminal, which is why it's spitting them back at you. Let’s pivot to the correct syntax for your environment so we can stop wasting time on "permission hell." 1. Fix the PATH for Fish In Fish, we don't use export or edit .zshrc. Run this single command in your Cursor terminal: fish_add_path ~/.npm-global/bin This command is persistent; you only need to run it once and it survives restarts. 2. Install Claude Code Now that the path is actually set correctly for Fish, run the install again: npm install -g @anthropic-ai/claude-code 3. Verify and Login Test if the command is recognized: claude --version If it gives you a version number, you're golden. Now run: claude Follow the browser prompts to link your Claude Pro account. The Advisor's Cold Reality: "The Tool vs. The Craftsman" You are currently battling the environment, not the code. This is a classic "Opportunity Cost" trap. You've spent the last 15 minutes fighting shell syntax because of a simple misidentification of your shell. The Strategy for immortal agent: Since you're on CachyOS (Arch-based) and using Fish, you likely value speed and modern tooling. Cursor (Free) is your "Read-Only" or "Minor Edit" window. Claude Code is your "Heavy Lifter." Stop "Playing Small": If immortal agent is a serious project, don't let these configuration hurdles derail you. Once claude is running, your first command should be to have it look at your structure. Next Step: Is claude --version working now? If yes, tell me: What is the tech stack for "Immortal Agent"? (Python? TypeScript? Rust?). I will then give you a CLAUDE.md file that ensures the AI doesn't hallucinate commands that don't work in your specific Fish/CachyOS setup.
