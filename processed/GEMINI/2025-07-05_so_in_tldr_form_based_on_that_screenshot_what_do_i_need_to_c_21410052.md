---
id: 837347
source: GEMINI
date: 2025-07-05
tags: ['troubleshooting', 'configuration', 'screenshot-analysis']
category: ai-tools
sentiment: stuck
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking for a concise explanation of what needs to be changed based on a provided screenshot, indicating he's stuck on a configuration issue.
---
# so in tl;dr form, based on that screenshot, what do i need to change? 

### USER
so in tl;dr form, based on that screenshot, what do i need to change? 

### GEMINI
In short, to speed up your AI's responses when using RAG (Retrieval-Augmented Generation), drastically reduce the amount of information it retrieves and processes from your local documents and the web. Changes to Make Here's a breakdown of the specific settings to adjust based on your screenshots: 1. Disable TTS (if not already done) Go to Extensions Tab. Uncheck coqui_tts. Why: Even if you weren't playing audio, coqui_tts still synthesizes it in the background, adding overhead. You want only STT for input and plain text for output to maximize speed. 2. Optimize Whisper STT Go to Whisper STT section (in settings). Whisper Model: Ensure this is set to base.en. Why: tiny.en is faster but often too inaccurate, leading to misunderstandings. base.en offers a better balance of speed and accuracy for practical use. Device: Confirm it's cuda. Submit the transcribed audio automatically: Keep this checked for seamless input. 3. Drastically Reduce RAG Context Lengths (This is the BIGGEST impact) For superboogav2 (Local Documents RAG): Go to superboogav2 settings tab. Context length: Change 250,800 to something very small, like 50, 50 or even 0, 0. Why: This controls how much extra text around a retrieved chunk is sent to the LLM. Reducing it significantly shortens the LLM's input, making it process much faster. For Web Retrieval-Augmented Generation (Web RAG): Go to Web RAG tab. Maximum characters of retrieved data to keep: Change 5000 to 500 or 1000. Why: This limits the amount of text scraped from web pages. Less text means faster processing. Number of pages to retrieve: Change 3 to 1 or 2. Why: Fewer pages mean less fetching and processing time. Final Step: Apply Changes After all changes, go to the "Extensions" tab. Click "Save settings to user_data/settings.yaml". Then click "Apply flags/extensions and restart". By making these changes, you're telling your AI to spend less time reading and processing supplementary information, which should significantly speed up its text-based responses after your voice input.
