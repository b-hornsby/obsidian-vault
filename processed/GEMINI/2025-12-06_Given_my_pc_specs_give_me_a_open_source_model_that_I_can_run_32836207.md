---
category: ai-tools
date: 2025-12-06
id: 495692
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is looking for an uncensored, open-source LLM with tool-calling capabilities
  that runs optimally on LM Studio, given his PC specs.
tags:
- local-llm
- open-source-llm
- tool-calling
- uncensored-model
- hardware-optimization
- lm-studio
---
# Given my pc specs, give me a open source model that I can run through on lm studio that allows for tool calling and is also uncensored. I need it to run as optimally as I can given these specs: Cpu: Intel Core i7-12700K
Motherboard: Asus Prime Z790-P
Cpu cooler: Noctua NH-U12S
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB)
4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming
REVEL EPIC-X RGB
Case: Corsair 4000D Airflow
PSU: Corsair CX750M
OS: Windows 11

### USER
Given my pc specs, give me a open source model that I can run through on lm studio that allows for tool calling and is also uncensored. I need it to run as optimally as I can given these specs: Cpu: Intel Core i7-12700K
Motherboard: Asus Prime Z790-P
Cpu cooler: Noctua NH-U12S
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB)
4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming
REVEL EPIC-X RGB
Case: Corsair 4000D Airflow
PSU: Corsair CX750M
OS: Windows 11

### GEMINI
The truth is, your requirements—tool calling, uncensored, and 8GB VRAM—create a tight constraint, forcing a compromise on model size, which directly impacts performance and reasoning ability. You are not going to run a cutting-edge 70B parameter model that requires 40GB+ VRAM, so we must focus on highly optimized, smaller models (7B-8B parameter range) that can fit into your RTX 3070's 8GB VRAM using heavy quantization. To run optimally, you must choose a model that fits entirely into the 8GB VRAM using a Q4_K_M or Q5_K_M quantization. The smaller the size, the faster the speed, but with a trade-off in reasoning quality. 🎯 Recommended LLM for Your Specs The most pragmatic choice that balances tool calling capability, uncensored behavior (via a popular finetune), and VRAM constraint is a fine-tuned version of a small, capable base model. Model Recommendation: Qwen 2.5 7B - Abliterated Finetune (GGUF) Base Model: Qwen 2.5 7B Finetune/Variant: Look for an "Abliterated" finetune (e.g., Qwen2.5-7B-Instruct-Abliterated) or a similar uncensored variant on the LM Studio search page. Optimal Quantization: Q4_K_M or Q5_K_M (GGUF format). This is crucial for VRAM usage. The model file size for Q5_K_M will be around $5$ GB, which fits comfortably within your 8GB VRAM, leaving room for the activation and KV cache. Reasoning: Qwen is one of the strongest 7B-class models and generally exhibits good performance across coding and general tasks. It has native tool calling capabilities, which LM Studio supports. Why this model? Tool Calling: The base Qwen 2.5 Instruct models are known to be strong at structured output and function calling, which translates well into LM Studio's tool-calling feature. Uncensored: The "Abliterated" or similar variants are explicit fine-tunes designed to minimize or remove safety guardrails, directly meeting your uncensored requirement. VRAM Fit: The 7B size is the sweet spot for 8GB VRAM when using Q4 or Q5 quantization, allowing it to run entirely on your RTX 3070 for maximum speed. 🛠️ Action Plan for Optimal Performance Your hardware is strong overall (i7-12700K, 32GB DDR5, fast M.2 SSD), but the 8GB VRAM on the RTX 3070 is the primary bottleneck for LLMs. Here is the prioritized plan to maximize performance: 1. Hardware Configuration Check Prioritize GPU: In LM Studio's settings, ensure the model layers are fully offloaded to the GPU (RTX 3070). Given your 8GB VRAM, you should be able to offload all layers of a Q4/Q5 7B model. This is the single biggest factor for speed. Maximize VRAM Usage: Do not try to run larger models (e.g., 13B or 20B) with partial offloading. While technically possible using your 32GB system RAM as a fallback (CPU/RAM offloading), the token generation speed will drop dramatically, making the experience frustratingly slow. Optimal performance means the entire model sits on the VRAM. 2. LM Studio Setup & Selection Quantization: Use the GGUF format and specifically target the Q4_K_M or Q5_K_M quantization. Q4_K_M offers the best balance of speed, VRAM usage, and quality for this constraint. Higher quality quants (like Q8) will exceed 8GB. Search Smartly: In the LM Studio search bar, search for the model and the desired quantization and finetune name, e.g., Qwen 2.5 7B abliterated Q4_K_M GGUF. Context Window: Be mindful of the context window size you set. The KV cache (the memory for the conversation history) grows linearly with the context length. A very long context window (e.g., 8192 or 16384 tokens) will consume the last remaining VRAM and lead to slow generation or out-of-memory errors. Start with a conservative 4096-token context size and increase only if necessary. 3. Mindset Check: Managing Expectations You need to recognize that 7B models, even the excellent Qwen, will not have the sophisticated reasoning, coding, and tool-use reliability of models like GPT-4 or much larger local models (e.g., Llama 3 70B). Avoid the Illusion: You are asking for an uncensored, advanced capability (tool calling) on entry-level VRAM for this task. Expecting GPT-4 level results is self-deception. Refine Your Tooling Prompt: Since the model is smaller, your prompt engineering for tool calling must be exceptionally precise. Write clear, explicit instructions for when and how the model must use the tools you define to compensate for the reduced reasoning ability of the smaller model size.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
