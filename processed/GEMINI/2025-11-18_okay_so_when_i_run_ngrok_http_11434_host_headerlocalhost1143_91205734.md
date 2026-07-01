---
id: 028705
source: GEMINI
date: 2025-11-18
tags: ['ngrok', 'ollama', 'tunneling', 'localhost', 'local-llm-deployment']
category: ai-tools
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan successfully ran ngrok to tunnel Ollama on port 11434 and was sharing the output to verify the setup.
---
# okay so when i run ngrok http 11434 --host-header="localhost:11434" i get this: �  Using ngrok for OSS? Request a community license: https://ngrok.com/r/oss

Session Status                online
Account                       bryh4m@gmail.com (Plan: Free)
Version                       3.24.0-msix
Region                        United States (us)
Latency                       19ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://delena-ungrinned-lemuel.ngrok-free.dev -> http://localhost:11434

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00

### USER
okay so when i run ngrok http 11434 --host-header="localhost:11434" i get this: �  Using ngrok for OSS? Request a community license: https://ngrok.com/r/oss

Session Status                online
Account                       bryh4m@gmail.com (Plan: Free)
Version                       3.24.0-msix
Region                        United States (us)
Latency                       19ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://delena-ungrinned-lemuel.ngrok-free.dev -> http://localhost:11434

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00

### GEMINI
That's perfect! You have successfully established the tunnel, and your ngrok terminal output gives you the exact address you need for Cursor. The Forwarding line is the key: Forwarding https://**delena-ungrinned-lemuel.ngrok-free.dev** -> http://localhost:11434 📝 Final Cursor Configuration Steps You are now ready to put this URL into Cursor. Follow the steps exactly to ensure the connection works and avoids the previous error. 1. The URL to Copy Copy the ngrok HTTPS URL: https://delena-ungrinned-lemuel.ngrok-free.dev The complete URL for Cursor (you must append the /v1 endpoint): https://delena-ungrinned-lemuel.ngrok-free.dev/v1 2. Cursor Settings (Finalization) Open Cursor Settings (Ctrl+, or Cmd+,) and go to "Models." Verify or Add the Model: Ensure your custom model is listed with the exact name: qwen2.5-coder:14b-instruct-q4_K_M Configure API Overrides: Scroll down to the "OpenAI API Key" section. API Key: Enter a placeholder, like Ollama Override the "OpenAI Base URL": Paste the complete URL from step 1: https://delena-ungrinned-lemuel.ngrok-free.dev/v1 Isolate the Model (Critical): Go back to the model list and uncheck/toggle OFF all other models (GPT-4, Claude, etc.). Only leave qwen2.5-coder:14b-instruct-q4_K_M checked. Save and Test: Click "Save" and then "Verify." If your Ollama server is still running in the background, this connection should now be live! You can start the chat/copilot (Cmd+L or Ctrl+L) and send your first coding prompt.
