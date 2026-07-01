---
category: ai-tools
date: 2025-07-29
id: 593172
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated because the Qwen2.5-coder model he added for autocompletion
  isn't working in VS Code.
tags:
- qwen2.5-coder
- autocomplete
- vscode-integration
- local-llm-setup
---
# i added qwen2.5-coder 1.5b for auto complete but i need it to work in vs code and it wont pick it up 

### USER
i added qwen2.5-coder 1.5b for auto complete but i need it to work in vs code and it wont pick it up 

### GEMINI
Okay, I see the situation. You've successfully added qwen2.5-coder-1.5b to your "LocalCode" assistant in the Continue Hub (second image), but it's not showing up in VS Code for autocomplete. The most likely reason for this is that your config.yaml in VS Code only has the llama3.1:8b model defined currently. The manual copy-paste you did earlier only brought over the Llama 3.1 configuration. To get qwen2.5-coder-1.5b to work for autocomplete in VS Code, you need to add its configuration to your config.yaml file. Here's how to do it: Open your ~/.continue/config.yaml file in VS Code. This is the file you modified previously (it's visible in your first screenshot). Add the qwen2.5-coder-1.5b model definition to the models: section. You'll add a new entry under models: that looks similar to your llama3.1:8b entry. Make sure you specify the correct name, provider: ollama, and model (which should match how it's named in Ollama, likely qwen2.5-coder:1.5b or qwen2.5-coder-1.5b). Crucially, ensure it has the autocomplete role. Here's an example of how your config.yaml might look after you add the Qwen model (I'm guessing the exact model name based on common Ollama naming, adjust if slightly different in your ollama list): name: llama3.1 8b version: 1.0.1 schema: v1 models: - name: llama3.1 8b provider: ollama model: llama3.1:8b roles: - chat - edit - apply - tool_use defaultCompletionOptions: contextLength: 128000 # --- ADD THIS SECTION FOR QWEN --- - name: qwen2.5-coder 1.5b provider: ollama model: qwen2.5-coder:1.5b # <-- IMPORTANT: Confirm this exact name from your Ollama install (ollama list) roles: - autocomplete - chat # Optional: Add chat if you want it for chat too defaultCompletionOptions: contextLength: 32768 # Or whatever is appropriate for Qwen Steps to get the exact YAML for Qwen: The easiest way to get the exact configuration for qwen2.5-coder-1.5b is: Go back to the Continue Hub (the webpage). Click on your "LocalCode" assistant. Find the "Models" section, and specifically the qwen2.5-coder-1.5b entry. Look for a "YAML" or "Edit" button/tab associated with that specific Qwen model entry. Sometimes, you can click on the model card itself within the assistant's configuration to see its full YAML. Copy the YAML for qwen2.5-coder-1.5b. Paste it into your ~/.continue/config.yaml file under the models: section, ensuring correct indentation. After updating config.yaml: Save the config.yaml file. The Continue.dev extension in VS Code should automatically reload the configuration. Check the Continue.dev sidebar again. You should now be able to select qwen2.5-coder 1.5b for "Autocomplete." Important: Make sure qwen2.5-coder:1.5b (or whatever its exact name is) is downloaded and running in your Ollama terminal. You should see similar [GIN] logs for it when it's being used.
