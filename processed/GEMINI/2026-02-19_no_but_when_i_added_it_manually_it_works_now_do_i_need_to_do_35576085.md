---
id: 804610
source: GEMINI
date: 2026-02-19
tags: ['lutris', 'manual-fix', 'application-menu', 'cachyos', 'follow-up']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan confirmed that manually adding Lutris to the application menu worked and was asking if any further steps were needed.
---
# no but when i added it manually it works now. do i need to do anything else?

### USER
no but when i added it manually it works now. do i need to do anything else?

### GEMINI
Since it works now, you’ve manually bypassed the indexing bug that was filtering out the system-wide entry. You don't need to do anything else for it to function, but there is one "maintenance" detail you should know to avoid future headaches: 1. The "Ghost" Check By adding it manually in kmenuedit, you likely created a new file at ~/.local/share/applications/Lutris.desktop (or similar). This file will now override the official one provided by CachyOS updates. The Good: It works and won't disappear. The Bad: If Lutris updates and changes its launch flags or icons in the future, your manual entry might stay "frozen" in time. 2. Clean Up the Redundancy (Optional but Recommended) To ensure your menu stays clean, run this to see if you now have two versions of the file: ls ~/.local/share/applications/ | grep -i lutris If you see a file there, that is your "manual" fix. Keep it. If you ever want to go back to the "official" version, you’d delete that file and run kbuildsycoca6 --noincremental again. 3. Why did this happen? (The Strategic Insight) On CachyOS/Arch, this specific glitch usually happens because of a MIME type conflict. Lutris registers itself to handle x-scheme-handler/steam, and sometimes the KDE menu database gets "confused" and hides the app from the grid to avoid a conflict with the actual Steam entry, even though Search (which is less "smart") still finds it. You're set. Your manual entry is a permanent fix. Would you like me to show you how to check if any other "missing" apps are hiding in your system with a quick script?
