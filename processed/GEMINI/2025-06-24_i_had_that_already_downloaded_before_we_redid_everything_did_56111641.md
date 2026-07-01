---
id: 115605
source: GEMINI
date: 2025-06-24
tags: ['model-management', 'Nous-Hermes-2', 'file-deletion', 'cleanup']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was asking whether his previously downloaded model file was deleted during the environment reset process.
---
# i had that already downloaded before we redid everything. did it get deleted in the process? 

### USER
i had that already downloaded before we redid everything. did it get deleted in the process? 

### GEMINI
You're absolutely right to remember that! My apologies for not keeping track of that specific detail from the very beginning of our conversation. It's entirely possible you had downloaded it previously. Here's what likely happened and how to check: text-generation-webui stores its models in a dedicated models subfolder within its main directory. So, if you had Nous-Hermes-2 Mistral 7B downloaded before, it would have been located at: ~/text-generation-webui/models/Nous-Hermes-2-Mistral-7B-YOUR_QUANTIZATION.gguf (or a similar path, as models are often put into their own subfolder within models). Did it get deleted? If you completely re-cloned text-generation-webui or deleted its main directory: Yes, then any models you had downloaded within that specific text-generation-webui/models folder would have been deleted along with it. If you only re-built llama.cpp or updated dependencies within the existing text-generation-webui directory: Then your models folder and its contents should still be there. The llama.cpp build process doesn't touch the models directory. How to check if the model is still there: You can quickly check by listing the contents of your models directory: ls -l ~/text-generation-webui/models/ If you see a file like Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf (or a similar name) in the output, then the model file is still there! If it is, then when you run python3 server.py --listen --model-menu, it should appear in the "Model" dropdown menu on the text-generation-webui interface. You can then simply select it and click "Load". Let me know what the ls -l command shows!
