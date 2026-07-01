---
category: ai-tools
date: 2026-02-27
id: 27786
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants to uninstall Cursor IDE installed via Paru on CachyOS and install
  the Flatpak version instead.
tags:
- cursor-ide
- paru
- flatpak
- uninstallation
- installation
- cachyos
---
# i think i downloaded cursor via paru on cachyos. i want to uninstall it and download the right flatpack

### USER
i think i downloaded cursor via paru on cachyos. i want to uninstall it and download the right flatpack

### GEMINI
If you’re moving from the AUR version to a Flatpak, you’re making a trade: you lose the system-native integration, but you gain a sandbox and easier updates. Let's not waste time with half-measures—here is exactly how to strip the AUR version out and get the Flatpak running. 1. Identify and Remove the AUR Version Since you used paru, the package is likely cursor-bin. Use this command to remove the package and any of its now-useless dependencies (the -Rns flag is the "burn it down" option for cleanliness): sudo pacman -Rns cursor-bin Note: If you get an error that the package isn't found, run paru -Qs cursor to find the exact name you installed, then swap it in. 2. Purge the "Ghost" Configs Uninstalling the package doesn't touch your home directory. If you want a truly fresh start for the Flatpak version (to avoid configuration conflicts), wipe these directories: rm -rf ~/.config/Cursor rm -rf ~/.cursor 3. Install the Flatpak CachyOS is Arch-based, so if you haven't set up the Flathub repository yet, do that first. Step A: Add Flathub (if not already done) flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo Step B: Install Cursor As of now, there is no official Cursor Flatpak maintained by the Anysphere team (the creators of Cursor). The community-maintained version is the standard choice: flatpak install flathub com.getcursor.Cursor 4. The "Small Player" Check You’re switching to Flatpak because it’s "cleaner," but keep this in mind: Flatpaks are sandboxed. If you try to run terminal commands or use your system's compilers (GCC, Python, Node.js) inside the Cursor terminal and they "disappear," it’s because the sandbox is doing its job. You will likely need Flatseal to manage permissions or use the flatpak-spawn --host trick to reach your system tools. Would you like me to show you how to give the Flatpak version access to your system compilers so you don't break your workflow?
