---
id: 532447
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'usb-reset', 'bash-script', 'audio-fix']
category: homelab
sentiment: executing
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is viewing the contents of a script designed to reset his Blue Yeti microphone via USB and then attempts to execute it, but encounters an error.
---
# ❯ cat /usr/local/bin/reset_yeti.sh
#!/bin/bash
sleep 5
/usr/bin/usbreset 046d:0ab7

~
❯ usr/local/bin/reset_yeti.sh
fish: Unknown command: usr/local/bin/reset_yeti.sh

~
❯ 

### USER
❯ cat /usr/local/bin/reset_yeti.sh
#!/bin/bash
sleep 5
/usr/bin/usbreset 046d:0ab7

~
❯ usr/local/bin/reset_yeti.sh
fish: Unknown command: usr/local/bin/reset_yeti.sh

~
❯ 

### GEMINI
The file is finally correct, but you are missing the leading slash in your command. In Linux, usr/local/... looks for a folder named "usr" inside your current folder. You need /usr/local/... (starting with a slash) to tell the system to look in the root directory. 1. Test it correctly Run it with the leading slash: /usr/local/bin/reset_yeti.sh If it waits 5 seconds and finishes: You are 100% ready. If it asks for a password: You still need to fix the visudo entry we discussed earlier so the script can run silently at startup. 2. The Final "Brutal" Reality Check We have built a solid software workaround, but software cannot fix a hardware state that is already "frozen" before the OS loads. Based on your previous BIOS images, you have two major "blind spots" that will likely make this script fail after a cold boot: USB Power in S5 (Soft Off): You had this Enabled. Change it to Disabled. If the Yeti stays powered while the PC is off, it never clears its crashed internal memory. Global C-State Control: You had this Enabled. Change it to Disabled. These deep CPU sleep states cause voltage drops on the USB bus that "frighten" the Yeti's sensitive, older controller into disconnecting. 3. The Plan Test the script one last time with the slash: /usr/local/bin/reset_yeti.sh. Go to BIOS and flip those two switches (Disable S5 USB Power and Disable C-States). Reboot and Log In. Wait 10 seconds. If the mic light is solid and it shows up in your sound settings, you've won. You've officially automated the "unplug/replug" and stabilized the power delivery that was killing the device. Does the script run now that you added the leading slash? If so, you are cleared for the final reboot.
