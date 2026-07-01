---
category: homelab
date: 2025-07-06
id: 370069
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is confirming whether he needs to re-run a command now that he has
  reconnected to the internet.
tags:
- internet-dependency
- installation
- wsl2
- dependencies
---
# so i just need to run  the command again now that i connected back to the internet? 

### USER
so i just need to run  the command again now that i connected back to the internet? 

### GEMINI
Yes, that's the most likely solution! Since the error was a "Temporary failure in name resolution" (meaning it couldn't connect to the internet to download a needed component), and you've now reconnected to the internet, you should: Ensure your WSL2 instance is properly connected: Open your WSL2 terminal. Run ping google.com. If it gets replies, you're good. If not, try wsl --shutdown in PowerShell and restart WSL2. Run the Oobabooga command again: cd ~/text-generation-webui/ ./installer_files/env/bin/python server.py superboogav2 will try again to download its required embedding model from Hugging Face. If your internet connection is stable, it should now succeed, cache the model, and then load the extension without the error. Once it successfully loads, superboogav2 (and your main LLM, and Whisper STT) should function offline for their core operations, only needing internet if web_rag is active and successfully queries for information.
