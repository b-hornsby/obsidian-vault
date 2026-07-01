---
category: ai-tools
date: 2025-07-14
id: 370837
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to locate the directory where his Phi-3 Mini model is stored
  within the text-generation-webui, indicating he's having trouble finding it.
tags:
- text-generation-webui
- model-directory
- phi-3-mini
- local-llm
---
# from text-generation-webui$ where can i find what directory my model is in? i used phi 3 mini but i'm not sure what the rest of the file name is 

### USER
from text-generation-webui$ where can i find what directory my model is in? i used phi 3 mini but i'm not sure what the rest of the file name is 

### GEMINI
In text-generation-webui, your models are typically located in the text-generation-webui/models/ directory. To find your "phi 3 mini" model, you'll need to look inside this models directory. It's likely in a subfolder named something like Phi-3-mini or similar. Here's how you can find it using the Linux command line within your WSL2 instance, assuming you are currently in the text-generation-webui directory: ls -l models/ This command will list the contents of the models directory. You should see a folder there that contains your "phi 3 mini" model. If you're not sure of the exact name, you can use find within that directory: find models/ -name "*phi*mini*" 2>/dev/null This will search for any files or directories containing "phi" and "mini" within the models/ folder. The actual model files (like .bin or .safetensors) will be inside that specific model's directory.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
