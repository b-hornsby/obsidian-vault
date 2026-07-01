---
id: 447219
source: GEMINI
date: 2025-06-23
tags: ['wsl2', 'ubuntu', 'powershell', 'local-llm-setup', 'environment-setup']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking about the correct way to launch WSL2 with Ubuntu, specifically whether using PowerShell is necessary if he has a desktop shortcut.
---
# do i need to launch wsl through powershell if i have ubuntu shortcut on desktop? 

### USER
do i need to launch wsl through powershell if i have ubuntu shortcut on desktop? 

### GEMINI
You're asking excellent questions that clarify common user experiences! No, you absolutely do not need to launch WSL through PowerShell if you have an Ubuntu shortcut on your desktop. Both methods do the same thing: they launch your default Ubuntu WSL2 distribution. The desktop shortcut is essentially a convenient way to run the wsl.exe command (or a similar command that points to your specific distribution) in the background. So, feel free to use your Ubuntu desktop shortcut to open the terminal. Once it's open, you'll be inside your Ubuntu WSL2 environment, and you can then proceed with Step 2 (or rather, continue with finding the model using the pwd, ls, and find commands) from there. Go ahead and launch it using your desktop shortcut, and then begin the search for your model file as described previously. Let me know what you find!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
