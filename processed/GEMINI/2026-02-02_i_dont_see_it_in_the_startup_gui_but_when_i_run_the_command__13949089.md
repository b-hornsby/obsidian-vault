---
id: 650485
source: GEMINI
date: 2026-02-02
tags: ['autostart', 'desktop-entry', 'yeti-fix', 'cachyos', 'startup-script']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed his Yeti fix desktop entry existed in ~/.config/autostart/ but wasn't appearing in the startup applications GUI.
---
# i don't see it in the startup gui but when i run the command i get this: ❯ cat ~/.config/autostart/yeti-fix.desktop
[Desktop Entry]
Type=Application
Exec=/usr/local/bin/reset_yeti.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Yeti Fix
Comment=Resets the Blue Yeti USB bus

~
❯ 

### USER
i don't see it in the startup gui but when i run the command i get this: ❯ cat ~/.config/autostart/yeti-fix.desktop
[Desktop Entry]
Type=Application
Exec=/usr/local/bin/reset_yeti.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Yeti Fix
Comment=Resets the Blue Yeti USB bus

~
❯ 

### GEMINI
The file is perfect. If it’s not showing up in the GNOME Tweaks GUI, it’s likely because GNOME Tweaks is looking for a matching .desktop file in /usr/share/applications to "verify" the app exists. Ignore the GUI. GNOME's autostart process follows the file you just created regardless of whether the Tweaks menu acknowledges it. If that file exists in ~/.config/autostart/, the system will attempt to execute it upon login. The Final Verification Before you reboot, let's do one last check to ensure the script actually works without a password. If this fails, the autostart will fail silently. Run this: /usr/local/bin/reset_yeti.sh If it waits 5 seconds and finishes quietly: You are officially ready. If it asks for a password: Your visudo change didn't stick or has a typo. Open it again with sudo EDITOR=nano visudo and ensure the line for toastedmel0n is at the very bottom of the file. The Advisor's Brutal Truth You've spent a lot of time on this. We have: Applied a Kernel Quirk to stop power management crashes. Disabled USB Autosuspend. Created a Reset Script to force a hardware handshake. Created a Startup Entry to automate that handshake. If you reboot and it still doesn't work, there is only one reason left: The BIOS. If the Yeti is still being powered while the PC is "off" (S5 state), it stays in its crashed state from the previous session. You must go into the BIOS and set USB power delivery in Soft Off state (S5) to Disabled. Go for the Reboot Restart your PC. Log in. Wait 10-15 seconds. Check your sound settings. Is the Yeti finally alive without you having to touch the cable? If so, we can finally close the book on this hardware ghost.
