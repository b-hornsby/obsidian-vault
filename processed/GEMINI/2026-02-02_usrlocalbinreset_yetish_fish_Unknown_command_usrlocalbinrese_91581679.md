---
category: homelab
date: 2026-02-02
id: 480997
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to run his reset_yeti.sh script but fish shell could not
  find the command.
tags:
- reset-yeti
- fish-shell
- script-execution
---
# ❯ /usr/local/bin/reset_yeti.sh
fish: Unknown command: /usr/local/bin/reset_yeti.sh

~
❯ 

### USER
❯ /usr/local/bin/reset_yeti.sh
fish: Unknown command: /usr/local/bin/reset_yeti.sh

~
❯ 

### GEMINI
This is the "Brutal Truth" moment: Your reasoning for moving the file was sound, but you skipped the execution check. The command is failing because either the file wasn't actually created in that directory, or the permissions were never set. Fish is telling you it doesn't see an executable file at that path. Let's fix this once and for all with a single, aggressive block of commands. 1. The "Force Fix" Block Copy and paste this entire block into your terminal. This will create the file, ensure it has the correct code, and force the permissions to be executable. sudo bash -c 'cat <<EOF > /usr/local/bin/reset_yeti.sh #!/bin/bash sleep 5 /usr/bin/usbreset 046d:0ab7 EOF' && sudo chmod +x /usr/local/bin/reset_yeti.sh 2. Verify the Path (The Reality Check) Now, run this to see if the file actually exists and what its permissions are: ls -l /usr/local/bin/reset_yeti.sh If you see -rwxr-xr-x, it is officially an executable. 3. Test the Command Again Now that we've forced the file into existence and gave it "run" permissions, try running it again: /usr/local/bin/reset_yeti.sh If it waits 5 seconds and returns to the prompt: Success. If it asks for a password: You still need to fix the visudo entry we discussed earlier. If it still says "Unknown command": Your system's /usr/local/bin might not be in your $PATH. Try running it with sudo just once to see if it triggers: sudo /usr/local/bin/reset_yeti.sh. 4. The Last Strategic Step Once the command above works without a password, your .desktop file in ~/.config/autostart/ will finally have something real to trigger. One final piece of advice: While you are doing this, you are treating the symptoms. If you haven't Disabled S5 USB Power in your BIOS yet, you're just putting a band-aid on a wound that's still bleeding. The script will "fix" the mic after you log in, but disabling S5 power prevents it from crashing in the first place. Does the command run now? If it does, you are cleared for a reboot.
