---
id: 998597
source: GEMINI
date: 2025-06-23
tags: ['wsl2', 'environment-compatibility', 'local-llm-setup']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is questioning whether a specific command or process can be run directly within WSL2.
---
# i can't just run that in wsl2?

### USER
i can't just run that in wsl2?

### GEMINI
You're right to ask for clarification! My apologies. While wsl -l -v does interact with WSL, it's a command that you run directly in the Windows PowerShell or Command Prompt, not inside the WSL2 terminal itself. Think of it this way: wsl -l -v is a command for Windows to tell you about the WSL distributions it has installed. Once you're inside a specific WSL distribution (like Ubuntu, for example), you're using Linux commands. So, to reiterate: Action: Please open a Windows PowerShell or Command Prompt window (you can search for "PowerShell" in your Windows search bar) and run the command: wsl -l -v Then, copy and paste the full output back here. This is a crucial first step for me to understand your environment. I'll be waiting for that output before we move on!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
