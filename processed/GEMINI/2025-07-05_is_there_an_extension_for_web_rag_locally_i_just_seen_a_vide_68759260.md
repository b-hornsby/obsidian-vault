---
category: ai-tools
date: 2025-07-05
id: 688560
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan was asking about local web RAG extensions after seeing a video, looking
  for an easier approach to web search integration.
tags:
- web-rag-extension
- local-web-search
- superboogav2
---
# is there an extension for web rag locally? i just seen a video on it and idk if that would be easier 

### USER
is there an extension for web rag locally? i just seen a video on it and idk if that would be easier 

### GEMINI
Yes, there are extensions for Web RAG (Retrieval Augmented Generation) that can run locally within Oobabooga's text-generation-webui. This is generally easier and more integrated than building a separate script, as it leverages the existing UI and server architecture. How Web RAG Extensions Work A Web RAG extension in Oobabooga typically allows you to: Ingest data from web sources: This can include specific URLs, entire websites, or even local files, which are then processed and added to a vector database. Perform embeddings: It uses an embedding model (often a local one or one from a service like OpenAI) to convert the ingested text into numerical vectors. Store in a vector database: These vectors are stored in a local database (like ChromaDB, which you're already using) for efficient similarity searches. Retrieve relevant information: When you ask a question in the chat interface, the extension intercepts it, finds the most relevant information from your custom knowledge base, and then sends both your question and the retrieved context to the large language model (LLM). Generate augmented responses: The LLM uses this combined information to generate a more accurate and contextually relevant answer. Finding a Web RAG Extension As we saw from your "Extensions" tab screenshot, there isn't a pre-installed extension explicitly named "RAG" or "Web RAG". This means you'll likely need to manually install one from the Oobabooga community. Here's the general process you'll follow: Identify a suitable extension: The Oobabooga GitHub repository and community forums are the best places to find these. Search for "RAG extension", "Web RAG", "Langchain extension", or similar terms. Common and well-supported extensions are often listed or linked there. Recommendation: Look for an extension that specifically supports local vector databases like Chroma (which you're already using for db). Download/Clone the extension: Once you find an extension, its documentation will usually provide instructions, which often involve using git clone to download the extension's files into your ~/text-generation-webui/extensions/ directory. Install dependencies: Many extensions have their own Python dependencies. You'll typically find a requirements.txt file within the extension's folder. You'll need to install these dependencies using pip within Oobabooga's Python environment. From your ~/text-generation-webui directory, if the extension's folder is my_rag_extension, you'd do: ./installer_files/env/bin/pip install -r extensions/my_rag_extension/requirements.txt Enable the extension in the UI: After installing the files and dependencies, restart Oobabooga. Go to http://127.0.0.1:7860, navigate to the "Extensions" tab, find your newly added Web RAG extension, check its box, and save/restart the server again. Configure the extension: Once enabled and restarted, the extension will likely add a new tab or a new section within an existing tab in the Oobabooga UI. Here, you'll configure settings such as: Path to your knowledge base/vector database: You'd point it to user_data/db (assuming you've moved your db folder as previously suggested). Embedding model: You might need to specify the embedding model you're using (e.g., nomic-embed-text via Ollama, or a local SentenceTransformer model). Retrieval settings: Options like the number of documents (k) to retrieve for context. Web scraping options: If it's a "Web RAG" specific extension, it will have fields to input URLs for crawling and ingesting data directly from the web. Next Steps: Your best bet is to start by searching the Oobabooga community resources for a suitable "RAG" or "Web RAG" extension. Once you find one, I can help you with the specific installation and configuration steps.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
