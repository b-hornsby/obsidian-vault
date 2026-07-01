---
category: coding
date: 2026-04-07
id: 123698
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- second-brain-vault
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to know the initial steps to start a project from scratch, without
  any models or Docker setup.
tags:
- project-setup
- local-llm-deployment
- step-by-step-guide
---
# Okay so not to get ahead of myself but from the beginning with no models, no docker, nothing.. what do I need to do to get started with this project

### USER
Okay so not to get ahead of myself but from the beginning with no models, no docker, nothing.. what do I need to do to get started with this project

### GEMINI
Since you’re starting from a fresh Tiny11 install with just Obsidian downloaded, we need to build the foundation in a specific order. Because you are using an RTX 3070 on a stripped-down OS, the "Step 0" is actually getting your drivers and environment ready for the heavy lifting. Step 1: The "Hardware Handshake" (Tiny11 Prep) Tiny11 is great, but it often lacks the "helper" files that AI software needs to talk to your GPU. NVIDIA Studio Drivers: Download the latest Studio (not Game Ready) drivers. They are more stable for long-running AI tasks. Visual C++ Redistributables: Download the "All-in-One" pack. Without this, Docker and Ollama will fail with .dll errors. Enable Virtualization: Restart your PC, enter BIOS, and ensure Intel Virtualization Technology (VT-x) is Enabled. Tiny11 needs this for Docker. Step 2: Install the "Cage" (Docker & NVIDIA Toolkit) This is your main security layer. Docker Desktop: Install it and choose the WSL2 Backend (not Hyper-V). NVIDIA Container Toolkit: This is a separate install that allows the Docker "Cage" to see your RTX 3070. Download here. The Test: Open PowerShell and type docker run --help. If it works, the cage is built. Step 3: Install the "Engine" (Ollama) Ollama is the easiest way to run Gemma 4 on Windows. Download Ollama for Windows: ollama.com/download. Move Model Storage (Optional but Recommended): By default, it saves models to your C: drive. Since you have a 970 Evo Plus, make sure it's on your fastest partition. Pull the Model: Open PowerShell and type: ollama pull gemma2:9b (Gemma 4 is the target, but we'll use Gemma 2 9B for the initial setup to verify VRAM limits). Step 4: Prepare the "Brain" (Obsidian Setup) Open Obsidian and do these three things: Create your Vault: Set it to C:\SecondMe\03_Vault. Install Community Plugins: Local REST API: This is the "bridge" that lets the AI write notes in your vault. Smart Connections: This will handle the "Neural Network" linking later. Enable "Advanced" Settings: Go to Editor → Advanced → Toggle "Convert pasted HTML into Markdown." Step 5: The "Data Harvest" (The Exports) While everything is installing, go to these sites and trigger your data exports: Google Takeout: (Select only Gemini). ChatGPT: (Settings → Data Controls → Export). Claude: (Settings → Privacy → Request Export). Grok (X): (Settings → Privacy → Download your data). Step 6: The "Converter" Tools Since you need the chats in Markdown, download these two specific Chrome extensions/tools: Obsidian AI Exporter: This is the current 2026 gold standard. It has a "Sync" button that appears directly on Gemini, Claude, and GPT. It exports them as beautifully formatted Markdown notes with one click. JSON-to-MD Script: If you prefer the "Big Dump" method, I will give you a Python script once your .zip files arrive. Summary Checklist [ ] NVIDIA Studio Drivers installed? [ ] Docker Desktop installed (WSL2 mode)? [ ] Ollama installed? [ ] Obsidian "Local REST API" plugin enabled? [ ] All AI platform exports requested? Brutally Honest Reality Check: The "Neural Network" can't start until the data is in the vault. Don't worry about the AI agent yet—just get the "Cage" (Docker) and the "Engine" (Ollama) installed. Which of those steps are you on right now?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
