---
id: 474479
source: GEMINI
date: 2026-02-03
tags: ['icon-theme', 'mactahoe-theme', 'file-system-search', 'linux-configuration']
category: homelab
sentiment: exploratory
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was trying to locate the MacTahoe icon theme files on his system.
---
# ~
❯ find ~/.local/share/icons /usr/share/icons -maxdepth 1 -name "*MacTahoe*"
/usr/share/icons/MacTahoe
/usr/share/icons/MacTahoe-light
/usr/share/icons/MacTahoe-dark

~
❯ 

### USER
~
❯ find ~/.local/share/icons /usr/share/icons -maxdepth 1 -name "*MacTahoe*"
/usr/share/icons/MacTahoe
/usr/share/icons/MacTahoe-light
/usr/share/icons/MacTahoe-dark

~
❯ 

### GEMINI
As your output shows, these files are sitting in /usr/share/icons/. This is exactly why the "Delete" button in the Settings UI was greyed out or non-functional: you do not own these files; the System (root) does. KDE's GUI won't let a standard user delete system-level resources to prevent accidental breakage. The Nuclear Option Since you want them gone and they are system-wide files, you must use sudo (SuperUser Do) to force the removal. Execute this command exactly: sudo rm -rf /usr/share/icons/MacTahoe* Note: You will be prompted for your password. You won't see characters moving as you type; just hit Enter when finished. The Advisor’s Perspective You’ve successfully identified the "enemy." Now, look at the pattern: The Mistake: You tried to use a consumer-grade UI to do a system-admin task. The Fix: You moved to the terminal, gained visibility (via find), and are now executing with authority (sudo). The Lesson: Stop poking at buttons and hoping for permission. In your work and your OS, if you want something changed, go to the root of the configuration. Wait—before you move on: Check your Global Theme and Plasma Style settings. If you installed a "MacTahoe" Global Theme, deleting just the icons is a half-measure. It’s like taking the badges off a car but leaving the body kit. Do you want the command to hunt down and wipe the rest of the MacTahoe theme components (Global Themes, Cursors, and Aurorae decorations) so your system is actually clean?
