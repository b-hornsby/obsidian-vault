---
category: ai-tools
date: 2025-07-29
id: 734953
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is trying to get continue.dev to recognize his Ollama model and sharing
  his config.yaml for troubleshooting help.
tags:
- continue.dev
- ollama
- config.yaml
- model-not-appearing
---
# trying to get continue.dev to pick up the model i have running in my terminal via ollama and my model still isnt popping up? this is what the config.yaml looks like for context

### USER
trying to get continue.dev to pick up the model i have running in my terminal via ollama and my model still isnt popping up? this is what the config.yaml looks like for context

### GEMINI
It looks like you're setting up continue.dev to use a local Ollama model, and your config.yaml seems to have the correct structure for defining an Ollama model. However, there are a few common reasons why the model might not be showing up or working as expected in continue.dev: Ollama Server Not Running: The most frequent issue is that the Ollama server isn't running or accessible. continue.dev connects to Ollama via http://localhost:11434. Action: In your terminal, make sure you have ollama serve running. If you close that terminal session, Ollama will stop, and continue.dev won't be able to connect. Model Not Downloaded in Ollama: Even if Ollama is running, you need to have the specific model llama3.1:8b-instruct-q4_K_M downloaded within Ollama. Action: In your terminal, run ollama list to see if llama3.1:8b-instruct-q4_K_M is listed. If not, you need to pull it first using ollama pull llama3.1:8b-instruct-q4_K_M. Incorrect apiBase or Port: While http://localhost:11434 is the default Ollama API base, if you've configured Ollama to run on a different port or IP, continue.dev needs to reflect that. Your config.yaml currently has apiBase: http://localhost:11434, which is correct for the default. Action: Double-check your Ollama setup to ensure it's indeed running on http://localhost:11434. If you've changed OLLAMA_HOST in your Ollama environment variables, make sure your config.yaml reflects that. Continue.dev Extension Reload/Restart: After making changes to config.yaml, the continue.dev extension in your IDE often needs to be reloaded or the IDE itself restarted to pick up the changes. Action: Try reloading your VS Code window (Cmd+Shift+P or Ctrl+Shift+P and search for "Reload Window") or restarting VS Code entirely. Model Naming in config.yaml vs. Ollama: Ensure the model field in your config.yaml (llama3.1:8b-instruct-q4_K_M) exactly matches the name of the model you have pulled in Ollama. Sometimes, minor discrepancies can cause issues. "Select model" dropdown: In the screenshot, the "Select model" dropdown says "No models configured." This indicates that continue.dev hasn't successfully loaded your config.yaml or interpreted the models defined within it. After checking the above points, ensure that your config.yaml is located in the correct directory (usually ~/.continue/config.yaml on Mac/Linux or %USERPROFILE%\.continue\config.yaml on Windows). Troubleshooting Steps: Open a new terminal and run ollama serve. Keep this terminal open. In another terminal, run ollama list to confirm llama3.1:8b-instruct-q4_K_M is downloaded. If not, run ollama pull llama3.1:8b-instruct-q4_K_M. Verify your config.yaml location (e.g., ~/.continue/config.yaml). Reload your VS Code window or restart VS Code. Check the "Output" tab in VS Code (View -> Output) and select "Continue" from the dropdown. This might provide error messages or logs related to model loading. By systematically checking these points, you should be able to identify why your Ollama model isn't appearing in continue.dev.
