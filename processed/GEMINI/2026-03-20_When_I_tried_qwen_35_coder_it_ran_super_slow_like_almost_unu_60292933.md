---
category: ai-tools
date: 2026-03-20
id: 488447
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting that the Qwen 3.5 Coder model is running too slowly to
  be usable.
tags:
- qwen-3.5-coder
- llm-performance
- slow-inference
- code-generation
---
# When I tried qwen 3.5 coder it ran super slow like almost unusable for simple things

### USER
When I tried qwen 3.5 coder it ran super slow like almost unusable for simple things

### GEMINI
The reason Qwen 3.5 Coder 14B felt like a slideshow is simple math: it’s a dense model. At 14B parameters with a standard 4-bit quantization, it needs about 9-10GB of VRAM just to load, plus extra for your context (code files). Since your RTX 3070 only has 8GB, your system was forced to offload the remaining ~30% of the model to your DDR5 system RAM. System RAM is roughly 10-20x slower than VRAM. Every time the model "thinks," it has to wait for data to crawl across that bottleneck. For a "Claude-like" experience that actually feels snappy on your hardware, you need to change your strategy. The "No-Lag" Tier List for 8GB VRAM If you want speed (30+ tokens/sec) without sacrificing the logic needed for your DeFi bot, these are your real March 2026 options: 1. The Efficiency King: GLM-4.7 Flash (30B MoE) Why it works: Even though it's "30B," it’s a Mixture of Experts (MoE). It only activates ~3B parameters per token. Performance: It fits much more comfortably in your 8GB VRAM because the "active" parts are tiny. It will feel 5x faster than Qwen 14B. Best for: Fast edits, boilerplate, and general agent tasks. 2. The Native Fit: Qwen 3.5 Coder 7B (Instruct) Why it works: This is the "little brother" of the one you tried. It only needs ~5.5GB of VRAM. Performance: It will run entirely on your GPU at 50-70 tokens/sec. The Reality Check: It is smarter than the old 7B models, but it will struggle with complex architectural logic compared to Sonnet 4.6. Use this for single-file tasks. 3. The Speed Demon: Mistral Small 3 (7B) Why it works: Mistral optimized this specifically for low-VRAM "agentic" use. It is incredibly stable for tool-calling (e.g., searching your files or running terminal commands). Performance: Pure GPU speed. Zero lag. How to "Fix" the Speed (3 Practical Steps) If you absolutely must use a "Heavy" model like Qwen 14B because the 7B models are too "dumb," do this: Lower the Quantization: Don't use the default. Look for "IQ4_XS" or "Q3_K_L" versions. They sacrifice a tiny bit of "intelligence" to fit more of the model into your 8GB VRAM. Limit Context: In Ollama or LM Studio, set your context limit to 4096 or 8192. If you leave it at the default "32k," the KV cache will eat all your VRAM before the model even starts talking. Kill the Bloat: You're on CachyOS—make sure you aren't running a heavy Electron app (like Discord or a dozen Chrome tabs) in the background. On an 8GB card, every 500MB matters. The Bottom Line GLM-4.7 Flash is specifically designed for people in your exact situation: users who have "mid-tier" VRAM (8GB-12GB) but need "large model" reasoning. It uses the MoE trick to give you 14B-level brains at 3B-level speeds. Would you like the specific Ollama command to pull the highly-compressed version of GLM-4.7 Flash that is guaranteed to stay on your GPU?
