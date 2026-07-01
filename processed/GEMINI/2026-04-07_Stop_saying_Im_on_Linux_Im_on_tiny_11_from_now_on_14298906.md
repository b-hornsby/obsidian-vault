---
id: 872990
source: GEMINI
date: 2026-04-07
tags: ['homelab', 'ollama', 'ai', 'agent', 'claude', 'gemini', 'model', 'mcp']
category: homelab
sentiment: building
resolution: abandoned
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/homelab.md']
---
# Stop saying I’m on Linux. I’m on tiny 11 from now on

### USER
Stop saying I’m on Linux. I’m on tiny 11 from now on

### GEMINI
Copy that. You’re on Tiny11. That actually simplifies a few things—you’ve stripped the Windows bloat, which buys us back some of that precious 32GB RAM, but it means we have to be more deliberate about your environment. Since Tiny11 often lacks the "extras" (like WSL or certain telemetry-heavy drivers), we’re going to build this as a lean, native Windows power-user setup. Here is your objective-driven, step-by-step roadmap to making the "Second Me" a reality on Tiny11. Phase 1: The Engine (Native Windows Ollama) Don't mess with WSL2 if you don't have to; it adds an overhead layer. We’ll run Ollama as a native Windows service. Download Ollama for Windows: Install it directly. Pull the "Efficiency" Quant: * Open PowerShell and run: ollama run gemma4:e4b-q4_K_M Why: At 4-bit, this hits about ~4.5GB VRAM. Since Tiny11 isn’t wasting VRAM on "Widgets" and "Teams," your RTX 3070 will have more breathing room for the 16k context window we need for your chat history. Environmental Variable: Set OLLAMA_NUM_PARALLEL=1 in your System Environment Variables to ensure all 8GB of VRAM stays dedicated to one high-speed stream. Phase 2: The Hands (Obsidian MCP & REST API) Since Tiny11 is your "daily driver," we’ll use the Model Context Protocol to let the agent talk to Obsidian while you're using it. Obsidian Setup: Install the Local REST API community plugin. Enable it and Copy the API Key. The Bridge (Node.js): Install the latest LTS Node.js for Windows. In PowerShell, run: npm install -g @modelcontextprotocol/server-obsidian The Connection: * You’ll need to point Hermes to this server. On Windows, you’ll usually run the server with a command like: npx @oleksandrkucherenko/mcp-obsidian --vault "C:\Users\Bryan\Documents\YourVault" --api-key "YOUR_KEY" Phase 3: The Library (Kiwix-Serve for Wikipedia) We aren't converting the ZIM to Markdown. We are going to "host" it locally so the agent can browse it like a private website. Kiwix Tools for Windows: Download the kiwix-tools Windows binary. The Local Host: Run this in a background terminal: kiwix-serve.exe --port 8080 "D:\Data\wikipedia_en_all_maxi_2026.zim" The Agent's Access: We will give Hermes a "Browser Skill." Instead of reading a file, it will query localhost:8080 to find facts. This keeps your Obsidian vault 100% clean of Wikipedia "clutter." Phase 4: The Ingestion (Building the "Mirror") This is the "Brutally Honest" part where the agent looks at your past. Prep the Exports: Put your Gemini and Claude exports into a folder (e.g., C:\AI_History). The Hermes Analysis: Launch Hermes Agent. The Prompt: "Hermes, use the Obsidian MCP to create a file called System/Persona/Logic_Patterns.md. Scan C:\AI_History and list the 3 most frequent technical 'rabbit holes' I fall into. Don't be nice. Show me where I waste time." Skill Extraction: * Tell it: "Identify the working code snippets from my 'Operation Immortal Agent' chats. Save them as functional 'Skills' in my vault so I can call them later." The Reality Check (Tiny11 Edition) The Driver Warning: Since you're on Tiny11, make sure you manually installed the latest NVIDIA Game Ready or Studio drivers. Tiny11 often skips the "Auto-Update" stuff, and without the latest CUDA libraries, Ollama will default to your CPU and be painfully slow. The "Wait" Factor: Building the initial index of your chats will take about 10–20 minutes of high CPU/GPU usage. Let it finish. Once the index is in the Hermes SQLite DB, the "Second Me" will be near-instant. The Bottom Line: You have the hardware, and Tiny11 is the leanest OS to run it on. The only thing standing between you and this system is the 2 hours of configuration it takes to link the MCP server. Are we starting with the Ollama model pull or the Obsidian REST API setup?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]