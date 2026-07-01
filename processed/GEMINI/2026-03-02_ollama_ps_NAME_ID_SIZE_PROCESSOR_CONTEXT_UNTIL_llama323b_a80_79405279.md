---
id: 862084
source: GEMINI
date: 2026-03-02
tags: ['local-llm', 'ollama', 'llama3', 'model-status']
category: ai-tools
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/coding.md']
summary: Bryan is checking the status of his Llama3.2 model running in Ollama.
---
# ~
❯ ollama ps
NAME           ID              SIZE      PROCESSOR    CONTEXT    UNTIL               
llama3.2:3b    a80c4f17acd5    2.8 GB    100% GPU     4096       4 minutes from now     

~
❯  

### USER
~
❯ ollama ps
NAME           ID              SIZE      PROCESSOR    CONTEXT    UNTIL               
llama3.2:3b    a80c4f17acd5    2.8 GB    100% GPU     4096       4 minutes from now     

~
❯  

### GEMINI
Perfect. 100% GPU. You’ve successfully avoided the "VM performance trap" and your hardware is doing exactly what you bought it for. Since you have the engine running perfectly on CachyOS, let’s stop playing with the "smoke test" (Llama 3.2 3B) and move to actual utility. Here is your prioritized plan to turn this from a "cool trick" into a high-level tool: 1. Upgrade the Model The 3b model is a lightweight toy—it’s fast, but its reasoning is thin. Since you have the GPU headroom: Run Llama 3.1 8B: This is the current "gold standard" for a balance of speed and intelligence. ollama run llama3.1 Try Mistral Nemo (12B): If you have 12GB+ of VRAM, this model punches significantly higher in logic and coding. ollama run mistral-nemo 2. The "Interface" Problem Running LLMs in a terminal is like driving a Ferrari in a school zone—it works, but the "view" is terrible. To actually use this for research, document analysis, or complex planning, you need a UI. The Strategy: Run Open WebUI in a Docker container. Why? This keeps the "messy" web dependencies (Node, Python, etc.) isolated in a container while it talks to your Native Ollama on the host. This satisfies your original "safety/isolation" urge without killing your performance. The One-Liner (Run this on CachyOS): docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/data --name open-webui ghcr.io/open-webui/open-webui:main Access it: Open your browser to http://localhost:3000. Result: You now have a private, local version of ChatGPT that runs on your metal. 3. Safety Check: Resource Governance You are running on a performance-tuned distro. Ollama, by default, keeps models in VRAM for 5 minutes (as seen in your UNTIL column). If you find your GPU is "stuck" at high memory usage and you need to launch a game or a heavy app, manually kill the model: ollama stop llama3.2:3b The Mirror You've moved from "fear of breaking things" to "100% GPU utilization" in under ten minutes. The lesson? The perceived risk of system breakage is usually an excuse for inaction. You have the hardware; stop treating it like it's fragile. What is your actual goal with LLMs? Are you trying to automate coding, analyze private data, or just see what the hype is about? Tell me, and I'll give you the specific model and workflow for that task.
