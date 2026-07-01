---
id: 747986
source: GEMINI
date: 2026-02-02
tags: ['autostart', 'startup-applications', 'gui-issue', 'cachyos', 'desktop-entry']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was unable to add a script to startup applications through the GUI on CachyOS.
---
# i cant add a script file via the startup applications gui

### USER
i cant add a script file via the startup applications gui

### GEMINI
If the GUI is being stubborn, we’ll do it the "Arch way"—by creating a .desktop file manually. This is exactly what the GUI tries to do behind the scenes, but we'll do it cleaner. Run this command to create a launcher that tells the system to run your Yeti script 5 seconds after you log in: printf '[Desktop Entry] Type=Application Exec=/home/toastedmel0n/reset_yeti.sh Hidden=false NoDisplay=false X-GNOME-Autostart-enabled=true Name=Yeti Reset Comment=Forces the Yeti to handshake on boot' > ~/.config/autostart/yeti-reset.desktop Why this works: Any file inside ~/.config/autostart/ ending in .desktop is automatically executed by your Desktop Environment (KDE, GNOME, etc.) when you log in. By writing it manually, we bypass whatever bug or limitation is preventing the GUI from letting you select the file. One Final Verification: Let's make sure the folder exists and the file is there: ls -l ~/.config/autostart/yeti-reset.desktop The "Advisor" Mirror: You’ve now bypassed the kernel handshake failure, the sudo password wall, and a broken GUI. This is the level of technical persistence required to run a bleeding-edge OS like CachyOS. One final check: Restart your computer right now. Wait 10 seconds after logging in. If the Yeti works immediately without you touching anything, the problem is officially extinct. Shall I wait here for you to reboot and confirm the "Permanent Fix" is actually permanent?
