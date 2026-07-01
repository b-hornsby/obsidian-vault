---
category: ai-tools
date: 2025-07-29
id: 830784
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan shared his full specs again to get a better model recommendation for
  a Cursor-like experience.
tags:
- pc-specs
- model-recommendation
- cursor-alternative
- local-llm
---
# Now to clarify these are my specs. If there’s a different model you would suggest for a similar experience to cursors, please let me know: Cpu: Intel Core i7-12700K

Motherboard: Asus Prime Z790-P
 
Cpu cooler: Noctua NH-U12S

Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40

Storage: 970 Evo Plus M.2 SSD 2TB

Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGB

Case: Corsair 4000D Airflow

PSU: Corsair CX750M

OS: Windows 11

### USER
Now to clarify these are my specs. If there’s a different model you would suggest for a similar experience to cursors, please let me know: Cpu: Intel Core i7-12700K

Motherboard: Asus Prime Z790-P
 
Cpu cooler: Noctua NH-U12S

Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40

Storage: 970 Evo Plus M.2 SSD 2TB

Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGB

Case: Corsair 4000D Airflow

PSU: Corsair CX750M

OS: Windows 11

### GEMINI
You've got a solid machine there, particularly for running local LLMs! Your Intel Core i7-12700K, 32GB of DDR5 RAM, and especially the RTX 3070 with 8GB of VRAM are well-suited for this. The 8GB VRAM is the most critical factor for which models you can comfortably run. Cursor leverages a variety of powerful cloud-based models like GPT-4o, Claude 3.5 Sonnet, and O3, along with their own custom "cursor-small" model. These are typically much larger than what you can run locally, and their performance benefits from massive, distributed compute. The "scaffolding" ability of these large models comes from their extensive training data and advanced reasoning capabilities. While you won't get exactly the same model on your local machine, you can get a surprisingly good and highly functional experience. The key is choosing the right quantized models that fit within your 8GB VRAM. Quantization reduces the precision of the model's weights, making it smaller and faster to run on consumer hardware, with some minor trade-offs in performance. Here's my refined suggestion for models you should try with Ollama on your setup, aiming for that "similar experience to Cursor" for scaffolding: Recommended Ollama Models for Your RTX 3070 (8GB VRAM) Your 8GB VRAM means you're generally looking for models around 7B to 13B (7 billion to 13 billion parameters), or highly quantized versions of slightly larger models. Deepseek-Coder-V2 (7B or 16B quantized) Why it's good: Deepseek-Coder models are often highly praised for their coding capabilities, excelling at code generation, completion, and understanding. They were specifically trained on a vast amount of code. VRAM Fit: The 7B parameter versions (e.g., deepseek-coder-v2:7b-lite-q4_K_M or similar 4-bit quantized versions) will fit comfortably within your 8GB VRAM, often leaving room for a larger context window. You might even be able to squeeze in some 16B quantized versions, but you'll need to monitor VRAM usage. Ollama Command: ollama run deepseek-coder-v2:7b-lite-q4_K_M (or check Ollama's library for the latest recommended 7B/16B versions). CodeLlama (13B quantized) Why it's good: You already have codellama installed, which is great. CodeLlama is Meta's dedicated family of code models and is a strong performer. VRAM Fit: The codellama:13b model (especially 4-bit or 5-bit quantized versions like codellama:13b-instruct-q4_K_M) should run on your 8GB RTX 3070. The 7B version will be even faster and more comfortable. The 34B version will likely be too large for your VRAM. Ollama Command: ollama run codellama:13b-instruct-q4_K_M (or experiment with other 13b quantizations). Qwen2 (7B or 14B quantized) Why it's good: Qwen models, especially the Qwen2-Coder variants, have been getting excellent reviews for their coding ability and general instruction following. They are often strong generalists that also excel at code. VRAM Fit: The 7B versions will be very comfortable, and you may find that some 14B quantized versions fit as well. Ollama Command: ollama run qwen2:7b-instruct-q4_K_M (or check for qwen2-coder specific versions if available on Ollama). Mistral (7B Instruct) Why it's good: While not specifically a "code" model, Mistral 7B Instruct is an incredibly capable general-purpose model that often performs very well on coding tasks, especially for its small size. It's fast and efficient. For scaffolding, its general reasoning can be a huge asset. VRAM Fit: Very comfortable. It's one of the most efficient models you can run locally. Ollama Command: ollama run mistral:7b-instruct-q4_K_M Key Considerations for Your Setup and Scaffolding Quantization: Always prioritize q4_K_M or q5_K_M (4-bit or 5-bit quantization) models in Ollama for your 8GB VRAM. These offer the best balance of performance and quality for your GPU. Performance: CPU: Your i7-12700K is excellent and will handle the CPU portion of the model inference very well, especially when offloading layers to the GPU. RAM: 32GB DDR5 is ample. If a model doesn't fully fit into VRAM, some layers will spill over into system RAM, which your fast DDR5 will handle better than slower RAM. GPU (RTX 3070 8GB): This is your main workhorse. You should get decent token generation speeds (how fast the AI writes code) with the recommended models. Faster than CPU-only, but not as instantaneous as cloud APIs. Context Window: When you download a model with Ollama, it will typically show its context window size (e.g., 4K, 8K, 16K tokens). Larger context windows are generally better for scaffolding because the model can "see" more of your existing project code and your prompt, leading to more coherent and relevant generations. Aim for models with at least an 8K context window if possible. Trial and Error: The best way to find what works for your specific use cases is to download a few of these recommended models and try them out with Continue.dev. See which one gives you the most satisfactory results for scaffolding. In summary, while you have codellama installed, I would strongly recommend trying out deepseek-coder-v2 (7B or 16B quantized) and potentially a Qwen2 (7B or 14B quantized) model in Ollama. These often have a slight edge in pure coding tasks compared to a general codellama model of similar size, which can translate to a better scaffolding experience for a beginner. The general instruction-following capabilities of Mistral 7B are also surprisingly effective for code and can be very fast.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
