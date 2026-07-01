---
category: ai-tools
date: 2025-07-29
id: 322030
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to figure out how to make Continue.dev recognize the model
  he has selected in Ollama.
tags:
- ollama-integration
- continue-dev-setup
- model-selection
- local-llm-configuration
---
# how do i go about adding my model that i chose in ollama in the continue hub so it knows to pick that one up? 

### USER
how do i go about adding my model that i chose in ollama in the continue hub so it knows to pick that one up? 

### GEMINI
You're on the right track! To ensure Continue.dev picks up the Ollama model you've downloaded, you'll primarily configure this within Continue.dev's config.yaml file. Here's a breakdown of the process: 1. Ensure Ollama is Running and Models are Downloaded: Ollama Server: From your previous image, Ollama is already running at http://localhost:11434. This is essential. Models Downloaded: You mentioned downloading models like llama3.1:8b, qwen2.5-coder:1.5b-base, and nomic-embed-text:latest. Make sure these downloads have completed successfully. You can verify this by running ollama list in your terminal, which will show you all the models Ollama has downloaded. 2. Access Continue.dev's Configuration: In VS Code: Open the Continue.dev sidebar (usually the sparkle icon ✨). Open Config: In the Continue sidebar, look for a "gear" or "settings" icon, usually near the bottom right or near the "Local Assistant" dropdown. Clicking this will open your config.yaml file. Alternatively, you can use the VS Code Command Palette (Cmd/Ctrl + Shift + P) and search for "Continue: Open Config". 3. Configure Your Ollama Models in config.yaml: The config.yaml file is where you tell Continue.dev which models to use and how to access them. You'll primarily be working with the models array and potentially tabAutocompleteModel and embeddingsProvider. Here's an example of how you'd configure the models you mentioned: # ~/.continue/config.yaml (or %USERPROFILE%\.continue\config.yaml on Windows) # ... (other config settings might be present, don't delete them) models: - name: Llama3.1 8B (Chat) provider: ollama model: llama3.1:8b # apiBase: http://localhost:11434 # Only needed if Ollama is not on default port or is remote - name: Qwen2.5 Coder (Autocomplete) provider: ollama model: qwen2.5-coder:1.5b-base # If you want this specifically for autocomplete, you might also set it below: tabAutocompleteModel: name: Qwen2.5 Coder (Autocomplete) # Reference the name you gave it above provider: ollama model: qwen2.5-coder:1.5b-base embeddingsProvider: provider: ollama model: nomic-embed-text:latest Explanation of the Configuration: models array: This is a list of models that Continue.dev will make available in its "Agent" and "Chat" modes. name: A display name for the model in Continue.dev's UI (e.g., "Llama3.1 8B (Chat)"). provider: Set this to ollama. model: This is the exact name of the model you downloaded via ollama pull (e.g., llama3.1:8b, qwen2.5-coder:1.5b-base). apiBase: (Optional) By default, Continue.dev assumes Ollama is running on http://localhost:11434. You only need to specify apiBase if your Ollama instance is on a different port or a remote machine. tabAutocompleteModel: This section explicitly tells Continue.dev which model to use for code autocomplete suggestions. You can reference one of the models you defined in the models array, or define it separately. embeddingsProvider: This tells Continue.dev which model to use for generating embeddings, which are crucial for features like @codebase (retrieving relevant code snippets from your project). 4. Save the config.yaml file: After making your changes, save the config.yaml file. Continue.dev usually reloads automatically when you save the config. If it doesn't, you might see a "Reload config" option in the assistant selector (the dropdown where you choose your assistant). 5. Select Your Model in Continue.dev: Once configured, open the Continue.dev sidebar. Above the chat input, you should see a dropdown selector (it might say "Local Assistant" or similar). Click on this dropdown. You should now see the name you gave your Ollama models (e.g., "Llama3.1 8B (Chat)") in the list. Select the model you want to use for your current chat or agent interaction. By following these steps, Continue.dev will know to pick up and utilize your chosen Ollama models for its various AI features.
