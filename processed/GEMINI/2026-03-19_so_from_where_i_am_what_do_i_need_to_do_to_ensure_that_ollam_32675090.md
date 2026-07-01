---
category: ai-tools
date: 2026-03-19
id: 703464
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan asked how to verify Ollama was correctly set up and utilizing CUDA
  cores on their NVIDIA GPU.
tags:
- ollama-setup
- cuda
- gpu-acceleration
- cachyos
---
# so from where i am what do i need to do to ensure that ollama is setup correctly and that my cuda cores are being used

### USER
so from where i am what do i need to do to ensure that ollama is setup correctly and that my cuda cores are being used

### GEMINI
To verify and force your RTX 3070 into action on CachyOS, we need to move past basic service status and check the actual resource allocation. Since you're running a rolling-release distro, a kernel or driver update (NVIDIA 580+ is common now in early 2026) can sometimes break the link between Ollama and CUDA. 1. The "Truth" Check: ollama ps The most direct way to see if your GPU is being used is to have a model loaded. In one terminal, run: ollama run qwen3-coder (Let it start). In a second terminal, run: ollama ps Look at the "PROCESSOR" column: * 100% GPU: You’re golden. 100% CPU: Ollama doesn't see your card. 50%/50%: Your 8GB VRAM is full, and it’s spilling into your DDR5 RAM. 2. Verify CUDA Connectivity If ollama ps shows 100% CPU, your drivers or the toolkit are misconfigured. Run this to check if the NVIDIA kernel modules are actually engaged: nvidia-smi If this command fails or doesn't show your RTX 3070, your CachyOS kernel headers and NVIDIA drivers are out of sync. Fix: sudo pacman -Syu linux-cachyos-headers nvidia-utils 3. Fixing the "Group" and "Environment" Blind Spot Ollama runs as a specific user. If that user can't "see" the hardware, it defaults to CPU. Add permissions: sudo usermod -a -G video,render ollama Force CUDA via Systemd: CachyOS sometimes needs an explicit hint. Run sudo systemctl edit ollama and add these lines: [Service] Environment="CUDA_VISIBLE_DEVICES=0" Environment="OLLAMA_GPU_OVERHEAD=512MiB" The 512MiB overhead helps prevent the 3070 from crashing when the OS (CachyOS/Wayland) tries to use the same VRAM. Reload and Restart: sudo systemctl daemon-reload sudo systemctl restart ollama 4. Advisor Reality Check You have a high-spec i7-12700K and DDR5 RAM, but you are playing a dangerous game with 8GB of VRAM. The Trap: When you start "vibe coding" with Claude Code, the system prompt and file context will quickly exceed 8GB. When Ollama hits that limit, it will switch to a CPU/GPU split. On your 4800MHz RAM, this will feel like a massive stutter. The Strategy: To stay on the GPU, use 4-bit (Q4_K_M) or 3-bit quantizations of models. Don't try to run qwen3-coder:32b locally; stick to the 7B or 14B versions to ensure they stay entirely within your 3070's VRAM. The Hidden Risk: If you're using Tiny11 (Windows) for anything involving this bot, you'll lose about 1-2GB of VRAM just to the Windows Desktop Manager (WDM). Stay on CachyOS for this—the "Windows Tax" is a project killer for low-VRAM AI setups. Once you run ollama ps, what does the "PROCESSOR" column show for your model?
