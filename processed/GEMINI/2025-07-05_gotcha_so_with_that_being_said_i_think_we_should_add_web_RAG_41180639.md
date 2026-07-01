---
category: ai-tools
date: 2025-07-05
id: 407310
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wanted to add web RAG capability to the helpdesk AI system in addition
  to the local knowledge base.
tags:
- web-rag
- superboogav2
- knowledge-base-expansion
---
# gotcha. so with that being said i think we should add web RAG as well if possible

### USER
gotcha. so with that being said i think we should add web RAG as well if possible

### GEMINI
To add web RAG capabilities to your Oobabooga setup, we'll need to explore a dedicated extension for it. There is indeed an extension called web_rag that performs Retrieval-Augmented Generation from web content. Just like we did with superboogav2, let's first check if the web_rag extension is already present in your Oobabooga installation. Go to your Oobabooga extensions directory in WSL2: cd ~/text-generation-webui/extensions List the contents of the directory to see if a web_rag folder exists: ls -l Please provide the output of the ls -l command. This will tell us if the folder is there. Once confirmed, I'll give you the specific commands to install its requirements (if needed) and then guide you through enabling and configuring it in the Oobabooga web UI.
