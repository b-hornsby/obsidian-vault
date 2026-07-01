---
category: homelab
date: 2026-04-07
id: 943423
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: resolved
sentiment: curious
source: GEMINI
tags:
- homelab
- docker
- ai
- agent
- gemini
- token
---
# And docker is a better solution here than a vm? Why do people recommend one then?

### USER
And docker is a better solution here than a vm? Why do people recommend one then?

### GEMINI
People recommend VMs (Virtual Machines) because they offer hardware-level isolation. In a VM, the guest OS has its own kernel; if the AI "breaks out" of its environment, it’s still trapped inside a virtual hardware box. Docker, by contrast, shares your host’s Linux kernel (via WSL2 on Windows). If there’s a kernel-level vulnerability, a truly "rogue" AI could theoretically jump from the container to your actual Tiny11 system. However, for your specific situation, here is why Docker is the superior choice over a traditional VM: 1. The "GPU Passthrough" Nightmare Running an AI on an RTX 3070 inside a traditional VM (like VirtualBox or VMware) is notoriously difficult on Windows. The VM Problem: You often have to "hide" the GPU from Windows and give it exclusively to the VM. This means you can't use your 3070 for gaming or Windows tasks while the agent is running. The Docker Solution: Docker Desktop uses WSL2 (Windows Subsystem for Linux). Microsoft and NVIDIA have spent years optimizing this so that your Windows host and your Docker containers can share the GPU simultaneously. You get near-native speed without losing your GPU in Windows. 2. Resource Efficiency (12700K & 32GB RAM) VMs are "Heavy": A VM requires you to set aside a fixed amount of RAM (e.g., 16GB) and CPU cores that are "locked" even when the AI is idling. Docker is "Lean": It only uses the RAM and CPU it needs at that exact second. If the agent isn't thinking, your 12700K stays cool and your RAM stays free for other apps. 3. The 2026 "Sandbox" Middle Ground In 2026, Docker introduced "Docker Sandboxes" (which use micro-VM technology). It gives you the security of a VM (a separate kernel for the agent) with the convenience of Docker (easy GPU access and file mounting). This effectively kills the "VM vs. Docker" debate by giving you the best of both worlds. The Verdict: Why we are sticking with Docker You are a power user on a high-performance machine. A traditional VM would feel like driving a Ferrari with a speed limiter. We choose Docker because: Speed: You get the full 30–50 tokens/sec from your 3070. Usability: You can keep using Tiny11 normally while the agent works in the background. Scoped Security: By only mounting C:\SecondMe\03_Vault, you’ve already mitigated 99% of the risk. Even if the AI "escapes" the container, it has to then find a way to exploit Tiny11—which is a much higher bar than just deleting a folder it can't see. The "One Source of Truth" Security Rule: "The Agent is a guest in a locked room (Docker). It can only touch the toys I put in the room (The Vault). It cannot see the rest of the house (The PC)." Does this clear up the VM confusion? If so, your only job now is to wait for those data exports and install Docker Desktop.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
