---
id: 420688
source: GPT
date: 2025-07-13
tags: ['wsl2', 'model-path', 'phi-3-mini', 'oobabooga', 'file-system']
category: homelab
sentiment: stuck
resolution: resolved
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to locate the exact file path of the Phi-3-mini model in his WSL2 file system.
---
# WSL2 Model Location Scan

### USER
what command can i run in wsl2 that allows me to scan the entire directory to find where the model is located?

### ASSISTANT
Got it! To find the exact location and filename of your **Phi-3 Mini** model in WSL2, you can run this command to look for anything with `phi` or `phi-3` in the filename (case-insensitive):

```bash
find ~ -iname "*phi*3*mini*" 2>/dev/null
```

This searches your **home directory** (usually where downloads or projects live) for files or folders with names containing those keywords.

If you want to scan the **entire filesystem** (this can take longer and show permission errors):

```bash
find / -iname "*phi*3*mini*" 2>/dev/null
```

If the model files tend to be `.bin` or `.pt` files, you could narrow it to:

```bash
find ~ -iname "*phi*3*mini*.bin" 2>/dev/null
```

or

```bash
find ~ -iname "*phi*3*mini*.pt" 2>/dev/null
```

If you want to limit the search to your home directory (which is usually faster):

```bash
find ~ -iname "*model*" 2>/dev/null
```

Let me know if you want help with filtering or a more specific search!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]