---
id: 875443
source: GEMINI
date: 2025-06-25
tags: ['coding', 'ai', 'gemini', 'oobabooga', 'text-generation', 'script', 'node', 'terminal']
category: coding
sentiment: executing
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
---
# so when i boot up now it'll always have: (base) bryan_@DESKTOP-NG2I0P2:~$

### USER
so when i boot up now it'll always have: (base) bryan_@DESKTOP-NG2I0P2:~$

### GEMINI
Yes, when you open a new WSL2 terminal window after a fresh bootup, it will typically default to the (base) Conda environment or no active environment at all, resulting in a prompt like (base) bryan_@DESKTOP-NG2I0P2:~$. This is because Conda environments need to be explicitly activated within each new terminal session. Therefore, to use Oobabooga, you'll always need to navigate to its directory and run its startup script after opening a new terminal, as described previously: cd ~/text-generation-webui ./start_linux.sh This ensures that Oobabooga's dedicated Conda environment is activated, and all necessary paths and dependencies are set correctly for its operation.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]