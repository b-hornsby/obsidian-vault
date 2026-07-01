---
category: general
date: 2026-02-03
id: 464450
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to remove gnome and gnome-extra using pacman but encounters
  a dependency error.
tags:
- pacman
- gnome
- package-removal
- dependency-error
---
# ❯ sudo pacman -Rs gnome gnome-extra
[sudo] password for toastedmel0n: 
checking dependencies...
error: failed to prepare transaction (could not satisfy dependencies)
:: removing gnome-shell breaks dependency 'gnome-shell' required by gnome-browser-connector

~
❯ 

### USER
❯ sudo pacman -Rs gnome gnome-extra
[sudo] password for toastedmel0n: 
checking dependencies...
error: failed to prepare transaction (could not satisfy dependencies)
:: removing gnome-shell breaks dependency 'gnome-shell' required by gnome-browser-connector

~
❯ 

### GEMINI
This is a classic Arch "dependency loop." gnome-browser-connector is a small background tool that lets your web browser talk to GNOME extensions, and it strictly requires gnome-shell to exist. Because it's not part of the core "gnome" group, your simple removal command fails because it doesn't want to leave that connector "orphaned". Since you are moving to KDE, you don't need GNOME extensions or their browser connectors anymore. We need to be a bit more "forceful." The "Surgical" Removal We will use the Cascade flag (-c). This tells pacman: "I want to remove GNOME, and I also want you to remove anything else that requires GNOME to work" (like that browser connector). Run this command: sudo pacman -Rsc gnome gnome-extra READ THE LIST: Before you hit "Y", look at the packages it wants to remove. It's okay to see: gnome-shell, mutter, nautilus, gnome-browser-connector, gdm, etc. Stop if you see: networkmanager, pipewire, nvidia-utils, or linux-cachyos. (It shouldn't, but the -c flag is powerful). If you want to be 100% Safe (Step-by-Step) If the command above looks too scary, just manually kill the connector first: sudo pacman -R gnome-browser-connector Then, go back to your original command: sudo pacman -Rs gnome gnome-extra Why this is the "Advisor" move You're cleaning house. Leaving a browser connector that is hard-coded to a desktop you aren't using is just asking for a broken update notification 3 months from now. One final warning: After you remove GNOME, you might lose your "GTK Theme" (the way apps like Firefox or Discord look). The Fix: In KDE, go to System Settings > Appearance > Global Theme > GNOME/GTK Application Style and set it to Breeze so your non-KDE apps look clean again. Did the manual removal of gnome-browser-connector let the rest of GNOME "float away" without errors?
