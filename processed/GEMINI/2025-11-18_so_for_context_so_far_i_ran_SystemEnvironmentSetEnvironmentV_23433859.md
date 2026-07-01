---
id: 445697
source: GEMINI
date: 2025-11-18
tags: ['ollama', 'ollama-origins', 'ngrok', 'windows-environment', 'local-llm-setup']
category: ai-tools
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan had set OLLAMA_ORIGINS, started Ollama serve, and ran ngrok, and wanted to know the next steps.
---
# so for context, so far i ran  [System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User') which returned nothing, i ran ollama serve and ran ngrok http 11434 --host-header="localhost:11434". now what? 

### USER
so for context, so far i ran  [System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User') which returned nothing, i ran ollama serve and ran ngrok http 11434 --host-header="localhost:11434". now what? 

### GEMINI
You're in the final stretch! You've correctly set the Ollama environment variable, and you have both the Ollama server and the ngrok tunnel running. The reason [System.Environment]::SetEnvironmentVariable('OLLAMA_ORIGINS', '*', 'User') returned nothing is normal—that PowerShell command sets the persistent variable without providing output. However, since you ran ollama serve and ngrok in separate, potentially older terminal windows, the running Ollama server might not have picked up the new environment variable yet. Here is the plan to finish the setup in Cursor: 1. Verify and Restart Ollama You need to make sure the running ollama serve process knows about the OLLAMA_ORIGINS variable. Stop Ollama: Go to the terminal window where you ran ollama serve and press Ctrl+C to stop the server. Restart Ollama: Start it again. You may also need to close and reopen your terminal window to ensure the new environment variables are loaded by the shell before running ollama serve. ollama serve Confirm ngrok URL: Check the terminal window where ngrok is running and copy the HTTPS forwarding address. Example URL: https://random-subdomain.ngrok-free.app 2. Configure Cursor Now, you'll use the ngrok URL to configure Cursor's custom model settings. Open Cursor Settings: Press Ctrl+, or Cmd+, and go to the "Models" section. Add Your Custom Model: Click "+ Add Model." Enter the exact model name: qwen2.5-coder:14b-instruct-q4_K_M Set API Overrides: Scroll down to the "OpenAI API Key" section. API Key: Type a placeholder, like Ollama Override the "OpenAI Base URL": Paste your ngrok URL and append /v1 to the end. This is the API-compatible endpoint Ollama exposes. Example: https://random-subdomain.ngrok-free.app/v1 Isolate the Model (Crucial!): In the list of available models, uncheck/disable all other models (GPT-4, Claude, etc.). Ensure only qwen2.5-coder:14b-instruct-q4_K_M is checked. Save and Test: Click "Save" and then "Verify." It should now verify successfully. You can now open the Cursor chat panel (Cmd+L / Ctrl+L), select your Qwen model from the dropdown, and start coding! You might be interested in a visual guide for setting up environment variables on Windows. Setting environment variables for Ollama on Windows provides a walkthrough of how to handle environment variables for Ollama on a Windows system.
