---
id: 393338
source: GEMINI
date: 2026-02-02
tags: ['yeti-microphone', 'usb-reset', 'scripting', 'linux']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is running a script to reset his Yeti microphone, likely to fix a connection issue.
---
# ❯ ~/reset_yeti.sh
Resetting Yeti at /sys/bus/usb/devices/1-3
0
1

~ 7s
❯ 

### USER
❯ ~/reset_yeti.sh
Resetting Yeti at /sys/bus/usb/devices/1-3
0
1

~ 7s
❯ 

### GEMINI
Success. The script successfully targeted only the Yeti at 1-3 and performed the "electronic replug" without asking for a password. That confirms your visudo edit is working perfectly. The Final Step: Ensure it runs at Boot If you haven't already, you need to make sure this script triggers every time you log in, so you never have to think about it again. Open your System Settings. Search for Autostart. Add a new Script File. Point it to ~/reset_yeti.sh. Ensure it is set to run at Startup (or Login). The Brutally Honest Summary You’ve effectively engineered a "software patch" for a hardware limitation. The Root Cause: Your Yeti's firmware is slow; your CachyOS kernel is fast. They miss each other's "handshake" at boot. The Solution: We now let the OS boot, wait 5 seconds, and then the script "unplugs and replugs" the mic for you via the authorized file. The Result: No more reaching behind the PC. No more dead audio. Is the mic actually picking up sound now? Do a quick test in Discord or OBS. If it is, you've officially moved from "fighting your tools" to "mastering your environment." Would you like me to show you how to check your Autostart folder via the terminal to confirm the script is linked correctly?
