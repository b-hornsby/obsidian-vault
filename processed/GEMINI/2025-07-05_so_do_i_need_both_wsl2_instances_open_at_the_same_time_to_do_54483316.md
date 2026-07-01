---
id: 978222
source: GEMINI
date: 2025-07-05
tags: ['wsl2', 'oobabooga', 'document-loading', 'rag-verification']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking if he needs to have two WSL2 instances running simultaneously to verify that his documents are being loaded correctly.
---
# so do i need both wsl2 instances open at the same time to double check that its loading my docs? 

### USER
so do i need both wsl2 instances open at the same time to double check that its loading my docs? 

### GEMINI
No, you do not need both WSL2 instances open to double-check that it's loading your docs. In fact, you only need one WSL2 terminal window open, running Oobabooga's text-generation-webui. Here's why and what you should be seeing: Your rag_chat.py script is now irrelevant for this setup. That script was an independent RAG application that communicated with Oobabooga's API. Now, you are trying to use RAG within Oobabooga's web UI itself, powered by the superboogav2 extension. Oobabooga (with superboogav2 loaded) handles everything. When you run ./installer_files/env/bin/python server.py ..., that single Oobabooga process: Loads your Nous-Hermes-2 model. Loads the superboogav2 extension. The superboogav2 extension then, internally, connects to your user_data/chroma_db knowledge base. When you type a query in the Oobabooga web UI, superboogav2 intercepts it, performs the retrieval from chroma_db, augments the prompt, and sends it to the LLM. To confirm it's loading your docs and using RAG: Keep only the one WSL2 terminal open where you launched Oobabooga (./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf). Go to your web browser at http://127.0.0.1:7860. Navigate to the "Chat" tab. Ensure the "Include attachments/search results from previous messages in the chat prompt" box is checked (in the "Settings" column on the right). Type a question that you know has a direct answer in your knowledge_base (e.g., "my wifi drops frequently", "how to clear browser cache", "common printer issues"). Look at the AI's response in the UI. What you should expect to see in the UI: A relevant answer: The AI's response should directly address your question using information consistent with your knowledge_base documents. Source Citation (most likely): Many RAG extensions, including potentially superboogav2, will display the source documents or chunks that were used to generate the answer. This might appear as: A section below the AI's response titled "Sources," "Retrieved Documents," "Knowledge Base," or similar. Sometimes, it shows the content of the relevant .txt files. If the AI's answer is good and you see source documents, then RAG is working in your Oobabooga UI! Let me know what you observe when you try this in the UI.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
