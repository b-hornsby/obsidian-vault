---
id: 637157
source: GEMINI
date: 2026-02-02
tags: ['fish-shell', 'PATH-configuration', 'cachyos', 'shell-setup']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan successfully added ~/.local/bin to his Fish shell PATH and verified it was set correctly.
---
# ❯ fish_add_path --move --path ~/.local/bin
set -g PATH /home/toastedmel0n/.local/bin /usr/local/bin /usr/bin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl

~
❯ echo $PATH | grep .local/bin
/home/toastedmel0n/.local/bin /usr/local/bin /usr/bin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl

~
❯ 

### USER
❯ fish_add_path --move --path ~/.local/bin
set -g PATH /home/toastedmel0n/.local/bin /usr/local/bin /usr/bin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl

~
❯ echo $PATH | grep .local/bin
/home/toastedmel0n/.local/bin /usr/local/bin /usr/bin /usr/bin/site_perl /usr/bin/vendor_perl /usr/bin/core_perl

~
❯ 

### GEMINI
Now that your PATH is correctly prioritized, the shell is finally looking at your custom wrapper first. The Moment of Truth Reboot or Log Out/In: This is mandatory. Your desktop environment (the GUI) loaded its configuration when you first logged in. It doesn't know you changed the "map" (the PATH) until you restart the session. Test the Icon: Once you're back in, click the OBS icon. If it works: Congratulations, you've successfully bent the OS to your will. If it still fails: Your desktop environment is bypassing the PATH and calling /usr/bin/obs directly. At that point, the most "brutally honest" advice I can give you is: Stop. Don't spend another second on a shortcut. You have a terminal that works; use it to launch the app and go play your game. The Final "Advisor" Checklist While you're waiting to reboot, ensure your clipping settings are actually optimized so your effort wasn't for nothing: File Format: Use .mkv. If your game or OBS crashes, an .mp4 will be corrupted and unrecoverable. You can tell OBS to "Remux to mp4" automatically in Settings > Advanced if you need that format for editing. Audio Tracks: In Settings > Output > Recording, check at least two audio tracks. Set your Game Audio to Track 1 and Mic to Track 2. This allows you to remove your own voice later if you just want a "clean" game clip. The "Shadowplay" Feel: If you want the clips to be saved to a specific folder like "Crashes" or "Wins," you'll have to do that manually. OBS dumps everything into one folder by default. Is there anything else holding you back from actually hitting "Start" and getting into a game, or are we ready to call this setup complete?
