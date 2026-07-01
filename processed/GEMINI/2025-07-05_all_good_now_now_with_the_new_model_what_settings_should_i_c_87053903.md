---
category: ai-tools
date: 2025-07-05
id: 751
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking for optimal extension settings to improve response speed
  and accuracy with a new model in text-generation-webui.
tags:
- model-optimization
- extension-settings
- speed-accuracy
---
# all good now. now with the new model, what settings should i change within those extensions to allow for the best possible responses both in speed and accuracy?

### USER
all good now. now with the new model, what settings should i change within those extensions to allow for the best possible responses both in speed and accuracy?

### GEMINI
Okay, now that you have the faster Phi-3-mini model loaded and your RAG extensions are visible again, the goal is to find the sweet spot for RAG settings that allows for the best possible balance of speed (avoiding long waits for RAG to gather context) and accuracy (providing enough relevant information for the LLM). Remember, RAG will always add some latency, but with a faster LLM, we can afford to give it a bit more context without making it excessively slow. Here are the recommended settings to adjust within superboogav2 and web_rag based on your screenshots, focusing on optimizing for Phi-3-mini: 1. SuperboogaV2 Settings (Local Documents RAG) This controls how much context from your local documents is fed to the LLM. Chunk length: Keep as is: 500,500,1000,700. Reasoning: These values define how your source documents are initially broken down. They are generally fine for indexing purposes and don't directly impact the speed of the LLM's response as much as the next setting. Context length: Change 250,800 to 100,200. Reasoning: This is the most crucial setting here. It dictates how many characters before and after a retrieved chunk are added to the LLM's prompt. 250,800 (1050 characters per chunk) is quite large and can quickly make the LLM's prompt very long if multiple chunks are retrieved, slowing down your Phi-3-mini. 100,200 (300 characters per chunk) provides a good balance. It gives enough surrounding context for the LLM to understand the chunk's relevance, without overwhelming the smaller Phi-3-mini's context window or adding excessive prompt processing time. 2. Web Retrieval-Augmented Generation Settings (Web RAG) This controls how much context is retrieved from web searches. Maximum characters of retrieved data to keep: Change 5000 to 1000 or 1500. Reasoning: 5000 characters is a very large amount of text to scrape from a web page and then feed to any LLM, especially a 3B model like Phi-3-mini. 1000-1500 characters is usually sufficient to get the most relevant information from a web page for a summary or to answer a direct question, without causing a massive slowdown. Number of pages to retrieve: Change 3 to 1 or 2. Reasoning: Retrieving 3 pages adds significant network latency and processing time for scraping. For most helpdesk queries, the first 1 or 2 relevant search results are often sufficient to get the core information. 3. Whisper STT Settings (Input) These were discussed previously, but just confirm for optimal input speed: Whisper Model: base.en. Reasoning: Provides the best balance of speed and accuracy. tiny.en is faster but often leads to too many misunderstandings. Device: cuda. Submit the transcribed audio automatically: Checked. 4. TTS Settings (Output) Activate TTS: UNCHECKED. Reasoning: As established, any TTS activity (even background synthesis) adds latency to the text response. Keep this off for the fastest text output. Final Steps to Apply Changes: After making all these adjustments in the respective tabs. Go to the "Extensions" tab. Click "Save settings to user_data/settings.yaml". Click "Apply flags/extensions and restart". Now, test with queries like "My PC keeps crashing..." or "Walk me through setting up a VPN." You should find a much better balance of speed and informed responses from your Phi-3-mini model, as you're giving it relevant context without overloading it.
