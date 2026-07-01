---
category: general
date: 2025-07-05
id: 094038
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan requested a TL;DR summary of the project with a list of major issues
  encountered along the way for documentation purposes.
tags:
- tldr-summary
- project-documentation
- issue-tracking
---
# make this in a tl;dr format and at the end list the major issues i had along the way 

### USER
make this in a tl;dr format and at the end list the major issues i had along the way 

### GEMINI
Got it. Here's the TL;DR summary and the major issues you tackled: TL;DR: Voice AI Helpdesk Setup & Optimization You built a voice-controlled AI helpdesk assistant running locally on your PC (via WSL2). It lets you speak your questions, then uses your own local documents and web search to find answers, and finally spits out the response in plain text. You spent a lot of time tweaking it to be as fast and accurate as possible. Major Issues Encountered: Slow Voice Output (TTS): Even when not playing sound, the AI was slow because the Text-to-Speech (TTS) extension was constantly making audio in the background. Fix: Completely disabled the TTS extension. Slow Answers (Initial RAG): Questions needing info (like "VPN setup") were super slow because the AI was trying to pull too much data from your local documents and the internet. Fix: Drastically cut down the "context" (extra info) the AI would grab from local documents and limit how much text it scraped from websites. Still Slow Answers (LLM Itself): Even with TTS and RAG turned off, the AI was still slow to reply. This meant the main AI model (the LLM) itself was too slow for your hardware. Fix: Switched to a smaller, more efficient AI model (Phi-3-mini) and made sure it used your graphics card (GPU) as much as possible for maximum speed. Missing Settings in UI: Sometimes, settings for the RAG extensions wouldn't show up in the web interface after enabling them. Fix: Required specific steps like restarting Oobabooga, ensuring extensions loaded before the main AI model, and doing hard browser refreshes.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
