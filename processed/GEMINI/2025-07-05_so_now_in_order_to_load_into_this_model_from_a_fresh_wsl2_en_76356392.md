---
id: 846895
source: GEMINI
date: 2025-07-05
tags: ['oobabooga', 'model-loading', 'wsl2', 'command-sequence']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking for the specific commands needed to load a model into oobabooga from a fresh WSL2 environment.
---
# so now in order to load into this model from a fresh wsl2 environment what commands would i use? 

### USER
so now in order to load into this model from a fresh wsl2 environment what commands would i use? 

### GEMINI
To load into your newly downloaded Phi-3-mini model from a fresh WSL2 environment, you'll use two main commands: one to start Oobabooga's web UI and another, within the UI, to load the specific model. Here's the step-by-step process: 1. Start Oobabooga's Web UI First, you need to launch the Oobabooga text generation web UI. Open your WSL2 terminal and navigate to your text-generation-webui directory. Then run: cd ~/text-generation-webui/ ./installer_files/env/bin/python server.py cd ~/text-generation-webui/: This changes your current directory to where Oobabooga is installed. ./installer_files/env/bin/python server.py: This command starts the Oobabooga web UI server. It won't load any large model by default at this stage, so it should start relatively quickly. 2. Load the Phi-3-mini Model in the UI Once the server is running, open your web browser and go to http://127.0.0.1:7860. a. Navigate to the Model Tab Click on the "Model" tab in the Oobabooga web UI. b. Select and Load the Model In the "Model" tab, locate the dropdown menu that lists the available models. From this dropdown, select your downloaded model, which should be something like phi-3-mini-4k-instruct.Q4_K_M.gguf. Below the model selection, you'll see a setting for "Number of layers to offload to GPU" (or n_gpu_layers). Set this to 999 to ensure the entire model runs on your GPU for maximum speed. Click the "Load" button next to the model dropdown. c. Verify and Configure Extensions After the model loads (which may take a minute or two), go to the "Extensions" tab. Ensure whisper_stt is checked. Ensure coqui_tts is UNCHECKED. Ensure superboogav2 is UNCHECKED. Ensure web_rag is UNCHECKED. Then, go to the Whisper STT section in your settings (often found under the "Settings" or "Interface" tab) and confirm: Device is set to cuda. Whisper Model is set to base.en (or tiny.en if you prioritize absolute input speed over accuracy). Submit the transcribed audio automatically is checked. d. Save Settings (Crucial for future loads) Finally, click "Save settings to user_data/settings.yaml" in the Extensions tab. This will save your current model and extension configuration, so the next time you start Oobabooga with just server.py, it will automatically load this setup. Now you're ready to use your voice input with the optimized Phi-3-mini model!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
