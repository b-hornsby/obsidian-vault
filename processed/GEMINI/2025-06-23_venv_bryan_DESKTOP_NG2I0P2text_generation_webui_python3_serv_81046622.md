---
category: homelab
date: 2025-06-23
id: 520595
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: resolved
sentiment: executing
source: GEMINI
summary: The user successfully launched the Text generation web UI with llama.cpp
  loader and GPU layer offloading on their local machine, confirming the service is
  running on localhost:7860.
tags:
- text-generation-webui
- llama.cpp
- local-llm
- gpu-offloading
- model-serving
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:08:30-831937 INFO     Starting Text generation web UI
14:08:30-833889 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
14:08:30-831937 INFO     Starting Text generation web UI
14:08:30-833889 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860

### GEMINI
OK, Bryan! This looks like a positive start. The output Running on local URL: http://127.0.0.1:7860 indicates that the web UI server itself has started successfully after the git pull. This is great because it means the previous IndentationError has likely been resolved by the updated code. Now, the critical part is whether the model loads. What I need you to do now: Go to your web browser and ensure you're on the oobabooga Text Generation WebUI page at http://127.0.0.1:7860. (You might need to refresh the page if it was open from before). Navigate to the "Model" tab. Select "Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf" from the dropdown menu on the left. Click the "Load" button (the big one below the model selection). What I need from you: Copy and paste all of the new output that appears in your Ubuntu WSL2 terminal after you click the "Load" button in the web UI. This output will show us the model loading process and confirm whether your RTX 3070 is being utilized. This is the moment of truth!