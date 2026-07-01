---
category: streaming
date: 2026-04-06
id: 667354
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was noting that NDI webcam appeared as a camera source option, contradicting
  earlier assumptions about NDI availability.
tags:
- ndi
- webcam
- camera-source
- obs
- troubleshooting
---
# When I choose a camera source I do see ndi webcam as an option?

### USER
When I choose a camera source I do see ndi webcam as an option?

### GEMINI
YES. If you see "NDI Webcam" as an option in TikTok Live Studio, use it immediately. This is the "holy grail" for your setup because it bypasses the buggy Windows Virtual Camera driver entirely. NDI (Network Device Interface) sends video data directly through your local memory/network protocol. It is professional-grade, handles high-motion games like CS2 much better, and is significantly lighter on your 3070 than the Virtual Camera or Window Capture methods. How to Link Them Up To make this work, you need a small "bridge" between OBS and TikTok: Install the "NDI Tools" (Free): Download and install the NDI Tools for Windows. Open "NDI Webcam" (formerly called Virtual Input): This is a small app that comes with the NDI Tools. Open it, and it will sit in your system tray (bottom right by the clock). In OBS: Make sure you have the OBS-NDI plugin installed. Go to Tools -> NDI Output Settings. Check the box for "Main Output" (or if Aitum Vertical has its own NDI output in its settings, use that). In the NDI Webcam App (System Tray): Right-click the icon, select your PC name, and then select the OBS NDI output you just turned on. This "tricks" TikTok into thinking OBS is a real, hardware-plugged-in webcam. In TikTok Live Studio: Select NDI Webcam as your camera source. Why this fixes your CS2 lag: Zero-Copy Memory: NDI moves video data without the CPU having to "re-wrap" it constantly, which is what the Virtual Camera does. Hardware Priority: NDI is designed for live broadcasting. Windows recognizes it as a high-priority stream, whereas it often treats "Virtual Camera" as a background process that gets throttled when CS2 gets intense. The "Brutal" Efficiency Check Even with NDI, you are still running two massive programs. To guarantee no stutters in CS2: Cap your CS2 FPS: If you're hitting 300+ FPS, your GPU has zero "breathing room" to even send the NDI signal. Cap it to your monitor's refresh rate (e.g., fps_max 144). Admin Mode: I cannot stress this enough—Run both OBS and TikTok Live Studio as Administrator. This is the difference between a smooth stream and a stuttering mess. Try the NDI route. It’s the "pro" way to handle dual-streaming when a platform like TikTok tries to lock you out.
