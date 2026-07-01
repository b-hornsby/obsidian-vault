---
id: 601045
source: GEMINI
date: 2025-07-05
tags: ['oobabooga', 'superbooga', 'local-llm-deployment', 'startup-script']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is inquiring about the necessity of manually starting Superbooga every time he runs the server, as it doesn't seem to be automatic.
---
# seems to be working properly. do i need to boot up superbooga every time? when i ran the command it didn't automatically: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf

### USER
seems to be working properly. do i need to boot up superbooga every time? when i ran the command it didn't automatically: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf

### GEMINI
No, you don't need to "boot up" superbooga manually every time. When you start Oobabooga with the command you provided, superboogav2 should load automatically if it's enabled in the "Extensions" tab and its settings are saved. Here's why it might seem like it's not: No explicit terminal message: The server startup logs won't explicitly say "Superbooga is now active and ready!" It will just say Loading the extension "superboogav2" (which you saw earlier). Web UI settings persistence: Once you check superboogav2 in the "Extensions" tab and click "Save settings" (and restart the server via the UI prompt), that setting is saved. The next time you start Oobabooga with your server.py command, it reads these saved settings and automatically enables superboogav2. Data persistence: The data you loaded into superbooga via the "File input" tab in the UI is also persistent. It saves its internal ChromaDB. You do not need to re-upload your documents every time you start the server. How to Confirm superboogav2 is Running (After a Fresh Server Start) Start Oobabooga: Use your standard command: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Check the Terminal Logs: Look for the line Loading the extension "superboogav2" during startup. If you see this, it's loading. Check Web UI "Extensions" Tab: Once the server is running and you're in the browser, go to the "Extensions" tab. The superboogav2 checkbox should still be checked. This indicates it's enabled and should be active. Test RAG in "Chat" Tab: Go to the "Chat" tab, ensure chat-instruct mode is selected, and that "Include attachments/search results..." is checked. Ask a question directly from your documents. If the AI provides an answer pulling from your knowledge base (especially if it shows the Consider the excerpts below as additional context: prompt injection), then superboogav2 is indeed working. You only need to manually re-enable it or re-load data if you explicitly uncheck it in the "Extensions" tab or click "Clear data" in the superbooga configuration interface. Otherwise, it should be ready to go on every startup.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
