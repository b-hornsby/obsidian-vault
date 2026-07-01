---
id: 235912
source: GEMINI
date: 2026-03-21
tags: ['kwin-settings', 'window-management', 'focus-stealing', 'desktop-environment']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is confirming that he has focus stealing prevention and accept focus settings enabled, likely as part of troubleshooting window behavior.
---
# so i have focus stealing prevention and accept focus

### USER
so i have focus stealing prevention and accept focus

### GEMINI
Since KDE Plasma 6.x (your current environment) has streamlined these menus, having Focus Stealing Prevention and Accept Focus is actually the "Golden Pair" for solving the lag. Here is exactly how to set those two, followed by the one final "Logistics" check to ensure your stream is smooth. 1. Configure the Two Rules You Found In your Vesktop Fix rule in KDE System Settings: Focus stealing prevention: * Set to Force. Set to None. Why: This stops KDE from "blocking" Vesktop’s requests to update its window (the stream) while you are clicking around in your game. Accept focus: * Set to Force. Set to Yes. Why: This ensures the window manager treats Vesktop as an "active" participant in the desktop session, preventing it from being put into a low-power "sleep" state. Apply these and click OK. 2. The Final "Handshake" Check Since you successfully saved the Nano file with the Wayland flags earlier, you have already fixed the "Translation Layer" flickering. Now you just need to ensure the NVIDIA Driver isn't fighting the Screen Capture. In Vesktop Settings (click the Gear icon in the bottom left of Discord/Vesktop, then scroll to the bottom for "Vesktop Settings"): Go to Capturer Settings. Make sure Use PipeWire is Enabled. Experimental Tip: If the stream is still laggy, look for "Force NVENC" or "Hardware Acceleration." * Try it ON first. If it lags, turn it OFF. * Brutal Truth: With an i7-12700K, your CPU is actually powerful enough to "software encode" the stream better than a buggy NVIDIA driver on Wayland can. 3. Restart the Desktop Session For the Nano changes and the Window Rules to fully "glue" together: Close Vesktop completely (check your system tray/task manager). Log out of your KDE session and log back in (or just restart). Launch Vesktop from your Application Menu (not the terminal). The "How do I know it's fixed?" Test Start a stream to a friend and look for these three things: No flickering: (The Nano flags fixed this). No "slideshow" effect: (The Window Rules fixed this). No "Black Screen": (The PipeWire setting in Vesktop fixed this). One last thing for an Akron/CachyOS user: Since you're on CachyOS, you have the cachyos-settings package. Open a terminal and run cachyos-settings-gui. Under the Tweaks or System tab, make sure "Latency" is set to "Low Latency" rather than "Powersave." This ensures your i7 stays awake to process those stream frames. Would you like me to show you how to check your network "Niceness" levels if your friends say the audio is lagging too?
