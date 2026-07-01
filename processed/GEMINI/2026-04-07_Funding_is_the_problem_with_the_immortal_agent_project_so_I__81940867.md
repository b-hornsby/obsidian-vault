---
id: 396305
source: GEMINI
date: 2026-04-07
tags: ['immortal-agent', 'funding', 'project-pause', 'hermes']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan acknowledged funding was blocking the Immortal Agent project and wanted to explore what Hermes could help with.
---
# Funding is the problem with the immortal agent project so I put a pin in it. This is something I’ve been meaning to do and I’m curious what Hermes can help me with

### USER
Funding is the problem with the immortal agent project so I put a pin in it. This is something I’ve been meaning to do and I’m curious what Hermes can help me with

### GEMINI
Putting a pin in "Immortal Agent" is the right move. If funding is the bottleneck, the project is currently a liability, not an asset. Diverting that energy into a "Second Me" system is a better use of your i7-12700K and RTX 3070 because it builds infrastructure you can use for any future project. Since you're diving into Hermes Agent (v0.6.0), here is the direct, unfiltered reality of what this specific tool can do for you and where it’s going to fight your hardware. 1. The "Self-Programming" Reality Hermes isn't just a chatbot; it’s an autonomous skill-builder. What it actually does: When you successfully complete a complex task (like a specific multi-step DeFi data scrape or a Linux kernel optimization), Hermes reflects on the process and writes a Markdown Skill file in ~/.hermes/skills/. The Benefit: Next time you ask for something similar, it doesn't "think" from scratch—it executes that pre-written procedure. It literally gets faster and more accurate the more you use it. The "Second Me" Angle: If you feed it your past Gemini/Claude chats, it won't just "remember" them; it will attempt to extract your decision-making logic into these skills. 2. The Obsidian "Live Sync" (The Gemini X Factor) There is a specific 2026 integration called Hermes Voice Assistant for Obsidian (leveraging Gemini X Native Audio). The Workflow: You can literally talk to your vault while you're working on your PC or out on your phone. The Skill: It uses read_file, edit_file, and create_file tools. You can say, "Hermes, look at my 'CachyOS Config' note and add a section for the new PipeWire latency tweaks we found." It does it in the background without you opening the app. The "Next Level": Use the MCP (Model Context Protocol) support in Hermes v0.6 to connect your Obsidian vault as a live data source. This bypasses the need for a massive "import" and lets the agent query your notes as if they were part of its own brain. 3. Wikipedia: Stop the "ZIM-to-Markdown" Madness You mentioned "extracting text from the ZIM in batches." Don't do that. * The Efficiency Play: Use the Code Wiki skill pattern. Instead of turning Wikipedia into 6 million markdown files, keep the ZIM file as a Read-Only Reference. How Hermes handles it: When you ask a question, Hermes uses the libzim tool to pull only the relevant article, summarizes it, and then—only if it’s important—creates a linked atomic note in your Obsidian vault. This keeps your vault clean and your i7-12700K from crying during an Obsidian re-index. 4. The Hardware Strategy (RTX 3070 / 8GB VRAM) You are at the limit. To make this "Second Me" feel "alive" (low latency), you must: Use Gemma 4:e4b (4-bit quantization). Do not try to run the 26b MoE locally; the context swapping will kill the "agentic" feel. Enable FTS5 (Full-Text Search) Memory. Hermes uses a SQLite backend for its memory. This is much lighter on VRAM than a full vector database (RAG) and is perfect for searching years of chat logs. Your Immediate "Next Level" Task If you want to see if Hermes is worth the hype, do this tonight: Install Hermes Agent v0.6.0 via the Nix Flake or Docker. Point it at your Obsidian Vault using the context_files configuration. Run the "Reflection" command on your exported Gemini/Claude chats. Ask it: "Based on my past chats, what is the one technical blind spot I consistently ignore when I start a new project?" If it gives you a generic answer, the setup is wrong. If it calls you out on a specific habit (like over-complicating infrastructure before having a product), then you’ve successfully built your "Mirror." The Opportunity Cost: Every hour you spend trying to "perfect" the Wikipedia import is an hour you aren't using the agent to actually summarize and link your own unique thoughts. Wikipedia is everywhere; your logic is only in your vault. Focus there first. Does this feel like a project you can actually execute this week, or is it another "Immortal Agent" scale-trap?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
