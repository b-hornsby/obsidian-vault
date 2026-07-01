---
id: 943673
source: GEMINI
date: 2026-03-21
tags: ['nvidia-driver', 'modeset-parameter', 'sudo-access']
category: coding
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is trying to read the nvidia_drm modeset parameter with sudo, indicating he's troubleshooting display issues and needs elevated privileges.
---
# ❯ sudo cat /sys/module/nvidia_drm/parameters/modeset
[sudo] password for toastedmel0n:  
Y

~
❯ 

### USER
❯ sudo cat /sys/module/nvidia_drm/parameters/modeset
[sudo] password for toastedmel0n:  
Y

~
❯ 

### GEMINI
The fact that it returned Y means your kernel-level infrastructure is perfectly configured for Wayland. Your NVIDIA 3070 is "talking" to the OS correctly at the base layer. Since the "pipes" are installed correctly, the issue is purely the software handshake between the game, the desktop, and Vesktop. If you are still seeing flickering or lag after everything we've done, here is the absolute final "No-Excuses" checklist to get this to 100% stability. 1. The "XWayland" Verification (The Truth Test) You saved the nano file, but we need to verify if Vesktop is actually respecting those flags. Open Vesktop. Open your terminal and run: xlsclients The Result: * If vesktop is in that list, the flags failed or you are launching it from a different shortcut. This is why it's flickering. If vesktop is NOT in that list, you are running natively on Wayland. 2. The "Window Rules" Final Touch Since we found the properties earlier, ensure they are active. In System Settings > Window Management > Window Rules: Accept focus: Force -> Yes Focus stealing prevention: Force -> None The "Secret" Rule: Add "Screen high dynamic range" (if available) and set to No, or "No screen grabbing" and set to No. This prevents KDE from trying to "protect" the screen from Vesktop’s capture. 3. The i7-12700K "Heavy Lifting" (The Real Fix) Because NVIDIA's Wayland encoder is notoriously buggy for streaming, let's stop using it. Open Vesktop Settings -> Voice & Video. UNCHECK "Hardware Acceleration." UNCHECK "OpenH264 Video Codec." UNCHECK "H.264 Hardware Acceleration." Why this works: Your i7-12700K has enough cores to encode a 1080p 60fps stream without breaking a sweat. By doing this, you bypass the NVIDIA "sync" bugs entirely. The CPU will handle the stream, and the GPU will handle the game. It’s better logistics. The "Brutally Honest" Verdict If you do these three things and your friends still see lag: The Game's FPS is too high: If you are pushing 300+ FPS in a game, the "capture" buffer can't keep up. Cap your game FPS to 144 or 165 (matching your monitor) to give the stream breathing room. Network Jitter: You're in Akron; if you're on a local ISP with high "bufferbloat," your upload might be choking when your game and stream both try to use the bandwidth. Run xlsclients now. Is vesktop in that list?
