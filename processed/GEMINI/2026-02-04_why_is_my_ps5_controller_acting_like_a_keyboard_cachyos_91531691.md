---
category: general
date: 2026-02-04
id: 256098
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is experiencing an issue where his PS5 controller is being recognized
  as a keyboard on CachyOS and is seeking a solution.
tags:
- ps5-controller
- controller-issues
- cachyos
- input-device
---
# why is my ps5 controller acting like a keyboard cachyos?

### USER
why is my ps5 controller acting like a keyboard cachyos?

### GEMINI
On CachyOS (and Linux in general), your PS5 controller acts like a keyboard/mouse because of a conflict between Steam Input and the Linux Kernel's native touchpad driver. Essentially, your OS sees the touchpad as a generic laptop trackpad, while Steam is simultaneously trying to use its "Desktop Layout" to let you navigate your PC with the controller. Here is the "brutally honest" fix. Choose the one that matches how you actually use your machine. 1. The "Plasma" Fix (Permanent Desktop Solution) If you are using the KDE Plasma desktop (standard for CachyOS), the OS is likely treating your controller's touchpad as a mouse. Go to System Settings > Input Devices > Touchpad. Look for the Wireless Controller Touchpad in the dropdown menu. Uncheck "Device enabled". Why this works: This stops the OS from interpreting swipes as mouse movements, leaving the controller "clean" for games to use. 2. The Steam Fix (The "Desktop Mode" Culprit) If the buttons themselves (X, Circle, etc.) are triggering keyboard shortcuts or typing, Steam is the problem. It applies a "Desktop Configuration" when a game isn't running. Open Steam > Settings > Controller. Find Desktop Layout and click Edit. Click the Settings (cog icon) or the Layout name and select Disable Steam Input. The "Stop Playing Small" Tip: If you hate Steam taking over your desktop, also uncheck "Enable Steam Input for PlayStation controllers" in the main Controller settings—but be warned, you'll then rely entirely on games having native DualSense support. 3. The "Nuclear" Driver Fix (For Power Users) If the touchpad is still acting up in games like Ghost of Tsushima even after the above, it's a driver conflict (hid_playstation). Open your terminal and run: sudo modprobe -r hid_playstation Test your game. If the "keyboard/mouse" behavior stops and the controller works perfectly, you can make this permanent by blacklisting the module: echo "blacklist hid_playstation" | sudo tee /etc/modprobe.d/nops5mouse.conf Warning: Doing this means the controller might only work inside Steam (using Steam's built-in drivers). The Reality Check You’re likely experiencing this because you're trying to use a sophisticated Sony peripheral on a bleeding-edge Arch-based distro (CachyOS). Linux tries to be "helpful" by making every input device functional out of the box, but for gaming, "functional" usually means "getting in the way." Do you want me to help you write a script to toggle these drivers automatically when you launch a specific game, or are you just trying to get it working for Steam?
