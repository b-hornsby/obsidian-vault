---
category: ai-tools
date: 2025-06-24
id: 302547
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
- second-brain-vault
- streaming-rig
- it-certification
- flappy-meme-bird
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is trying to run the text-generation-webui server but encounters
  a Python traceback error when starting the server with --listen and --model-menu
  flags.
tags:
- text-generation-webui
- python-server
- local-ai
- model-menu
- traceback-error
---
# bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui
python3 server.py --listen --model-menu
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
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui
python3 server.py --listen --model-menu
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
Ah, classic Python dependency error! The traceback clearly states: ModuleNotFoundError: No module named 'gradio'. This means that the gradio Python library, which text-generation-webui uses to create its web interface, is not installed in your Python environment within WSL. We've installed a lot of dependencies, but it looks like gradio either wasn't included in a previous pip install or its installation failed. Action: Install gradio You just need to install this missing Python package. pip install gradio After gradio finishes installing, try running the text-generation-webui again: python3 server.py --listen --model-menu This should now resolve that error and allow the web UI to start!