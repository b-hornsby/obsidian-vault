---
category: general
date: 2026-03-21
id: 070084
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is asking for a holistic diagnosis of what's wrong with his current
  setup.
tags:
- troubleshooting
- system-diagnosis
---
# So overall what’s wrong?

### USER
So overall what’s wrong?

### GEMINI
To be brutally honest: You’re hitting the "Early Adopter Tax" for choosing a cutting-edge Linux setup while using NVIDIA hardware. You’ve built a high-performance machine, but you’re trying to run a professional-grade logistics operation (your gaming/streaming) over a bridge that’s still under construction. Here is the objective breakdown of why your setup is failing you right now: 1. The "Wayland-NVIDIA" Friction You are using Wayland (KDE’s default) on an NVIDIA 3070. Historically, these two have hated each other. While it's getting better, they still struggle with Explicit Sync. The Reality: Your GPU is finishing a frame, but the display server (Kwin) isn't ready for it, or vice versa. This lack of synchronization is the literal cause of that flickering. You’re essentially watching a "fight" between your driver and your desktop environment in real-time. 2. The Electron Bottleneck Vesktop (and Discord) is built on Electron, which is basically a Chrome browser stripped down to run as an app. The Reality: Chrome’s implementation of Wayland screen sharing is, frankly, mediocre. It relies on PipeWire to "capture" the screen, but because NVIDIA's drivers handle memory differently than AMD/Intel, the handoff between the screen capture and the app is laggy and buggy. 3. Resource Deprioritization KDE Plasma is designed to be efficient. When you are focused on your game, it assumes your background apps (Vesktop) don't need maximum resources. The Reality: Your system is intentionally "starving" your stream to keep your game smooth. In a Windows environment, this is handled fairly seamlessly; in Linux, you often have to manually tell the OS not to choke the background process. 4. The XWayland "Translation" Lag If Vesktop is running through XWayland (the compatibility layer for old apps), you’re adding an extra step to every single frame being processed. The Reality: You're asking your system to translate "Windows-style" instructions into "Wayland-style" instructions, capture them, encode them, and send them over the web—all while playing a high-intensity game. It’s an inefficient chain that leads to the "slideshow" effect your friends see. The Verdict There is nothing "broken" with your hardware. The issue is a configuration mismatch. You are running a highly optimized, custom OS (CachyOS) but using the "out of the box" settings for a streaming app that wasn't built with your specific Linux kernel/NVIDIA combo in mind. The most direct "Next Level" move: If you want to stop making excuses for the lag, you need to force Vesktop to run natively on Wayland (using the flags I mentioned) and ensure XWayland Video Bridge is handling the handshake. Would you like me to give you the exact terminal commands to "Full Send" these optimizations so you can stop being the laggy friend in the group chat?
