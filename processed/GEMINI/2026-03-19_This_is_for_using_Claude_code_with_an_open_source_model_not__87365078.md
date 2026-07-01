---
id: 420368
source: GEMINI
date: 2026-03-19
tags: ['claude-code', 'local-llm', 'clarification', 'not-agent-brain']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified that the local LLM setup was for Claude Code usage, not for the Operation Immortal Agent brain.
---
# This is for using Claude code with an open source model not for the agents brain for that project

### USER
This is for using Claude code with an open source model not for the agents brain for that project

### GEMINI
Claude is correct about the environment, but the recommendation for DeepSeek-R1-Distill-14B is where the real "unlock" for your specific project lies. Since you are running CachyOS, you have a massive advantage: lower system overhead compared to Windows 11 means your 8GB VRAM is actually "purer." In Windows, the OS and desktop compositor often eat 1.5–2GB of VRAM just to exist. On CachyOS, you can get that down to under 500MB, giving the model more room to breathe. As of March 2026, Claude Code (the CLI tool) now has a built-in compatibility layer for the Anthropic Messages API via Ollama and other local providers. If you are using it as your primary terminal assistant, you should choose a model specifically tuned for the "Agentic Loop" (Plan -> Tool Call -> Execute -> Verify). Here is the objective ranking for your hardware (8GB VRAM / 32GB DDR5) on CachyOS: 1. The Heavyweight: DeepSeek-R1-Distill-14B This is the most "intelligent" choice for Claude Code. Why: Unlike standard models, R1 uses a "Thinking" process. When Claude Code asks it to "Refactor this entire folder," R1 will actually reason through the dependencies before outputting code. Efficiency: A 4-bit quantization will fit entirely in your 8GB VRAM on CachyOS (since you don't have Windows bloat). The Catch: It can be slightly more verbose, which can sometimes slow down the agentic loop if the context gets too long. 2. The Specialist: Qwen3-Coder-Next (14B or 32B MoE) Why: This model was trained specifically for the Claude Code/Cline era of agentic tools. It understands the "Diff" format and tool-calling better than almost any other open-weight model. Fit: The 14B fits in VRAM. The 32B MoE will spill into your 32GB of RAM, but because it's an MoE, it will still feel snappy (around 20-30 tokens/sec). The Verdict: If R1 feels too slow or "overthinks" simple tasks, this is the most reliable "workhorse" for coding. 3. The "Legacy" Choice: Qwen 3.5 9B The Advisor's Reality Check: You are underutilizing your 12700K and 32GB RAM if you stick with this. It’s fine for simple scripts, but it will frequently fail on complex multi-file edits where the 14B models succeed. CachyOS Optimization Tip Since you're on Arch-based CachyOS, you can squeeze more out of that 3070 by using the linux-cachyos-v3 or v4 kernel and ensuring you have the latest Ollama (v0.14+) which handles the Anthropic API mapping natively. To run Claude Code with your local model, just set your environment variables: export ANTHROPIC_BASE_URL="http://localhost:11434" export ANTHROPIC_API_KEY="ollama" # Dummy key claude --model qwen3-coder:14b Would you like me to show you how to set up an MCP (Model Context Protocol) gateway on CachyOS to let Claude Code access your local files and system tools more effectively?
