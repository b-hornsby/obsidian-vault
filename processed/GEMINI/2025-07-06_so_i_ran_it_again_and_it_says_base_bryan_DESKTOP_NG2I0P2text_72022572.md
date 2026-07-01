---
id: 760649
source: GEMINI
date: 2025-07-06
tags: ['ai-tools', 'ai', 'gemini', 'rag', 'text-generation', 'perp', 'hype', 'python']
category: ai-tools
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md', 'nodes/topics/tech/coding.md']
---
# so i ran it again and it says: (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui/
./installer_files/env/bin/python server.py
20:28:17-337005 INFO     Starting Text generation web UI
20:28:17-338977 INFO     Loading settings from "user_data/settings.yaml"
20:28:17-340939 INFO     Loading the extension "whisper_stt"
20:28:20-775855 INFO     Loading the extension "web_rag"
20:28:20-776982 INFO     Loading the extension "superboogav2"
20:28:23-744318 DEBUG    Loading hyperparameters...

Running on local URL:  http://127.0.0.1:7860

### USER
so i ran it again and it says: (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui/
./installer_files/env/bin/python server.py
20:28:17-337005 INFO     Starting Text generation web UI
20:28:17-338977 INFO     Loading settings from "user_data/settings.yaml"
20:28:17-340939 INFO     Loading the extension "whisper_stt"
20:28:20-775855 INFO     Loading the extension "web_rag"
20:28:20-776982 INFO     Loading the extension "superboogav2"
20:28:23-744318 DEBUG    Loading hyperparameters...

Running on local URL:  http://127.0.0.1:7860

### GEMINI
Great news! 🎉 The output you've shared shows that all your extensions (whisper_stt, web_rag, and superboogav2) loaded successfully this time, without the previous NameResolutionError. The DEBUG line for "Loading hyperparameters..." also indicates that the system is proceeding as expected. This means your internet connection within WSL2 was likely the issue, and now that it's resolved, superboogav2 was able to download its necessary components. You should now be able to access the web UI at http://127.0.0.1:7860 and have all the features (voice input, web RAG, local RAG) working as configured.