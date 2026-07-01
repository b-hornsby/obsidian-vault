---
category: homelab
date: 2026-02-02
id: 539811
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan is trying to locate a script he previously created to reset his Blue
  Yeti microphone, suggesting he's having issues with it again.
tags:
- shell-script
- blue-yeti
- microphone
- script-recovery
- linux
---
# i had a yeti reset script how can i find it?

### USER
i had a yeti reset script how can i find it?

### GEMINI
To find that script, we’ll use the find command to look for the filename and grep to look for the specific Yeti-related code inside it. Run these three commands in your terminal: 1. Search by Filename This looks for any file in your home directory that has "yeti" or "reset" in the name: find ~ -iname "*yeti*" -o -iname "*reset*" 2>/dev/null 2. Search by Content (The "Handshake" Code) If you renamed the script to something generic (like fix.sh), this command will find it by searching for the "authorized" command we know is inside it: grep -rl "authorized" ~ 2>/dev/null 3. Check your Autostart Folder If the script was set to run at boot, the link to it is likely sitting in your local autostart directory. Check there: ls ~/.config/autostart/ If you find it: Once you see the path (e.g., /home/toastedmel0n/scripts/yeti.sh), you can check its contents with cat to make sure it's the right one: cat [path-to-your-script] The "Mirror" Advice: If you find the old script and it still doesn't work, it’s likely because your USB Bus path changed (e.g., from 1-3 to 1-1.2). USB paths are not permanent. Next Step: Did any of those commands return a file path? If you find the script, paste the contents here and I'll make sure the USB path matches your current setup so you don't have to "replug" again.
