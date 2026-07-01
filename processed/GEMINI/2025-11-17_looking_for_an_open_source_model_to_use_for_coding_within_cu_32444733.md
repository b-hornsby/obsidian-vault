---
category: ai-tools
date: 2025-11-17
id: 081587
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is looking for the best open-source LLM for coding within Cursor, using
  Ollama and ngrok, that provides production-ready code comparable to Claude Sonnet
  4.5, given his hardware specs.
tags:
- open-source-llm
- ai-coding
- cursor-ide
- ollama
- ngrok
- production-ready-code
---
# looking for an open source model to use for coding within cursor using ollama and ngrok to do so. given my current specs, give me the absolute best model i should use that gives me production ready level code similar to what claude sonnet 4.5 provides. these are those given specs: Cpu: Intel Core i7-12700K

Motherboard: Asus Prime Z790-P
 
Cpu cooler: Noctua NH-U12S

Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40

Storage: 970 Evo Plus M.2 SSD 2TB

Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGB

Case: Corsair 4000D Airflow

PSU: Corsair CX750M

OS: Windows 11

### USER
looking for an open source model to use for coding within cursor using ollama and ngrok to do so. given my current specs, give me the absolute best model i should use that gives me production ready level code similar to what claude sonnet 4.5 provides. these are those given specs: Cpu: Intel Core i7-12700K

Motherboard: Asus Prime Z790-P
 
Cpu cooler: Noctua NH-U12S

Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40

Storage: 970 Evo Plus M.2 SSD 2TB

Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGB

Case: Corsair 4000D Airflow

PSU: Corsair CX750M

OS: Windows 11

### GEMINI
The absolute best open-source model for your specs that aims for a production-ready code level similar to Claude Sonnet 4.5 is the Qwen3-Coder-30B (4-bit Quantization). 💻 Model Recommendation: Qwen3-Coder-30B Based on your system specifications—specifically your 8GB VRAM RTX 3070 and 32GB DDR5 RAM—a large, highly performant coding model that can leverage both your GPU and CPU is required. Model: Qwen3-Coder-30B Quantization: 4-bit (e.g., Q4_K_M or IQ4_XS GGUF) Reasoning: This model is part of a family that has shown excellent performance in coding benchmarks, even rivaling state-of-the-art closed models. Benchmarks and user reports indicate that the 30B parameter size, specifically the 4-bit quantized version, is a highly viable option for systems with 32GB of RAM. It is explicitly mentioned as the "only viable local model for coding" for 32GB machines by one source, suggesting it strikes the best balance of quality and resource usage in this tier. By using a highly compressed 4-bit quantization (GGUF format via Ollama), you can load the majority of the model weights onto your fast 32GB system RAM and offload as much as possible to the 8GB of VRAM on your RTX 3070 for faster processing. Performance and Constraints ComponentSpecificationModel Constraint & ImpactVRAM8GB (RTX 3070)This is the main bottleneck. Limits you to ~7B-9B models for full GPU offload or highly quantized versions of larger models.System RAM32GB DDR5Crucial asset. Allows you to load large models (like 30B) in a 4-bit quantized format, using the RAM to store model layers the VRAM can't hold (CPU offload).CPUi7-12700KStrong CPU is excellent for processing the layers that are offloaded to RAM, ensuring a usable response speed. The key trade-off for running a 30B-parameter model is speed. While the quality of the code generated will be much closer to a production-ready level, the inference speed (tokens per second) will be slower than if you ran a smaller 7B-8B model fully on your GPU. 🥈 Alternative: Best Pure-Speed Coding Model If the speed of the 30B model is too slow for an interactive experience (like code completion), consider a top-tier 8-9 Billion parameter model. These will run much faster, fully on your 8GB VRAM. Model: DeepSeek R1 0528 Qwen3 8B or NVIDIA Nemotron Nano 9B V2 (if available on Ollama/GGUF) Reasoning: 7B-9B models are in the "sweet spot" for 8GB VRAM. These models will offer very fast inference speeds and still provide excellent code quality. However, they will generally not match the complexity and "production-ready" quality of a 30B-parameter model like Qwen3-Coder, which is the quality you requested. 🛠️ Key to Success with Ollama and Cursor Regardless of the model you choose, the crucial step for success is managing how Ollama distributes the model layers between your VRAM and RAM. Use Quantized GGUF: Ensure you pull the Q4_K_M (or similar 4-bit) version of the 30B model from Ollama. GPU Offload: When running the model via Ollama, you will need to set the num_gpu parameter to offload as many layers as possible to your 8GB VRAM (the default behavior in a modern Ollama install should try to maximize this automatically). Context Length: Start with a reasonable context length (e.g., 8K or 16K) to prevent the KV cache (which also sits in VRAM/RAM) from filling up memory and forcing layers to the slow CPU. This video walks through how to set up an LLM with Ollama and an 8GB VRAM GPU. Setting up LLM with 8GB VRAM and Ollama.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
