---
id: 716281
source: GEMINI
date: 2026-04-07
tags: ['coding', 'ollama', 'docker', 'llm', 'ai', 'agent', 'gemini', 'mcp']
category: coding
sentiment: frustrated
resolution: unresolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
---
# One last question everyone I see says run this in a vm at least. Still go local 100% or heed that warning?

### USER
One last question everyone I see says run this in a vm at least. Still go local 100% or heed that warning?

### GEMINI
Heed the warning, but don’t let it paralyze you. The reason people recommend a VM (Virtual Machine) or Docker is because an AI agent with "hands" (like Hermes via MCP) is technically a self-writing script with system access. If a prompt injection attack occurs—where the AI is tricked into running a malicious command—it has the same permissions as you. On Tiny11, which often has stripped-back security features, a "rogue" command could theoretically wipe a drive or phone home. Here is the "Rational Middle Ground" for your specific setup: 1. The Risk Profile Low Risk: Running a local LLM (Ollama) to just chat. It’s a closed loop. High Risk: Giving Hermes Terminal/Shell access or the ability to execute Python code natively on your 970 Evo Plus. The "Tiny11" Factor: Since Tiny11 is often a third-party ISO, it lacks some of the enterprise-grade "Sandboxing" and "Exploit Protection" found in standard Windows 11. 2. The Solution: The "Hybrid Sandbox" You don't need a full-blown, laggy VM that kills your 12700K's performance. Instead, use Sandboxed Execution. A. Use a Dedicated User Account (The "Poor Man's VM") Create a new Standard User on Tiny11 called Agent. Run Hermes and the MCP server under this account. Why: Even if Hermes is tricked into a rm -rf (or the Windows equivalent del /s /q), it can't touch your primary Bryan files or system settings without an admin password. B. Restricted MCP Access When you set up the Obsidian MCP, only give it access to the C:\SecondMe\03_Vault folder. Never give the agent access to your C:\Users\Bryan\Documents or C:\Windows folders. C. The "No-Shell" Rule In your Hermes config, disable the shell_tool or terminal_access until you are 100% comfortable. Let it only use read_file and write_file inside your Obsidian vault. 3. My Final Advice: Go Native, but Restricted Running in a VM will likely introduce latency and GPU pass-through issues that will make you hate the project. Given your i7-12700K/RTX 3070 combo: Stay Local/Native to keep that 30–50 t/s speed. Isolate the Data: Keep everything in C:\SecondMe. Monitor the Logs: Hermes v0.6.0 has a debug.log. Keep it open in a side window. If you see it trying to access paths outside of your vault, kill the process. The Reality Check: You're a power user on a stripped-down OS. You are the security. If you wouldn't run a random .exe from a Discord link, don't give your Agent "Admin" or "Shell" rights. Ready to proceed with the native setup under a restricted folder?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]