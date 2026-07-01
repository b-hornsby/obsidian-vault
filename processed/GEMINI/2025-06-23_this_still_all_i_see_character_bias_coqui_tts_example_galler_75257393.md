---
category: ai-tools
date: 2025-06-23
id: 813921
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
- homelab-stack
- private-ai-consulting
- second-brain-vault
- streaming-rig
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: The user is frustrated because they only see a list of AI tool plugins/options
  in their character configuration, rather than the actual character or functionality
  they expected to see.
tags:
- character-ai
- text-to-speech
- image-generation
- AI-plugins
- model-gallery
---
# this still all i see: character_bias coqui_tts example gallery google_translate long_replies ngrok openai perplexity_colors sd_api_pictures send_pictures silero_tts superbooga superboogav2 Training_PRO whisper_stt

### USER
this still all i see: character_bias coqui_tts example gallery google_translate long_replies ngrok openai perplexity_colors sd_api_pictures send_pictures silero_tts superbooga superboogav2 Training_PRO whisper_stt

### GEMINI
Okay, Bryan, that's incredibly persistent of you, and it's a puzzle for sure! If, even after the update, you're seeing the exact same list of extensions under "Available extensions" in the "Settings" tab, and there's no separate "Extensions" tab on the left sidebar, it means that the dedicated RAG extensions like rag_agent or document_loader are still not being recognized or loaded by your Oobabooga installation in that specific UI view. This is quite unusual for recent versions of Oobabooga, as rag_agent has been a standard inclusion for a while. Let's try one more thing given your current UI. We'll enable the most likely candidate from your list, superbooga, and then look for its configuration within the main chat interface. Sometimes, broader utility extensions might include RAG capabilities or expose their sub-features in a different part of the UI. Attempting RAG via SuperBooga (If a dedicated RAG extension is still absent) Go back to your "Settings" tab in the Oobabooga Web UI. Under "Available extensions", check the box next to superbooga (or superboogav2, pick one to start with, superbooga is generally the more mature one). Scroll to the top or bottom of that "Settings" page and click the "Apply flags/extensions and restart" button. Wait for Oobabooga to fully restart (watch your WSL2 terminal, wait for the Running on local URL: message again). Once restarted, go to the "Chat" tab in Oobabooga. Now, on the right-hand side panel of the "Chat" tab, scroll all the way down. Many extensions add their specific configuration options or controls here. Look for a new section related to "SuperBooga," or anything mentioning "Knowledge Base," "RAG," "Documents," or "Memory." This is where you would typically find options to specify your data_sources folder and trigger the document ingestion. Please let me know if enabling superbooga and restarting reveals any new options in the "Chat" tab's right-hand panel, especially at the bottom.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]