---
id: 987042
source: GEMINI
date: 2026-02-02
tags: ['shell-script', 'home-directory', 'linux']
category: coding
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is stating that he found a .sh file in his home directory, likely related to a script he was looking for.
---
# i found the .sh in my home folder

### USER
i found the .sh in my home folder

### GEMINI
Open it up and check the contents. Specifically, we need to see if it’s using a hardcoded USB path (like 1-3) or if it’s using the Vendor ID. Run this to see what's inside: cat ~/.yeti-reset.sh (Or whatever the filename is). Why this matters right now: In your dmesg output earlier, your Yeti was at 1-3. If your old script says 1-1 or 1-4, it’s "plugging and unplugging" a port that doesn't have a Yeti in it, which is why it's failing you now. The "Bulletproof" Version If your script looks outdated, I recommend replacing its content with this version. It automatically finds the Yeti, so even if you move the USB port or the system reassigns the bus, it will still work: #!/bin/bash # Automatically find the Yeti's USB path and reset it YETI_PATH=$(ls /sys/bus/usb/devices/*/idVendor 2>/dev/null | xargs grep -l "046d" | sed 's/idVendor//') if [ -n "$YETI_PATH" ]; then echo "Resetting Yeti at $YETI_PATH" echo 0 | sudo tee "${YETI_PATH}authorized" sleep 2 echo 1 | sudo tee "${YETI_PATH}authorized" systemctl --user restart pipewire wireplumber else echo "Yeti not found on USB bus." fi What does your current script say? Paste it here, and I'll tell you if the logic is still sound or if it’s trying to reset a "ghost" port.
