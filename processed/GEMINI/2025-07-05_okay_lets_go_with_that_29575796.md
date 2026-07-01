---
id: 252110
source: GEMINI
date: 2025-07-05
tags: ['oobabooga', 'model-selection']
category: ai-tools
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is agreeing to proceed with a suggested model or setting within oobabooga.
---
# okay lets go with that 

### USER
okay lets go with that 

### GEMINI
Perfect! Then you are all set for a cleaner project folder. To reiterate the cleanup steps: Open your WSL2 terminal. Navigate to your helpdesk_ai_rag directory: cd ~/helpdesk_ai_rag Delete the scripts and the old ChromaDB folder: rm create_db.py rag_chat.py rm -r chroma_db (The rm -r command is used for deleting directories and their contents). Confirm the knowledge_base folder remains: ls -l You should still see knowledge_base/ listed, but create_db.py, rag_chat.py, and chroma_db/ should be gone. Your Oobabooga Web UI with the superboogav2 RAG extension should continue to function normally, using the knowledge base you loaded directly through its interface.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
