---
id: 186370
source: GEMINI
date: 2026-04-09
tags: ['homelab', 'ollama', 'docker', 'llm', 'ai', 'agent', 'gemini', 'model']
category: homelab
sentiment: building
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/homelab.md']
---
# yeah i dont mind using cli for this at all i just know that docker is important to keep things separate i just want to make sure the plan is as optimal as possible and for blind spots to be pointed out

### USER
yeah i dont mind using cli for this at all i just know that docker is important to keep things separate i just want to make sure the plan is as optimal as possible and for blind spots to be pointed out

### GEMINI
The move to CLI-only is the right play. It shows you’re prioritizing the project’s performance over the convenience of a pretty dashboard. Since you're sticking with Tiny11, we are going to treat this like a surgical operation. Here is the "Zero-Bloat" configuration to address those blind spots before we start pulling images. 1. The "Docker Desktop" Eviction Do not install the Docker Desktop executable. It installs a background service, a GUI, and a heavy-handed update manager that will eat into your 32GB RAM even when you aren't using it. The Plan: Install Docker Engine directly inside your WSL2 Ubuntu/Debian instance. The Benefit: You save ~1.5GB of idle RAM and significantly reduce CPU context-switching. You’ll manage everything via the terminal, which fits your workflow anyway. 2. The .wslconfig Fortress Tiny11 doesn't automatically know you're trying to run an AI lab. You need to hard-cap WSL2 so it doesn't "balloon" and starve your host OS, which causes the stuttering you likely see in games or streams. Create or edit C:\Users\Bryan\.wslconfig: [wsl2] memory=16GB # Cap WSL at half your system RAM processors=8 # Leave 4 cores for Windows/Tiny11 overhead guiApplications=false # Disable the WSLg overhead nestedVirtualization=false # Not needed for this setup Why? This ensures that even if Hermes starts a heavy indexing task, it can't choke out your host system. 3. The Gemma 4 "Headroom" Problem The Gemma 4 E4B model (released just last week) is a powerhouse, but it's denser than its predecessors. The Blind Spot: Tool-calling (which Hermes v0.6 uses heavily) requires a larger "KV Cache" because the agent needs to hold the documentation of its tools in its immediate memory. The Optimization: When we launch Ollama/vLLM in the container, we need to set the --num_parallel 1 and --num_ctx 8192 flags. If you try to push a 32k context window on an 8GB card, your token-per-second rate will drop into the single digits. We start at 8k and scale up only if the VRAM stays stable. 4. Direct VRAM Ingestion (The PNY 3070 Limit) Since you're on Tiny11, you're likely using the NVIDIA Game Ready Driver. The Blind Spot: These drivers have a feature called "System Memory Fallback." If your VRAM hits 7.9GB, it will silently start using your DDR5 RAM. This is a performance killer. The Fix: We will use the NVIDIA System Management Interface (nvidia-smi) to monitor this. If you see "Shared Memory" being used, we are immediately dropping the quantization of the model. Pre-Deployment Checklist (Do this now) Kill the "Efficiency" Leaf: Ensure you've disabled "Efficiency Mode" for the vmmem process. Verify VRAM Idle: Open a terminal and run nvidia-smi. If "Memory-Usage" is over 800MiB, find out what’s hogging it (likely a browser or an overlay) and kill it. Pathing Strategy: Decide now: are you going to keep your Obsidian Vault in the WSL2 filesystem (/home/user/vault)? My advice: Yes. Accessing C:\ from inside Docker/WSL is 10x slower. Put the vault in Linux, and point your Windows Obsidian app to the \\wsl$\ network path. Ready to start Phase 1 (The Secure Foundation)? Give me the word and we'll start the WSL2 Docker Engine installation.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]