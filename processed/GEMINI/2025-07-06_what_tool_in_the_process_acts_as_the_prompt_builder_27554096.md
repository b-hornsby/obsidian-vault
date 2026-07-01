---
category: ai-tools
date: 2025-07-06
id: 770018
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking which component in his project's architecture acts as the
  prompt builder.
tags:
- prompt-builder
- RAG
- architecture
- process-flow
---
# what tool in the process acts as the prompt builder? 

### USER
what tool in the process acts as the prompt builder? 

### GEMINI
Based on our project's process flow, the component that acts as the prompt builder would primarily be the one labeled "Processing & Knowledge Retrieval (RAG)". This is the central part of the system where: The output from the Speech-to-Text (STT) is taken. Relevant information is retrieved from your knowledge base (likely using the "sentence-transformers & Knowledge Retriever" to query ChromaDB). All this information, along with the user's query, is then synthesized and formatted into the final prompt that will be fed into the Large Language Model (LLM), which is Phi-3 in our case. So, while "sentence-transformers & Knowledge Retriever" helps gather the necessary information, the "Processing & Knowledge Retrieval (RAG)" component is where the actual construction and optimization of the prompt take place before it's sent to the LLM.
