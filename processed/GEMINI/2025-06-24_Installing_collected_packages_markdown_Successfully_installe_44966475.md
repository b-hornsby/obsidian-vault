---
category: homelab
date: 2025-06-24
id: 743129
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: User is trying to run text-generation-webui with llama.cpp loader and superbooga
  extension but hits an import error during startup.
tags:
- text-generation-webui
- llama.cpp
- GPU configuration
- Python environment
- extension loading
---
# Installing collected packages: markdown
Successfully installed markdown-3.8.2
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
│ /home/bryan_/text-generation-webui/modules/ui.py:67 in <module>                                                      │
│                                                                                                                      │
│    66 if not shared.args.old_colors:                                                                                 │
│ ❱  67     theme = theme.set(                                                                                         │
│    68         # General Colors                                                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
TypeError: Base.set() got an unexpected keyword argument 'button_shadow_hover'
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
Installing collected packages: markdown
Successfully installed markdown-3.8.2
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
│ /home/bryan_/text-generation-webui/modules/ui.py:67 in <module>                                                      │
│                                                                                                                      │
│    66 if not shared.args.old_colors:                                                                                 │
│ ❱  67     theme = theme.set(                                                                                         │
│    68         # General Colors                                                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
TypeError: Base.set() got an unexpected keyword argument 'button_shadow_hover'
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Okay, we're making progress, even though it feels like a whack-a-mole game! You successfully installed markdown. Great! However, now we have a new error when launching: TypeError: Base.set() got an unexpected keyword argument 'button_shadow_hover' This error is very specific. It means that the version of gradio you have installed (which is 5.34.2 from your previous pip install output) is trying to use a theming parameter called button_shadow_hover that the underlying Gradio Base.set() method doesn't recognize. This is almost certainly an incompatibility between your version of Oobabooga's text-generation-webui code and the version of gradio that was just installed. Oobabooga is often designed to work with very specific Gradio versions. When start_linux.sh doesn't work as expected, and we manually install, we might grab the absolute latest Gradio, which could be newer than what Oobabooga's UI code expects. What to do now: We need to install a specific, known-compatible version of gradio (and gradio_client). Based on common Oobabooga installations, Gradio 4.x (specifically often 4.37.2 or similar) is usually the stable range. You even had 4.37.2 installed before you uninstalled it! Step 23: Downgrade Gradio to a Compatible Version Action: Stop Oobabooga completely. (It's currently erroring out). Press Ctrl + C repeatedly in your WSL2 terminal until you see your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Ensure you are in the top-level text-generation-webui directory: cd ~/text-generation-webui Ensure your virtual environment is active. Your prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ indicates it is. Uninstall the current Gradio and Gradio Client versions: pip uninstall gradio gradio_client -y Confirm that this completes successfully. Install a specific, older (but compatible) version of Gradio and Gradio Client: pip install gradio==4.37.2 gradio_client==1.0.2 This should install the versions that are more likely to be compatible with your Oobabooga code. Once that command finishes and returns you to your prompt, launch Oobabooga again: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 Once the server fully starts and displays the URL, open a new incognito/private browser window and go to http://127.0.0.1:7860. First, navigate to the "Extensions" tab to verify superboogav2 is listed and checked. If not, check it and "Reload UI". Then, very carefully check all the main tabs at the top of the UI for "SuperBooga". This is the most common reason for TypeError: Base.set() got an unexpected keyword argument in Oobabooga. By fixing the Gradio version, we should resolve this. Please provide the output of the pip uninstall and pip install commands, and then the output when you launch Oobabooga. Fingers still crossed!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]