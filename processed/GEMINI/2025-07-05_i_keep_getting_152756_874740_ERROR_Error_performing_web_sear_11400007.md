---
category: ai-tools
date: 2025-07-05
id: 549731
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was hitting DuckDuckGo rate limits (202 errors) when trying to use
  web RAG search functionality.
tags:
- web-rag
- duckduckgo-ratelimit
- 202-error
---
# i keep getting: 15:27:56-874740 ERROR    Error performing web search: https://html.duckduckgo.com/html 202 Ratelimit
15:27:56-875514 WARNING  No search results found
prompt processing progress, n_past = 832, n_tokens = 5, progress = 0.006010
prompt eval time =      40.21 ms /     5 tokens (    8.04 ms per token,   124.36 tokens per second)
       eval time =    9255.89 ms /   397 tokens (   23.31 ms per token,    42.89 tokens per second)
      total time =    9296.09 ms /   402 tokens
15:28:06-312295 INFO     Output generated in -52.07 seconds (-7.64 tokens/s, 398 tokens, context 832, seed 1332643647)
 

### USER
i keep getting: 15:27:56-874740 ERROR    Error performing web search: https://html.duckduckgo.com/html 202 Ratelimit
15:27:56-875514 WARNING  No search results found
prompt processing progress, n_past = 832, n_tokens = 5, progress = 0.006010
prompt eval time =      40.21 ms /     5 tokens (    8.04 ms per token,   124.36 tokens per second)
       eval time =    9255.89 ms /   397 tokens (   23.31 ms per token,    42.89 tokens per second)
      total time =    9296.09 ms /   402 tokens
15:28:06-312295 INFO     Output generated in -52.07 seconds (-7.64 tokens/s, 398 tokens, context 832, seed 1332643647)
 

### GEMINI
You're getting a 202 Ratelimit error from DuckDuckGo, which means you've hit the usage limit for their HTML search API from your IP address within a certain timeframe. Here's what that error means and how to address it: 202 Ratelimit from https://html.duckduckgo.com/html: This is a direct message from DuckDuckGo's server telling you that you've sent too many requests too quickly, and they're temporarily blocking you to prevent abuse of their service. WARNING No search results found: Because you're being rate-limited, DuckDuckGo isn't returning any search results to your web_rag extension. prompt processing progress... eval time... total time...: The LLM then continues to process the prompt without any web search results. The 9-second eval time for 397 tokens is the time your Phi-3-mini model took to process the prompt and generate its response, after waiting for the (failed) web search. Output generated in -52.07 seconds: This negative time is a bit odd, usually indicates a timing glitch or a very long wait that reset the clock. Ignore the negative number, the key is the eval time. Why this is happening: Frequent Searches: Your web_rag extension is likely performing web searches very frequently, possibly for every query, even if you adjusted its settings to retrieve fewer characters or pages. Rapid-Fire Queries: If you're sending multiple questions to the AI in quick succession, each potentially triggering a web search, you can hit the rate limit quickly. Shared IP: If you're on a network with many users (e.g., a university, large office, or even some ISPs), others on your network might also be making DuckDuckGo requests, contributing to the shared rate limit for your public IP address. How to Address the 202 Ratelimit Error: Reduce Web Search Frequency (Most Effective): Keep "Activate web search" in the chat UNCHECKED by default. Only check it manually when you absolutely need the AI to perform a web search for a specific question. This is the best way to control your usage. Temporarily disable web_rag extension entirely. If you don't need web search for a while, go to the "Extensions" tab and uncheck web_rag. Remember to save settings and restart. This completely stops web search attempts. Increase Delays (If web_rag is essential): The web_rag extension sometimes has an internal delay setting (though it might not be exposed in the UI or might be fixed for DuckDuckGo Lite). If there's an option for "delay between searches" or "rate limit delay," increasing it could help. (Check the web_rag configuration in Oobabooga's extensions/web_rag/script.py if you're comfortable with code, but there might not be a direct user setting for this with DuckDuckGo Lite). Wait it Out: Rate limits are usually temporary. DuckDuckGo will eventually unblock your IP after some time (could be minutes to hours, depending on their policy and your usage pattern). Consider an Alternative Search API (Advanced/Not Oobabooga Built-in): For a serious helpdesk AI that requires consistent web access, relying on a free, unauthenticated API like DuckDuckGo Lite can be problematic. Paid search APIs (e.g., Google Custom Search API, SerpApi, Brave Search API) offer higher rate limits, but require API keys and custom integration, which is a more advanced task outside Oobabooga's direct settings. For now, the easiest and most effective solution is to control when web_rag performs searches by keeping the "Activate web search" option in the chat unchecked unless explicitly needed, or by temporarily disabling the web_rag extension.
