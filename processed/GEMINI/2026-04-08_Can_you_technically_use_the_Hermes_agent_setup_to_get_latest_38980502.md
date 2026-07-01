---
category: ai-tools
date: 2026-04-08
id: 171949
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked if the Hermes agent setup could be used to compile a daily Twitter
  news dashboard each morning.
tags:
- hermes-agent
- twitter-news
- morning-dashboard
- news-aggregation
---
# Can you technically use the Hermes agent setup to get latest Twitter news I may miss and have it compile a sort of dashboard I can look at every morning when I wake up?

### USER
Can you technically use the Hermes agent setup to get latest Twitter news I may miss and have it compile a sort of dashboard I can look at every morning when I wake up?

### GEMINI
This is exactly where the Hermes + Obsidian stack becomes a superpower. You aren't just building a "news reader"; you're building a Personal Intelligence Agency. In the 2026 ecosystem, this is a standard Multi-MCP Workflow. You don't need to write a single line of scraper code. You just need to connect the right "Hands" to Hermes. The "Morning Brief" Stack To make this work, you add two specific MCPs to your Docker/Hermes setup: The X (Twitter) MCP: X launched an official MCP server in early 2026. It allows agents to natively read_tweets and query_profiles. It’s pay-as-you-go (about $0.005 per tweet), which is perfect for your $300 "Immortal" budget. The Obsidian MCP: This allows Hermes to write directly into your vault. How to build the "Dashboard Skill" You create a new Skill Node in your vault: Vault/Skills/Intelligence/Morning_Brief.md. 1. The Strategy (The "Skill" Logic) In this file, you tell Hermes exactly what "latest news" means to you: Objective: Compile a high-signal dashboard of Solana DeFi and AI Agent news. Sources: Search for tweets from @hey_madni, @MeteoraAG, @JupiterExchange, and keywords like "DLMM strategy" or "Hermes Agent update." Filtering: Ignore engagement farming. Only include tweets with technical updates, TVL shifts, or new MCP releases. Output: Format as a Markdown table in Vault/Dashboards/2026-04-07_Brief.md. 2. The Execution (The Hermes Workflow) Every morning (you can trigger this with a simple cron job or a "Good morning" prompt), Hermes does the following: Scans X: Uses the X MCP to pull the last 12 hours of data from your specified accounts. Analyzes: Hermes filters the "noise" (memes/hype) and keeps the "signal" (alpha/updates). Composes: He writes a beautiful dashboard in your Obsidian vault. Links: He cross-references the news with your Operation Immortal fund. "Note: Meteora just updated their dynamic fees; I may need to adjust our Sniper Fund logic." Why this is better than a regular Dashboard It's Interactive: You don't just look at the dashboard. You can ask Hermes, "That tweet about the Jupiter LST—does that affect our Kamino Multiply position?" It's Self-Cleaning: Since it's in Obsidian, Hermes can archive old news and keep your "Active Alpha" folder lean. It's "Immortal" Ready: If you find a new yield strategy on Twitter, Hermes can automatically draft a new Skill Node for it and ask for your approval to deploy it. The "Hype" Setup (Docker Version) Since you’re using Docker, you just add the X API key to your .env and register the x-mcp server. Does this sound like the missing piece for your "Second Me"? Having an agent that manages your money and filters the world’s noise into a private briefing every morning? If you're ready, we can draft the "Signal Filter" rules for your Morning Brief skill so Hermes knows exactly what you consider "important."


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
