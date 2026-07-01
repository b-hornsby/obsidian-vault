---
category: ai-tools
date: 2025-06-23
id: 534566
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
- second-brain-vault
- streaming-rig
- it-certification
- flappy-meme-bird
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: The user was trying to navigate an AI tool interface and expressed confusion
  about the available menu options, seeking help to understand the platform's features
  and capabilities.
tags:
- UI navigation
- interface confusion
- AI tool exploration
- feature discovery
- user onboarding
---
# all i see on the left is chat, notebook, parameters, character, model, training and session 

### USER
all i see on the left is chat, notebook, parameters, character, model, training and session 

### GEMINI
You're absolutely right, Bryan! My apologies. Based on your description, it appears your Oobabooga interface might be a slightly different version or configuration than the one I'm most familiar with that has a dedicated "Extensions" tab in the main left sidebar. The screenshot you previously shared (Screenshot 2025-06-23 163804.png) shows you were in the right area, just under the "Settings" menu item. That's where you see "Extensions & flags" and "Available extensions." So, let's work with what you see there! Re-attempting RAG Extension Setup (Using Your UI Layout) Go back to the "Settings" tab: Click on "Settings" in the left-hand navigation. This will bring you to the "Extensions & flags" page you previously screenshotted. Look for RAG-related extensions under "Available extensions": In that list, look for names that suggest knowledge base, documents, or RAG. From your screenshot, I see superbooga and superboogav2. Sometimes, these more comprehensive extensions include RAG capabilities within them, or they are prerequisites. You might also see document_loader or rag_agent, but based on your screenshot, those aren't directly visible. Enable the most promising RAG extension: If superbooga or superboogav2 sounds like it might include RAG (they often do, as general utility extensions), click the checkbox next to one of them to enable it. If you see any other extension that explicitly says "rag" or "document" that wasn't visible in the screenshot, enable that one. Apply Changes and Restart (if prompted): After enabling, there should be a button near the top of the "Settings" page that says "Apply flags/extensions and restart" or just "Restart." Click this. Your WSL2 terminal will show Oobabooga shutting down and restarting. Wait for the browser UI to refresh and the model to reload. Check for Configuration Options (This is the tricky part without a dedicated tab): If a RAG extension was successfully enabled, how do you configure it? Option A (Most likely if no dedicated "Extensions" tab): Sometimes, after enabling an extension this way, its configuration options will appear under a new section in the "Chat" tab's right-hand panel, or sometimes even in the "Parameters" tab. Go back to the "Chat" tab and scroll down the right panel to see if any new options (like "Data directory," "Load Documents," etc.) have appeared. Option B (Less common for RAG but possible): A separate dedicated "Configure" button might appear somewhere else on the Settings page after enabling, but this is less intuitive. If you enable superbooga or superboogav2, go back to the "Chat" tab, and then scroll down the right-hand panel. Look for any new sections or options that mention "SuperBooga," "RAG," "Knowledge Base," or "Document Loading." This is where you would typically point it to your data_sources folder and trigger the ingestion. Let me know what you find after enabling a potential RAG extension and restarting!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]