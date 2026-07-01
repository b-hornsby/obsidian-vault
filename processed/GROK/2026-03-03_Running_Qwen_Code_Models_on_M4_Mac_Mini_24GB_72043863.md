---
id: 987195
source: GROK
date: 2026-03-03
tags: ['qwen-code-model', 'm4-mac-mini', 'local-llm', 'hardware-requirements', '24gb-ram']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan wanted to know if the Qwen code model could run locally on an M4 Mac Mini with 24GB of RAM.
---
# Running Qwen Code Models on M4 Mac Mini 24GB

### HUMAN
Can you run qwens new code model with a Mac mini m4 with 24gb?

### ASSISTANT
Yes, you can run **Qwen's latest/new code-focused models** on a Mac Mini M4 with 24GB unified memory, but it depends on which specific "new" model you're referring to (Qwen has released several coding-oriented ones recently, like in the Qwen3 / Qwen3.5 / Qwen3-Coder-Next families).

The M4's unified memory works great for local LLM inference via tools like **MLX** (Apple-optimized), **llama.cpp**, **Ollama**, or **LM Studio** — all of which support Qwen models well on Apple Silicon. The 24GB allows comfortable runs of smaller-to-mid-size quantized models with good speeds (often 20–50+ tokens/sec depending on size/quant and context length), but larger ones may require heavy quantization, shorter context, or feel slower / swap to SSD.

Here's a breakdown based on the most recent Qwen coding models as of early 2026:

- **Smaller / efficient coding models** (best fit for your 24GB Mac Mini M4):
  - Qwen3-Coder-Next (80B total params, but only ~3B active thanks to ultra-sparse MoE + hybrid architecture) — This is one of the newest (Feb 2026) and most efficient "new code models" from Qwen. It's designed for fast local/agentic coding use.
    - Quantized versions (e.g. 4-bit or lower) can run in ~18–25GB or less.
    - Expect solid performance: 30–60+ t/s possible on M4 hardware for code tasks, with 128K–256K context support.
    - Many users run similar MoE Qwen variants (like Qwen3-30B-A3B) successfully on 24GB M4 systems.
  - Qwen3.5 / Qwen3 small coding variants (0.8B–9B params, or 4B–14B dense) — These fit easily (often <15GB quantized) and run very fast (40–80+ t/s).
    - Great for quick code completion, debugging, etc.

- **Mid-size** (still doable):
  - Qwen2.5-Coder or Qwen3-14B / 32B variants (dense or MoE like 30B-A3B) — 4-bit / Q4_K_M quants typically use 16–22GB.
    - Runs well at ~15–40 t/s on M4 (faster on smaller context).
    - Community reports confirm Qwen-14B Q4 and similar work "amazing" on 24GB M4 Mac Minis for coding.

- **Larger flagship coding models** (more challenging / not ideal):
  - Full Qwen3-Coder-480B-A35B or huge MoE ones — These push 30–50GB+ even quantized → they'd swap heavily or not fit smoothly on 24GB. You'd need 48GB+ for comfortable use.

In practice:
- Use **4-bit** (or even 3-bit / dynamic quants via Unsloth or GGUF) to stay under 24GB.
- Tools like Ollama or LM Studio make it plug-and-play.
- Real-world M4 24GB users report good results with Qwen coding models around 14B–32B equiv (or efficient MoE like the 3B-active ones) for actual coding work — fast enough for VS Code integration via Continue.dev, etc.
- If you're hitting memory pressure during long contexts or big projects, drop to a smaller quant or limit context to 8K–32K tokens.

Overall: **Yes — especially the newer efficient ones like Qwen3-Coder-Next** — your Mac Mini M4 24GB is actually a strong setup for local Qwen code models in 2026. It's one of the better "bang-for-buck" machines for this right now. If you tell me exactly which Qwen model/version (e.g. from Hugging Face link), I can give more precise memory/speed estimates!
