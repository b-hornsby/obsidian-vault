---
id: 848182
source: GEMINI
date: 2026-02-02
tags: ['visudo', 'nano-editor', 'sudoers', 'reset-yeti-script']
category: homelab
sentiment: building
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan fixed the visudo editor issue by setting nano as the editor and then ran his reset_yeti.sh script which had path issues.
---
# ❯ sudo visudo
[sudo] password for toastedmel0n: 
visudo: no editor found (editor path = /usr/bin/vi)

~
❯ sudo EDITOR=nano visudo

~ 33s
❯ ~/reset_yeti.sh
tee: '/sys/bus/usb/devices/1-10/'$'\n''/sys/bus/usb/devices/1-3/authorized': No such file or directory
0
tee: '/sys/bus/usb/devices/1-10/'$'\n''/sys/bus/usb/devices/1-3/authorized': No such file or directory
1

~ 7s
❯ 

### USER
❯ sudo visudo
[sudo] password for toastedmel0n: 
visudo: no editor found (editor path = /usr/bin/vi)

~
❯ sudo EDITOR=nano visudo

~ 33s
❯ ~/reset_yeti.sh
tee: '/sys/bus/usb/devices/1-10/'$'\n''/sys/bus/usb/devices/1-3/authorized': No such file or directory
0
tee: '/sys/bus/usb/devices/1-10/'$'\n''/sys/bus/usb/devices/1-3/authorized': No such file or directory
1

~ 7s
❯ 

### GEMINI
The error happened because you have two Logitech/Blue devices plugged in (likely the Yeti and a mouse/webcam), so the script got confused and tried to combine their paths into one mess. We need to make the "search" more surgical so it only targets the Yeti. 1. Fix the Script Run this to overwrite the script with a version that handles multiple devices correctly: printf '#!/bin/bash sleep 5 # Search for the Yeti specifically by Vendor (046d) AND Product (0ab7) for dev in /sys/bus/usb/devices/*; do if [ -f "$dev/idVendor" ] && [ -f "$dev/idProduct" ]; then vid=$(cat "$dev/idVendor") pid=$(cat "$dev/idProduct") if [ "$vid" == "046d" ] && [ "$pid" == "0ab7" ]; then echo "Resetting Yeti at $dev" echo 0 | sudo tee "$dev/authorized" sleep 2 echo 1 | sudo tee "$dev/authorized" fi fi done systemctl --user restart pipewire wireplumber' > ~/reset_yeti.sh chmod +x ~/reset_yeti.sh 2. Test it again Now run it: ~/reset_yeti.sh 3. The Strategy Check The Error: Your previous run showed /sys/bus/usb/devices/1-10/ and /sys/bus/usb/devices/1-3/ both matching. One is likely your Yeti and the other is another Logitech device. The new script above checks the Product ID as well, so it will ignore your other gear and only "kick" the mic. The Sudo Rule: Since you already did the visudo step, this should now run without asking for a password. Run the script now. Does it say "Resetting Yeti at /sys/bus/usb/devices/1-3" and do the bars in your sound settings start moving?
