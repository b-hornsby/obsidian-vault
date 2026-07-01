---
category: homelab
date: 2026-02-03
id: 413398
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that his KDE CachyOS login screen flips between his two
  monitors instead of staying on the main monitor.
tags:
- kde
- cachyos
- login-screen
- multi-monitor
- display-settings
---
# why does my login screen flip between screens (i have 2 monitors) when logging into kde cachyos? it should be locked to my main monitor only 

### USER
why does my login screen flip between screens (i have 2 monitors) when logging into kde cachyos? it should be locked to my main monitor only 

### GEMINI
This isn't a "glitch" in the way you think; it’s a fundamental architectural disconnect between your user session (Plasma) and the system-level login manager (SDDM). The login screen doesn't know what your "main monitor" is because your monitor preferences are stored in your home directory, which is encrypted or locked until you actually log in. To the system, both monitors are just available canvases. Here is the objective reality of your situation and how to fix it. The Problem: SDDM vs. Plasma SDDM (the login manager) is a separate program from KDE Plasma. When you "Apply Plasma Settings" in the SDDM menu, it tries to copy your configuration, but it often fails with multi-monitor layouts because it loads before the drivers have fully negotiated which screen is "Primary." It defaults to whichever monitor responds to the GPU first—often the secondary one. The Precision Plan: Fixes 1. The "Sync" Fix (Easiest) KDE has a built-in tool to force SDDM to mimic your desktop setup. If it’s flipping, the sync is likely broken or hasn't been run since you changed a setting. Go to System Settings > Colors & Themes > Login Screen (SDDM). Click the Apply Plasma Settings... button at the bottom. Enter your password. Crucial: Restart the machine immediately to bake this into the system's startup config. 2. The Physical Port Priority (The Hard Truth) If you are using a mix of DisplayPort and HDMI, or multiple ports on one GPU, your BIOS and the Linux Kernel have a hardcoded "priority list" for which port gets the signal first. The Fact: DisplayPort usually takes priority over HDMI. Port 1 takes priority over Port 2. The Action: If your "main" monitor is on a lower-priority port, the login screen will always jump to the "secondary" one first during the handshake. Swap the cables on your GPU so your primary monitor is in the "first" physical slot. This is the only 100% reliable way to force the login screen to stay put. 3. Force Primary via Configuration (Advanced) If you're on Wayland (which CachyOS defaults to), SDDM uses a minimal compositor to show the login screen. You can force it to ignore the second monitor by editing the SDDM startup script or using a tool like kscreen-doctor to identify the output names and script a layout. However, for CachyOS users, the most effective "clean" way is to ensure you aren't using a custom SDDM theme that lacks multi-monitor logic. Switch back to the Breeze SDDM theme to see if the jumping persists; many third-party "gaming" themes are poorly coded for dual-head setups. Strategy & Blind Spots You’re "playing small" by letting the software dictate your workflow. If this jarring flip is wasting 5 seconds of your focus every morning, the opportunity cost over a year is hours of frustration. Stop trying to "tweak" the software into submission if the hardware ports are the root cause. Linux respects the hardware's internal numbering. If you haven't checked your physical cable order, you're fighting an uphill battle against the kernel's boot sequence. Next Step: Check the back of your GPU—is your main monitor plugged into the first port? If not, swap them and let me know if the "flipping" stops immediately.
