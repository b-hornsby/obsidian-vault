---
id: 569812
source: GEMINI
date: 2025-06-25
tags: ['tool-integration', 'local-llm', 'workflow', 'wsl2']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan asked whether multiple tools were needed for his project or if everything could be done within a single UI.
---
# but for each thing i want do i need to use each tool or is it all within one ui i can use? 

### USER
but for each thing i want do i need to use each tool or is it all within one ui i can use? 

### GEMINI
No, it's not all within one UI you can use directly. Each of those advanced features (image generation, image-to-text, voice STT, voice TTS) typically requires a different tool and a different underlying model to do what you want to accomplish. Oobabooga's text-generation-webui is primarily designed for running and interacting with Large Language Models (LLMs) that handle text input and text output. For image generation, you would typically use a separate web UI like Automatic1111's Stable Diffusion WebUI. For image-to-text (multimodal input), you'd need a Large Multimodal Model (LMM), and how that integrates into a UI for input would depend on the specific LMM and its runners (Oobabooga does not currently support direct image input for its LLMs). For voice conversation (STT and TTS), you'd use separate libraries like Whisper and Coqui-AI TTS, which don't have their own interactive web UIs for this purpose but are usually integrated into custom Python scripts. To have them all work together as a cohesive "personal helpdesk assistant," you would generally need to write custom Python scripts to act as an "orchestration layer" that connects these different tools via their APIs or direct library calls. This script would be your "single UI" (or backend to a custom UI you build) that manages the flow between all these separate components.
