---
id: 939799
source: GEMINI
date: 2025-06-24
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'llama.cpp', 'text-generation']
category: ai-tools
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
13:20:18-387606 INFO     Starting Text generation web UI
13:20:18-390075 INFO     Loading settings from "user_data/settings.yaml"
13:20:18-392088 INFO     Loading the extension "superboogav2"
13:20:25-074200 DEBUG    Loading hyperparameters...

Running on local URL:  http://127.0.0.1:7860

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp --extensions superboogav2
13:20:18-387606 INFO     Starting Text generation web UI
13:20:18-390075 INFO     Loading settings from "user_data/settings.yaml"
13:20:18-392088 INFO     Loading the extension "superboogav2"
13:20:25-074200 DEBUG    Loading hyperparameters...

Running on local URL:  http://127.0.0.1:7860

### GEMINI
Excellent! This terminal output is exactly what we want to see. Loading the extension "superboogav2" appears. Loading hyperparameters... also appears. Crucially, there are NO error messages regarding superboogav2 failing to load. This confirms that from the backend perspective, Oobabooga successfully loaded the superboogav2 extension. The issue now is purely with the front-end (web browser UI) displaying the tab. Since you've done everything right on the backend, and we've confirmed the files are there and flash-attn is uninstalled, let's look at the screenshot you provided to see if there's any hint in the UI itself. Analysis of "Screenshot 2025-06-24 125630.png": I see your screenshot. It shows the Oobabooga web UI. I can see the tabs: Chat Notebook Model Parameters Training Extensions Settings And on the Extensions tab, I see that superboogav2 is indeed checked. The "SuperBooga" tab is definitely not present in the visible tab bar in your screenshot. This points strongly to a browser caching issue or a very specific Gradio UI rendering problem in your environment. Given that you've tried a hard refresh and a new incognito window, let's try one more browser-side trick. Sometimes, clearing the site data for 127.0.0.1 explicitly can resolve stubborn caching issues for web applications like this. Step 14: Clear Site Data and Final Verification Action: Keep Oobabooga running in your WSL2 terminal (it looks like it's currently running from the output you just provided). In your web browser (e.g., Chrome, Edge, Firefox): Go to http://127.0.0.1:7860. Open your browser's Developer Tools. (Usually by pressing F12 or Ctrl+Shift+I on Windows/Linux, Cmd+Option+I on Mac). Navigate to the "Application" tab (in Chrome/Edge) or "Storage" tab (in Firefox). On the left-hand side, find "Local Storage", "Session Storage", and "IndexedDB". Expand them if necessary. Right-click on http://127.0.0.1:7860 (or http://127.0.0.1:7860 itself if it's directly listed) under "Local Storage" or "Storage". Select "Clear" or "Delete" or "Clear Site Data" (the exact wording varies by browser). Confirm any prompts. Also, go to "Cache Storage" and "Cache" (or "Service Workers" if visible) and try to clear those as well for 127.0.0.1:7860. Alternatively, a simpler way in Chrome/Edge: Go to chrome://settings/siteData (or edge://settings/siteData), search for 127.0.0.1, and click "Remove All Shown". After clearing site data, close the Developer Tools. Perform a hard refresh again ( Ctrl + F5 or Cmd + Shift + R). Look very carefully at all the tabs. If, after this, the "SuperBooga" tab still does not appear, then we are dealing with an extremely rare UI rendering bug, or potentially a very subtle conflict that isn't throwing an explicit error. Please let me know the result after trying this detailed site data clearing. If it's still missing, we might have to consider a fresh re-installation of Oobabooga itself as a last resort, but let's try this first.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]