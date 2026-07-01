---
category: ai-tools
date: 2025-11-18
id: 881658
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was getting an API key/plan error when trying to use qwen 2.5 coder
  in Cursor via ngrok and needed help resolving it.
tags:
- qwen25-coder
- cursor-ide
- ngrok
- api-key-error
- local-llm-deployment
---
# trying to get qwen 2.5 coder to work in cursor using ngrok to do so. i just tried to do these steps and it said that qwen 2.5 coder does not work with your current plan or api key: Open Cursor settings
Navigate to “Models”
Add a new custom model
Enter your model name (e.g., “llama2”)
Go to “OpenAI API Key” section
Override the “OpenAI Base URL” with your ngrok URL
In the key field, type “Ollama”
Save and test

### USER
trying to get qwen 2.5 coder to work in cursor using ngrok to do so. i just tried to do these steps and it said that qwen 2.5 coder does not work with your current plan or api key: Open Cursor settings
Navigate to “Models”
Add a new custom model
Enter your model name (e.g., “llama2”)
Go to “OpenAI API Key” section
Override the “OpenAI Base URL” with your ngrok URL
In the key field, type “Ollama”
Save and test

### GEMINI
That error message, "The model does not work with your current plan or API key," is a very common issue when trying to connect a local LLM (like Qwen 2.5 Coder via Ollama and ngrok) to Cursor. It often appears even when your setup is technically correct. Based on your steps and common troubleshooting, here are the most likely issues and the full, corrected steps you should follow: 🛠️ Troubleshooting Your Cursor Setup The error you're seeing usually points to one of two things: Missing Endpoint Suffix: The URL you're overriding the base URL with needs to point to the OpenAI-compatible API endpoint, which is usually */v1. Model Selection Conflict: Cursor is trying to validate all selected models against the new base URL and key. Since the real OpenAI models will fail this check, you must only select your custom local model. Corrected Setup Steps (The "Full Guide") Follow these steps precisely, paying close attention to the details in bold: 1. Prerequisite: Ollama and ngrok Setup Before configuring Cursor, ensure these are running: Ollama is installed and running with Qwen 2.5 Coder downloaded. (e.g., in a terminal: ollama run qwen2.5-coder:7b) CORS is enabled for Ollama (Crucial for remote access like ngrok). macOS/Linux: export OLLAMA_ORIGINS='*' (Run this in the same terminal before running ollama serve, or add it to your shell profile). Windows (PowerShell Admin): [System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User') (Then restart Ollama). Ollama server is running. (e.g., in a terminal: ollama serve) ngrok is running and tunneling the Ollama port. The default Ollama port is 11434. (e.g., in a terminal: ngrok http 11434 --host-header="localhost:11434") Get your ngrok URL. It will look something like https://random-subdomain.ngrok-free.app. 2. Configure Cursor Open Cursor Settings (Ctrl+, or Cmd+,). Navigate to "Models." Click "+Add Model" to add a new custom model. Model Name: Enter the exact name of your Ollama model. Example: qwen2.5-coder:7b (or qwen2.5-coder:32b, etc.) Scroll down to the "OpenAI API Key" section. Override the "OpenAI Base URL": Paste your ngrok URL and append /v1 to the end. Example: https://random-subdomain.ngrok-free.app/v1 API Key Field: Type a placeholder. Your choice of Ollama is perfect. Critical Step: Unselect Other Models Uncheck/toggle OFF all other models (GPT-4, Claude, etc.), leaving only your custom model (qwen2.5-coder:...) selected. Click "Save" and then "Verify." If your Ollama and ngrok setups are running correctly with CORS enabled, this configuration should now pass the verification and the error should be resolved. 💡 Why this fixes the issue: /v1 Suffix: This tells Cursor's API requests where the actual OpenAI-compatible endpoint is on your local server. Unselecting Other Models: This prevents Cursor from attempting to send test requests for models like GPT-4 to your Ollama/ngrok URL, which would cause an authentication failure and trigger the error message you received. Would you like me to find the specific command to enable CORS permanently on your operating system (Windows, macOS, or Linux)?
