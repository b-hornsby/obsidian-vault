---
id: 303254
source: GEMINI
date: 2025-07-29
tags: ['continue-dev-configuration', 'yaml-file-editing', 'model-integration', 'vscode-setup']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan provides context that he copied YAML configuration from Continue Hub into VS Code, and the model now appears, indicating progress in setting up his local LLM environment.
---
# for context i just took the yaml from the continue hub (the model we added to my agent in the hub) and pasted it into the yaml in vs code and the model shows up now?

### USER
for context i just took the yaml from the continue hub (the model we added to my agent in the hub) and pasted it into the yaml in vs code and the model shows up now?

### GEMINI
Yes, that's absolutely correct! You've found an alternative and often more direct way to configure Continue.dev with your local Ollama model. By copying the YAML configuration from the Continue Hub (which effectively represents the "model block" you just added to your assistant) and pasting it directly into your local ~/.continue/config.yaml file in VS Code, you're bypassing the need for the web-based synchronization to happen instantly. The VS Code extension reads from this config.yaml file to understand which models and configurations it should use. When you added the model to your "LocalCode" assistant on the Hub, the Hub was essentially trying to update this same config.yaml (or an equivalent internal configuration) for you. By manually pasting it, you achieved the same result directly. Your screenshot confirms this success: On the left, you see the config.yaml file with the llama3.1:8b model defined, specifying provider: ollama and model: llama3.1:8b, along with its roles. On the right, in the Continue.dev sidebar, you can clearly see llama3.1:8b is now selectable in the model dropdown for "Chat." This is fantastic! You are now all set to use your llama3.1:8b-instruct-q4_K_M model via the Continue.dev extension in VS Code. Just make sure: Ollama is running. The llama3.1:8b-instruct-q4_K_M model is downloaded in Ollama. You can now start interacting with it in the chat interface!
