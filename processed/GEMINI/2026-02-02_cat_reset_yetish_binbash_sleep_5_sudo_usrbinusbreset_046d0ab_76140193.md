---
id: 393732
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'usb-reset', 'bash-script', 'audio-fix', 'udev', 'pipewire']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is creating and modifying a script to dynamically reset his Blue Yeti microphone, including restarting the audio stack, and attempting to edit sudoers file.
---
# ~
❯ cat ~/reset_yeti.sh
#!/bin/bash
sleep 5
sudo /usr/bin/usbreset 046d:0ab7

~
❯ printf '#!/bin/bash
  sleep 5
  # Find the Yeti path dynamically
  YETI_PATH=$(grep -l "046d" /sys/bus/usb/devices/*/idVendor 2>/dev/null | sed "s/idVendor//")

  if [ -n "$YETI_PATH" ]; then
      # Force a hardware power-cycle
      echo 0 | sudo tee "${YETI_PATH}authorized"
      sleep 2
      echo 1 | sudo tee "${YETI_PATH}authorized"
      # Restart audio stack to catch the new handshake
      systemctl --user restart pipewire wireplumber
  fi' > ~/reset_yeti.sh

  chmod +x ~/reset_yeti.sh

~
❯ sudo visudo
[sudo] password for toastedmel0n: 
visudo: no editor found (editor path = /usr/bin/vi)

~
❯ 

### USER
~
❯ cat ~/reset_yeti.sh
#!/bin/bash
sleep 5
sudo /usr/bin/usbreset 046d:0ab7

~
❯ printf '#!/bin/bash
  sleep 5
  # Find the Yeti path dynamically
  YETI_PATH=$(grep -l "046d" /sys/bus/usb/devices/*/idVendor 2>/dev/null | sed "s/idVendor//")

  if [ -n "$YETI_PATH" ]; then
      # Force a hardware power-cycle
      echo 0 | sudo tee "${YETI_PATH}authorized"
      sleep 2
      echo 1 | sudo tee "${YETI_PATH}authorized"
      # Restart audio stack to catch the new handshake
      systemctl --user restart pipewire wireplumber
  fi' > ~/reset_yeti.sh

  chmod +x ~/reset_yeti.sh

~
❯ sudo visudo
[sudo] password for toastedmel0n: 
visudo: no editor found (editor path = /usr/bin/vi)

~
❯ 

### GEMINI
CachyOS is being lean—it doesn't have vi linked, which is why visudo failed. We’ll force it to use nano, which is much more user-friendly and almost certainly installed on your system. 1. Fix the sudo permissions (The "No-Password" Hack) Run this command to open the editor: sudo EDITOR=nano visudo What to do inside the file: Scroll all the way to the very bottom. Add this exact line: toastedmel0n ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/bus/usb/devices/*/authorized Press Ctrl+O, then Enter to save. Press Ctrl+X to exit. 2. Test the Script Now that you've updated the script and (hopefully) fixed the permissions, run it manually to see if it works without asking for a password: ~/reset_yeti.sh Wait about 8 seconds. Check your audio: If the script finishes and your mic starts working (check wpctl status or your sound settings), then the logic is 100% solid. 3. The "Brutally Honest" Reality Check If you don't do the visudo step, that script will never work on boot. It will just sit there in the dark, asking a ghost for a password. Once the manual test works, the only thing left is to make sure this script is in your System Settings > Autostart. If it's already there from before, you're done. If not, add it now. Did the manual run of ~/reset_yeti.sh work and show "1" in the output without asking for a password?
