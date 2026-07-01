---
category: general
date: 2026-03-21
id: 658131
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan wants a full explanation of the issue he's facing and how to fix it
  from scratch.
tags:
- troubleshooting
- problem-diagnosis
- step-by-step
---
# So from the beginning what issue am I describing and how do I fix it?

### USER
So from the beginning what issue am I describing and how do I fix it?

### GEMINI
To cut through the noise: You are describing a synchronization failure between your NVIDIA GPU and the Wayland display protocol, combined with resource throttling from your desktop environment (KDE). Basically, your computer is too smart for its own good—it's trying to save power and "perfectly" sync frames while you're trying to blast a high-bandwidth video stream to your friends. The Two Core Issues The Flicker (Explicit Sync Issues): On NVIDIA + Wayland, your GPU and the screen (Kwin) often disagree on when a frame is "finished." This causes that rapid flashing or black-bar flickering. The Lag (Electron Throttling): Vesktop is based on Chromium. When you're in a game, KDE sees Vesktop as a "background task" and lowers its priority. This makes your stream look like 5 FPS to your friends, even if your game is running at 144 FPS. The Precise Fix (Step-by-Step) Step 1: Force Native Wayland (Eliminate the "Middleman") By default, Vesktop often runs through XWayland (a compatibility layer). This adds lag. You need to force it to speak Wayland natively. Open your terminal. Launch Vesktop with these specific flags to see if it fixes the flicker: vesktop --enable-features=UseOzonePlatform --ozone-platform=wayland --enable-features=WaylandWindowDecorations If this works, you can permanently add these flags to your launcher (usually found in ~/.local/share/applications/vesktop.desktop). Step 2: Stop KDE from Throttling Vesktop You need to tell KDE that Vesktop is a high-priority "VIP" app that shouldn't be slowed down. Open System Settings > Window Management > Window Rules. Click Add New... Set Description to "Vesktop Stream Fix." Set Window class to "Exact Match" and type vesktop. Click Add Property and find Focus stealing prevention. Set it to Force and None. Click Add Property and find Lowered priority. Set it to Force and No. Step 3: Disable VRR (The "G-Sync" Flicker) If your monitor has Variable Refresh Rate (G-Sync/FreeSync), it often causes flickering on Wayland when sharing a window that isn't running at the same refresh rate as the monitor. Go to System Settings > Display and Monitor. Set Adaptive Sync to Never. (You can turn it back on when you're done streaming, but for now, it's a known conflict). Step 4: Toggle Hardware Acceleration In Vesktop settings (under Vesktop Settings, not Discord's native settings): If it's ON: Turn it OFF. Sometimes the NVIDIA encoder "fights" with the Wayland capture tool. If it's OFF: Turn it ON. Note: One way usually works better than the other depending on your specific kernel version in CachyOS. The "I just want it to work" Alternative If the above is still giving you grief, the most stable "Pro" workaround on CachyOS right now is to install the XWayland Video Bridge: sudo pacman -S xwaylandvideobridge Once installed, start it, and it will act as a translator that allows Vesktop to capture your game windows without the Wayland-specific flickering. Would you like me to show you how to automate those terminal flags so you don't have to type them every time you open Vesktop?
