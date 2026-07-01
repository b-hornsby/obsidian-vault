---
id: 478856
source: GEMINI
date: 2025-07-29
tags: ['continue.dev', 'ollama', 'local-model', 'configuration']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan wants to confirm that using Ollama as the backend will still allow continue.dev to be powered by his locally running model.
---
# so to clarify, doing it that way still allows for continue.dev to be powered by the model i have running in ollama via terminal? 

### USER
so to clarify, doing it that way still allows for continue.dev to be powered by the model i have running in ollama via terminal? 

### GEMINI
Yes, to clarify definitively: Absolutely, doing it that way (by pasting the YAML into ~/.continue/config.yaml) still allows Continue.dev to be powered by the model you have running in Ollama via the terminal. Here's why: config.yaml is the Source of Truth (for local config): The ~/.continue/config.yaml file on your local machine is where the Continue.dev VS Code extension looks for its configuration. When you paste the model definition into this file, you are directly telling the extension: "Hey, I have a model named llama3.1:8b, and its provider is ollama, and the specific model name within Ollama is also llama3.1:8b." provider: ollama is the Key: The line provider: ollama in your config.yaml is the crucial part. This tells the Continue.dev extension to look for and connect to an Ollama server (which it expects to be running locally, usually on http://localhost:11434 by default) to fulfill requests for that model. Ollama Handles the Model: Continue.dev doesn't run the Llama 3.1 model itself. It acts as an interface. It sends your prompts and requests to the Ollama server, and Ollama (which you started via the terminal and has your llama3.1:8b-instruct-q4_K_M model loaded) then performs the inference and sends the response back to Continue.dev. Essentially, whether you configure it via the web-based Continue Hub (which pushes changes to your local config) or by directly editing the config.yaml file, the end result is the same: the Continue.dev extension in VS Code gets the instructions it needs to connect to your local Ollama instance and use your specified model. So, yes, you're good to go. Your Continue.dev extension is now configured to leverage your local Llama 3.1 model running via Ollama.
