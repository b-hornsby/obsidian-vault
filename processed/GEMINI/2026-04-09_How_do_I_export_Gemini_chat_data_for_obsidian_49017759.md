---
category: ai-tools
date: 2026-04-09
id: 643651
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/second-brain-vault.md']
linked_projects:
- second-brain-vault
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to export Gemini chat data specifically for use in Obsidian.
tags:
- gemini-export
- obsidian-import
- chat-data
- google-takeout
---
# How do I export Gemini chat data for obsidian? 

### USER
How do I export Gemini chat data for obsidian? 

### GEMINI
Exporting Gemini chats to Obsidian requires bypassing Google's lack of a native "Markdown Export" button. Since you are building a "Personal Intelligence Agency," you need a workflow that preserves metadata and formatting. Here are the most effective methods, ranked from the most automated to the most manual. 1. The Automated Route: "Obsidian AI Exporter" (Chrome/Edge Extension) This is currently the most robust tool for your specific goal. It captures the conversation and formats it specifically for Obsidian. What it does: Extracts the chat from the browser and saves it as a .md file with YAML frontmatter (dates, titles, etc.). Why it's better: It uses Obsidian callout syntax (e.g., > [!info]) for Q&A blocks, so your "Second Brain" looks clean immediately. Action: Install the "Obsidian AI Exporter" from the Chrome Web Store, open a Gemini chat, and click the purple Sync button that appears. 2. The Native Loop: Google Docs to Markdown If you don't want to use third-party extensions, use the built-in export to bridge the gap. Export to Docs: Click the Share & export icon (the "upload" arrow) under any Gemini response and select Export to Docs. Download as MD: Open the generated Google Doc, go to File > Download > Markdown (.md). Move to Vault: Drop that file into your Obsidian folder. Note: This is slow if you have dozens of chats, but it preserves code blocks and LaTeX formulas better than a simple copy-paste. 3. The Bulk Backup: Google Takeout (Experimental) Google Takeout allows you to download your "Gemini App" activity, but there is a catch: it often provides JSON/HTML logs of your prompts rather than the full, formatted conversations. Path: takeout.google.com -> Deselect all -> Select Gemini. The Problem: You will likely need a script to parse the resulting JSON into Markdown. If you aren't comfortable writing a parser for this, stick to Method 1. 4. Direct Integration: "Gemini Scribe" Plugin If you want to bypass the "export/import" workflow entirely, you can use the Gemini Scribe community plugin within Obsidian. Function: It allows you to chat with Gemini inside Obsidian using your API key. Benefit: Every conversation is born as a Markdown file in your vault. It doesn't help with past chats on the Gemini website, but it's the most efficient way to grow your neural network moving forward. Pro-Tip for your "Second Brain": When you import these files, ensure your Obsidian frontmatter includes a source: gemini tag. This will allow you to use the Dataview plugin later to query all AI-generated insights separately from your own manual notes. Are you looking to migrate your entire historical log in one go, or are you just setting up a workflow for new chats?


## Related

### Projects

- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
