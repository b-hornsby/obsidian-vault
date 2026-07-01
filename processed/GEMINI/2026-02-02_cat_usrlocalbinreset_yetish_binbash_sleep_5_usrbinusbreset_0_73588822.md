---
id: 695707
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'usb-reset', 'bash-script', 'audio-fix']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is viewing the contents of a script designed to reset his Blue Yeti microphone via USB.
---
# ❯ cat /usr/local/bin/reset_yeti.sh
#!/bin/bash
sleep 5
/usr/bin/usbreset 046d:0ab7

~
❯ 

### USER
❯ cat /usr/local/bin/reset_yeti.sh
#!/bin/bash
sleep 5
/usr/bin/usbreset 046d:0ab7

~
❯ 

### GEMINI
That script is a "band-aid" for a known hardware handshake flaw in the Blue Yeti. It uses usbreset to power-cycle the device at the protocol level. The reason it’s acting up now is likely because OBS is already holding the device handle, and you’re trying to reset the hardware while the software is "locking" it. Here is the objective reality: Running usbreset while OBS is active is like trying to change a tire while the car is moving. It’s going to cause a conflict. 1. Fix the Permissions (Why your earlier command failed) Your earlier attempt to chmod failed because of a syntax error. If you want that script to actually work, you need to give it permission: sudo chmod +x /usr/local/bin/reset_yeti.sh 2. The Strategic "Yeti" Workflow Since you now have OBS auto-starting, the timing is clashing. OBS opens, grabs the Yeti, the Yeti glitches, and your reset script (if it's running on startup) fails because the device is "busy." Do this instead: Close OBS. Run the script manually: sudo /usr/local/bin/reset_yeti.sh Wait for the Mic light to stop flashing. Open OBS. 3. The Permanent Solution (The "Blind Spot") If you have to reset your mic every time you boot, your USB controller is likely trying to "autosuspend" the Yeti to save power. Linux is aggressive about this. Disable USB Autosuspend for the Yeti: Open your GRUB configuration: sudo nano /etc/default/grub Look for the line GRUB_CMDLINE_LINUX_DEFAULT. Add usbcore.autosuspend=-1 to the list of parameters inside the quotes. Save and exit (Ctrl+O, Enter, Ctrl+X). Update GRUB: sudo update-grub (or sudo grub-mkconfig -o /boot/grub/grub.cfg on CachyOS). Reboot. This prevents the OS from ever "putting the mic to sleep," which is usually what causes the Yeti to require a reset in the first place. 4. Direct Validation Run the script now with sudo and see if the mic comes back: sudo /usr/local/bin/reset_yeti.sh If the mic comes back, go into OBS and ensure the "Mic/Aux" is not red/muted. Do you want me to help you integrate that reset script into your OBS wrapper so the mic resets automatically three seconds before OBS launches? That would solve your "it was working right before this" headache forever.
