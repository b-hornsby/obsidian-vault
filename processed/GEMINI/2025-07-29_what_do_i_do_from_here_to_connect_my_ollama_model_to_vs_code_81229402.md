---
category: coding
date: 2025-07-29
id: 097869
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to connect his Ollama model to VS Code using the Continue.dev
  extension and is unsure how to proceed.
tags:
- vscode-integration
- ollama
- continue.dev
- local-llm-setup
---
# what do i do from here to connect my ollama model to vs code and the continue.dev ext

### USER
what do i do from here to connect my ollama model to vs code and the continue.dev ext

### GEMINI
Based on the image, you're currently in the "Local" tab of the Continue.dev extension in VS Code, and it looks like Ollama is already running at http://localhost:11434. To connect your Ollama model to VS Code and the Continue.dev extension, you need to follow these steps: Download the models you want to use: The image shows options to download: Chat model: ollama pull llama3.1:8b Autocomplete model: ollama pull qwen2.5-coder:1.5b-base Embeddings model: ollama pull nomic-embed-text:latest You can click the grey box next to each ollama pull command to initiate the download. You might also be able to run these commands directly in your terminal if you have Ollama installed globally. Click the "Connect" button: Once you have downloaded the models you want to use, click the "Connect" button in the Continue.dev extension. This button will likely configure Continue.dev to use the locally available Ollama models. (Optional) Skip and configure manually: If the "Connect" button doesn't work as expected or if you want more control, you can click "Skip and configure manually." This will likely open a configuration file (e.g., config.json or settings.json within your VS Code workspace or user settings) where you can manually specify the Ollama endpoint and the models you want to use. You would typically add something like this (exact syntax might vary): { "continue.config": { "models": [ { "name": "llama3.1:8b", // Or whatever model you downloaded "provider": "ollama", "model": "llama3.1:8b" // The model name from Ollama } // Add other models here if you downloaded them ] } } After completing these steps, your Ollama models should be connected to the Continue.dev extension, and you should be able to start using them for chat, autocomplete, and embeddings within VS Code.
