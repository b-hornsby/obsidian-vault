---
category: ai-tools
date: 2025-06-24
id: 472626
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user enabled superbooga but cannot find its tab in the interface, indicating
  a UI or configuration issue with the tool's visibility.
tags:
- superbooga
- UI navigation
- missing feature
- tab visibility
- tool configuration
---
# superbooga is checked but i dont see a tab for it? 

### USER
superbooga is checked but i dont see a tab for it? 

### GEMINI
Okay, that's a bit unusual, but not entirely uncommon with extensions. If SuperBooga is checked on the "Extensions" tab but no "SuperBooga" tab appears, it usually means one of two things: UI Refresh Issue: The Oobabooga UI sometimes needs a more forceful refresh to display new elements. Specific Extension Behavior: Occasionally, an extension might integrate its features into an existing tab (like "Chat" or "Parameters") rather than creating a brand new one, or it might be hiding in a less obvious place. However, superboogav2 is designed to create its own tab. Let's try a full, explicit restart of the server from the terminal, and then carefully check all the tabs. Step 10: Full Restart and Tab Verification Action: Go to your WSL2 terminal where Oobabooga is running. Stop the server completely. Press Ctrl + C multiple times until you see your command prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Relaunch Oobabooga from the main text-generation-webui directory. Ensure your virtual environment is active. cd ~/text-generation-webui source .venv/bin/activate python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2 (Double-check that superboogav2 is included in the --extensions list). Wait for the server to fully start and give you the Running on local URL: http://127.0.0.1:7860 message. Go to your web browser and navigate to http://127.0.0.1:7860 again. Even if it's already open, perform a hard refresh of the page (usually Ctrl + F5 on Windows/Linux or Cmd + Shift + R on Mac). This clears the browser's cache for that page and forces it to reload everything. Carefully examine all the tabs at the top of the Oobabooga UI. Look for "SuperBooga", "Booga", "RAG", "Knowledge Base", or anything similarly named. It should usually appear between "Model" and "Settings" or "Extensions". If you still don't see it, check the "Extensions" tab again. Make sure superboogav2 is still checked. If it isn't, re-check it and click "Reload UI" (or "Apply and restart the server") again. Observe the terminal output closely during this reload to see if any new errors appear. Please let me know the outcome of this. Did you find the tab after the hard refresh and explicit restart? If not, please confirm that superboogav2 remains checked on the Extensions tab after the reload.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]