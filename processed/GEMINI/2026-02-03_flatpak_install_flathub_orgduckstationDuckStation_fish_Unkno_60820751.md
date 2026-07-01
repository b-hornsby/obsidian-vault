---
category: homelab
date: 2026-02-03
id: 553275
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to install DuckStation via Flatpak but encountered a 'command
  not found' error, indicating Flatpak wasn't recognized.
tags:
- flatpak
- duckstation
- emulator
- package-manager
- command-not-found
---
# ❯ flatpak install flathub org.duckstation.DuckStation
fish: Unknown command: flatpak

~
❯ 

### USER
❯ flatpak install flathub org.duckstation.DuckStation
fish: Unknown command: flatpak

~
❯ 

### GEMINI
You’re trying to run a command for a tool that isn't even installed on your system. You’re skipping the foundation and wondering why the house won't stand. If you’re on a fresh install or a distro that doesn't ship with it, you can't just wish flatpak into existence. You’re wasting time troubleshooting a command when the real issue is a missing dependency. The Reality Check You likely haven't installed the Flatpak framework itself, or your PATH is severely misconfigured. Assuming you are on a Debian/Ubuntu-based system, here is the objective path to fixing this: Install the Flatpak package: sudo apt update && sudo apt install flatpak Add the Flathub repository: (Flatpak is useless without a source) flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo Restart your shell or session: If you just installed it, fish might not pick up the new binary path immediately. The Strategy Stop guessing: Before running a tool-specific command, verify the tool exists with which flatpak. Check your environment: If you know it’s installed, fish isn't seeing it. You're likely missing /var/lib/flatpak/exports/bin or similar in your $PATH. Execution: Run the install command again only after the framework is confirmed. Would you like me to show you how to permanently add the Flatpak paths to your config.fish?
