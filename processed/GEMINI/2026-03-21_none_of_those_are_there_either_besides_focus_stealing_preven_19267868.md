---
category: homelab
date: 2026-03-21
id: 586648
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is indicating that certain KWin settings are missing, except for focus
  stealing prevention, suggesting he's trying to configure window behavior.
tags:
- kwin-settings
- window-management
- focus-stealing
- desktop-environment
---
# none of those are there either besides focus stealing prevention

### USER
none of those are there either besides focus stealing prevention

### GEMINI
This is the frustration of "Version Drift." Since you are on CachyOS (which is hyper-updated), you are likely on KDE Plasma 6.2 or 6.3 (from 2026), and they have consolidated the menu to be "smarter" (which usually means harder to find). Here is exactly how to find the modern equivalents for those missing rules. 1. Re-detect the Window Before you add properties, make sure KDE is looking at the right thing: Click Detect Window Properties. Click on your open Vesktop window. Make sure it says vesktop under Window class. 2. The "Missing" Properties (Modern Names) KDE 6 grouped these into new categories. Click Add Property and search for these specific terms: Instead of "Lowered priority": Look for Priority. If "Priority" isn't there: Use Inhibition. There is a property called Inhibit screen saver or Inhibit shortcuts. Set it to Force -> Yes. (This prevents the OS from "sleeping" the process). Instead of "Allow compositing": This has been removed because Wayland requires compositing. The modern equivalent to ensure smooth frames is Prefer High Dynamic Range (if you have an HDR monitor) or Accept focus. Set Accept focus to Force -> Yes. The "Most Important" One for NVIDIA: Look for Focus stealing prevention. Set it to Force -> None. 3. The "CachyOS" Performance Override Since you can't find the old priority rules, we'll do it via the Task Manager (Process level) which is more effective anyway: Open System Monitor (the KDE version of Task Manager). Find vesktop in the list. Right-click it > Change Priority (or Set Niceness). Set it to High (or a lower "Nice" value like -5). Note: This tells the Linux kernel itself to give Vesktop your i7's CPU cycles before other background apps. The "Nuclear" Fix for NVIDIA Flickering (2026 Edition) If you have applied the Wayland Flags in the Nano editor and the flickering is still there, it’s because of a conflict with the KDE Renderer. Try this: Press Alt + Space and type "Plasma Renderer". Change the rendering backend from "Automatic" to Vulkan. Log out and log back in. Why: NVIDIA’s Wayland drivers in 2026 often have a "race condition" with OpenGL (the default). Switching the whole desktop to Vulkan usually kills the flicker instantly because it handles frame synchronization (Explicit Sync) much better. Since you've got the Nano file saved, have you tried launching Vesktop again to see if the Wayland flags at least fixed the "black bar" flickering?
