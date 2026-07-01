---
category: ai-tools
date: 2026-03-20
id: 703353
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked for confirmation that they were using the correct local LLM model
  for their setup.
tags:
- local-llm
- model-confirmation
- claude-code
- qwen
---
# So I’m using the correct model?

### USER
So I’m using the correct model?

### GEMINI
Yes, for your specific hardware and goals, you are likely using the best possible compromise currently available in 2026. Since you're on an RTX 3070 (8GB), you are constantly fighting a "VRAM war." Here is why GLM-4.7 Flash is the right choice for your "Claude failover" compared to the others you've tried: 1. Why Qwen 14B Failed You When you tried Qwen 3.5 Coder 14B, you hit the "System RAM Wall." At 14 billion parameters, that model needs ~10GB of VRAM just to exist. Your card only has 8GB, so your PC offloaded the rest to your DDR5 RAM. Even though DDR5 is fast, it's a bottleneck that makes the model feel like it's "stuttering" or "thinking" in slow motion. 2. Why GLM-4.7 Flash is the "Sweet Spot" GLM-4.7 Flash uses a Mixture of Experts (MoE) architecture (specifically 30B-A3B). The Brains: It has the "knowledge" of a 30B model. The Speed: It only "wakes up" about 3 billion parameters to answer any single prompt. The Result: It fits much more comfortably in your 8GB of VRAM and runs at a "snappy" speed while maintaining significantly higher reasoning than a standard 7B or 8B model. 3. How it Compares to Sonnet 4.6 Let’s be real: Nothing local on an 8GB card is going to 1:1 match Claude 4.6 Sonnet. Claude: Exceptional at "multi-file planning" and "reasoning-before-acting." GLM-4.7 Flash: It is known as a "Haiku-tier" model. It’s a "speed-first" agent. It will be great at tool-calling and writing single-file scripts for your DeFi bot, but it might get "lazy" if you ask it to refactor ten files at once. Pro-Tip for Your Setup (CachyOS/Ollama) To make sure you are getting the absolute maximum out of that 3070, ensure you are using a high-compression quantization (like IQ4_XS or Q4_K_S). This keeps the "KV Cache" (the model's memory of your code) inside the VRAM longer so it doesn't slow down as the conversation gets longer. The Verdict: Stick with GLM-4.7 Flash for your daily "fast" local tasks. If you ever have a truly complex logic bug that GLM can't solve, then switch to the slow Qwen 14B and grab a coffee while it thinks—but for 90% of your "Claude is down" moments, you're on the right horse. Would you like the specific configuration to set up a "Deep Thinking" mode for GLM so it mimics Claude's reasoning a bit better?
