---
id: 356527
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'model', 'gguf', 'hermes', 'text-generation', 'go']
category: ai-tools
sentiment: stuck
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# if i'm here: (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ where do i go to find the model for this? 

### USER
if i'm here: (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ where do i go to find the model for this? 

### GEMINI
Okay, great question! You're in the right spot to find your model. From (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$, your models are almost certainly located in the models/ subdirectory. To find the exact filename of your Nous-Hermes-2 Mistral GGUF model, just type: ls models/ This command will list all the contents of the models/ folder. Look for a file that ends with .gguf and has "hermes" and "mistral" in its name. For example, you might see something like: TheBloke_Nous-Hermes-2-Mistral-7B-DPO-GGUF/ (this is a folder containing the model) nous-hermes-2-mistral-7b-dpo.Q4_K_M.gguf (this is the actual model file) If you see a folder, you'll need to look inside that folder. For example, if you see TheBloke_Nous-Hermes-2-Mistral-7B-DPO-GGUF/, then you'd type: ls models/TheBloke_Nous-Hermes-2-Mistral-7B-DPO-GGUF/ Once you find the exact .gguf filename, that's what you'll use with the --model flag. Please run ls models/ and tell me what you see listed. That will help us confirm the model's exact path.