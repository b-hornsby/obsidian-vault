---
category: streaming
date: 2026-03-21
id: 547264
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan wants to fix Discord screen sharing flickering and lag on CachyOS with
  Vesktop on KDE.
tags:
- discord
- screen-sharing
- cachyos
- vesktop
- kde
- streaming-issues
---
# Why does discord screen sharing flicker when using cachyos and vesktop? I’m on kde but when I stream my game to my friends it doesn’t work that great it’s laggy and buggy 

### USER
Why does discord screen sharing flicker when using cachyos and vesktop? I’m on kde but when I stream my game to my friends it doesn’t work that great it’s laggy and buggy 

### GEMINI
The flickering and lag you're seeing on CachyOS is a classic "perfect storm" of how NVIDIA, Wayland, and Electron (which powers Vesktop/Discord) interact. Since you're on a high-performance 3070, the hardware isn't the bottleneck—it's the software handshakes. Here is why it's happening and how to fix it. The Problem: The "Out-of-Sync" Loop Wayland & NVIDIA: While NVIDIA support on Wayland has improved significantly, there is still an issue with Explicit Sync. Essentially, the GPU and the display manager (Kwin) aren't always agreeing on exactly when a frame is ready to be shown, leading to that "flicker" or "stutter." Electron Throttling: Vesktop is an Electron app. When you switch focus to your game, Plasma/Wayland often lowers the priority of background windows. Vesktop's "render" speed drops, causing the stream to look like a slideshow to your friends even if your game feels smooth. DMA-Buf Issues: There's a known bug in Chromium (which Electron uses) regarding how it handles memory buffers (DMA-BUFs) during screen capture on Linux, often resulting in flickering or green screens. The Solutions 1. Enable Hardware Acceleration (The Right Way) In Vesktop, go to Settings > Vesktop Settings. Ensure Hardware Acceleration is ON. Crucial: If you see "Experimental Chromium Features" or "Use Pipewire for Screen Capture," make sure these are enabled. Note: If flickering persists, try toggling Hardware Acceleration OFF just to test. Sometimes the CPU can handle the encode better than a buggy GPU driver handshake. 2. Fix Background Throttling (The "Lag" Fix) KDE Plasma is likely putting Vesktop to "sleep" when it's not the active window. Open System Settings > Window Management > Window Rules. Add a new rule for Vesktop. Add the property Focus stealing prevention and set it to None. Add Lowered priority and set it to No. 3. Use the Ozone Platform Flags Force Vesktop to run natively on Wayland instead of through XWayland (which adds overhead and lag). Launch Vesktop from the terminal with these flags to test: vesktop --enable-features=UseOzonePlatform --ozone-platform=wayland --enable-features=WaylandWindowDecorations If this works better, you can edit your .desktop entry in ~/.local/share/applications/ to make it permanent. 4. The "Nuclear" Fix: XWayland Video Bridge If native Wayland capture is still buggy, install the XWayland Video Bridge (it's in the Cachy/Arch repos). sudo pacman -S xwaylandvideobridge This creates a "fake" window that Discord can "see" more easily, bypassing some of the Wayland security layers that cause lag. 5. Check VRR (Variable Refresh Rate) If you have a G-Sync monitor, KDE’s Variable Refresh Rate can cause flickering during screen sharing. Go to System Settings > Display and Monitor. Set Adaptive Sync to Never just to see if the flickering stops. If it does, you know VRR is the culprit. Pro-Tip for CachyOS Since you're on CachyOS, you have access to the cachyos-settings. Make sure your NVIDIA Power Management is set to "Performance" rather than "Adaptive," as the power-state switching can sometimes trigger flickers during high-load tasks like gaming + streaming. Would you like me to walk you through how to permanently add those Ozone flags to your application launcher?
