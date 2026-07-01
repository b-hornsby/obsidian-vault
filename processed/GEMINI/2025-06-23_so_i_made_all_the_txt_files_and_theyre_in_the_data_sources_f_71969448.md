---
id: 352302
source: GEMINI
date: 2025-06-23
tags: ['data-sources', 'txt-files', 'training-data']
category: ai-tools
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan created text files for his helpdesk AI and placed them in the data_sources folder.
---
# so i made all the txt files and they're in the data_sources folder. whats next? 

### USER
so i made all the txt files and they're in the data_sources folder. whats next? 

### GEMINI
Excellent! That's a huge step forward. Having your .txt files in the data_sources folder means your knowledge base is ready to be "read" by your AI. Now, the next crucial step is to ingest these documents using the RAG extension in Oobabooga. This process reads your text files, processes them, and creates a searchable index that your AI can use. Here's what you need to do: Step 1: Ensure Oobabooga is Running If your Oobabooga terminal is still open and running from our last session, great! Just make sure it hasn't crashed or stopped. If it's not running, open your WSL2 Ubuntu terminal and start it using your script: cd ~/text-generation-webui ./start_ooba.sh Wait for the browser UI to open and the model to load. Step 2: Go to the "Extensions" Tab In your Oobabooga Web UI (in your browser), click on the "Extensions" tab in the left-hand navigation panel. Step 3: Find and Enable a RAG Extension On the "Extensions" page, you'll see a list of available extensions. Scroll through the list and look for an extension related to "RAG," "Knowledge Base," "Vector Store," or "Document Loader." Common names you might see are rag_agent, simple_rag, document_loader, or similar. The exact name can sometimes change or new ones emerge. Just look for something that clearly implies "giving the AI a memory/knowledge base." If you find one that's not installed, click the "Install" button next to it. Once installed, click the checkbox next to its name to ENABLE it. Important: After enabling an extension, sometimes Oobabooga will prompt you to "Restart the server to apply changes." If you see this, click that button. Wait for the server to restart (you'll see activity in your WSL2 terminal, and the browser UI might refresh). Step 4: Configure the RAG Extension Once the RAG extension is enabled and Oobabooga has potentially restarted: The RAG extension should now appear in the list under "Active extensions." Next to its name, you should see a "Configure" button (often a gear icon or similar). Click this button. A configuration panel will appear, specific to that RAG extension. Look for fields such as: "Data directory" or "Knowledge base path": This is where you'll tell it where your .txt files are. Type in data_sources/ (or data_sources depending on the field's expected format). "Embedding Model": Some RAG extensions require you to select or download an "embedding model." If you see a button to "Download" or "Install" an embedding model, click it. This model is used to convert your text documents into numerical vectors for efficient searching. Follow any prompts. Step 5: Ingest Your Documents Within the RAG extension's configuration panel (the one you're currently in), look for a button that says something like: "Load Documents" "Process Documents" "Build Vector Store" "Index Documents" Click that button. Watch your WSL2 terminal! It will show progress as the extension reads each of your .txt files, chunks them, and processes them. This step can take anywhere from a few seconds to several minutes, depending on the number and size of your documents and your CPU speed. Step 6: Test Your RAG-Powered AI Once the ingestion process finishes (the terminal stops showing activity and returns to its prompt, or the UI indicates completion), go back to the "Chat" tab in Oobabooga. Activate RAG in Chat: Some RAG extensions will add a new "Mode" to the left panel (e.g., "Chat - RAG"). Select this mode. Others might add a checkbox or toggle switch directly in the chat interface that you need to turn on to enable RAG for your queries. Ask Questions from Your Documents: Now, ask your AI questions that can only be answered by the content you put into your .txt files. Example: "How do I clear browser cache in Chrome?" or "What's the process for fixing a slow computer?" or "Explain what a VPN is." Your AI should now retrieve information from your data_sources and use it to formulate its answers, making it a much more informed help desk agent! Let me know if you run into any specific issues or error messages during this process.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
