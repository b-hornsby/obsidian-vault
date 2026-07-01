---
category: ai-tools
date: 2025-07-05
id: 251433
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that the LLM is providing outdated information when asked
  about the population of Tokyo, indicating a problem with the web search or RAG component.
tags:
- local-llm
- rag-accuracy
- web-search
- tokyo-population
---
# when i asked it web, What is the current population of Tokyo? it gave me stats from 2020

### USER
when i asked it web, What is the current population of Tokyo? it gave me stats from 2020

### GEMINI
That's an important observation! If you asked "web, What is the current population of Tokyo?" and received data from 2020, it indicates that the web_rag extension successfully performed a web search and retrieved information, but the source it found was outdated. Here's why this can happen with web RAG and what it means: Search Engine Indexing: DuckDuckGo Lite (the default search engine web_rag uses) provides results based on its index. While search engines try to be current, not all pages are updated instantly, and search results might prioritize well-established, but potentially older, sources that rank highly for a given query. Scraping Limitations: The web_rag extension is designed to scrape the visible text from a web page. If the top search result for "current population of Tokyo" prominently displayed 2020 data, that's what it would retrieve. It doesn't necessarily interpret the freshness of the data. No Guarantee of Real-time Data: Web RAG, while powerful, doesn't guarantee real-time, minute-by-minute updates unless the query specifically targets a live data source (which is rare for general population statistics). It retrieves what's readily available and indexed on the web pages it accesses. What this means for your setup: web_rag is working as intended: The fact that it retrieved any population stats (even if outdated) confirms that the web search, retrieval, and context injection parts of web_rag are functioning correctly. It's a limitation of the data source, not the RAG system: The challenge here isn't with web_rag itself, but with the search results it obtained. For constantly changing data like "current population," a precise real-time figure might be hard to get from a general web search without hitting a very specific, frequently updated data source. To potentially get more current information (using web_rag): You could try to refine your query to guide the search engine to more recent data, though there's no guarantee: "web, Tokyo population 2024" (or current year) "web, Latest Tokyo population statistics" "web, How many people live in Tokyo right now?" For truly real-time or frequently updated data, dedicated APIs or specific news sources are often more reliable than general web scraping. However, for a general web RAG solution, web_rag is doing its job by pulling relevant (even if slightly aged) information from the web.
