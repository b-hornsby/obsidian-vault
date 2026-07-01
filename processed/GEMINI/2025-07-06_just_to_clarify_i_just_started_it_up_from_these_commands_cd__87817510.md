---
category: homelab
date: 2025-07-06
id: 839628
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is clarifying how he starts oobabooga in WSL2 and sharing the terminal
  output to debug startup issues.
tags:
- oobabooga
- startup-commands
- wsl2
- server-launch
---
# just to clarify i just started it up from these commands: cd ~/text-generation-webui/
./installer_files/env/bin/python server.py and when i ran those it did this:

### USER
just to clarify i just started it up from these commands: cd ~/text-generation-webui/
./installer_files/env/bin/python server.py and when i ran those it did this:

### GEMINI
From the image you provided, it's clear that the Oobabooga text-generation-webui, including the SuperBoogaV2 extension, has successfully started and is running on your local machine. The output shows: Loading the extension "superboogav2": This confirms the extension was initialized. Running on local URL: http://127.0.0.1:7860: This is the address where you can access the web UI in your browser. The fact that these messages appeared and it provided a local URL means the process did not stall in this instance. It indicates that all necessary components and dependencies for SuperBoogaV2 were successfully loaded, at least to the point where the web UI became accessible. The previous issue you described, where it "stalled" when you unplugged the internet, was likely due to SuperBoogaV2 (or one of its underlying libraries like sentence-transformers for embedding models) attempting a first-time download of model weights or other assets. Since you launched it with internet connectivity this time, those downloads likely completed, allowing the extension to initialize properly. You should now be able to open a web browser and navigate to http://127.0.0.1:7860 to access the Oobabooga UI and use SuperBoogaV2. Once these initial downloads are done, you should be able to run it offline without issues.
