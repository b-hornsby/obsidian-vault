---
category: homelab
date: 2026-02-03
id: 068412
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to remove the GNOME desktop environment from his system.
tags:
- gnome
- desktop-environment
- package-removal
- linux-configuration
---
# how do i delete gnome then?

### USER
how do i delete gnome then?

### GEMINI
To delete GNOME on CachyOS (Arch-based), you use the pacman removal command. However, because you’re a streamer, we have to be surgical. If you just nuked everything with "gnome" in the name, you might accidentally delete your Bluetooth drivers, network manager, or your settings for certain apps that share libraries. Here is the precise, safe way to strip GNOME out without breaking your new KDE sanctuary. 1. The "Safe Removal" Command This command removes the core GNOME desktop groups but keeps the files that are "unneeded" by KDE. sudo pacman -Rs gnome gnome-extra -R: Remove. -s: Recursive (removes dependencies that nothing else is using). Wait for the prompt: It will list what it's deleting. If you see something like networkmanager or bluez in that list, stop and tell me. If it's just gnome-shell, nautilus, gedit, etc., proceed. 2. Cleanup the Leftovers GNOME leaves a lot of "orphans" behind. Run this to clean the "junk" that didn't get caught in the first command: sudo pacman -Rns $(pacman -Qtdq) (If this says "error: no targets specified," it just means your system is already clean). The Advisor’s "Don’t Regret This Later" Warning Don't delete the configuration files (yet). Even after you uninstall GNOME, there will be folders in your home directory (like .config/dconf) that hold your old settings. Leave them for a week. They take up almost zero space, and if you realize you forgot to copy a specific setting or keybind, they are still there. Keep these "GNOME" apps (The Exception Rule): KDE is great, but some GNOME-adjacent apps are actually better for certain tasks. You might want to keep: Nautilus (if you prefer it over Dolphin). Gedit (if you find KWrite/Kate too complex). GParted (the best disk tool). If you want to keep one specifically, don't run the -Rs command on it. One Final Step for a Clean Boot Since you moved to plasmalogin, ensure GDM (GNOME's manager) is truly gone so it never tries to "hijack" your boot again: sudo pacman -R gdm Did the pacman -Rs command finish without errors? Once it's done, your "Menu" in KDE will be much cleaner—all those duplicate "Calculator" and "Terminal" icons from GNOME will have vanished. Would you like me to show you how to set up a "Global Shortcut" in KDE to instantly restart your GPU driver if it ever glitches during a stream? It’s a lifesaver for NVIDIA users.
