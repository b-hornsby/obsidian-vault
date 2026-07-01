---
category: coding
date: 2026-02-28
id: 179264
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to authenticate with GitHub via `gh auth login` but the
  `gh` command was not found in fish shell.
tags:
- github-cli
- fish-shell
- authentication
- gh-not-found
---
# ❯ gh auth login
fish: Unknown command: gh

~/vc projects/immortal agent main*
❯ 

### USER
❯ gh auth login
fish: Unknown command: gh

~/vc projects/immortal agent main*
❯ 

### GEMINI
You don't have the GitHub CLI installed, and you're using the Fish shell, which is why the previous command with < > failed so spectacularly (Fish is even more sensitive to those characters). Since you are in a flow and don't want to stop to install new software, we are going to use the Manual Token Injection method. This is the "brute force" way to bypass the 401 error. The "Brute Force" Fix (Fish Shell Compatible) Get your Token: If you don't have a Personal Access Token (PAT) with repo permissions, create one here. Copy it immediately. Run this exact command (I have wrapped the URL in single quotes so Fish doesn't try to "help" you by parsing it): git push -f 'https://YOUR_TOKEN_HERE@github.com/toastedmel0n/self_sustained_agent.git' main (Replace YOUR_TOKEN_HERE with the actual string of letters and numbers GitHub gave you.) The Advisor’s Cold Truth You are hitting "Tooling Friction." You’re using Fish, which is a great shell for productivity, but it handles syntax differently than standard Bash/Zsh. The Blind Spot: You’re trying to use "Pro" commands (gh) without the "Pro" setup. If you're going to build an "Immortal Agent," your local environment needs to be bulletproof. Install the GitHub CLI later today. The Security Leak: Because you are in Fish, your command history is saved in ~/.local/share/fish/fish_history. Once this push works, you must delete that token from your history. If someone gets access to your machine, they own your GitHub. The Opportunity Cost: This is the 10th turn of our conversation about "how to push code." In a high-stakes environment, this delay is a bottleneck. The Final Step to Freedom Execute the command with the single quotes. Verify on GitHub: Refresh the page. You should see 1 Commit and No .env. Clean your history: Run history delete --contains YOUR_TOKEN_HERE in Fish to scrub the evidence. Once that push hits, do you want to move on to the actual logic in src/engine/meteora.ts, or is there another "cleanup" task holding you back?
