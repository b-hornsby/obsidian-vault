---
id: 541880
source: GEMINI
date: 2026-03-21
tags: ['icue', 'uninstall', 'rgb-control', 'software-cleanup']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wants to uninstall iCUE and transition to a different RGB control solution.
---
# So start your finish I want to uninstall icue and get on the right path

### USER
So start your finish I want to uninstall icue and get on the right path

### GEMINI
To get your i7-12700K / RTX 3070 rig shining on Tiny11 without the bloat, we need to treat this like a clean deployment. iCUE leaves "ghost" drivers that will conflict with OpenRGB if not purged correctly. Follow this exact "Operations" checklist. Phase 1: The Scorched Earth Uninstall iCUE is notorious for leaving background services that "lock" your hardware, preventing OpenRGB from talking to it. Standard Uninstall: Go to Settings > Apps > Installed Apps and uninstall Corsair iCUE. Choose "Delete settings for all users" if prompted. Purge AppData: Press Win + R, type %appdata% and delete the Corsair folder. Repeat this for %localappdata%. Registry Cleanup: Press Win + R, type regedit. Navigate to HKEY_CURRENT_USER\Software and HKEY_LOCAL_MACHINE\SOFTWARE. Delete the Corsair folders in both. The "Cold Boot" (Vital): Shut down. Unplug the PC from the wall. Hold the power button for 30 seconds. This drains the capacitors on your Commander Pro/Core or RAM so they "forget" the iCUE instructions. Phase 2: Building the Foundation (Tiny11 Fixes) Tiny11 is missing the libraries OpenRGB needs to communicate with your SMBus (RAM) and USB controllers. Install C++ Runtimes: OpenRGB will crash or fail to open without these. Download and install the Visual C++ Redistributable All-in-One (2015-2022). Disable Windows "Dynamic Lighting": This is a new Windows 11 feature that fights other RGB apps. Go to Settings > Personalization > Dynamic Lighting and toggle it OFF. Phase 3: The OpenRGB "Full Send" Download: Get the latest 64-bit Windows Pipeline/Experimental build from OpenRGB.org. PawnIO Driver: For your RAM and Motherboard to show up, you must install the PawnIO driver. This is the Windows equivalent of the kernel modules you used in CachyOS. First Launch: Right-click OpenRGB.exe and select Run as Administrator. Rescan: Click Find Devices. Your Corsair fans (via Commander Core/Node) and RAM should pop up. Phase 4: Automation (Set and Forget) Since you’re on a performance-tuned OS, you don't want a GUI running. Set your colors in OpenRGB. Go to the Settings tab. Enable "Start Minimized" and "Open at Login". If your Corsair gear supports it, use the "Save to Device" button—then you can actually delete OpenRGB and the lights will stay that way forever (until the next power loss). Strategic Advice: You switched to Tiny11 for efficiency. iCUE on Tiny11 is like putting a semi-truck engine in a go-kart—it’s too much weight for the frame. OpenRGB is the lightweight, logical choice for your setup. Would you like me to walk you through setting up a specific "Canvas" layout in OpenRGB to sync your fans and RAM perfectly?
