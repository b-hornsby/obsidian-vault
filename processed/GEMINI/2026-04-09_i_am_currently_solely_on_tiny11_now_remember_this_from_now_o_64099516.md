---
id: 395729
source: GEMINI
date: 2026-04-09
tags: ['tiny11', 'brainstorm-mode', 'pre-planning', 'environment-setup']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/second-brain-vault.md', 'nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed he's on Tiny11, hasn't started building yet, is in brainstorm mode, and asked what needs to be addressed before proceeding.
---
# i am currently solely on tiny11 now (remember this from now on). i havent started any of this right now we're just in brainstorm mode. what needs to be addressed before we proceed?

### USER
i am currently solely on tiny11 now (remember this from now on). i havent started any of this right now we're just in brainstorm mode. what needs to be addressed before we proceed?

### GEMINI
If we're locking in on Tiny11 as your sole environment for now, we need to address three immediate technical "tripwires" before you touch a line of code. You’re building on a stripped-back OS to save resources, but you’re about to invite a resource-hungry Docker monster into the room. Here is what needs to be addressed immediately: 1. The "Efficiency Mode" Death Trap Tiny11 doesn't stop Windows from being Windows. Windows 11 has a "Process Governor" that loves to tag WSL2 and vmmem with Efficiency Mode (the green leaf). The Problem: Once this happens, your CPU performance will drop by ~75%. Since you're using a MoE-style or dense Gemma 4 model, you'll see token generation speeds drop from "usable" to "painfully slow." The Fix: Before you start, you need to verify you can kill Efficiency Mode permanently. Use the Registry to set UseEcoQoS = 0 for docker-desktop.exe and ensure your Power Plan is set to Ultimate Performance. If you can't keep the leaf icon away from Task Manager, your "Second Me" will feel like it has a lobotomy. 2. The Gemma 4 VRAM Reality Check You mentioned Gemma 4 E4B. This model is the current "sweet spot" for 8GB cards, but "sweet spot" means you're at the absolute limit. The Math Check: * Model (4-bit): ~4.5GB - 5.0GB. KV Cache (Context): If you want a 16k+ context window (essential for reading your past logs), you’re looking at another 1.5GB - 2GB. Total: ~7GB. The Conflict: Your RTX 3070 is also driving your display. Even in Tiny11, the desktop takes ~1GB. Pre-Flight Action: You must use a "headless" or "minimal" display profile. If you have any "Vibe Coder" RGB software or secondary monitors running off the 3070, kill them. You have zero margin for error here. 3. The Docker Desktop Resource Tax Docker Desktop on Windows isn't just a container runner; it’s a Linux VM (WSL2) with a heavy GUI wrapper. The Strategic Shift: Since you're on Tiny11, do not use the Docker Desktop installer. It’s bloatware for your specific use case. The Alternative: Install Docker Engine directly inside a raw WSL2 Ubuntu/Debian distro. This bypasses the Docker Desktop GUI, saves you ~1-2GB of system RAM, and gives you better control over the "Efficiency Mode" issues mentioned above. 4. The "Second Brain" File Pathing You mentioned mounting C:\SecondMe\03_Vault. The Performance Warning: WSL2 (and by extension Docker) is notoriously slow when accessing files on the Windows host (/mnt/c/). The Correction: If you want "sub-second search results" as your blueprint claims, the Obsidian Vault should live inside the WSL2 file system, not on the Windows C: drive. You can still point the Windows Obsidian app to the WSL path (\\wsl$\ubuntu\home\user\vault), but the source must be Linux-native for the agent to read/write without massive latency. The "Advisor" Verdict You are trying to run a high-level intelligence operation on a consumer-grade mid-range card while fighting an OS that wants to throttle you. What I need from you before Step 1: Confirm: Are you willing to ditch the Docker Desktop GUI and go CLI-only in WSL2 to save that 2GB of RAM? Verify: Open Task Manager right now. How much VRAM is "In Use" while you're just sitting at the desktop? If it's over 1.0GB, we need to strip your startup apps even further. Are we optimizing for comfort (GUI, Windows folders) or performance (CLI, WSL paths)? Pick one.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/second-brain-vault|Second Brain Vault]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
