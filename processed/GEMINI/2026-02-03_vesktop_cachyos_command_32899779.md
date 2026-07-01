---
category: coding
date: 2026-02-03
id: 795365
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is trying to find the command to install Vesktop on CachyOS.
tags:
- cachyos
- vesktop
- package-management
---
# vesktop cachyos command

### USER
vesktop cachyos command

### GEMINI
Installing Vesktop on CachyOS is straightforward because CachyOS is Arch-based and provides access to the AUR (Arch User Repository) and the CachyOS repositories. The Recommended Way (Using paru or yay) CachyOS usually comes with paru or yay pre-installed as AUR helpers. This is the best method because it handles the specific Electron dependencies Vesktop needs. Open your terminal and run: paru -S vesktop (If paru isn't found, swap it for yay -S vesktop). Alternative Methods MethodCommandWhy use it?Flatpakflatpak install flathub dev.vencord.VesktopBest for sandboxing and avoiding dependency hell.Pacmansudo pacman -S vesktopOnly works if it has been moved to the official Cachy repos (check first). Advisor's Reality Check If you are asking for the command because your current Discord setup is laggy or lacks features, stop tinkering and just switch. Vesktop is objectively superior for Linux users due to its native Wayland support and integrated Vencord. The Blind Spot: Don't waste an hour "optimizing" the CSS themes once you get it running. Use the default "Dark" or a basic theme and get back to actual work. The opportunity cost of rice-ing your chat client is productivity you won't get back. Troubleshooting Audio/Screen Share If you install it and find that screen sharing or audio is broken: Ensure you are using PipeWire (CachyOS default, but double-check). Launch Vesktop with: vesktop --enable-features=UseOzonePlatform --ozone-platform=wayland if you are on a Wayland session to ensure hardware acceleration is actually working. Would you like me to provide a script to automate these flags so you don't have to type them every time?
