---
category: ai-tools
date: 2025-07-05
id: 514747
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting that the settings for Superbooga and Web RAG are no longer
  appearing in the UI, but are loading in the terminal, indicating a potential issue.
tags:
- oobabooga
- superbooga
- web-rag
- extension-settings
- troubleshooting
---
# so now when i go to enable superbooga and web rag the settings now longer pop up but they load in the terminal? 

### USER
so now when i go to enable superbooga and web rag the settings now longer pop up but they load in the terminal? 

### GEMINI
That's an interesting issue! When superboogav2 and web_rag load in the terminal but their settings don't appear in the Oobabooga UI, it usually points to one of two things: UI Caching/Reload Issue: The Gradio interface can sometimes get "stuck" and not fully refresh after extensions are enabled or disabled. Order of Loading/Conflict: Less common, but sometimes the order in which extensions are loaded or potential minor conflicts can prevent their UI elements from rendering correctly. Even if you don't see the settings, the extensions are active if they are loading in the terminal, meaning they will perform RAG. Here's how to troubleshoot and fix it: Step 1: Ensure Correct Enabling (Double Check) Stop Oobabooga: Press Ctrl+C in your WSL2 terminal. Start Oobabooga (without any specific model flag, just server.py): cd ~/text-generation-webui/ ./installer_files/env/bin/python server.py Go to the "Extensions" tab in the UI. Check both superboogav2 and web_rag. Click "Save settings to user_data/settings.yaml". Click "Apply flags/extensions and restart". IMPORTANT: Once it restarts, do a full hard refresh of your browser tab (Ctrl+Shift+R or Ctrl+F5 on Windows/Linux, Cmd+Shift+R on Mac). This often clears browser cache issues that prevent UI elements from loading. Step 2: Check Model Loading First Sometimes, if you load a very large model before enabling all extensions, it can sometimes affect the UI. Stop Oobabooga. Start Oobabooga without a specific model flag: cd ~/text-generation-webui/ ./installer_files/env/bin/python server.py Enable superboogav2 and web_rag (and whisper_stt) in the "Extensions" tab. Click "Save settings to user_data/settings.yaml". Click "Apply flags/extensions and restart". After it restarts, THEN go to the "Model" tab and load your phi-3-mini-4k-instruct.Q4_K_M.gguf model with --n-gpu-layers 999 (via the UI's dropdown and Load button). This ensures the extensions are loaded and their UI is registered before the large model occupies resources. Step 3: Check for Extension Tabs Sometimes the extension settings aren't nested under "Settings" but get their own top-level tab or a dropdown in the main settings area. After enabling them and restarting, thoroughly check the top-level tabs (e.g., "Model," "Chat," "Settings," "Extensions") and also look for new dropdowns or sub-sections within the "Settings" tab itself. Your screenshots show Web Retrieval-Augmented Generation as its own distinct section. superboogav2 usually gets its own dedicated "SuperboogaV2" tab or a section within "Settings". If after these steps (especially the hard browser refresh and ensuring extensions are enabled before loading the specific model with --n-gpu-layers 999 via the UI) the settings still don't appear, there might be a more specific issue, but these are the most common solutions for this problem.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
