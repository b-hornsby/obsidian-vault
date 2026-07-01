---
category: homelab
date: 2025-06-24
id: 262617
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is searching for a specific GGUF model file (Nous-Hermes-2-Mistral)
  in their home directory but the find command returned no results, indicating the
  model file may not be present or was named differently.
tags:
- local-llm
- model-file-search
- text-generation-webui
- gguf-models
- file-system-navigation
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ find ~ -iname "*Nous-Hermes-2*Mistral*.gguf" 2>/dev/null
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ find ~ -iname "*Nous-Hermes-2*Mistral*.gguf" 2>/dev/null
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Okay, the fact that the find command returned no output is a definitive answer: the Nous-Hermes-2 Mistral 7B.gguf model file is no longer present on your WSL filesystem. This means that during the process of troubleshooting and re-setting up, at some point, the directory where you had it stored (likely ~/text-generation-webui/models/) was either deleted or recreated. What to do now: Now that llama.cpp is successfully built with CUDA support, and we've confirmed the model is not present, your next step is to download Nous-Hermes-2 Mistral 7B again. Run the text-generation-webui and use its built-in model download functionality: Start text-generation-webui: cd ~/text-generation-webui python3 server.py --listen --model-menu Access the Web UI: Once it starts, it will provide a URL (usually http://127.0.0.1:7860). Open this in your Windows web browser. Download the Model: In the web UI, go to the "Model" tab. In the "Download model or LoRA" section, you'll enter the Hugging Face repository ID. For Nous-Hermes-2 Mistral 7B, a popular one from TheBloke (who converts models to GGUF) is: TheBloke/Nous-Hermes-2-Mistral-7B-DPO-GGUF After entering that, a dropdown list will appear below it, showing various .gguf files (different quantizations). Choose one that fits your GPU's VRAM. A common choice for a good balance of speed and quality is nous-hermes-2-mistral-7b-dpo.Q4_K_M.gguf. Click the "Download" button. This will download the model into your ~/text-generation-webui/models/ directory. This is a large file (several GBs), so it will take some time. Load the Model: Once downloaded, it should appear in the "Model" dropdown list at the top of the "Model" tab. Select it and click the "Load" button. Once the model is loaded, text-generation-webui will report that it's offloading layers to the GPU, and you can then go to the "Text generation" tab to start chatting with your AI!