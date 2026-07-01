---
category: general
date: 2026-04-07
id: 539968
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- second-brain-vault
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to know the initial steps to start a project from the very beginning.
tags:
- project-setup
- step-by-step-guide
- ai-implementation
---
# So from the beginning what do I need to do?

### USER
So from the beginning what do I need to do?

### GEMINI
This is the day-one checklist. Since you are on Tiny11 with an i7-12700K and an RTX 3070, we are building for speed and VRAM efficiency. Follow these steps in order to get the "Second Me" operational. Step 1: The Environment (Tiny11 Clean-Up) Tiny11 is lean, but often misses the libraries AI tools need to "talk" to your hardware. Install NVIDIA Studio Drivers: Get the latest version from NVIDIA. Studio drivers are more stable for long-running AI workloads than Game Ready drivers. Install Runtimes: Download and install the Visual C++ Redistributable All-in-One pack. Without this, Ollama or Node.js will likely throw "Missing DLL" errors. Install Node.js (LTS): Download the Windows .msi from nodejs.org. This is required for the Obsidian bridge. Install Git: Download Git for Windows. You'll need this to pull the Hermes Agent files. Step 2: The Engine (Ollama & Gemma 4) Download Ollama: Install the native Windows version from ollama.com. Pull the Model: Open PowerShell and run: ollama run gemma4:e4b-q4_K_M Why: This specific "Edge" 4B model at 4-bit quantization fits perfectly into ~4.5GB of your 8GB VRAM, leaving room for your browser and the agent's memory. Set Environment Variable: To keep things snappy, search Windows for "Edit the system environment variables." Under Environment Variables, add a new User Variable: Name: OLLAMA_NUM_PARALLEL Value: 1 Step 3: The Hands (Obsidian MCP) Create your Vault: Open Obsidian and create a new vault at C:\SecondMe\03_Vault. Install "Local REST API": * Settings → Community Plugins → Browse → Search "Local REST API". Install and Enable. Copy the API Key from the plugin settings. Launch the Bridge: Open PowerShell and run: npm install -g @modelcontextprotocol/server-obsidian npx @modelcontextprotocol/server-obsidian --vault "C:\SecondMe\03_Vault" --api-key "YOUR_KEY_HERE" Step 4: The Agent (Hermes v0.6.0) Hermes v0.6.0 is designed to run in WSL2 for full stability, but you can run it on Tiny11 via the uv Python manager for a native feel. Install uv: ```powershell powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" Clone Hermes: git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git cd hermes-agent Setup: Run hermes setup and follow the prompts to connect it to your local Ollama instance (http://localhost:11434). Step 5: The Library (Wikipedia ZIM) Download Kiwix Tools: Get the Windows binary for kiwix-tools. Host the Wiki: Run this in a background terminal to let Hermes "browse" Wikipedia without bloating your vault: .\kiwix-serve.exe --port 8080 "C:\Path\To\Your\wikipedia.zim" Step 6: The "First Mirror" Task Once you have your first chat export (e.g., your Claude conversations.json), drop it into C:\SecondMe\01_Inbox. Run this command in Hermes: "Hermes, I've added my first chat history to the Inbox. Use the Obsidian MCP to create a file in System/Identity.md. Read the history and define my 'Technical Persona.' Tell me three things I am currently over-complicating based on my questions." Immediate Action Items Trigger the Exports: Go to Claude and Gemini right now and hit "Export Data." They can take anywhere from 30 minutes to 24 hours to arrive in your email. Download the ZIM: If you don't have the 2026 Wikipedia ZIM yet, start that download now—it’s roughly 100GB. Does your 970 Evo Plus have enough space for the 100GB ZIM and the 0.5GB model, or should we path the library to a different drive?
