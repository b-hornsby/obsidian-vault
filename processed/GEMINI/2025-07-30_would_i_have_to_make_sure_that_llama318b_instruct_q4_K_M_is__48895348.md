---
id: 640173
source: GEMINI
date: 2025-07-30
tags: ['ollama', 'continue.dev', 'model-registry', 'hub']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking whether the llama3.1:8b model needs to be available on Ollama's hub for continue.dev to use it.
---
# would i have to make sure that llama3.1:8b-instruct-q4_K_M  is installed on the hub side of things as well? 

### USER
would i have to make sure that llama3.1:8b-instruct-q4_K_M  is installed on the hub side of things as well? 

### GEMINI
No, you do NOT need to "install" llama3.1:8b-instruct-q4_K_M on the Hub side of things. Let's clarify the roles of the different components: Ollama (your terminal/local server): This is where the actual model files (llama3.1:8b-instruct-q4_K_M) are stored and where the model runs. When you run ollama pull ... you're installing it here. Your ~/.continue/config.yaml file (in VS Code): This is the configuration file for your local VS Code Continue.dev extension. It tells the extension what models to look for and where to find them (i.e., from provider: ollama with a specific model: name). The Continue Hub (the website: hub.continue.dev): This is primarily a discovery and management interface. It lists publicly available models. It allows you to create and manage "assistants" and "blocks" (model configurations). Crucially, when you "add" an Ollama model on the Hub, it's essentially just helping you generate the correct YAML configuration that should go into your ~/.continue/config.yaml file. It doesn't actually install anything on the Hub's servers or directly on your machine. It's a way to visually build your configuration. You already have llama3.1:8b-instruct-q4_K_M installed correctly where it matters (in Ollama). The only reason you got the "Model not found in Ollama" error was a mismatch between the model name in your config.yaml (llama3.1:8b) and the exact model tag you had pulled in Ollama (llama3.1:8b-instruct-q4_K_M). By updating your config.yaml to precisely reflect llama3.1:8b-instruct-q4_K_M, you are now telling your VS Code extension to request the model using the exact name Ollama expects and has available. So, to reiterate: No further action is needed on the Continue Hub website for this specific model once your config.yaml is updated to match what's in Ollama.
