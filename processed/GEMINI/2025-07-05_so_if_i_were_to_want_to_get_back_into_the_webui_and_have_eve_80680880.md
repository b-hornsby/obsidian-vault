---
id: 132825
source: GEMINI
date: 2025-07-05
tags: ['oobabooga', 'webui-restart', 'document-loading', 'command-sequence']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking for the specific commands needed to restart the oobabooga web UI and load documents from a fresh instance.
---
# so if i were to want to get back into the webui and have everything running from those documents off a fresh instance, what commands would i have to put in? 

### USER
so if i were to want to get back into the webui and have everything running from those documents off a fresh instance, what commands would i have to put in? 

### GEMINI
To get back into the Oobabooga web UI with your RAG system running from your existing documents (chroma_db), you only need to perform a few commands to start the server. You won't need to reinstall extensions or copy your database again, as those steps are already complete. Here's the sequence of commands for a fresh start: Start Oobabooga Web UI with RAG Open your WSL2 terminal. Navigate to the Oobabooga text-generation-webui root directory: cd ~/text-generation-webui Start the Oobabooga server with your model: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf This command will: Activate Oobabooga's Python environment. Start the web server. Load your Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf model. Automatically load the superboogav2 extension (because it's enabled in your Oobabooga settings). Wait for the server to fully load. You'll see output in the terminal indicating the model loading process, and finally, it will display the local URL: Running on local URL: http://127.0.0.1:7860 Verify RAG in the Web UI Open your web browser and go to http://127.0.0.1:7860. Navigate to the "Chat" tab. Confirm the RAG setting is active: In the right-hand "Settings" panel, ensure the checkbox "Include attachments/search results from previous messages in the chat prompt" is checked. If not, check it. Start chatting! Ask a question that your knowledge base can answer (e.g., "my wifi drops frequently"). The superboogav2 extension, leveraging your user_data/chroma_db, should automatically provide relevant context to the AI's responses. You don't need to manually tell it to load the documents each time; once configured and the extension is enabled, it's part of the standard startup.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
