---
category: general
date: 2026-02-03
id: 476270
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if he needs to uninstall a program before installing it via
  Flatpak.
tags:
- flatpak
- software-installation
- package-management
---
# so do i need to delete anything before running flatpak install flathub org.duckstation.DuckStation

### USER
so do i need to delete anything before running flatpak install flathub org.duckstation.DuckStation

### GEMINI
No. You don't need to delete anything. The previous command failed during the prepare and build stages. This means nothing was actually installed to your system. It essentially tried to cook a meal, realized it was missing an ingredient, and threw the whole thing out before it ever hit the plate. Why you’re safe to proceed: No Binary Collision: Since the duckstation-git build failed, there is no executable sitting in /usr/bin/ to conflict with the Flatpak. Isolated Environments: Flatpak installs its files in a completely separate directory (/var/lib/flatpak/ or ~/.local/share/flatpak/). It doesn't care about failed AUR attempts. Clean Slate: The "junk" left over from your failed paru command is likely just a temporary build folder in ~/.cache/paru/clone/duckstation-git. You can leave it there, or run paru -Sc if you're obsessed with reclaiming a few megabytes of disk space. One Minor Detail If you managed to create a configuration folder at ~/.local/share/duckstation/ during your tinkering, the Flatpak will not see it by default because Flatpaks are sandboxed. It will look in: ~/.var/app/org.duckstation.DuckStation/data/duckstation/ If you have a BIOS file or saves you already moved, you'll need to move them to that path above. The Plan Run the install: flatpak install flathub org.duckstation.DuckStation Launch it: Find it in your application menu or run flatpak run org.duckstation.DuckStation. Move BIOS: Put your BIOS files in ~/.var/app/org.duckstation.DuckStation/data/duckstation/bios/. Stop worrying about the "mess" from the failed build; it’s non-existent. Are you ready to actually set up the emulator, or are we going to keep cleaning up ghosts?
