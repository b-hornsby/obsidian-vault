---
id: 161963
source: GPT
date: 2025-11-25
tags: ['claude-code', 'plan-limits', 'cursor-free-tier', 'feature-restrictions']
category: coding
sentiment: curious
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan wanted to know what features would be unavailable if he used the $20/mo Claude Code plan with Cursor's free tier.
---
# Claude code plan limits

### ASSISTANT
Good question. There’s no public doc that says *exactly* “these features are blocked if you use Claude Code via Cursor + the $20/mo Claude Code (Pro) plan,” but based on how the pricing, rate limits, and architecture work, there are practical limitations / trade-offs. Here’s what you **won’t be able to do (or will be limited)**, or things you should be careful about — plus what *you still can do*. (If you tell me exactly how you plan to use it [e.g., big projects, small scripts, lots of parallel tasks], I can tailor this more.)

## What **You Still Can Do / What Works Well**

- You can **use Claude Code for real development work** — refactoring, writing functions, debugging, planning — just within the usage limits.  
- Using Claude via Cursor gives you the familiar IDE environment + inline completions, while using your own Claude API key gives more efficient usage (less markup).  
- You can work around context limits by using *plan-mode*, breaking tasks into smaller steps, summarizing, or manually compacting.  
- For moderate-sized projects, the 200K token window may be more than enough, especially if you’re careful about how you present the code to Claude.

If you like, I can run a **cost + usage simulation** for the $20 plan *vs* higher Claude plans *vs* Cursor Ultra*, based on a few typical dev workflows (e.g. 2-hour sprint, all-day coding, background agents) — do you want me to do that?

### USER
What features can I not use if I get Claude code 20/mo plan and plug that into cursor free plan?