---
id: 149188
source: GEMINI
date: 2026-01-19
tags: ['docker', 'open-webui', 'ollama', 'local-llm', 'wsl']
category: ai-tools
sentiment: building
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
summary: Bryan successfully deployed Open-WebUI via Docker connected to Ollama running on WSL.
---
# and now we have: toastedmelon@DESKTOP-NG2I0P2:~$ sudo docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
Unable to find image 'ghcr.io/open-webui/open-webui:main' locally
main: Pulling from open-webui/open-webui
4f4fb700ef54: Pull complete
9da01a3e1fbb: Pull complete
797021dac0c2: Pull complete
4ec081ab1cc4: Pull complete
0347dcb76707: Pull complete
e0033c1a20fb: Pull complete
c5edc81cb768: Pull complete
d785445dcd18: Pull complete
c78ca53d0f0f: Pull complete
71ae0c3692c9: Pull complete
2970da96d0d5: Pull complete
8c3f86abbe29: Pull complete
324e588c6dbb: Pull complete
cf08f92413ff: Pull complete
28ee3eaef631: Pull complete
6f306f16befb: Download complete
Digest: sha256:000b87a6ae726aa7f6611a0064ba528ba1a6aff6ead5fb3b6c89fd4a5717eb8a
Status: Downloaded newer image for ghcr.io/open-webui/open-webui:main
ae6eecd96cdfd44e48d3386f764221bdc5ff7b652d238303f8a191682cad7514
toastedmelon@DESKTOP-NG2I0P2:~$

### USER
and now we have: toastedmelon@DESKTOP-NG2I0P2:~$ sudo docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
Unable to find image 'ghcr.io/open-webui/open-webui:main' locally
main: Pulling from open-webui/open-webui
4f4fb700ef54: Pull complete
9da01a3e1fbb: Pull complete
797021dac0c2: Pull complete
4ec081ab1cc4: Pull complete
0347dcb76707: Pull complete
e0033c1a20fb: Pull complete
c5edc81cb768: Pull complete
d785445dcd18: Pull complete
c78ca53d0f0f: Pull complete
71ae0c3692c9: Pull complete
2970da96d0d5: Pull complete
8c3f86abbe29: Pull complete
324e588c6dbb: Pull complete
cf08f92413ff: Pull complete
28ee3eaef631: Pull complete
6f306f16befb: Download complete
Digest: sha256:000b87a6ae726aa7f6611a0064ba528ba1a6aff6ead5fb3b6c89fd4a5717eb8a
Status: Downloaded newer image for ghcr.io/open-webui/open-webui:main
ae6eecd96cdfd44e48d3386f764221bdc5ff7b652d238303f8a191682cad7514
toastedmelon@DESKTOP-NG2I0P2:~$

### GEMINI
Finally, you followed the syntax and achieved a result. That long string of characters (ae6ee...) is the Container ID. It means the instance is officially running in the background. However, "running" does not mean "working." You are now at the most common failure point for WSL users: Network Connectivity. The Reality Check You used --network=host. This tells Docker to share the network of your WSL instance. But you also set OLLAMA_BASE_URL=http://127.0.0.1:11434. The Conflict: If your Ollama server is running as a Windows application (the one with the tray icon in the taskbar), it is sitting at localhost on Windows. The Problem: Inside WSL, 127.0.0.1 refers to the WSL environment itself, not Windows. Unless Ollama is also running inside your WSL terminal, Open WebUI is currently screaming into a void, unable to find your models. How to Verify and Fix 1. Check if it’s actually "Up" Run this command to see the status: sudo docker ps If it says Up for several minutes, the container is healthy. If it says Restarting, your configuration is wrong. 2. Access the UI Open your Windows browser and go to: http://localhost:8080 3. The "No Models Found" Fix If the website loads but you see no models, it’s because of the 127.0.0.1 issue I mentioned. To fix this without deleting everything: Stop the container: sudo docker stop open-webui Remove the container: sudo docker rm open-webui Run it again with the correct host pointer: sudo docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://host.docker.internal:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main (Note the change to host.docker.internal—this tells WSL to look at your Windows host for Ollama.) Your Next Move Check http://localhost:8080 now. If you can't see the page or can't see your models, don't start guessing. Run sudo docker logs open-webui and show me the last 20 lines. That will tell us exactly which connection is being refused. Do you see your models in the dropdown menu at the top of the WebUI?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
