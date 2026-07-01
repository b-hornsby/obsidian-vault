---
id: 788759
source: GEMINI
date: 2025-07-05
tags: ['text-generation-webui', 'web-rag', 'chroma-db', 'extension-search']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is requesting assistance in finding a web RAG extension for Oobabooga that supports ChromaDB.
---
# can you find me a web RAG extension for oobabooga? Look for an extension that specifically supports local vector databases like Chroma (which i'm already using for db).

### USER
can you find me a web RAG extension for oobabooga? Look for an extension that specifically supports local vector databases like Chroma (which i'm already using for db).

### GEMINI
Yes, I can help you find a suitable web RAG extension for Oobabooga's text-generation-webui that supports local vector databases like Chroma. Based on recent community activity and common use cases, the rag extension is a strong candidate for what you're looking for. This extension is designed to integrate RAG functionality directly into the Oobabooga web UI and typically supports local vector databases. Here's how to proceed with finding and setting it up: 1. Locate the rag Extension The rag extension is usually found within the main Oobabooga GitHub repository under the extensions directory. You can find its specific location here: https://github.com/oobabooga/text-generation-webui/tree/main/extensions/rag 2. Manual Installation Steps Even though it might be part of the main repository, you'll often need to ensure all its specific dependencies are installed. First, stop Oobabooga if it's currently running in your WSL2 terminal (Ctrl + C). Then, follow these commands in your WSL2 terminal (the one where Oobabooga is installed): Step 2.1: Navigate to the Oobabooga Root Directory cd ~/text-generation-webui Step 2.2: Install rag Extension Dependencies The rag extension has its own requirements.txt file. We need to install these using Oobabooga's specific Python environment. ./installer_files/env/bin/pip install -r extensions/rag/requirements.txt This command will install any Python libraries required by the rag extension. Let it complete fully. Step 2.3: Copy Your Knowledge Base As discussed before, you need to copy your existing ChromaDB database (db folder) into a location Oobabooga can easily access, such as its user_data directory. If you haven't already, ensure you copy your db folder from ~/helpdesk_ai_rag/ to ~/text-generation-webui/user_data/: cp -r ~/helpdesk_ai_rag/db ~/text-generation-webui/user_data/ Step 2.4: Restart Oobabooga Now, restart Oobabooga with your model. We'll no longer need the --api flag specifically for your RAG script once the extension is configured, as the extension will handle it directly within the UI. However, keeping --api doesn't hurt if you still want to use your rag_chat.py script for testing. ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf (You can add --api back if you still need it for external scripts, but for UI RAG, it's not strictly necessary). Wait for Oobabooga to fully load and display the local URL. 3. Enable and Configure the rag Extension in the Web UI Open the Oobabooga Web UI: Go to http://127.0.0.1:7860 in your web browser. Navigate to the "Extensions" Tab: Click on the "Extensions" tab. Enable rag: Find rag in the list of available extensions and check its box. Save Settings and Restart: Click the "Save settings" button and then restart the server as prompted by the UI. Configure rag Extension: After the server restarts, you should now see a new tab specifically for the rag extension (it's often named "RAG"). Click on this "RAG" tab. Knowledge Base Path: Look for an input field labeled "Knowledge base path" or similar. Enter the path to your copied database: user_data/db. Embedding Model: The rag extension often lets you choose an embedding model. If it offers an "Ollama" option or a "Local" option, select it and specify nomic-embed-text as the model name. If it only lists HuggingFace models, you might need to install that embedding model separately or adjust the extension's configuration. Retrieval Parameters: You might find options for k (number of documents to retrieve) and other parameters. You can leave these as default for now or adjust them as needed. Ingestion (Optional): The rag extension also has capabilities to ingest new documents directly from the UI (including web pages, usually). This is where you can add new knowledge later if you choose to. Save Configuration: Don't forget to save the settings within the "RAG" tab itself. Once configured, you should be able to go to the "Chat" or "Text Generation" tab, type your query, and the rag extension will automatically retrieve context from your knowledge base to enhance the LLM's response.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
