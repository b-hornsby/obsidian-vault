---
id: 841917
source: GEMINI
date: 2026-03-19
tags: ['claude-code', 'model-ranking', 'r1-distill-14b', 'qwen3-35b', 'cachyos']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan shared Claude's recommendation ranking R1-Distill 14B as the best model for Claude Code on their hardware.
---
# This is what Claude had to say about it: Good — CachyOS is the better environment for this anyway. CUDA/ROCm support is cleaner on Arch-based distros, and you won’t have the Windows driver overhead eating into your VRAM headroom.

So back to the core question: the 9B plugged into Claude Code is functional but you’re leaving capability on the table for anything non-trivial. For Operation Immortal Agent especially, you’ll hit the 9B’s ceiling pretty fast on multi-step agentic reasoning.

Given you’re on CachyOS with 8GB VRAM + 32GB DDR5, my honest ranking for Claude Code specifically:

1. R1-Distill 14B — best fit for Claude Code’s agentic loop. Reasoning model, fits mostly in VRAM with minimal RAM spillover, and handles multi-step tool use noticeably better than a standard 9B.

2. Qwen3 35B-A3B — better raw knowledge, but the MoE layer offloading adds latency variability that can make Claude Code feel inconsistent. Great for chat/research, slightly awkward for tight agentic loops.

3. Stay on 9B — only if speed is the priority and tasks are simple.

### USER
This is what Claude had to say about it: Good — CachyOS is the better environment for this anyway. CUDA/ROCm support is cleaner on Arch-based distros, and you won’t have the Windows driver overhead eating into your VRAM headroom.

So back to the core question: the 9B plugged into Claude Code is functional but you’re leaving capability on the table for anything non-trivial. For Operation Immortal Agent especially, you’ll hit the 9B’s ceiling pretty fast on multi-step agentic reasoning.

Given you’re on CachyOS with 8GB VRAM + 32GB DDR5, my honest ranking for Claude Code specifically:

1. R1-Distill 14B — best fit for Claude Code’s agentic loop. Reasoning model, fits mostly in VRAM with minimal RAM spillover, and handles multi-step tool use noticeably better than a standard 9B.

2. Qwen3 35B-A3B — better raw knowledge, but the MoE layer offloading adds latency variability that can make Claude Code feel inconsistent. Great for chat/research, slightly awkward for tight agentic loops.

3. Stay on 9B — only if speed is the priority and tasks are simple.

### GEMINI
Claude is correct about the environment, but the recommendation for DeepSeek-R1-Distill-14B is where the real "unlock" for your specific project lies. Since you are running CachyOS, you have a massive advantage: lower system overhead compared to Windows 11 means your 8GB VRAM is actually "purer." In Windows, the OS and desktop compositor often eat 1.5–2GB of VRAM just to exist. On CachyOS, you can get that down to under 500MB, giving the model more room to breathe. Here is the "advisor" level breakdown of those options for Operation Immortal Agent: 1. The Strategic Winner: DeepSeek-R1-Distill-14B This is the correct choice for agentic work. Why: Standard models (like Qwen 3.5 9B) predict the next token based on pattern matching. Reasoning models (R1-Distill) use a "Chain of Thought" (<think> tags). The Agentic Edge: For a trading bot, "thinking" before acting is the difference between a successful trade and a bugged API call. It will literally talk itself through the logic of your Phantom MCP connection before executing. Fit: At a 4-bit or 5-bit quantization, it will fit almost entirely in your 8GB VRAM on CachyOS. You'll get incredible speed with elite logic. 2. The Research Bench: Qwen 3.5 35B-A3B Why: This model has more "world knowledge." If you're asking it high-level questions about Solana DeFi protocols or Rust memory safety, it will know more than the 14B. The Trade-off: As Claude noted, MoE models have "latency jitter." Sometimes a token is fast, sometimes it's slow. For Claude Code, which relies on a tight loop of "Plan -> Execute -> Check," this jitter can lead to time-outs or broken tool calls. Use this for brainstorming the architecture, not for the agent actually writing the code. 3. The Retirement: Qwen 3.5 9B The Verdict: You’ve outgrown it. You have 32GB of DDR5 and a 12700K. Using the 9B for a complex autonomous project is like putting a lawnmower engine in a Porsche. It'll move, but you're wasting the chassis. The "Advisor" Action Plan If you want to move Operation Immortal Agent to the next level, do this: Switch to R1-Distill-14B (GGUF or EXL2): This should be your primary model for the agent's "brain." Optimize CachyOS for VRAM: Use nvtop to monitor your VRAM usage. If you're using a heavy desktop environment like GNOME or KDE, consider a "Game Mode" or a Tiling Window Manager (like Sway or Hyprland) when running your agent to maximize the VRAM available to the GPU. Context Management: Since you only have 8GB VRAM, don't try to cram a 128k context into the GPU. Limit your context window to 16k or 32k in your runner (Ollama/LM Studio). This keeps the KV Cache small enough to stay on the GPU, preventing the "PCIe bottleneck" slowdown. Would you like me to provide the specific terminal commands to pull and optimize the 14B Reasoning model on CachyOS?
