---
category: ai-tools
date: 2025-06-24
id: 20710
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble finding where to set the model path in text-generation-webui.
tags:
- text-generation-webui
- model-path-configuration
- local-llm-setup
---
# this is what i see i can't find where to se the model path

### USER
this is what i see i can't find where to se the model path

### GEMINI
Thank you for the screenshot! This is extremely helpful. You're right, Oobabooga's UI has evolved, and the explicit "Model folder" path isn't always directly visible on that main Model tab anymore, especially for GGUF models. However, the fact that you see "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" successfully loaded tells me a lot. Since it's a GGUF file, and you mentioned nothing was in your models directory when you ran ls -F, it strongly suggests that the GGUF file itself is located within the main text-generation-webui directory, or in a subfolder that server.py is implicitly looking in. Let's try one more diagnostic step to pinpoint its exact location. Step 3: Locate the .gguf file using a Linux command. We'll use the find command within your WSL2 environment to locate the model file. Action: Go back to your WSL2 terminal. Navigate to your home directory: To ensure we search a broad area, let's start from your home directory (~). cd ~ Run the find command: We'll search for the specific filename you showed in the screenshot: Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf. find . -name "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" find .: This tells the command to start searching from the current directory (., which is your home directory in this case) and all its subdirectories. -name "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf": This tells find to look for files with this exact name. Please paste the output of this find command. It should give us the full path to your .gguf model file. This is crucial for knowing where to place other related files for future steps.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
