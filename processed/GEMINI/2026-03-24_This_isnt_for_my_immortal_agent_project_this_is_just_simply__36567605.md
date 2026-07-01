---
id: 347789
source: GEMINI
date: 2026-03-24
tags: ['open-claw', 'setup', 'personal-use', 'ai-agent']
category: ai-tools
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md', ''nodes/projects/operation-immortal-agent.md'']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarifies he's setting up Open Claw for personal use, not for his immortal agent project.
---
# This isn’t for my immortal agent project this is just simply to be able to set up open claw and to be able to use it

### USER
This isn’t for my immortal agent project this is just simply to be able to set up open claw and to be able to use it

### GEMINI
Since you're on Tiny11, keeping the "Brain" of OpenClaw in the cloud is the smartest move you can make. It protects your stripped-down OS from the agent's full-system access while letting you use your RTX 3070 at home to power the actual AI models for free. Here is the precise, low-friction path to get this set up. 1. The Cloud: Your "Command Center" Don't waste time manually configuring a server. By March 2026, several providers offer one-click images that handle the Docker/Node.js mess for you. Best Value: Hostinger VPS (KVM 2 or higher) or Tencent Cloud Lighthouse. Why: They have a pre-configured OpenClaw template. You literally click "Deploy," and it gives you a public IP and a Gateway Token. Alternative (Pro): If you want to use a standard Ubuntu 24.04 VPS (DigitalOcean/Linode): curl -fsSL https://openclaw.ai/install.sh | bash openclaw onboard --install-daemon 2. The Model: Using Open Source for Free To avoid paying Anthropic or OpenAI every time the agent "thinks," you’ll point the Cloud instance back to your Tiny11 PC. On your Tiny11 PC: Install Ollama. The Model: Run ollama run qwen2.5-coder:7b. It is the current "king" of open-source agent models and fits perfectly in your 8GB VRAM. The Bridge: Install Tailscale on both your Tiny11 PC and the Cloud VPS. This gives them a private, secure connection. The Link: In the OpenClaw Cloud Dashboard, set your Model Provider to Ollama and the URL to your PC's Tailscale IP (e.g., http://100.x.y.z:11434). 3. The "NemoClaw" Security Upgrade As seen in the recent NVIDIA news (March 2026), they released NemoClaw to fix the security holes in standard OpenClaw. Since you're on a lean OS like Tiny11, I highly recommend using this wrapper. It puts the agent in a "sandbox" so it can't accidentally wipe your system. To install the security wrapper on your Cloud VPS: curl -fsSL https://nvidia.com/nemoclaw.sh | bash This will automatically wrap your OpenClaw instance in OpenShell, which limits the agent to only writing files in a specific /sandbox folder. 4. Brutal Reality Check RAM is the Killer: Your Cloud VPS needs at least 4GB of RAM (8GB recommended). If you try to run NemoClaw on a 1GB or 2GB "micro" instance, the Linux OOM (Out Of Memory) killer will crash the agent every time it tries to think. Tiny11 Stability: Ensure you've disabled "Sleep" mode on your PC. If your Tiny11 machine goes to sleep, your Cloud agent loses its "brain" (the Ollama model) and will just sit there throwing errors. The "Vibe" Factor: Since you're a beginner at coding, stick to the Dashboard UI. Don't try to configure the YAML files manually yet. Get it running in the browser first. Next Step Would you like me to give you the specific configuration block to paste into your Cloud OpenClaw settings to link it to your home Ollama?
