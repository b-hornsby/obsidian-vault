---
category: ai-tools
date: 2025-11-18
id: 508464
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan wanted a step-by-step walkthrough to get qwen2.5-coder:14b running
  in Cursor using ngrok.
tags:
- ollama
- qwen25-coder
- cursor-ide
- ngrok
- local-llm-setup
---
# run me through what it is that i need to do to get this model running in cursor using ngrok: qwen2.5-coder:14b-instruct-q4_K_M

### USER
run me through what it is that i need to do to get this model running in cursor using ngrok: qwen2.5-coder:14b-instruct-q4_K_M

### GEMINI
That's a fantastic model to choose for coding! The specific quantization and instruct version (qwen2.5-coder:14b-instruct-q4_K_M) is excellent. Here is the full, step-by-step process to get this model running in Cursor via Ollama and ngrok, which includes the critical steps to avoid the "API key/plan" error you saw previously. 🚀 Qwen 2.5 Coder Setup Guide This process has three main phases: Ollama setup, ngrok tunneling, and Cursor configuration. Phase 1: Ollama Setup You need to ensure the Ollama server is running and configured to accept external requests (which ngrok counts as). Pull the Model (If you haven't yet): Open your terminal/command prompt and download the model. ollama pull qwen2.5-coder:14b-instruct-q4_K_M Enable CORS (Crucial Step): You must set the OLLAMA_ORIGINS environment variable to allow requests from the public ngrok URL. Do not skip this. The command depends on your operating system: macOS/Linux: export OLLAMA_ORIGINS="*" Windows (PowerShell Admin): [System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User') (Note: If you use the Windows Installer GUI, you might need to restart it after this.) Start the Ollama Server: Run the server in the same terminal session where you set the environment variable (or ensure the variable is set permanently). ollama serve (The server runs on port 11434 by default.) Phase 2: ngrok Tunneling Next, you'll create a public URL that forwards traffic directly to your local Ollama server. Start the ngrok Tunnel: Open a new terminal/command prompt window and run the ngrok command, pointing it to Ollama's default port (11434). The --host-header flag is essential for compatibility with Ollama. ngrok http 11434 --host-header="localhost:11434" Capture the URL: ngrok will display an interface. Look for the Forwarding line and copy the https:// URL. Example: https://**random-subdomain.ngrok-free.app** This is your NGROK_BASE_URL. Phase 3: Cursor Configuration This is where you tell Cursor to use the ngrok URL instead of the default OpenAI endpoint. Open Cursor Settings: Press Ctrl+, or Cmd+, to open the settings, then navigate to the "Models" section. Add Your Custom Model: Scroll down and click "+ Add Model." In the text field, enter the exact model name you pulled: Model Name: qwen2.5-coder:14b-instruct-q4_K_M Override API Settings: Scroll to the "OpenAI API Key" section (yes, even though it's Ollama). API Key: Type a placeholder key, like Ollama Override the "OpenAI Base URL": Paste the ngrok URL you copied and append /v1 to it. This is critical. Example: https://random-subdomain.ngrok-free.app/v1 Isolate the Custom Model (Avoid the Error): Look at the list of models in your settings. Uncheck/toggle OFF all other models (GPT-4, Claude, etc.). Ensure only your new custom model (qwen2.5-coder:14b-instruct-q4_K_M) is checked/enabled. Save and Test: Click "Save" and then "Verify." It should now pass the verification check. Open the Cursor chat panel (Cmd+L / Ctrl+L) and ensure your new Qwen model is selected in the dropdown. Send a test prompt like "Write a Python function for a binary search." You should see traffic logs appear in your ngrok and Ollama terminal windows as the model generates the response! Would you like me to clarify the best way to make the OLLAMA_ORIGINS setting permanent on your specific operating system?
