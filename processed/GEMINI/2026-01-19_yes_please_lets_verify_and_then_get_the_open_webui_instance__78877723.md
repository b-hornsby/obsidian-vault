---
id: 962859
source: GEMINI
date: 2026-01-19
tags: ['docker', 'open-webui', 'local-llm', 'setup', 'verification']
category: ai-tools
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is planning to verify his Docker setup and then proceed with setting up an Open WebUI instance.
---
# yes please lets verify and then get the open webui instance set up in docker

### USER
yes please lets verify and then get the open webui instance set up in docker

### GEMINI
To move from "messy execution" to "precision architecture," we need to verify your networking. Because you are using WSL2, your Linux environment is technically a separate machine from your Windows host. If Ollama is running on Windows, WSL2 cannot see it via 127.0.0.1 by default. Phase 1: The Verification (The "Mirror") Run this command inside your WSL terminal to see if you can even talk to the Windows side: curl http://host.docker.internal:11434/api/tags If you see a list of models (JSON): You're good. Proceed to Phase 2. If you get "Connection Refused": Ollama is currently "playing small"—it’s only listening to Windows, not your WSL "network." The Fix: 1. On Windows, search for "Environment Variables" in the Start menu. 2. Add a new User Variable: OLLAMA_HOST with value 0.0.0.0. 3. Restart Ollama (Quit from the system tray and re-open). 4. Run the curl command again. Do not proceed until this works. Phase 2: The Precision Strike (Docker Setup) Once the connection is verified, execute this exactly. Note that I have swapped --network=host for a port mapping (-p). Using host networking in WSL2 often causes port conflicts with Windows services. This way is cleaner and more isolated. Run these commands in order: Grant yourself permissions (so you stop seeing "Permission Denied"): sudo usermod -aG docker $USER (Note: You must close and restart your WSL terminal for this to take effect.) Clean the slate: docker rm -f open-webui Deploy the instance: docker run -d -p 3000:8080 \ --add-host=host.docker.internal:host-gateway \ -v open-webui:/app/backend/data \ -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \ --name open-webui \ --restart always \ ghcr.io/open-webui/open-webui:main Why this works (and yours didn't): -p 3000:8080: Explicitly maps the WebUI to your browser. You can now visit http://localhost:3000 in Windows. --add-host: This is the "bridge." It tells the Docker container exactly how to find the Windows host. host.docker.internal: This replaces the 127.0.0.1 mistake. Inside a container, 127.0.0.1 means "this container," not your PC. Opportunity Cost Warning If you continue to run commands with random spaces and incorrect IPs, you will spend your night debugging network layers instead of actually using the AI. Follow the syntax exactly—every backslash and character matters. Once you run the deployment, would you like me to give you the command to check the logs and confirm the container actually connected to Ollama?
