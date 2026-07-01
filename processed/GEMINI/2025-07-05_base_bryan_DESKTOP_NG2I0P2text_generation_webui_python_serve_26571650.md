---
category: ai-tools
date: 2025-07-05
id: 979613
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: Bryan is trying to run the text-generation-webui server with a specific model
  and API enabled, but encounters an error.
tags:
- text-generation-webui
- '''local-llm-deployment'''
- '''api-setup'''
- '''nous-hermes-2-mistral-7b'''
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf --api
╭───────────────────────────────────────── Traceback (most recent call last) ──────────────────────────────────────────╮
│ /home/bryan_/text-generation-webui/server.py:6 in <module>                                                           │
│                                                                                                                      │
│     5                                                                                                                │
│ ❱   6 from modules import shared                                                                                     │
│     7 from modules.block_requests import OpenMonkeyPatch, RequestBlocker                                             │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/shared.py:12 in <module>                                                  │
│                                                                                                                      │
│    11 from modules.logging_colors import logger                                                                      │
│ ❱  12 from modules.presets import default_preset                                                                     │
│    13                                                                                                                │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/presets.py:8 in <module>                                                  │
│                                                                                                                      │
│     7 from modules import shared                                                                                     │
│ ❱   8 from modules.loaders import loaders_samplers                                                                   │
│     9 from modules.logging_colors import logger                                                                      │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/loaders.py:4 in <module>                                                  │
│                                                                                                                      │
│     3                                                                                                                │
│ ❱   4 import gradio as gr                                                                                            │
│     5                                                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
ModuleNotFoundError: No module named 'gradio'
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf --api
╭───────────────────────────────────────── Traceback (most recent call last) ──────────────────────────────────────────╮
│ /home/bryan_/text-generation-webui/server.py:6 in <module>                                                           │
│                                                                                                                      │
│     5                                                                                                                │
│ ❱   6 from modules import shared                                                                                     │
│     7 from modules.block_requests import OpenMonkeyPatch, RequestBlocker                                             │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/shared.py:12 in <module>                                                  │
│                                                                                                                      │
│    11 from modules.logging_colors import logger                                                                      │
│ ❱  12 from modules.presets import default_preset                                                                     │
│    13                                                                                                                │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/presets.py:8 in <module>                                                  │
│                                                                                                                      │
│     7 from modules import shared                                                                                     │
│ ❱   8 from modules.loaders import loaders_samplers                                                                   │
│     9 from modules.logging_colors import logger                                                                      │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/loaders.py:4 in <module>                                                  │
│                                                                                                                      │
│     3                                                                                                                │
│ ❱   4 import gradio as gr                                                                                            │
│     5                                                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
ModuleNotFoundError: No module named 'gradio'
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Got it. Another Python module issue! This ModuleNotFoundError: No module named 'gradio' means that the gradio library, which Oobabooga uses for its web interface, isn't installed in the Python environment that Oobabooga is trying to use. This is a bit unusual if you've used start_linux.sh before, as that script is designed to set up the environment with all necessary dependencies. However, sometimes things can get out of sync or an installation might have been incomplete. Let's explicitly install gradio and make sure all Oobabooga's requirements are met. Solution: Install gradio and other Oobabooga dependencies Ensure you are in your Oobabooga directory in the second WSL2 terminal: cd ~/text-generation-webui (Your prompt should be (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$) Activate Oobabooga's specific Python environment. Oobabooga usually manages its own Python environment within installer_files/env/. To ensure we install gradio into the correct environment, it's best to run its setup script again, or explicitly activate its environment. Since you're using start_linux.sh, that usually handles it, but let's try a robust way. The easiest way to ensure all dependencies are met for Oobabooga is to run its installation script again. It's designed to check for and install missing packages without reinstalling everything if it's already there. ./start_linux.sh --update-only The --update-only flag will tell the script to just update dependencies and not try to launch the UI directly. This is a safer way to ensure everything is installed. This command might take a few minutes as it checks and potentially installs many packages, including gradio. After the update script finishes, restart Oobabooga again, explicitly loading the model with --model and enabling the API with --api. python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf --api Once again, wait for it to load completely. You'll know it's ready when you see the Uvicorn running on http://127.0.0.1:5000 message. Please perform these steps in your second WSL2 terminal (the Oobabooga one). Paste the full output of the python server.py command after the update has completed. This should finally get Oobabooga running correctly with the model loaded!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]