---
category: general
date: 2026-03-02
id: 448008
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking what the next steps are after installing a piece of software
  natively.
tags:
- native-installation
- software-setup
- general
---
# so now that installed native, now what? 

### USER
so now that installed native, now what? 

### GEMINI
Now that it's installed, you need to verify it’s actually using your hardware and not just dragging your CPU through the mud. Since you're on CachyOS, you have the advantage of a high-performance environment, but Ollama needs to "see" your GPU to be useful. 1. The Smoke Test Run a small, fast model to ensure the engine is turning over. ollama run llama3.2:3b Action: Type a prompt like "Tell me a joke." The "Feel" Test: If the text streams out instantly, you're likely on GPU. If it chunks out word-by-word like an old typewriter, you're on CPU. 2. Verify GPU Acceleration (The "Advisor" Check) Don't guess. Check the math. While a model is running, open a second terminal and run: ollama ps Look at the "PROCESSOR" column: 100% GPU: Perfect. You are fully accelerated. 100% CPU: Failure. You are wasting electricity and time. Mixed (e.g., 70%/30%): Your model is too big for your VRAM, and it's "spilling over" into your system RAM. Expect slow performance. 3. Monitoring Your Hardware Since you care about "safety" and system health, monitor the actual heat and load. Install nvtop (it works for both NVIDIA and AMD): sudo pacman -S nvtop nvtop Keep this open. When you ask Ollama a question, you should see the GPU Graph spike. If it doesn't move but your CPU fans start screaming, Ollama isn't configured correctly for your drivers. 4. Troubleshooting CachyOS Specifics If ollama ps shows 100% CPU, here is your fix based on your hardware: For NVIDIA: Ensure you have the nvidia or nvidia-open drivers installed. CachyOS usually handles this, but verify with nvidia-smi. For AMD: You may need to add yourself to the render group: sudo usermod -aG render $USER sudo usermod -aG video $USER Then log out and back in. 5. Next Level: The "No-Distraction" UI Using the terminal is fine for testing, but for "high-level" work, you want a clean interface. I recommend Open WebUI. Since you wanted isolation earlier, this is where Docker actually makes sense—not for the backend, but for the frontend. Would you like the one-liner to launch a ChatGPT-style web interface that connects to your native Ollama?
