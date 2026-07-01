---
id: 512558
source: GEMINI
date: 2025-06-24
tags: ['coding', 'module', 'ai', 'gemini', 'model', 'oobabooga', 'llama.cpp', 'text-generation']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
╭───────────────────────────────────────── Traceback (most recent call last) ──────────────────────────────────────────╮
│ /home/bryan_/text-generation-webui/server.py:7 in <module>                                                           │
│                                                                                                                      │
│     6 from modules import shared                                                                                     │
│ ❱   7 from modules.block_requests import OpenMonkeyPatch, RequestBlocker                                             │
│     8 from modules.logging_colors import logger                                                                      │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/block_requests.py:7 in <module>                                           │
│                                                                                                                      │
│    6                                                                                                                 │
│ ❱  7 from modules import shared, ui                                                                                  │
│    8 from modules.logging_colors import logger                                                                       │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/ui.py:11 in <module>                                                      │
│                                                                                                                      │
│    10 from modules import shared                                                                                     │
│ ❱  11 from modules.chat import load_history                                                                          │
│    12 from modules.utils import gradio                                                                               │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/chat.py:22 in <module>                                                    │
│                                                                                                                      │
│     21 from modules.extensions import apply_extensions                                                               │
│ ❱   22 from modules.html_generator import (                                                                          │
│     23     chat_html_wrapper,                                                                                        │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/html_generator.py:9 in <module>                                           │
│                                                                                                                      │
│     8                                                                                                                │
│ ❱   9 import markdown                                                                                                │
│    10 from PIL import Image, ImageOps                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
ModuleNotFoundError: No module named 'markdown'
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
╭───────────────────────────────────────── Traceback (most recent call last) ──────────────────────────────────────────╮
│ /home/bryan_/text-generation-webui/server.py:7 in <module>                                                           │
│                                                                                                                      │
│     6 from modules import shared                                                                                     │
│ ❱   7 from modules.block_requests import OpenMonkeyPatch, RequestBlocker                                             │
│     8 from modules.logging_colors import logger                                                                      │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/block_requests.py:7 in <module>                                           │
│                                                                                                                      │
│    6                                                                                                                 │
│ ❱  7 from modules import shared, ui                                                                                  │
│    8 from modules.logging_colors import logger                                                                       │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/ui.py:11 in <module>                                                      │
│                                                                                                                      │
│    10 from modules import shared                                                                                     │
│ ❱  11 from modules.chat import load_history                                                                          │
│    12 from modules.utils import gradio                                                                               │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/chat.py:22 in <module>                                                    │
│                                                                                                                      │
│     21 from modules.extensions import apply_extensions                                                               │
│ ❱   22 from modules.html_generator import (                                                                          │
│     23     chat_html_wrapper,                                                                                        │
│                                                                                                                      │
│ /home/bryan_/text-generation-webui/modules/html_generator.py:9 in <module>                                           │
│                                                                                                                      │
│     8                                                                                                                │
│ ❱   9 import markdown                                                                                                │
│    10 from PIL import Image, ImageOps                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
ModuleNotFoundError: No module named 'markdown'
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Well, that's frustrating, but it's a new and specific error, which is actually a good sign because it tells us exactly what's wrong! ModuleNotFoundError: No module named 'markdown' This error means that the markdown Python package, which Oobabooga needs to render its HTML (and likely chat output), is missing from your newly created virtual environment. My apologies, I missed including this in the manual installation steps. When you re-create the virtual environment and manually install, we have to be very precise about every single dependency. Let's fix this missing module. Step 22: Install the Missing markdown Module Action: Stop Oobabooga completely. (If it's still attempting to run and showing that traceback). Press Ctrl + C repeatedly in your WSL2 terminal until you see your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Ensure you are in the top-level text-generation-webui directory: cd ~/text-generation-webui Ensure your virtual environment is active. Your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ indicates it is. If it ever isn't, run source .venv/bin/activate. Install the missing markdown package: pip install markdown This should be a quick installation. Once that command finishes and returns you to your prompt, launch Oobabooga again: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Once the server fully starts and displays the URL, open a new incognito/private browser window and go to http://127.0.0.1:7860. First, navigate to the "Extensions" tab to verify superboogav2 is listed and checked. If not, check it and "Reload UI". Then, very carefully check all the main tabs at the top of the UI for "SuperBooga". This ModuleNotFoundError is a very common issue when manually managing Python environments, and fixing it often resolves the problem immediately. We're incrementally patching the environment until all Oobabooga's requirements are met. Please provide the output of the pip install markdown command, and then the output when you launch Oobabooga again. Fingers crossed for this one!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]