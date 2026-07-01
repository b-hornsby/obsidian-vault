---
category: ai-tools
date: 2025-07-06
id: 626409
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking whether his local AI setup will require internet every time
  he runs the startup command.
tags:
- internet-dependency
- offline-mode
- superbooga
- local-deployment
---
# will it need to be online every time i run that command? 

### USER
will it need to be online every time i run that command? 

### GEMINI
No, it will not need to be online every time you run that command for the core components (LLM, Whisper STT, and superboogav2's embedding model). Here's a breakdown: Main LLM (Phi-3 Mini) & Whisper STT: Once these models are downloaded and saved in your ~/text-generation-webui/models/ directory, they run entirely offline. They do not require an internet connection to load or operate. superboogav2 (Local RAG): This is where the recent issue was. It needed an internet connection the first time it loaded successfully to download its embedding model (e.g., all-MiniLM-L6-v2) from Hugging Face Hub. Now that it has successfully downloaded and cached that embedding model, superboogav2 itself should load and function offline for its core purpose of processing your local documents. web_rag (Web Search RAG): This is the only extension that will continuously require an internet connection every time it needs to perform a web search. If you have web_rag enabled and ask a question that triggers a search (and "Activate web search" is checked in the chat), it will attempt to go online to query DuckDuckGo. If you disable web_rag in the extensions, then your system can run completely offline. In summary: Offline Functionality (after initial setup): Your main AI conversation (LLM + STT + superboogav2 with local docs) will work fine without internet once all necessary models are downloaded. Online Requirement: Only web_rag demands a live internet connection to perform its specific function of searching the web. If web_rag is disabled or not triggered, you can run the system fully offline.
