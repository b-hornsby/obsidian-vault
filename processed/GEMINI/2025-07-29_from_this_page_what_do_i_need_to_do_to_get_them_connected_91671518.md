---
category: ai-tools
date: 2025-07-29
id: 667907
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for specific instructions on how to connect Ollama and Continue.dev,
  likely following a guide or documentation page.
tags:
- ollama-integration
- continue-dev-setup
- local-llm-connection
- vscode-configuration
---
# from this page what do i need to do to get them connected?

### USER
from this page what do i need to do to get them connected?

### GEMINI
Great! You're in the right place now. The image shows you're on the Continue Hub, filtered by "ollama" models, and you can see llama3.1:8b listed. To get your llama3.1:8b-instruct-q4_K_M model connected and available in your VS Code extension, here's what you need to do from this page: Click the "+" button next to "llama3.1:8b": On the card for llama3.1:8b (which is the base model for your llama3.1:8b-instruct-q4_K_M variant), you'll see a "+" icon. Click this. Confirm the Model Addition: Clicking the "+" will likely trigger a confirmation or "Add Model" action. You might be asked to confirm that you want to add this model to your Continue.dev configuration. What happens next: Synchronization with VS Code: The Continue Hub and your Continue.dev VS Code extension are designed to synchronize. Once you "add" the llama3.1:8b model from the Hub, this configuration should automatically be sent to your VS Code extension. Availability in VS Code: Go back to your VS Code window. Open the Continue.dev extension sidebar (if it's not already open). Go to the "Models" section within the Continue.dev settings (the one from your very first image). You should now see llama3.1:8b (or similar, sometimes it will automatically pick up the instruction variant if available locally) listed under "Chat" or "Autocomplete" as a selectable option, instead of "Setup Chat model." Important Considerations: Ollama Running: Ensure your Ollama server is running in the background and that you have the llama3.1:8b-instruct-q4_K_M model downloaded and available in Ollama (you can check with ollama list in your terminal). Continue.dev will attempt to connect to your local Ollama instance to use this model. Specific Variant: While you're adding llama3.1:8b from the Hub, Continue.dev is smart enough to often detect the specific variant (like llama3.1:8b-instruct-q4_K_M) if that's what's actually running in your local Ollama. So don't worry too much if the Hub just shows llama3.1:8b. Restart VS Code (if needed): In rare cases, if the model doesn't appear immediately in VS Code, restarting VS Code can help refresh the extension's configuration. By clicking that "+" button, you're essentially telling Continue.dev (via the Hub) to include this Ollama-hosted llama3.1 model in your accessible models within the VS Code extension.
