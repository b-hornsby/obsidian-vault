---
category: homelab
date: 2026-02-02
id: 850884
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that his Yeti microphone is still not working after a
  reboot.
tags:
- yeti-microphone
- audio-issue
- hardware-troubleshooting
- linux
---
# rebooted and still not working 

### USER
rebooted and still not working 

### GEMINI
That is the "CachyOS Experience" in a nutshell—bleeding-edge speed often skips the very things we need to initialize. If it didn't work, it means the .desktop file either fired too early (before the USB bus was fully mapped) or your Desktop Environment (likely KDE Plasma 6) ignored it because of a formatting quirk. Let's stop playing "nice" with the GUI/Desktop and move the fix to the System level. We’re going to create a Systemd User Service. This is much more reliable because it has built-in retry logic and doesn't depend on the "Autostart" folder. 1. Create the Service File Run this command to create a service that will manage the Yeti reset: mkdir -p ~/.config/systemd/user/ printf '[Unit] Description=Reset Yeti USB Handshake After=pipewire.service [Service] Type=oneshot ExecStart=/home/toastedmel0n/reset_yeti.sh RemainAfterExit=yes [Install] WantedBy=default.target' > ~/.config/systemd/user/yeti-fix.service 2. Enable and Start the Service Now, tell the system to use it: systemctl --user daemon-reload systemctl --user enable yeti-fix.service systemctl --user start yeti-fix.service 3. Check the "Truth" If the script ran, Systemd will tell us exactly what happened. Run this: systemctl --user status yeti-fix.service Look for: If it says Active: active (exited), it ran. If you see the error 0: No such file or directory, it means the USB path changed again (e.g., from 1-3 to 1-4). The Advisor's Cold Hard Truth: The reason it's "still not working" is likely a timing issue. The desktop loads, tries to run the script, but the USB bus is still "settling." One simple test: If you manually run ~/reset_yeti.sh right now in the terminal, does the mic turn on? If YES: The script works, but the "Autostart" is firing too early. We need to increase the sleep in the script from 5 to 10. If NO: The USB path has changed. We need to update the script to find the new path. Run the script manually now and tell me: does it fix it immediately?
