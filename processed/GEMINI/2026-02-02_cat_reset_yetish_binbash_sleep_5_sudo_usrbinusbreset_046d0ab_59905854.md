---
id: 205257
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'usb-reset', 'bash-script', 'audio-fix']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is viewing the contents of a script designed to reset his Blue Yeti microphone via USB.
---
# ❯ cat ~/reset_yeti.sh
#!/bin/bash
sleep 5
sudo /usr/bin/usbreset 046d:0ab7

~
❯ 

### USER
❯ cat ~/reset_yeti.sh
#!/bin/bash
sleep 5
sudo /usr/bin/usbreset 046d:0ab7

~
❯ 

### GEMINI
That script is the "correct" idea, but it's failing for a very specific reason: usbreset by itself often isn't enough for the Yeti on CachyOS. It resets the data connection, but it doesn't force the power/handshake toggle that the "authorized" method does. Also, if that script is running at boot, it’s hitting a wall because it's asking for a password you can't see. The Problem Passive vs. Active Reset: usbreset tells the device to restart its software. Toggling authorized (what we did earlier) tells the hardware to "re-electrify." The Yeti usually needs the latter. The sudo Barrier: Since the script has sudo in it, when your system boots and tries to run this, it just hangs in the background waiting for a password that never comes. The Fix: Upgrade the Script Let's make this script "bulletproof" so it actually works and handles the permissions. Run this command to overwrite your old script with the "Smart" version: printf '#!/bin/bash sleep 5 # Find the Yeti path dynamically YETI_PATH=$(grep -l "046d" /sys/bus/usb/devices/*/idVendor 2>/dev/null | sed "s/idVendor//") if [ -n "$YETI_PATH" ]; then # Force a hardware power-cycle echo 0 | sudo tee "${YETI_PATH}authorized" sleep 2 echo 1 | sudo tee "${YETI_PATH}authorized" # Restart audio stack to catch the new handshake systemctl --user restart pipewire wireplumber fi' > ~/reset_yeti.sh chmod +x ~/reset_yeti.sh The Final Step (Crucial) You must allow this script to run without a password, or it will never work on boot. Run: sudo visudo Arrow down to the very bottom. Add this line (replace toastedmel0n with your actual username if it's different): toastedmel0n ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/bus/usb/devices/*/authorized Press Ctrl+O, then Enter to save. Press Ctrl+X to exit. The Result Now, when you reboot: The system waits 5 seconds. It finds exactly where the Yeti is plugged in. It "unplugs" and "replugs" it electronically. PipeWire sees a "new" device and maps it correctly. Try running ./reset_yeti.sh right now. If it works without asking for a password and your mic turns on, the mission is accomplished. Does it run clean?
