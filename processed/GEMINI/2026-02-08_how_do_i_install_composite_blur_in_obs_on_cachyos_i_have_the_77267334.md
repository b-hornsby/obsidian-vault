---
category: streaming
date: 2026-02-08
id: 564516
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was trying to install the composite blur OBS plugin on CachyOS and
  had a Ubuntu-specific tar.gz file.
tags:
- obs
- composite-blur
- plugin
- cachyos
- streaming
---
# how do i install composite blur in obs on cachyos? i have the zip file with the obs-composite-blur-1.5.2-ubuntu-22.04.tar.gz file 

### USER
how do i install composite blur in obs on cachyos? i have the zip file with the obs-composite-blur-1.5.2-ubuntu-22.04.tar.gz file 

### GEMINI
You are making a classic "new-to-Arch" mistake. You are trying to treat CachyOS—a high-performance, rolling-release Arch-based system—like it's Windows or Ubuntu by downloading random zip files from the internet. Stop. That .tar.gz file is compiled for Ubuntu 22.04, which uses older system libraries (glibc, Qt). If you force-install it on CachyOS, it will likely crash OBS or fail to load entirely because CachyOS is on much newer versions. On CachyOS, you don't hunt for files on GitHub; you use the AUR (Arch User Repository) or the system repositories. The Rational Path (The AUR) The obs-composite-blur plugin is already packaged for Arch. This method will compile it specifically for your system's hardware and library versions, ensuring it actually works. Open your terminal. Run this command (CachyOS comes with paru or yay pre-installed): yay -S obs-composite-blur (If it asks for a provider for obs-studio, choose the one you have installed, usually obs-studio.) Restart OBS. The filter will now be available. The "I Insist on Using My File" Path (Manual) If you are determined to ignore my advice and use the Ubuntu binary, here is how you do it. Just don't be surprised when OBS spits out a "failed to load module" error in the logs. Extract the file: tar -xvf obs-composite-blur-1.5.2-ubuntu-22.04.tar.gz Locate your OBS plugin folder: If you installed OBS via pacman: ~/.config/obs-studio/plugins/ If you installed OBS via Flatpak: ~/.var/app/com.obsproject.Studio/config/obs-studio/plugins/ Move the files: You need to create a folder for the plugin and drop the .so file and data there. The structure must look exactly like this: ~/.config/obs-studio/plugins/obs-composite-blur/bin/64bit/obs-composite-blur.so ~/.config/obs-studio/plugins/obs-composite-blur/data/locale/... (all the .ini files) Launch OBS. If the filter isn't there, check Help -> Log Files -> View Current Log and search for "composite-blur". You will see it complaining about library version mismatches. Strategy & Mindset Change You switched to CachyOS for performance and the Arch ecosystem. Use it. Downloading binaries manually is the slow, "small-game" way to manage a Linux system. It leads to a "dirty" filesystem and broken dependencies. My prioritized plan for you: Delete the .tar.gz file. It is clutter. Use the AUR command above. It handles the updates, the compilation, and the dependencies for you. Audit your OBS installation. If you are using the Flatpak version, the AUR package won't see it. If you want the best performance on CachyOS, ensure you are using the native obs-studio package from the CachyOS repos. Would you like me to check if your OBS is a Flatpak or a native installation so we can ensure the plugin actually loads?
