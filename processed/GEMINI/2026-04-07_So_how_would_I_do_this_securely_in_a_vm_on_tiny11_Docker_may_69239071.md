---
category: homelab
date: 2026-04-07
id: 376410
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- second-brain-vault
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to securely run his project in a VM on Tiny11, considering
  Docker.
tags:
- vm-security
- docker-containerization
- tiny11-os
- local-llm-security
---
# So how would I do this securely in a vm on tiny11? Docker maybe? I’m not sure

### USER
So how would I do this securely in a vm on tiny11? Docker maybe? I’m not sure

### GEMINI
The warning about running AI agents "naked" on your host machine is valid, but a full VM (Virtual Machine) will absolutely crush your performance. You'll lose the low-latency "real-time" feel of the 12700K and likely struggle with GPU passthrough for the 3070. On Tiny11, the best balance of "Locked-Down Security" and "Raw Power" is Docker Desktop with NVIDIA Container Toolkit. Think of it as a "halfway house": it isolates the agent's files and commands from your Windows system, but still lets the agent use your GPU at 100% speed. The Secure Blueprint (Docker on Tiny11) 1. The Security Boundary Instead of the agent having access to your C:\ drive, we create a "Sandbox" folder. The agent literally won't know the rest of your computer exists. Sandbox Folder: C:\SecondMe\Sandbox Obsidian Access: We only "mount" (share) your Obsidian vault into the container. The agent can't see your browser history, your photos, or your Windows system files. 2. Step-by-Step Setup Step A: Install the "Walls" Install Docker Desktop for Windows: (Make sure to choose the WSL2 Backend during install). Install NVIDIA Container Toolkit: This is the magic "tunnel" that lets the Docker container use your RTX 3070. In Tiny11: Ensure "Virtual Machine Platform" is enabled in Windows Features. Step B: The Secure Engine (Ollama in Docker) Instead of running Ollama on Windows, run it in a container. It’s isolated, but has GPU power. Run this in PowerShell: docker run -d --gpus=all -v ollama_storage:/root/.ollama -p 11434:11434 --name ollama ollama/ollama Step C: The Agent's Cage (Hermes in Docker) You will run the Hermes Agent inside its own container. The Rule: You only map the 03_Vault and 01_Inbox folders. The Command: docker run -it --name second-me-agent ` -v C:\SecondMe\03_Vault:/workspace/vault ` -v C:\SecondMe\01_Inbox:/workspace/inbox ` --net=host hermes-agent:v0.6.0 (This keeps the agent "trapped" inside /workspace/. If it tries to delete C:\Windows, it finds nothing.) 3. The "Human-in-the-Loop" Killswitch Even with Docker, Hermes v0.6.0 has a "YOLO Mode" and a "Safe Mode." Keep YOLO Mode OFF: By default, Hermes will ask for your permission before it runs a terminal command or deletes a file. Manual Approval: You’ll see a prompt like: Agent wants to run: rm -rf /workspace/old_notes. Confirm? (y/n). Result: You are the final firewall. 4. Why this is perfect for your Specs i7-12700K: Docker on Windows uses a utility called Vmmem. Your 12-core CPU handles this background overhead without breaking a sweat. 32GB DDR5: Docker likes to hog RAM. Your 32GB is plenty; you can give the Docker "VM" 16GB and still have 16GB for Windows and gaming. RTX 3070: The NVIDIA Container Toolkit ensures you get the full 8GB VRAM and CUDA cores. No laggy "virtualized" graphics. Your Final Decision Native (Faster, Riskier): Easier to set up, but if you accidentally give the agent a "Delete everything" command, it might actually do it. Docker (Secure, Professional): Takes an extra hour to set up, but you can sleep knowing the agent is in a digital cage. Since you're waiting on those chat exports anyway, do you want to spend the next 20 minutes setting up the Docker "Cage," or do you want to stick to the Native setup and just be very careful with permissions?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
