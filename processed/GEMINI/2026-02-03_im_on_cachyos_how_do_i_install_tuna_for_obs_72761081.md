---
category: streaming
date: 2026-02-03
id: 704617
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to install the Tuna now-playing plugin for OBS on CachyOS.
tags:
- tuna
- obs-studio
- cachyos
- now-playing
- streaming-plugin
---
# im on cachyos how do i install tuna for obs?

### USER
im on cachyos how do i install tuna for obs?

### GEMINI
Since you're on CachyOS (an Arch-based powerhouse), you don't need to manually mess with folders and zip files like a Windows user. You have the AUR (Arch User Repository), which is the most efficient way to handle this. Stop trying to find a "Linux installer" on a website. Use your terminal to build it correctly for your system. 1. The Pro Way: Using an AUR Helper CachyOS usually comes with paru or yay pre-installed. Open your terminal and run: # Try paru first paru -S obs-plugin-tuna-bin # Or if you prefer yay yay -S obs-plugin-tuna-bin Why the -bin version? It uses the pre-compiled binary. If you choose obs-plugin-tuna-git, your computer will compile it from source code, which is fine but takes longer and can sometimes throw errors if your dependencies aren't perfect. 2. The Flatpak "Trap" If you installed OBS via Flatpak (which CachyOS sometimes defaults to in the GUI store), the AUR method above will not work. Plugins installed via system packages cannot talk to Flatpak apps. If you are using the Flatpak version: You must install the Tuna plugin specifically for Flatpak. flatpak install flathub com.obsproject.Studio.Plugin.Tuna My Advice: If you're serious about streaming on Arch/CachyOS, uninstall the Flatpak and install the native version (sudo pacman -S obs-studio). Native OBS handles plugins, hardware encoding (VA-API/NVENC), and browser sources much more reliably on Arch. 3. Verify the Install Launch OBS. Look at the top menu bar. If you see Tools > Tuna Settings, you’ve succeeded. If it's not there, run obs from the terminal and look at the output—it will tell you exactly which library is missing (usually mbedtls or taglib). 4. Connecting your Music Once Tuna is open, go to the "Basics" tab: Music Source: Select MPRIS. Why? On Linux, MPRIS is the universal standard. This allows Tuna to "talk" to almost any player (Spotify, Strawberry, Cider, VLC, or even a Firefox tab playing YouTube) without needing specific APIs for each one. The Reality Check You chose an Arch-based distro for performance and control. Don't fall back into "Windows habits" of downloading .zip files from GitHub. Use the AUR; it’s the reason you’re using this OS in the first place. Would you like me to show you how to set up the MPRIS listener so it automatically switches between your browser and your music player?
