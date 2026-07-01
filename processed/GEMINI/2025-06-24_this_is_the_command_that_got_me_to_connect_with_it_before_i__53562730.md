---
id: 191533
source: GEMINI
date: 2025-06-24
tags: ['text-generation-webui', 'llama.cpp', 'local-llm-execution']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is providing the command he previously used to connect to text-generation-webui, likely to help troubleshoot a current issue.
---
# this is the command that got me to connect with it before i try these steps if that helps: cd ~/text-generation-webuisource .venv/bin/activatepython3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp

### USER
this is the command that got me to connect with it before i try these steps if that helps: cd ~/text-generation-webuisource .venv/bin/activatepython3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp

### GEMINI
Aha! That command is extremely helpful and tells me exactly what's going on! The --model-dir "user_data/models" argument is the key. This means that when you start Oobabooga, it's explicitly told to look for models inside a folder named models which is inside user_data, which is itself inside your text-generation-webui directory. This explains why ls -F in ~/text-generation-webui/models showed nothing – your model isn't there! It's in ~/text-generation-webui/user_data/models. Thank you for providing that detail. This confirms the location we need to work with. Step 3 (Revisited): Verify the model's actual location Now that we know where it should be, let's confirm it. Action: Go back to your WSL2 terminal. Navigate to the user_data/models directory within your Oobabooga installation: cd ~/text-generation-webui/user_data/models List the contents of this directory: ls -F Please paste the output of this ls -F command. This should finally show your Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf file. Once we confirm its presence here, we can move on to setting up knowledge retrieval.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
