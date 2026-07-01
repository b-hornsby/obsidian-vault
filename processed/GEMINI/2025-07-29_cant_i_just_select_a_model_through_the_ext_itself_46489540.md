---
category: ai-tools
date: 2025-07-29
id: 991205
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is asking if he can select a model directly through an extension interface.
tags:
- ollama
- model-selection
- extension
- cursor-alternative
---
# can't i just select a model through the ext itself? 

### USER
can't i just select a model through the ext itself? 

### GEMINI
You're asking a very good and logical question: "Can't I just select a model through the extension itself?" The ideal answer is: Yes, absolutely! That's exactly how it's designed to work. However, in your specific situation, the problem is that the continue.dev extension itself isn't fully loading or initializing correctly. When the extension is working as intended, its sidebar (the AI icon) should have a "Select model" dropdown that automatically populates with models it finds from providers like Ollama (based on your config.yaml). The reason we've gone through all these troubleshooting steps (checking config.yaml, ensuring ollama serve is running, disabling startup apps, deep cleaning VS Code data, checking Extension Host logs) is because: Your "Select model" dropdown currently says "No models configured" (as seen in image_9a35b4.png and image_98e07e.png). The "Continue" output channel is not even appearing in the Output dropdown. This is the critical symptom indicating the extension isn't fully operational. So, yes, normally you would just select the model in the extension's sidebar. But because the extension isn't loading properly, it can't see your config.yaml or connect to Ollama to populate that list. It's stuck at a very early stage of initialization. Unfortunately, at this point, if you're not willing to try VS Code Insiders, and given that all standard troubleshooting has failed to get the "Continue" output channel to appear, your best bet for a resolution is to file a detailed bug report on the continue.dev GitHub page. They can review your environment details and logs to determine why their extension isn't fully initializing on your specific system, preventing it from showing any models or its own logs.
