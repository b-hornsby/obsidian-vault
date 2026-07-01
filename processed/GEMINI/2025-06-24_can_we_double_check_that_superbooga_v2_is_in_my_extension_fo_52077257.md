---
id: 634351
source: GEMINI
date: 2025-06-24
tags: ['text-generation-webui', 'superboogav2', 'extension-directory', 'troubleshooting']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan requested to double-check that the `superboogav2` extension is present in the extensions folder before attempting to launch it again.
---
# can we double check that superbooga v2 is in my extension folder before we try to launch it again?

### USER
can we double check that superbooga v2 is in my extension folder before we try to launch it again?

### GEMINI
You are absolutely right to double-check! My apologies for assuming it was in the right place based on a previous ls -F output that included superbooga/ and superboogav2/ at ~/text-generation-webui/extensions. It's always best to verify directly, especially when troubleshooting a stubborn issue. Let's do that right now. Step 10 (Revised): Confirm superboogav2 is in the extensions folder. Action: Go to your WSL2 terminal. Ensure you are in the text-generation-webui/extensions directory: cd ~/text-generation-webui/extensions List the contents of this directory, specifically looking for superboogav2/: ls -F Please paste the output of this ls -F command. This will confirm definitively if the superboogav2 directory is present where Oobabooga expects to find it. Once we confirm it's there, we'll try the full restart and UI refresh again. If it's not there, that's a different problem we need to fix first.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
