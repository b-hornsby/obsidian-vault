---
category: ai-tools
date: 2025-07-05
id: 256498
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking about the 'activate web search' tab feature in the oobabooga
  chat interface.
tags:
- web-search
- webui
- oobabooga
- RAG
---
# what is the activate web search tab in the chat?

### USER
what is the activate web search tab in the chat?

### GEMINI
The "Activate web search" tab in the chat refers to a checkbox or toggle that appears directly within the "Chat" interface of Oobabooga's text-generation-webui, specifically when the web_rag extension is enabled. When web_rag is active, this "Activate web search" option gives you a quick way to turn the web search functionality on or off for individual interactions or sessions, without having to go back to the "Extensions" tab and restart the server every time. Here's its purpose: Conditional Web Search: You might want the AI to answer most questions from its own knowledge or your local documents, but only perform a web search for specific queries where current or external information is needed (e.g., "What's the weather today in Tokyo?" or "Explain the latest discovery in quantum physics."). Faster Non-Web Queries: If you know a question doesn't require web access, you can uncheck this box to prevent the AI from initiating a web search, saving you the latency associated with web retrieval and processing. User Control: It provides direct user control over a core RAG feature right where the conversation is happening. In essence, the "Activate web search" tab (or checkbox/toggle) allows you to quickly enable or disable the web_rag functionality on the fly during your chat session, giving you more granular control over when the AI performs web searches.
