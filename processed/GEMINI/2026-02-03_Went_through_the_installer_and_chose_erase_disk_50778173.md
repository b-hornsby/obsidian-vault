---
id: 621006
source: GEMINI
date: 2026-02-03
tags: ['os-installation', 'erase-disk', 'cachyos-installer']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was going through a CachyOS installer and selected the erase disk option, likely setting up or reinstalling his system.
---
# Went through the installer and chose erase disk

### USER
Went through the installer and chose erase disk

### GEMINI
Then you have officially crossed the rubicon. There is no "undo" button for your 2TB drive now. The installer is currently formatting your partitions, creating the BTRFS subvolumes, and pulling the latest packages from the CachyOS mirrors. Depending on your internet speed and drive type, this will take between 5 and 15 minutes. While you wait, let's fix your mindset for the "New Instance": Most users treat a fresh install like a blank check and immediately start "overdrawing" their system resources. To actually reach the "next level" of system performance and stability you're looking for, adhere to these three rules the moment you hit that Restart Now button: The "One-at-a-Time" Rule: Do not mass-install software. Install your browser, get your work/gaming environment up, and stop. Use the system for an hour. If it feels fast, it’s because you haven't bogged it down yet. Verify the Kernel: Once you're in, open a terminal and run uname -r. Ensure you are actually running the optimized CachyOS kernel you selected. If it says generic, you've already missed a step. Snapshot Early: Before you touch a single config file or install a single AUR package, open Snapper or Timeshift (whichever you chose) and take a "Baseline" snapshot. If you break the system in 2 hours, you shouldn't have to use that USB again. The Strategic Question: You wiped 2TB of data. That’s a lot of "baggage" gone. What was the single biggest point of friction or "jank" in your last installation that you are absolutely determined to avoid this time? Tell me, and I'll tell you the specific setting or habit that will prevent it from happening again.
