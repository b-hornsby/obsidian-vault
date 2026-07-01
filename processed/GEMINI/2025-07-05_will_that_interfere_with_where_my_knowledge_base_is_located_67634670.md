---
category: ai-tools
date: 2025-07-05
id: 563250
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- second-brain-vault
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is concerned about potential conflicts between a new configuration
  or setting and the location of his existing knowledge base for the RAG system.
tags:
- local-llm
- rag-implementation
- knowledge-base
- data-location
---
# will that interfere with where my knowledge base is located?

### USER
will that interfere with where my knowledge base is located?

### GEMINI
No, deleting those Python scripts (create_db.py and rag_chat.py) will not interfere with where your knowledge base is located or how superboogav2 accesses it. Here's why: Your primary knowledge base that superboogav2 uses is now managed internally by superboogav2 within Oobabooga's own file structure, after you uploaded your documents via its "File input" interface. The chroma_db folder you created earlier (located at ~/helpdesk_ai_rag/chroma_db) is separate and independent. superboogav2 is not directly using that specific folder for its RAG operations. So, deleting the scripts (create_db.py and rag_chat.py) only removes the tools you used to build and interact with that external chroma_db. It doesn't affect superboogav2's functionality or its internal database.
