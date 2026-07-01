---
category: ai-tools
date: 2025-07-05
id: 891985
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to confirm whether the 'adding new embeddings' terminal message
  indicates the RAG system is working correctly.
tags:
- embeddings
- RAG
- chromadb
- terminal-output
---
# so you can tell its working when the terminal says adding new embeddings? 

### USER
so you can tell its working when the terminal says adding new embeddings? 

### GEMINI
Yes, when your WSL2 terminal shows Adding X new embeddings (like Adding 5 new embeddings you saw earlier) after you send a message in the Oobabooga UI, it's a strong indication that the superboogav2 extension is actively performing a retrieval from your knowledge base as part of the RAG process. Here's a breakdown: Embeddings are the core of RAG: When superboogav2 receives your query, it takes that query, converts it into a numerical "embedding," and then uses that embedding to search your chroma_db for the most similar document chunks. "Adding new embeddings" during RAG: This message means the extension is processing your input (and possibly some internal context) to create new embeddings for the search query itself or for any new context it's internally building. It then uses these to find relevant information in your existing chroma_db (which holds the embeddings of your knowledge base documents). So, while the "Adding new embeddings" log might sound like it's creating new documents, in the context of superboogav2 during a chat, it primarily signifies that it's generating embeddings for the current interaction to perform the retrieval step of RAG. The ultimate confirmation that RAG is fully working is seeing a relevant, augmented response from the AI in the Oobabooga web UI, and ideally, a display of the source documents used.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
