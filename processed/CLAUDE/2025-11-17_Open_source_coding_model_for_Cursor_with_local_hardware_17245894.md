---
id: 231198
source: CLAUDE
date: 2025-11-17
tags: ['open-source-llm', 'coding-model', 'cursor-integration', 'ollama-ngrok', 'rtx-3070', 'production-ready-code']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is looking for the optimal open-source coding model to use with Cursor via Ollama and ngrok, aiming for production-ready code similar to Claude Sonnet 4.5, given his RTX 3070 and other hardware specs.
---
# Open source coding model for Cursor with local hardware

### HUMAN
looking for an open source model to use for coding within cursor using ollama and ngrok to do so. given my current specs, give me the absolute best model i should use that gives me production ready level code similar to what claude sonnet 4.5 provides. these are those given specs: Cpu: Intel Core i7-12700K
Motherboard: Asus Prime Z790-P
 
Cpu cooler: Noctua NH-U12S
Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
Storage: 970 Evo Plus M.2 SSD 2TB
Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGB
Case: Corsair 4000D Airflow
PSU: Corsair CX750M
OS: Windows 11

### ASSISTANT
<thinking>
The user is asking for an open source model recommendation for coding in Cursor using Ollama and ngrok. They want something that matches Claude Sonnet 4.5's production-ready code quality.

Let me analyze their specs:
- CPU: Intel Core i7-12700K (12 cores, 20 threads - very capable)
- RAM: 32GB DDR5 4800MHz (good amount, but this is the key constraint for model size)
- GPU: RTX 3070 8GB (8GB VRAM is limiting for larger models)
- Storage: 2TB NVMe (plenty for models)

Key constraints:
1. **RAM: 32GB** - This is the main limiting factor for running large models
2. **VRAM: 8GB** - This limits GPU-accelerated inference

For Ollama models, the memory requirements roughly are:
- 7B models: ~8GB RAM (4-bit quantized) to ~14GB (full precision)
- 13B models: ~16GB RAM (quantized)
- 34B models: ~20-24GB RAM (quantized)
- 70B models: ~40GB+ RAM (quantized)

With 32GB RAM, they can realistically run:
- 7B-13B models comfortably with GPU acceleration
- Up to 34B models with CPU inference (but slower)
- 70B+ models would require heavy quantization and would be very slow

The 8GB VRAM on the RTX 3070 means:
- 7B models can fully run on GPU
- 13B models might need CPU offloading
- Larger models will need significant CPU usage

Best coding models available via Ollama:
1. **Qwen 2.5 Coder** (7B, 14B, 32B versions) - Very strong for coding
2. **DeepSeek Coder V2** (16B, 236B) - Excellent but 236B is too large
3. **CodeLlama** (7B, 13B, 34B, 70B) - Good but older
4. **Mistral/Mixtral** models
5. **Llama 3.1** (8B, 70B, 405B)

Given the constraints, I should recommend:
- **Primary recommendation**: Qwen 2.5 Coder 32B (quantized to 4-bit) - This would fit in 32GB RAM and provide excellent code quality
- **Alternative**: DeepSeek Coder V2 16B - Also excellent, lighter on resources
- **GPU-optimized option**: Qwen 2.5 Coder 14B - Can leverage the GPU better

However, I need to be realistic: NO open source model will truly match Claude Sonnet 4.5's production-ready code quality. Claude Sonnet 4.5 is a frontier model that's significantly larger and more capable. I should be honest about this while giving them the best options.

The user wants "production ready level code similar to what claude sonnet 4.5 provides" - I need to manage expectations here while giving the best recommendation.
</thinking>

Given your specs, here's the reality: **no open source model will truly match Claude Sonnet 4.5's production-ready code quality** - Sonnet 4.5 is a frontier model that's significantly larger and more capable. However, I can recommend the best options for your hardware.

## Best Recommendation: **Qwen2.5-Coder-32B-Instruct (Q4_K_M quantization)**

This is your optimal choice because:
- **Fits your RAM**: ~20-22GB with 4-bit quantization
- **Best coding performance**: Consistently ranks at the top of open source coding models
- **Context window**: 32K tokens (great for large codebases)
- **Production-ready**: Strongest reasoning and code generation in the open source space

### Setup in Ollama:
```bash
ollama pull qwen2.5-coder:32b-instruct-q4_K_M
```

## Alternative Options (ordered by quality):

**If 32B is too slow:**
- **Qwen2.5-Coder-14B-Instruct** - Better GPU utilization with your RTX 3070, still excellent quality
  ```bash
  ollama pull qwen2.5-coder:14b
  ```

**If you want more GPU acceleration:**
- **DeepSeek-Coder-V2-16B-Instruct** - Strong alternative, can run mostly on GPU
  ```bash
  ollama pull deepseek-coder-v2:16b
  ```

## Performance Expectations:

With the 32B model on your specs:
- Inference speed: ~10-20 tokens/second (mostly CPU)
- The RTX 3070 will help with partial offloading
- Expect ~70-80% of Sonnet 4.5's quality for straightforward tasks
- More significant gap on complex reasoning/architecture decisions

## Tips for Best Results:
1. Use **Q4_K_M quantization** (best quality/speed balance)
2. Enable GPU offloading in Ollama settings
3. Close other applications to maximize available RAM
4. Use detailed prompts with context - these models need more guidance than Claude

**Bottom line**: Qwen2.5-Coder-32B is your best bet, but temper expectations - it's good for most coding tasks but won't match Sonnet 4.5's architectural reasoning and edge case handling.

### HUMAN
for clarification i have 8gb of vram with my 3070. will it still run this model?

### ASSISTANT
Yes, it will run, but **not fully on the GPU** - the 8GB VRAM isn't enough for the entire 32B model. Here's what will actually happen:

## How Qwen2.5-Coder-32B will work on your system:

**Hybrid CPU/GPU execution:**
- Ollama will automatically **offload layers** between your RTX 3070 (8GB VRAM) and system RAM (32GB)
- With Q4_K_M quantization (~20-22GB total), roughly **6-7GB can fit in VRAM**
- The remaining ~14-16GB will run on your CPU (i7-12700K)

**What this means:**
- ✅ It will work fine
- ⚠️ Slower than full GPU (~10-15 tokens/sec vs 30-40+ if it fit entirely)
- ✅ Still significantly faster than pure CPU inference
- ✅ Your i7-12700K is strong enough to handle the CPU portion well

## Better GPU-optimized alternatives:

If you want **maximum GPU utilization** with your 8GB VRAM:

**1. Qwen2.5-Coder-14B (Q4_K_M)** ← **Best balance for your GPU**
- ~8-10GB quantized - fits almost entirely in VRAM
- ~80-90% of 32B's quality
- Much faster inference (~25-35 tokens/sec)
```bash
ollama pull qwen2.5-coder:14b-instruct-q4_K_M
```

**2. Qwen2.5-Coder-7B**
- Fits completely in VRAM
- Fastest option (~40-50 tokens/sec)
- Still quite capable for most coding tasks
```bash
ollama pull qwen2.5-coder:7b-instruct
```

## My updated recommendation:

**Start with the 14B model** - it's the sweet spot for your RTX 3070's 8GB VRAM. You'll get near-32B quality with much better speed. You can always try the 32B later if you want slightly better quality and don't mind the slower generation.

### HUMAN
so given my specs what is the absolute optimal model to be using given what i want to use it for?

### ASSISTANT
Given your specs and goal (production-ready coding), the **absolute optimal model** is:

## **Qwen2.5-Coder-14B-Instruct (Q4_K_M)**

This is the sweet spot because:

### Why it's optimal for YOUR hardware:
- ✅ **Fits almost entirely in your 8GB VRAM** (~8-10GB quantized)
- ✅ **Maximizes your RTX 3070** - minimal CPU offloading needed
- ✅ **Fast inference**: 25-35 tokens/second (vs 10-15 for 32B)
- ✅ **Plenty of headroom in your 32GB RAM** for OS + Cursor + context
- ✅ **Best quality-to-speed ratio** for your exact configuration

### Why NOT the 32B:
- Only ~10-15% better code quality
- 2-3x slower inference (kills developer flow)
- Majority runs on CPU anyway due to VRAM limits
- Diminishing returns for the performance hit

### Why NOT the 7B:
- Noticeably weaker reasoning on complex tasks
- More prone to bugs in production code
- The 14B is worth the minor VRAM increase

## Setup command:
```bash
ollama pull qwen2.5-coder:14b-instruct-q4_K_M
```

## Expected performance:
- **Speed**: Smooth, responsive (25-35 tok/sec)
- **Quality**: ~75-80% of Claude Sonnet 4.5 for typical coding tasks
- **Best for**: Functions, classes, refactoring, debugging, API integration
- **Weaker on**: Complex architectural decisions, novel algorithm design

**Bottom line**: The 14B model is engineered perfectly for your 8GB VRAM + 32GB RAM setup. It maximizes both your GPU and the coding quality you'll actually get in practice.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
