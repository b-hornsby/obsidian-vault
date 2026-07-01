---
id: 690253
source: GEMINI
date: 2026-03-24
tags: ['open-source-models', 'open-claw', 'local-llm', 'compatibility']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking if Open Claw can be used with open source models.
---
# Is it possible to use it with open source models?

### USER
Is it possible to use it with open source models?

### GEMINI
Absolutely. In fact, using open-source models is the "Pro" way to run OpenClaw because it eliminates the massive API costs associated with autonomous agents (which can burn through $10–$50 a day if they get stuck in a loop). Since you’re already deep into the Arch/CachyOS ecosystem and running an i7-12700K / RTX 3070 setup, you are in the perfect position to do this. 1. The Strategy: Hybrid Cloud + Local For your "Operation Immortal Agent," the most robust setup isn't choosing between cloud or local—it's using both: The Cloud (VPS): Runs the "Brain" (OpenClaw/NemoClaw). It stays online 24/7, monitors the Solana chain, and handles the "glue" tasks (log summaries, simple routing). The Local (Your PC): Runs the "Heavy Lifter" (Ollama/vLLM). When the agent needs to write complex code or analyze a deep DeFi strategy, it sends the request to your 3070 via a secure tunnel. 2. Best Open-Source Models for OpenClaw (2026) OpenClaw requires models that are excellent at Tool Use (JSON formatting). If the model fails to format its thoughts correctly, the agent breaks. Qwen 3.5 Coder (32B or 7B): Currently the "Gold Standard" for open-source agents. The 7B version will run like lightning on your RTX 3070. NVIDIA Nemotron-3-Nano (30B): Specifically optimized for NemoClaw. It fits perfectly in your 8GB VRAM if you use 4-bit quantization (GGUF/EXL2). Ministral 8B: Great for "fast" tasks and lower power consumption. 3. How to Connect Them You have two main paths depending on how much "under the hood" work you want to do: Path A: The Ollama Bridge (easiest for "Vibe Coding") If you already have Ollama running on your CachyOS machine: Set OLLAMA_HOST=0.0.0.0 on your local PC so it accepts outside connections. Use Tailscale (easiest) or Cloudflare Tunnels to create a secure link between your Cloud VPS and your home PC. In the OpenClaw config on your VPS, set the provider to Ollama and the URL to your Tailscale IP (e.g., http://100.x.x.x:11434). Path B: The NemoClaw Installer (most secure) NVIDIA recently added a "one-liner" that configures this for you. Run this on your VPS: curl -fsSL https://nvidia.com/nemoclaw.sh | \ NEMOCLAW_PROVIDER=ollama \ NEMOCLAW_MODEL=qwen3.5-coder:7b \ bash 4. The "Brutally Honest" Reality Check The VRAM Wall: Your RTX 3070 has 8GB VRAM. This is your bottleneck. Running a 30B model will be slow (2–3 tokens/sec). Stick to 7B or 8B models for the agent's "active" loops, and only call 30B+ models for "reasoning" steps. The Context Problem: OpenClaw eats context for breakfast. Local models struggle once the conversation history gets long. You will need to clear your agent's "memory" more often than you would with Claude 3.5. The Solana Risk: If your local PC goes offline (update, power flicker), your Cloud agent loses its "brain." Make sure you have a tiny "fallback" model (like a free-tier Groq API) so the bot can at least send you an alert if it loses connection to your home GPU. Would you like me to help you write the systemd service for your local Ollama setup to ensure it's always ready for the cloud agent?
