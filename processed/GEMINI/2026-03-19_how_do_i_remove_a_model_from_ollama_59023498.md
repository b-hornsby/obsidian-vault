---
category: ai-tools
date: 2026-03-19
id: 437962
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked how to remove a model from Ollama's local storage.
tags:
- ollama
- model-management
- remove-model
---
# how do i remove a model from ollama

### USER
how do i remove a model from ollama

### GEMINI
To remove a model from Ollama, you use the rm command. 1. The Command Open your terminal in CachyOS and run: ollama rm qwen3-coder (Replace qwen3-coder with the exact name of the model you want to delete.) 2. Verify Cleanup To ensure the space has been reclaimed on your 970 Evo Plus SSD, list your remaining models: ollama list 3. Direct Advice (Advisor Mode) You are likely deleting a model because it performed poorly or maxed out your 8GB VRAM. The Trap: Don't just delete and give up. If a model was too slow, it was likely because it was too large for your RTX 3070 and spilled into your DDR5 RAM. The Strategy: Before you download another massive model, check the file size. On an 8GB card, you want the total model size to be under 6GB to leave room for the context window (KV Cache) and your CachyOS desktop environment. If you're hunting for a replacement for Claude Code, try pulling a smaller quantization specifically: ollama pull qwen3-coder:7b-instruct-q4_K_M. The Opportunity Cost: Every gigabyte you waste on a model that "chokes" your GPU is a gigabyte that could be used for a faster, smaller model that actually helps you finish Operation Immortal Agent. Would you like me to recommend a specific "lightweight" model that fits perfectly within your 8GB VRAM limit?
