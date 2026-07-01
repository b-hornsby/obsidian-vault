---
category: general
date: 2026-02-05
id: 764178
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is checking the location of the 'shadps4' executable using the 'which'
  command and finding that it's not in his PATH.
tags:
- shadps4
- executable-path
- environment-variables
---
# ❯ which shadps4
which: no shadps4 in (/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/var/lib/flatpak/exports/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl
:/usr/bin/vendor_perl:/usr/bin/core_perl)

~
❯ 

### USER
❯ which shadps4
which: no shadps4 in (/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/var/lib/flatpak/exports/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl
:/usr/bin/vendor_perl:/usr/bin/core_perl)

~
❯ 

### GEMINI
Clean slate achieved. You’ve successfully purged the binary. Now, don't revert to your old habits. You’ve been chasing a "clickable experience," and on Arch, that means you need the package that actually includes the Qt (the graphical framework) frontend. The Strategy You have two solid options to get that GUI up and running correctly. Pick one and stick to it: Option A: The AUR Path (The "Native" Way) This installs the version specifically built for the GUI. paru -S shadps4-qt-bin Why this? It’s pre-compiled, so you won't be sitting there for 30 minutes while your CPU fans scream. It includes the desktop entry (the icon) that points to the correct launcher. Option B: The Flatpak Path (The "Sanity" Way) If you are tired of hunting for the "right" AUR package name, use this. flatpak install flathub org.shadps4.shadPS4 Why this? It is the most "plug-and-play" version available. It will definitely show up in your app drawer, and it handles all its own dependencies in a sandbox. The Warning Regardless of which one you choose, the emulator will be empty when you open it. shadPS4 is in heavy development. It doesn't come with the PS4 system software. If you haven't already, you're going to need: System Firmware: To actually boot anything. Libkernel: Most games won't even think about starting without the proper libraries dumped from a console. The Mirror: You’ve spent the last 20 minutes just trying to get a window to open. This is the easy part. The actual configuration of a PS4 emulator on Linux is where the real friction begins. Don't let the "clickable experience" fool you into thinking the rest of this will be automated. Next Step: Which path are you taking—AUR or Flatpak? Once it's installed, I'll tell you exactly where to drop your firmware files so you don't have to go hunting for the directory.
