---
category: ai-tools
date: 2025-07-29
id: 040608
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to configure a specific tab in VS Code using the Continue.dev
  extension to use his Llama3 model.
tags:
- vscode-configuration
- continue-dev-extension
- model-selection
- local-llm-integration
---
# how do i set this tab up in vs code via the continue.dev ext so that it picks up my llama3.1:8b-instruct-q4_K_M model 

### USER
how do i set this tab up in vs code via the continue.dev ext so that it picks up my llama3.1:8b-instruct-q4_K_M model 

### GEMINI
Based on the image you provided, you're looking at the "Models" section within the continue.dev extension settings in VS Code. To set up your llama3.1:8b-instruct-q4_K_M model, you'll likely need to configure either the "Chat" or "Autocomplete" model options to point to your local Llama 3.1 instance. Here's how you generally do this, along with some important considerations: Understanding the Options in the Image: Chat: This is for conversational AI interactions. You'll likely want to configure your Llama 3.1 model here for general chat. Autocomplete: This is for code completion and suggestions. If you want Llama 3.1 to help with code, you might configure it here as well. Edit: For model-powered code editing. Apply: For applying model suggestions or transformations. Embed: This is currently set to "Transformers.js (Built-In)," which is likely for generating embeddings locally using a JavaScript-based library. This is less relevant for directly using your Llama 3.1 inference model. Rerank: For re-ranking search results or similar. Steps to Set Up Your llama3.1:8b-instruct-q4_K_M Model: Ensure Your Llama 3.1 Model is Running (Ollama): The most common way to run Llama 3.1 locally is using Ollama. Make sure Ollama is installed and your llama3.1:8b-instruct-q4_K_M model is downloaded and running. You can check its status by opening a terminal and running ollama list or ollama run llama3.1:8b-instruct-q4_K_M. Configure the "Chat" or "Autocomplete" Model in Continue.dev: Click "Setup Chat model" or "Setup Autocomplete model": In the image you provided, click on the "Setup Chat model" link (or "Setup Autocomplete model" if that's your primary use case). This will open a new configuration page or prompt within the continue.dev settings. Select "Ollama": Continue.dev has direct integration with Ollama. When you click "Setup Chat model," you'll likely be presented with a list of model providers. Choose "Ollama." Specify Your Model Name: Once you select Ollama, you'll typically be asked to enter the model name. Enter the exact name of your Llama 3.1 model as it appears in Ollama: llama3.1:8b-instruct-q4_K_M. Confirm/Save: Save the changes. The continue.dev extension will then attempt to connect to your running Ollama instance and use your specified Llama 3.1 model. Troubleshooting and Important Notes: Ollama Server Address: By default, Continue.dev assumes Ollama is running on http://localhost:11434. If you've configured Ollama to run on a different address or port, you might need to specify that in the continue.dev settings as well. Look for an "Ollama API Base URL" or similar setting. Resources: Running Llama 3.1 (even the 8B Q4_K_M version) locally requires significant RAM. Ensure your system has enough memory to load and run the model efficiently. Error Messages: If you encounter errors, check the VS Code Output panel for the "Continue" extension for more detailed error messages. This can help diagnose connection issues or incorrect model names. Restart VS Code: Sometimes, after making significant changes to extension settings, restarting VS Code can help ensure the changes are applied correctly. Continue.dev Documentation: For the most accurate and up-to-date instructions, refer to the official documentation for the continue.dev VS Code extension. They often have specific guides for integrating with Ollama. By following these steps, you should be able to configure the continue.dev extension to utilize your local llama3.1:8b-instruct-q4_K_M model for chat or autocomplete functionalities.
