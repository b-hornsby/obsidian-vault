---
category: ai-tools
date: 2025-06-23
id: 392459
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: User is trying to run text-generation-webui with llama.cpp loader and GPU
  offloading but encounters an import error during startup, indicating a missing or
  misconfigured dependency.
tags:
- text-generation-webui
- llama.cpp
- GPU configuration
- model loading
- debugging
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Fantastic! This is a very clear error and indicates exactly what the problem is: ModuleNotFoundError: No module named 'gradio'. This means that a required Python library, gradio (which oobabooga uses for its web interface), is not installed in your Python environment within WSL2. This is extremely common when you first set up a new Python project or environment. Step 4: Install Missing Python Dependencies We need to install gradio and potentially other dependencies that oobabooga requires. Oobabooga typically comes with a requirements.txt file that lists all necessary Python packages. We'll use pip (Python's package installer) to install these. Action: Install the required Python packages using pip. What I need you to do now (in your Ubuntu WSL2 terminal, still in ~/text-generation-webui): Install the dependencies: Command: pip install -r requirements.txt Explanation of this command: pip: The Python package installer. install: Tells pip to install packages. -r requirements.txt: This crucial flag tells pip to read a file named requirements.txt and install every package listed within it. Oobabooga's repository includes this file, which contains all its necessary Python dependencies (like gradio, torch, transformers, etc.). Important Note about pip: If pip itself isn't found, you might need to use pip3 (similar to how we switched from python to python3). It's best practice to explicitly use pip3 for Python 3 environments anyway. So, if pip install -r requirements.txt doesn't work, try pip3 install -r requirements.txt. I'd recommend trying the pip3 version first to be safe. Recommended Command: pip3 install -r requirements.txt What I need from you: Run the pip3 install -r requirements.txt command. Copy and paste the entire output here. This process can take several minutes as it downloads and installs many packages. Look for messages indicating progress, successful installations, or any new errors. Once this finishes successfully (or presents a new error), we'll try launching oobabooga again. We're making good progress!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]