---
id: 191531
source: GEMINI
date: 2026-02-02
tags: ['linux', 'desktop-entry', 'autostart', 'yeti-microphone', 'udev-rules']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is creating a desktop entry to automatically run a script to reset his Yeti microphone on boot.
---
# ❯ printf '[Desktop Entry]
  Type=Application
  Exec=/home/toastedmel0n/reset_yeti.sh
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Yeti Reset
  Comment=Forces the Yeti to handshake on boot' > ~/.config/autostart/yeti-reset.desktop

~
❯ ls -l ~/.config/autostart/yeti-reset.desktop
.rw-r--r-- 191 toastedmel0n  2 Feb 17:25  /home/toastedmel0n/.config/autostart/yeti-reset.desktop

~
❯ 

### USER
❯ printf '[Desktop Entry]
  Type=Application
  Exec=/home/toastedmel0n/reset_yeti.sh
  Hidden=false
  NoDisplay=false
  X-GNOME-Autostart-enabled=true
  Name=Yeti Reset
  Comment=Forces the Yeti to handshake on boot' > ~/.config/autostart/yeti-reset.desktop

~
❯ ls -l ~/.config/autostart/yeti-reset.desktop
.rw-r--r-- 191 toastedmel0n  2 Feb 17:25  /home/toastedmel0n/.config/autostart/yeti-reset.desktop

~
❯ 

### GEMINI
The file is in place and the permissions are correct. You've successfully built a customized "driver-kick" that bypasses the GUI, the sudo wall, and the hardware's own laziness. The Moment of Truth Your environment is now configured to handle the Yeti's failure modes automatically. To be 100% sure this is "set it and forget it," you need to reboot now. When you log back in: Don't touch the cable. Count to 10 (to allow the script's sleep 5 and the USB handshake to finish). Check your audio levels. A Final Advisory Note If for any reason it doesn't fire, it's usually because the Desktop Environment is picky about the Exec path. If it fails after reboot, run this one command to make the path "bulletproof" by using the literal home variable: sed -i "s|/home/toastedmel0n/|$HOME/|" ~/.config/autostart/yeti-reset.desktop Go ahead and reboot. If you log back in and that mic is "hot" without you lifting a finger, you've won. Should I stay on the line to verify the post-reboot results with you?
