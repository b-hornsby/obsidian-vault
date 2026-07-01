---
id: 550839
source: GEMINI
date: 2026-03-19
tags: ['ollama-install', 'cachyos', 'qwen3-coder', 'nvidia-gpu']
category: ai-tools
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan installed Ollama on CachyOS and attempted to pull the qwen3-coder model, but the server failed to connect.
---
# ❯ curl -fsSL https://ollama.com/install.sh | sh
  ollama pull qwen3-coder
>>> Cleaning up old version at /usr/local/lib/ollama
[sudo] password for toastedmel0n:  
>>> Installing ollama to /usr/local
>>> Downloading ollama-linux-amd64.tar.zst
######################################################################## 100.0%
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
>>> NVIDIA GPU installed.
Error: could not connect to ollama server, run 'ollama serve' to start it

~ 30s
❯ 

### USER
❯ curl -fsSL https://ollama.com/install.sh | sh
  ollama pull qwen3-coder
>>> Cleaning up old version at /usr/local/lib/ollama
[sudo] password for toastedmel0n:  
>>> Installing ollama to /usr/local
>>> Downloading ollama-linux-amd64.tar.zst
######################################################################## 100.0%
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
>>> NVIDIA GPU installed.
Error: could not connect to ollama server, run 'ollama serve' to start it

~ 30s
❯ 

### GEMINI
The "could not connect" error on CachyOS usually stems from a race condition where the systemd service hasn't fully initialized the socket before you ran the pull command. Since CachyOS uses highly optimized kernels (like linux-cachyos), the service initialization is fast, but the GPU driver handshake sometimes lags. 1. The Immediate Fix (Manual Service Check) Run these commands to verify the background process is actually alive: # Check if the service is active and running systemctl status ollama # If it's "inactive" or "failed," start it manually sudo systemctl start ollama # If it's running but still giving the error, restart it to clear the socket sudo systemctl restart ollama 2. The NVIDIA Driver/Group Issue On Arch-based systems like yours, sometimes the render and video groups don't propagate to your user session until you log out and back in. Quick Test: Run groups in your terminal. If you don't see ollama in the list, the installer's group addition hasn't registered yet. The "Brute Force" Start: If the systemd service keeps failing, kill any ghost processes and run it directly in a separate terminal tab to see the real-time logs: # Stop the background service first sudo systemctl stop ollama # Run the server manually to watch for errors ollama serve 3. High-Level Reality Check (Advisor Mode) You are running into basic environment friction. If you can't get the daemon running, your "Immortal Agent" project is going to stall on the very first hurdle of local orchestration. The Mistake: You’re likely trying to run this on the Tiny11 side of your dual-boot or within a misconfigured WSL2 instance if you aren't strictly on the CachyOS partition. If you are on CachyOS, ensure you have the open-nvidia-libs or the proprietary drivers correctly mapped to the ollama user. The Opportunity Cost: Every minute you spend troubleshooting a systemd socket is a minute you aren't refining the trading logic for your bot. The Strategic Move: Once the server is up, run nvidia-smi while the model is loading. If you see your VRAM usage spike past 7.2GB (out of your 8GB), your system will start swapping to that DDR5-4800 RAM. That RAM is "slow" compared to VRAM. Expect a massive latency hit. Would you like me to provide a Python script to verify your NVIDIA Container Toolkit is correctly talking to Ollama on CachyOS?
