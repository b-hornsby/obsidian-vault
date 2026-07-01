---
id: 089961
source: GEMINI
date: 2026-02-03
tags: ['homelab', 'ai', 'gemini', 'go', 'terminal', 'at', 'linux', 'cachyos']
category: homelab
sentiment: exploratory
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
---
# I messed up how do I get it to take my name again?

### USER
I messed up how do I get it to take my name again?

### GEMINI
You haven't "messed up" the whole system, you just encountered a standard Linux "hang" when forcing display protocols. If the screen is frozen and won't let you type, it's because the graphical interface is stuck, but the underlying system is still listening. To get your name and login back, you need to perform this "blind" rescue: 1. The Rescue Sequence Force the Terminal: Press Ctrl + Alt + F3 simultaneously. What to expect: The screen should turn black and show a text-based prompt asking for your login. Log In via Text: * Login: Type bryan (or toastedmel0n based on your prompt) and hit Enter. Password: Type your password. Note: You will not see any characters or stars as you type; this is a security feature. Just type it and hit Enter. Undo the Damage: Type: sudo nano /etc/gdm/custom.conf. Navigate with the arrow keys to the line WaylandEnable=false. Add the # back to the front so it looks like: #WaylandEnable=false. Press Ctrl + O, Enter to save, then Ctrl + X to exit. Reboot: Type sudo reboot. If "Ctrl + Alt + F3" Does Nothing If your keyboard is completely unresponsive due to the NVIDIA driver crash: Hardware Reset: Hold the physical power button on your PC until it shuts down. Snapshot Boot (The CachyOS Lifesaver): * Turn the PC back on. In the boot menu (where you choose CachyOS), look for an option that says "Wayback" or "Snapshots". Select the most recent snapshot from earlier today. This will boot you into a version of your system from before you edited that file. The Strategy Shift Once you are back at your desktop, we are done trying to force Xorg. It clearly breaks your specific CachyOS/NVIDIA link. To fix the OBS flickering on Wayland: Open OBS. Go to Settings > Advanced. Uncheck "Enable Browser Source Hardware Acceleration". Are you able to get to the black text screen with Ctrl+Alt+F3, or do we need to use the Snapshot method?