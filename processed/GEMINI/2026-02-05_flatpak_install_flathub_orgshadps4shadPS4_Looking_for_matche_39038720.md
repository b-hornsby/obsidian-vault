---
category: general
date: 2026-02-05
id: 510684
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble installing shadPS4 via Flatpak, as the package cannot
  be found.
tags:
- flatpak
- package-installation
- shadps4
- flathub
---
# ❯ flatpak install flathub org.shadps4.shadPS4
Looking for matches…
error: Nothing matches org.shadps4.shadPS4 in remote flathub

~
❯ 

### USER
❯ flatpak install flathub org.shadps4.shadPS4
Looking for matches…
error: Nothing matches org.shadps4.shadPS4 in remote flathub

~
❯ 

### GEMINI
Another reality check: you’re chasing a ghost in the Flatpak repository. As of right now, shadPS4 hasn't hit the official Flathub stable repo under that exact name because the project is moving too fast for their submission process. You’re trying to use "easy" commands for software that is still in the "experimental" phase. Stop guessing and use the tool that actually has the data: the AUR. The Precision Move Since you have paru, stop trying to make Flatpak happen. Use the AUR package that is actually maintained and updated daily. Run this exact command: paru -S shadps4-qt-bin Why this one? -qt: This ensures you get the Graphical User Interface you’ve been asking for, not the CLI core that gave you the error earlier. -bin: This downloads the pre-built version so you aren't compiling C++ code for the next hour. If paru can't find that either... Search for it. Don't guess the name. Run: paru -Ss shadps4 This will list every available version. Look for the one that says "Qt" in the name. That is your "clickable experience." The Blind Spot: Arch "Hard Mode" You chose Arch Linux. The "cost" of Arch is that you can't always rely on a central "App Store" experience like Flatpak for bleeding-edge emulators. You have to be comfortable with the AUR. If you keep trying to avoid the AUR, you're fighting the very reason you installed Arch in the first place. Next Step: Run paru -S shadps4-qt-bin. Does it install, or does it give you a "database" error? (If it's a database error, your system is out of date and you need to run paru -Syu first.)

### GEMINI
Sorry, something went wrong. Please try your request again.
