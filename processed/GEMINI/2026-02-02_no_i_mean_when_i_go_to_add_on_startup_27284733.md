---
category: homelab
date: 2026-02-02
id: 450746
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to add an application to startup but was having difficulty
  with the process.
tags:
- startup-applications
- autostart
- cachyos
---
# no i mean when i go to add on startup

### USER
no i mean when i go to add on startup

### GEMINI
Ah, I see the confusion. When you use the "Add" button in a graphical Startup menu (like GNOME or KDE), it often opens a file browser that might hide files, or it expects a full path that isn't obvious. Since we put the script in /usr/local/bin/reset_yeti.sh, you don't need to browse for it. You can just type the command manually. How to add it (The Direct Way) Open your Startup Applications (GNOME) or Autostart (KDE). Click Add. Fill it out exactly like this: Name: Yeti Fix Command: /usr/local/bin/reset_yeti.sh Comment: Resets the Blue Yeti USB bus on login Click Save/Add. Why the browser might have failed you: If you were looking in your "Home" folder (~/), you wouldn't see it because we moved it to a system folder (/usr/local/bin) for better stability. The "Brutal Advisor" Safety Check Before you reboot, let's make 100% sure the script actually works when called that way. Run this one last time in your terminal: /usr/local/bin/reset_yeti.sh If the terminal waits 5 seconds and then finishes without asking for a password, you are golden. If it asks for a password, your visudo entry has a typo (likely the username toastedmel0n or the path). If it says "Permission denied," you missed the sudo chmod +x step. Are you ready to reboot? Once you log back in, wait about 10 seconds for the script's sleep 5 to finish, then check if your mic is hot.
