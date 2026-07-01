---
category: ai-tools
date: 2026-03-19
id: 166855
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan asked how to set up Claude Code with an open-source model on their
  CachyOS system with an RTX 3070.
tags:
- claude-code
- local-llm
- open-source-model
- cachyos
- rtx-3070
---
# How do I set up Claude code with an open source model? These are my specs as well: ‣Cpu: Intel Core i7-12700K
‣Motherboard: Asus Prime Z790-P
‣Cpu cooler: Noctua NH-U12S
‣Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
‣Storage: 970 Evo Plus M.2 SSD 2TB
‣Graphics card: PNY GeForce RTX™ 3070 8GB
‣Case: Corsair 4000D Airflow
‣PSU: Corsair CX750M
‣OS: CachyOS + Tiny11

### USER
How do I set up Claude code with an open source model? These are my specs as well: ‣Cpu: Intel Core i7-12700K
‣Motherboard: Asus Prime Z790-P
‣Cpu cooler: Noctua NH-U12S
‣Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40
‣Storage: 970 Evo Plus M.2 SSD 2TB
‣Graphics card: PNY GeForce RTX™ 3070 8GB
‣Case: Corsair 4000D Airflow
‣PSU: Corsair CX750M
‣OS: CachyOS + Tiny11

### GEMINI
Your setup—CachyOS and an RTX 3070 (8GB VRAM)—is a solid foundation for this, though the 8GB VRAM is your primary bottleneck for "agentic" coding models which typically require larger context windows. Since January 2026, Ollama and LM Studio have added native compatibility for the Anthropic Messages API, making the "Claude Code Router" proxies of late 2025 mostly obsolete. 1. The Model Choice (The "Agentic" Constraint) Claude Code is extremely "chatty" and relies heavily on tool-calling. Best for 8GB VRAM: qwen3-coder:7b or deepseek-coder-v2:16b (quantized). The "Power" Option: qwen3-coder:32b (will likely spill into your 32GB DDR5 RAM, making it significantly slower, but much smarter for complex refactoring). Recommendation: Start with Qwen3-Coder-Next or GLM-4.7-9B-Chat for the best tool-calling reliability on your hardware. 2. Implementation via Ollama (Recommended for CachyOS) Since you're already on an Arch-based distro, Ollama is the cleanest path. Step 1: Install/Update Ollama Ensure you are on v0.14.0 or later for Messages API support. curl -fsSL https://ollama.com/install.sh | sh ollama pull qwen3-coder Step 2: Configure Environment Variables Claude Code looks for the ANTHROPIC_BASE_URL. You need to point it to Ollama’s local endpoint. Add these to your .zshrc or .bashrc: export ANTHROPIC_BASE_URL="http://localhost:11434" export ANTHROPIC_AUTH_TOKEN="ollama" # Dummy token required by the CLI Step 3: Launch Claude Code Run the installer if you haven't: curl -fsSL https://claude.ai/install.sh | bash. Then launch it specifying your local model: claude --model qwen3-coder 3. Critical Hardware Tuning for your Specs Your i7-12700K and 32GB RAM will handle the heavy lifting if the model exceeds your 8GB VRAM, but performance will tank. Use these tweaks: Increase Context Window: Claude Code sends massive system prompts (up to 16.5K tokens). Ollama defaults to 4K. You must increase this or the agent will "forget" your project instantly. Create a Modelfile: FROM qwen3-coder PARAMETER num_ctx 32768 ollama create qwen3-coder-large -f Modelfile KV Cache Fix: There is a known issue in early 2026 where Claude Code's "Attribution Headers" invalidate the KV cache on local models, making them 90% slower. Fix: Ensure you are using the latest CachyOS kernel updates which include optimized schedulers for LLM inference workloads. 4. Direct Advice (Advisor Mode) You have a high-performance Linux setup, but you're trying to run an "Agent" on an 8GB card. The Blind Spot: You’re likely going to hit Out of Memory (OOM) errors the moment Claude tries to read your entire repository into context. Strategic Adjustment: Do not use Claude Code for "repository-wide" refactoring on this local setup. Use it for file-specific tasks. If you want the full "Immortal Agent" experience you’ve been building, you will eventually hit a wall with that 3070. Consider offloading inference to a dedicated provider (like OpenRouter) while keeping the orchestration local on your CachyOS box. Would you like me to help you write a custom MCP server to bridge your local Ollama instance with specialized tools for your "Operation Immortal Agent" project?
