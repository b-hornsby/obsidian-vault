---
category: ai-tools
date: 2025-07-05
id: 104314
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is exploring whether web-based RAG can be achieved locally without
  relying on external services.
tags:
- web-RAG
- local-deployment
- web-search
- RAG
---
# what about web RAG? Can that be achieved locally as well? 

### USER
what about web RAG? Can that be achieved locally as well? 

### GEMINI
Yes, web RAG can be achieved locally, though the specific setup will depend on how the Oobabooga extension or your custom script handles web content. Previously, during our troubleshooting, we briefly encountered a web_rag extension. This extension is designed for "Retrieval-Augmented Generation from Web content". Here's how local web RAG generally works and what you'd need: Web Content Acquisition: Instead of having pre-saved .txt files, the RAG system first needs to fetch content from the web. This can be done by: Manual URL Input: You provide specific URLs for the RAG system to scrape. Automated Search: The system might take your prompt, convert it into a search query, and then use a tool (like a command-line browser, as mentioned for web_rag) to find relevant web pages and retrieve their content. Local Storage and Embedding: Once the web content is retrieved, it needs to be processed. This involves: Chunking: Breaking down the long web pages into smaller, manageable chunks of text. Embedding: Converting these text chunks into numerical vectors (embeddings) using a local embedding model (like nomic-embed-text with Ollama, which you've used). Local Vector Database: Storing these embeddings in a local vector database (like ChromaDB), which is then queried for retrieval. Integration with LLM: Similar to your current RAG setup, when you ask a question, the system queries this local web-content database, retrieves relevant chunks, and feeds them to your local LLM (Nous-Hermes-2) to generate an augmented response. Steps if using the web_rag extension (or similar): If you were to explore the web_rag extension or a similar one, the process would likely involve: Installing the web_rag extension (if it's available and compatible with your Oobabooga version). Installing any specific dependencies it might have (e.g., a command-line browser like Links, as mentioned in its description). Configuring it in the Oobabooga UI to either: Provide URLs directly. Allow it to perform automated web searches based on your prompts. Specify a local directory where it stores the scraped web data and its associated vector database. Essentially, the "local" part refers to where the vector database containing the web content is stored and processed (on your machine), even if the source of the data is the internet.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
