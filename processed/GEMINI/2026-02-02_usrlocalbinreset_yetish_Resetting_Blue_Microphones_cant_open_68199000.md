---
category: homelab
date: 2026-02-02
id: 923522
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to run his reset_yeti.sh script but got a permission denied
  error when trying to open the USB device.
tags:
- reset-yeti
- permission-denied
- usb-device-reset
---
# ❯ /usr/local/bin/reset_yeti.sh
Resetting Blue Microphones ... can't open [Permission denied]

~
❯ 

### USER
❯ /usr/local/bin/reset_yeti.sh
Resetting Blue Microphones ... can't open [Permission denied]

~
❯ 

### GEMINI
We are at the final hurdle. The "Permission denied" error confirms that the script is trying to reset the hardware but doesn't have the authority to talk to the USB bus without sudo. Since an autostart script can't pop up a password window every time you log in, we must finalize that "hall pass" in your system configuration. 1. Fix the Permissions (The "Visudo" Step) This is the only way to let the script run silently at startup. Run this command: sudo EDITOR=nano visudo Scroll to the very bottom of the file and add this exact line: toastedmel0n ALL=(ALL) NOPASSWD: /usr/bin/usbreset Save and Exit: Press Ctrl+O, Enter, then Ctrl+X. 2. The Verification Test Run the script again exactly as you did before: /usr/local/bin/reset_yeti.sh If it waits 5 seconds and returns to the prompt without an error: You have won. The "electronic replug" is now authorized to happen automatically. If it still says "Permission denied": It means the path to usbreset is different on your system. Run which usbreset to check. If it says /bin/usbreset, update the visudo line to match that path. 3. The Advisor's Brutal Strategic Final Call You have successfully built a software "robot" that will unplug and replug your mic 5 seconds after you log in. However, this robot only works if the Yeti is "sane" enough to hear the command. Do not ignore the BIOS settings I pointed out in your photos: Disable "USB power delivery in Soft Off state (S5)": If the Yeti stays powered while the PC is off, it remains in its crashed state. You want it to lose power entirely so it "cold boots" when you turn the PC on. Disable "Global C-state Control": These power-saving states cause the voltage drops that trigger this entire mess. The Sequence for Success Verify the script runs without a password using the test in Step 2. Reboot into BIOS. Disable S5 USB Power and Disable C-States. Save and Exit BIOS. Log in and wait 10 seconds. Does the Yeti light stay solid and does it appear in your sound settings? If yes, you've successfully overcome a decade-old hardware flaw with modern automation. Would you like me to show you how to check the journalctl logs after the reboot to prove the script fired successfully?
