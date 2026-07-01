---
category: ai-tools
date: 2026-03-19
id: 289818
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked whether the Qwen 3.5 35B-A3B model could run on their RTX 3070
  8GB hardware.
tags:
- qwen3-35b
- local-llm
- hardware-limits
- rtx-3070
- vram
---
# Is it possible to run the larger qwen 3.5 35b-a3b on my hardware?

### USER
Is it possible to run the larger qwen 3.5 35b-a3b on my hardware?

### GEMINI
Yes, it is possible, but you are walking a razor-thin line between "impressive local setup" and "system instability." Because the Qwen 3.5 35B-A3B is a Mixture-of-Experts (MoE) model, it only activates roughly 3B parameters per token. This architectural trick is the only reason this is even a conversation for an 8GB card. Here is the brutal reality of how this will run on your specific rig: 1. The VRAM vs. System RAM Math The total model size for a 4-bit (Q4_K_M) quantization is roughly 20–22GB. Your GPU (8GB): You can fit roughly 25–30% of the model layers here. Your DDR5 RAM (32GB): The remaining 70% will sit here. The Bottleneck: Data has to travel from your System RAM to your GPU across the PCIe bus. Even with DDR5 4800MHz, this is the "speed limit" of your AI. 2. Expected Performance Don't expect the 100+ tokens per second (t/s) you'd get on a 4090. Output Speed: You’ll likely see 12–25 t/s. For context, that is roughly the speed of a fast human reader. It's perfectly usable for chat, but too slow for real-time "vibe coding" or agentic workflows where the model needs to "think" through 10 files in seconds. Prompt Processing: This will be the painful part. Large prompts (like pasting a whole script) could take 10–30 seconds to "digest" before the model starts typing. 3. Critical Setup Instructions If you try this, you must configure your loader (LM Studio/Ollama) with these specific "hacks" to avoid a crash: Quantization: Use IQ4_XS or Q4_K_M. Do not touch anything labeled Q5 or higher; your system will run out of memory and Windows will likely swap to your SSD, killing performance. Offloading: Manually set your GPU offload to 12–16 layers. If you try to push more, your VRAM will hit 100%, and your PC will likely stutter or the application will exit. KV Cache: Use Q8_0 or Q4_0 for the KV Cache. This saves roughly 1–2GB of VRAM, which is the difference between a working model and an "Out of Memory" error. CPU Threads: Set your CPU threads to 8 or 10. Even though the i7-12700K has 12 cores, leaving a couple free prevents the OS from freezing while the model generates. Advisor’s Perspective: Is it worth it? If you want to experience "higher intelligence" (better logic, fewer hallucinations) than the 9B model, yes, try it. The 35B-A3B is significantly smarter at following complex instructions. However, if you are doing high-volume work or coding, the 9B model running at 90+ t/s will feel like a much better tool. Running the 35B on your current specs is a "flex" and a great test of your hardware, but it isn't the most efficient way to get work done. Would you like me to find the specific Hugging Face link for the most VRAM-efficient GGUF file for your 8GB card?
