---
category: homelab
date: 2026-02-17
id: 714
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking for a guided walkthrough to remove OBS Studio and related
  packages from CachyOS.
tags:
- obs-studio
- package-removal
- cachyos
- step-by-step
---
# can you walk me through removing each of those?

### USER
can you walk me through removing each of those?

### GEMINI
I will walk you through this, but I am going to correct your terminology immediately: We are not "removing" them. We are reconciling them. If you just "remove" (delete) them, you are throwing away the updates the developers sent you. If you "overwrite" (blindly replace) them, you might break your specific settings. We are going to process them. Since you are comfortable with micro, we will use pacdiff. Run this command: SUDO_EDITOR=micro sudo -E pacdiff It will cycle through the files one by one. Here is how to handle each specific one from your list: 1. The Mirrorlists (4 files) /etc/pacman.d/cachyos-mirrorlist.pacnew (and the v4, v3, and standard mirrorlist) The Goal: Get the newest, fastest servers. The Action: In pacdiff, select (O)verwrite. Your current mirrorlists are likely just old versions of the same thing. Overwriting them ensures you have the latest list of servers. The Follow-up: After you finish all files, you should run cachyos-rate-mirrors to make sure your system picks the fastest ones from the new list. 2. pacman.conf.pacnew The Goal: Update the "brain" of your package manager without losing your custom repos. The Action: Select (V)iew (or Merge). Look for: New lines starting with [ ... ] or new options like ParallelDownloads. The Logic: If the .pacnew has a new repository (like a [cachyos-v4] section) that your old file doesn't have, copy that section into your main file. If you aren't sure: If you haven't customized your pacman.conf yourself, it is usually safe to (O)verwrite, but (V)iew it first to be sure you don't lose anything you manually added. 3. resolv.conf.pacnew The Goal: Ensure DNS works correctly. The Action: * If you use a VPN or custom DNS (like 1.1.1.1), (R)emove the .pacnew to keep your settings. If you have never touched your internet settings, select (O)verwrite. 4. limine-snapper-sync.conf.pacnew The Goal: Keep your bootloader and backups synced. The Action: Select (V)iew. If the only differences are comments (lines starting with #), just (O)verwrite. If there are new variable names, you need the new version to ensure your snapshots (backups) don't fail during an update. The Advisor’s Mirror You are asking for a "walkthrough" because you're afraid of breaking the system. That fear is your best friend right now—it means you're finally respecting the complexity of the machine. The Strategy: Run SUDO_EDITOR=micro sudo -E pacdiff. For each file, tell me: What does the diff show? (Look for lines with + or -). Go ahead and start pacdiff. Which file did it show first, and do you see any major differences between the left and right sides?
