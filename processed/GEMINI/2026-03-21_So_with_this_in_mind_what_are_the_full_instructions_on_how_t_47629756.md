---
category: general
date: 2026-03-21
id: 928119
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan wants complete step-by-step instructions to fix an ongoing issue.
tags:
- troubleshooting
- full-instructions
- step-by-step-fix
---
# So with this in mind what are the full instructions on how to get this issue fixed

### USER
So with this in mind what are the full instructions on how to get this issue fixed

### GEMINI
To get this fixed, we’re going to address the synchronization failure between your NVIDIA 3070 and the Wayland protocol. This requires a two-pronged approach: forcing the app to run natively and adjusting how your OS (CachyOS/KDE) handles that specific window. Follow these steps exactly to resolve the flickering and lag. Step 1: The "Clean Handshake" (Vesktop Setup) Standard Discord runs through a compatibility layer called XWayland, which is the primary cause of flickering. We need to force Vesktop to use Native Wayland. Create a local override: Open your terminal and run: mkdir -p ~/.local/share/applications/ cp /usr/share/applications/vesktop.desktop ~/.local/share/applications/ Edit the launcher: Open the file with a text editor (e.g., nano ~/.local/share/applications/vesktop.desktop). Update the Exec line: Find the line starting with Exec= and change it to: Exec=vesktop --enable-features=UseOzonePlatform,WaylandWindowDecorations --ozone-platform=wayland --enable-gpu-rasterization --enable-zero-copy %U This forces the app to talk directly to Wayland and uses your 3070 for rendering, eliminating the translation lag. Step 2: The "VIP Treatment" (KDE Window Rules) KDE Plasma often "throttles" background apps to save power. You need to tell it that Vesktop is a high-priority process. Go to System Settings > Window Management > Window Rules. Click Add New... and set the name to "Vesktop Fix." Set Window class (application) to Exact Match and type vesktop. Click Add Property and search/add these three: Focus stealing prevention: Set to Force -> None. Lowered priority: Set to Force -> No. Allow compositing: Set to Force -> Yes. Click Apply. Step 3: Kill the "G-Sync" Conflict Variable Refresh Rate (VRR) is notorious for causing flickering during screen capture on NVIDIA + Wayland. Go to System Settings > Display and Monitor. Set Adaptive Sync to Never. Note: You can turn this back on for solo gaming, but it's a known deal-breaker for stable streaming on your current setup. Step 4: Install the Fail-Safe (XWayland Bridge) If you still experience issues when sharing a specific window (instead of the whole screen), install the specialized bridge tool for KDE: sudo pacman -S xwaylandvideobridge Once installed, ensure it is running in your system tray before you start your stream. The "Brutally Honest" Check If you complete these steps and it is still laggy, go into Vesktop Settings (the gear icon, then "Vesktop Settings" at the bottom left) and disable Hardware Acceleration. While it sounds counterintuitive to disable your GPU, NVIDIA's Linux encoders can sometimes "choke" when trying to play a high-end game and encode a stream simultaneously. Letting your CPU (the i7-12700K) handle the stream encoding—which CachyOS is highly optimized for—will often provide a much smoother 60 FPS experience for your friends. Would you like me to show you how to check if your current CachyOS kernel has "Explicit Sync" enabled for your NVIDIA driver?
