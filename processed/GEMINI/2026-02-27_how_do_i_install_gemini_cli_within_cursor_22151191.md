---
category: ai-tools
date: 2026-02-27
id: 232687
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to install the Gemini CLI within the Cursor IDE.
tags:
- gemini-cli
- cursor-ide
- installation
---
# how do i install gemini cli within cursor? 

### USER
how do i install gemini cli within cursor? 

### GEMINI
Installing the Gemini CLI (the official open-source AI agent from Google) inside Cursor is a two-part process: you install the core tool in the terminal and then link it to Cursor using the Gemini CLI Companion extension. 1. Install the Gemini CLI Open the integrated terminal in Cursor (Ctrl + ~ or Cmd + ` ) and run the following command. You must have Node.js (v18+) installed. npm install -g @google/gemini-cli 2. Authenticate Once installed, initialize the CLI to set up your credentials: Type gemini in your terminal. Follow the prompts to Login with Google (OAuth). This is the easiest method and provides a generous free tier (approx. 1,000 requests/day). Alternatively, if you have a specific API key from Google AI Studio, you can export it: Mac/Linux: export GEMINI_API_KEY="your_key_here" Windows: setx GEMINI_API_KEY "your_key_here" 3. Connect to Cursor (IDE Integration) To let the CLI "see" your active files and cursor position within the editor, you need the companion extension. Install the Extension: * Go to the Extensions view in Cursor (Ctrl+Shift+X). Search for "Gemini CLI Companion" (published by Google) and install it. Enable the Link: * In your Cursor terminal, while the Gemini CLI is running, type the following command: /ide enable Verify: * The CLI should now say 🟢 Connected to IDE. You can now ask questions like "Explain the code I have selected" or "Refactor the open file." Strategy & Blind Spots Since you asked for a "brutally honest" take: Why are you doing this? The Overlap: Cursor already has a world-class "Composer" and "Chat" (CMD+K / CMD+L) that uses Gemini 1.5 Pro/Flash. By installing the CLI, you are adding a second, terminal-based agent into an IDE that is already built to be an agent. The Opportunity Cost: Unless you specifically need the 1-million+ token context window or the MCP (Model Context Protocol) tools that the CLI offers for external data fetching, you might just be adding friction to your workflow. The Blind Spot: People often install "the next shiny tool" thinking it will solve their productivity issues. If your current bottleneck is "the AI isn't good enough," switching from Cursor's native Gemini integration to a CLI Gemini integration won't fix your logic. It just changes the UI. Action Plan: Identify the Gap: If you just want Gemini's brain, use Cursor's native "Models" settings and plug in your API key there. It’s cleaner. Use CLI for Scale: Only use the CLI version if you are analyzing a massive repo that exceeds Cursor's standard indexing or if you need to run terminal-based automation scripts. Would you like me to show you how to configure your Gemini API key directly in Cursor's native settings instead to avoid the CLI overhead?
