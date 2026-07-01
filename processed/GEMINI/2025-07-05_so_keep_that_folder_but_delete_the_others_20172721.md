---
id: 483329
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'oobabooga', 'rag', 'chroma', 'long', 'go']
category: ai-tools
sentiment: building
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# so keep that folder but delete the others? 

### USER
so keep that folder but delete the others? 

### GEMINI
Yes, that's correct. You should keep: The knowledge_base folder (\\wsl.localhost\Ubuntu\home\bryan_\helpdesk_ai_rag\knowledge_base). This contains your original raw text documents, which you loaded into superboogav2's internal database. It's a good idea to retain your source data. You can delete: The create_db.py script. The rag_chat.py script. The chroma_db folder (located at ~/helpdesk_ai_rag/chroma_db). This was your original, external ChromaDB. superboogav2 is now using its own internally built database, so this folder is no longer needed for your Oobabooga RAG setup. Deleting these items will free up some space and clean up your project folder without affecting your working RAG setup in Oobabooga.