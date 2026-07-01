---
category: homelab
date: 2026-02-03
id: 260799
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to configure Chromium to use DuckDuckGo as the default
  search engine, likely for privacy reasons.
tags:
- chromium
- duckduckgo
- search-engine
- browser-configuration
- privacy
---
# how to get chromium running with duck duck go

### USER
how to get chromium running with duck duck go

### GEMINI
If you’re moving to Chromium for privacy but still have it tethered to Google’s search engine, you’re only doing half the job. You’re essentially sitting in a secure room but leaving the window wide open for Google to watch everything you type into the address bar. Here is exactly how to stop playing small and switch your search engine to DuckDuckGo (DDG). The Direct Method: GUI Settings Most modern builds of Chromium already include DuckDuckGo as a pre-configured option. If it's there, don't overcomplicate it. Open Chromium and click the three dots (⋮) in the top right. Go to Settings > Search engine. Next to "Search engine used in the address bar," select DuckDuckGo from the dropdown menu. To be thorough, click Manage search engines and site search, find DuckDuckGo under "Shortcut," click the three dots next to it, and select Make default. The Manual Method: If DDG is Missing If your specific Chromium build (common in some Linux distros) doesn't have it listed, you have to stop waiting for it to appear and add it yourself. In Manage search engines and site search, click Add. Fill in the fields exactly as follows: Search engine: DuckDuckGo Shortcut: ddg (or whatever you prefer) URL with %s in place of query: https://duckduckgo.com/?q=%s Click Add, then find it in the list and select Make default. The Privacy Layer: Browser Extension Setting the search engine only protects your searches. It does nothing for the trackers on the sites you actually visit. If you’re serious about this shift, you should install the DuckDuckGo Privacy Essentials extension from the Chrome Web Store. It handles the search engine switch automatically and adds tracker blocking. The Hard Truth: Blind Spots The Sync Trap: If you sign into your Google account in Chromium to sync bookmarks or history, you are essentially nullifying a large portion of the privacy benefits of using Chromium and DDG. You’re handing your browsing metadata back to the entity you’re trying to avoid. DNS Leaks: Even with DDG, your ISP still knows which domains you visit unless you configure a private DNS or a VPN. What’s your next move? Would you like me to help you configure Chromium’s Privacy and Security settings to further minimize data leakage, or should we look at hardened Chromium forks like Ungoogled-Chromium?
