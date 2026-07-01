---
id: 887273
source: GEMINI
date: 2026-02-02
tags: ['reset-yeti', 'script-missing', 'cachyos', 'usb-audio']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan couldn't find the ~/reset_yeti.sh script that should have been created to fix his Blue Yeti microphone.
---
# i dont see ~/reset_yeti.sh

### USER
i dont see ~/reset_yeti.sh

### GEMINI
If you don't see it when you type ls, it's likely because you are looking in the wrong directory or the echo command didn't land where we thought. Let’s find it, fix it, and make it bulletproof. 1. Locate the file Run this to see exactly where it is: find ~ -name "reset_yeti.sh" If it returns nothing, the file wasn't created. If it returns a path, use that path for the next steps. 2. Re-create it (The "Advisor's certain" way) Let's put it in /usr/local/bin instead. This is a "proper" place for scripts, making it system-wide and easier for the OS to find. Run this block (copy and paste the whole thing): sudo bash -c 'cat <<EOF > /usr/local/bin/reset_yeti.sh #!/bin/bash sleep 5 /usr/bin/usbreset 046d:0ab7 EOF' Now, make it executable: sudo chmod +x /usr/local/bin/reset_yeti.sh 3. Update your "Hall Pass" (Visudo) Since we moved the script, we need to make sure sudo knows it's allowed to run without a password. Run: sudo EDITOR=nano visudo Change the line we added earlier to this: toastedmel0n ALL=(ALL) NOPASSWD: /usr/local/bin/reset_yeti.sh Save and exit (Ctrl+O, Enter, Ctrl+X). 4. Why this is the "Pro" Move By putting the script in /usr/local/bin, you can now trigger it from anywhere just by typing reset_yeti.sh. Test it now: Type reset_yeti.sh in your terminal. If it waits 5 seconds and then finishes without asking for a password, it is perfect. If it says "command not found," run hash -r and try again. 5. Add to Startup Now, when you go to your Startup Applications (GNOME) or Autostart (KDE), just put reset_yeti.sh as the command. No paths, no mess. The Strategy Check: Does the mic respond when you run reset_yeti.sh manually right now? If the light on the Yeti flashes or it suddenly appears in your audio settings, you have successfully automated the "unplug/replug" fix. Ready to reboot and see if the ghost in the machine finally behaves?
