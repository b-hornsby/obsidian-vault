---
id: 373883
source: GEMINI
date: 2026-02-09
tags: ['hyprland', 'wayland', 'window-manager', 'cachyos', 'desktop-environment']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan asked about Hyprland, likely considering it as an alternative desktop environment or window manager on CachyOS.
---
# What about hyprland?

### USER
What about hyprland?

### GEMINI
If you’re moving to Hyprland, the situation is somewhere between GNOME’s "mostly fixed" and KDE’s "best-in-class" for NVIDIA. On CachyOS, you are likely using a modern kernel and driver (555 or 560+), which is the baseline requirement to even attempt flicker-free recording on Hyprland. Here is the objective breakdown of why Hyprland might still give you trouble: 1. Explicit Sync Implementation While KDE and GNOME (Mutter) have integrated Explicit Sync directly into their main release pipelines, Hyprland (based on wlroots) had a more fragmented rollout. The Problem: If you are on an older version of Hyprland or have not enabled the explicit sync flags, the "out-of-order frames" bug will return. This manifests as the screen (and the OBS recording) rapidly flickering between the current frame and a frame from 2-3 milliseconds ago. The Fix: You need to ensure these are in your hyprland.conf: render { explicit_sync = 1 explicit_sync_kms = 1 } 2. Variable Refresh Rate (VRR) Sensitivity Hyprland is significantly more sensitive to VRR (FreeSync/G-Sync) than GNOME. The Problem: Hyprland’s "Direct Scanout" (which bypasses the compositor for performance) can clash with OBS’s PipeWire capture. When the frame rate fluctuates, the capture buffer can "miss" a sync point, causing a flicker in the recording. The Fix: Try setting vrr = 0 in your monitor config within Hyprland to see if the flicker stops. If it does, you have a VRR-Compositor timing conflict. 3. Screen Capture Source In Hyprland, how you capture matters more than in KDE: Standard Wayland Capture: Always use the "Screen Capture (PipeWire)" source in OBS. XWayland Bridge: If you are trying to capture an XWayland window (like an older game) specifically, the "Window Capture" source in Hyprland is notoriously prone to flickering because the buffer handoff between XWayland and Hyprland's Wayland core is still "Implicitly Synced" in many cases. 4. CachyOS Optimizations Since you are on CachyOS, you might be using the hyprland-nvidia or hyprland-git packages. CachyOS often applies patches early, but if you are using their customized configs, check if they have specific environment variables set for NVIDIA. Ensure __GL_GSYNC_ALLOWED=0 and __GL_VRR_ALLOWED=0 aren't being forced if you are trying to use VRR, as this can cause flickering in the screen-sharing stream even if the monitor looks fine. The Strategy Hyprland gives you more performance, but KDE gives you more stability for "production" tasks like recording. If you want to make Hyprland work: Update everything: cachyos-rate-mirrors followed by a full pacman -Syu. Toggle Explicit Sync: Add the render block mentioned above. Use GPU Screen Recorder: On Hyprland, the gpu-screen-recorder tool (available in the AUR/Cachy repos) is often superior to OBS because it captures the NVFBC (NVIDIA Frame Buffer Capture) directly, bypassing the PipeWire/Wayland flicker issues entirely. Would you like me to provide the specific gpu-screen-recorder command to test if your hardware can record without the compositor getting in the way?
