---
category: ai-tools
date: 2025-07-05
id: 429193
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking for the best possible web RAG settings for his helpdesk
  AI use case.
tags:
- web-rag-settings
- optimization
- best-configuration
---
# if i want the absolute best settings for this use case what would i use for web RAG]

### USER
if i want the absolute best settings for this use case what would i use for web RAG]

### GEMINI
You're aiming for the best possible web RAG for your use case, which likely means accurate and comprehensive retrieval. Looking at the web_rag settings, here's how to optimize them: Recommended Web RAG Settings for Best Performance "Activate Web RAG": Ensure this box is checked at the top of the "Web Retrieval-Augmented Generation" tab. Mode: AUTO (Default): AUTO: This is generally the best for a conversational RAG system, as it automatically performs a web search based on your question. Keep the default key text "web," unless you have a specific reason to change it. DIRECT: Useful if you know the exact URL you want the AI to process. You would type "get http://example.com". For general questions, AUTO is superior. URL Template: https://lite.duckduckgo.com/lite/?q=%q: Keep this as the default. DuckDuckGo Lite is simple, fast, and often easier for automated scraping compared to more complex search engine pages. Start/End Markers: "Start: Retrieved data capture starts after this text is found (starts at beginning if not found)": Leave this as [ Next Page > ]. This is a common element on DuckDuckGo Lite search results pages, helping the scraper skip navigation elements and get to the core results. "End: Retrieved data capture ends when this text is found (overrides maximum characters if found)": Leave this as 6.. This likely corresponds to the end of a block of initial search results on DuckDuckGo Lite. Maximum characters of retrieved data to keep (if end text not found): 5000: This is a good starting point. It means the system will retrieve up to 5000 characters (roughly 1000 words) from the web page's relevant section. Optimization: If you find the AI's answers are too short or lack detail for complex web-based questions, you could try increasing this value slightly (e.g., to 7500 or 10000). However, remember that more characters mean a longer prompt sent to your LLM, which consumes more context window space and can slow down generation. Test this incrementally. Other Considerations for Best Web RAG Internet Connection: A stable and fast internet connection is crucial for efficient web scraping. LLM Context Window: Ensure your chosen LLM (Nous-Hermes-2) has a sufficiently large context window to handle both your original prompt and the retrieved web content. The "5000 characters" from web RAG, plus the retrieved chunks from superboogav2, plus your prompt, all add up. Prompting: When using AUTO mode, phrase your question clearly and directly, similar to how you'd type it into a search engine. By sticking to the default settings for URL template and start/end markers, and intelligently adjusting the maximum characters, you'll be using web_rag effectively for its intended purpose.
