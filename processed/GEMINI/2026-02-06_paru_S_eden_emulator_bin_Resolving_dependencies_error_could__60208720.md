---
category: general
date: 2026-02-06
id: 351135
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is failing to install the Eden emulator using Paru, as the package
  cannot be found in the AUR.
tags:
- paru
- package-installation
- eden-emulator
- aur
- dependency-resolution
---
# ❯ paru -S eden-emulator-bin
:: Resolving dependencies...
error: could not find all required packages:
    eden-emulator-bin (target)

~
❯ paru -S eden-emu
:: Resolving dependencies...
error: could not find all required packages:
    eden-emu (target)

~
❯ paru -S eden-emulator-git
:: Resolving dependencies...
error: could not find all required packages:
    eden-emulator-git (target)

~
❯ 

### USER
❯ paru -S eden-emulator-bin
:: Resolving dependencies...
error: could not find all required packages:
    eden-emulator-bin (target)

~
❯ paru -S eden-emu
:: Resolving dependencies...
error: could not find all required packages:
    eden-emu (target)

~
❯ paru -S eden-emulator-git
:: Resolving dependencies...
error: could not find all required packages:
    eden-emulator-git (target)

~
❯ 

### GEMINI
Stop trying to force the AUR. You’re hitting a wall because Eden is currently in a "Grey Market" state. Due to the legal fallout surrounding Switch emulation, many of these forks are being nuked from the AUR or renamed faster than maintainers can track. By repeatedly pinging non-existent packages, you're wasting time on "The Arch Way" when the software isn't officially there to meet you. You are playing a game of whack-a-mole with package names that don't exist yet. The Reality Check Eden is a fast-moving, high-risk project. Relying on an AUR helper for a fork that is frequently DMCA'd or relocated is a strategy for failure. You need the binary directly from the source to ensure you actually have the optimized build. The Direct Action Plan Stop messing with paru for this specific tool and do this: Go to the Source: Open your browser and go to the Eden Releases GitHub (or their official Discord/Telegram if the repo is currently down). Download the AppImage: This is the only way to ensure you have the specific optimizations Eden claims to provide without build errors. Manual Integration: Move the AppImage to ~/Applications or /opt/. Make it executable: chmod +x Eden-Whatever-Version.AppImage. The "Pro" Move: Use appimagelauncher or gear-lever (install via sudo pacman -S gear-lever). It will "install" the AppImage into your system menu so it behaves exactly like a native AUR package without the headache of broken builds. Why you’re failing right now You are assuming the AUR is a magical repository for every niche fork. It’s not. It’s community-maintained. If the community is scared or the project is too new/volatile, the AUR will be empty. Next Step: Do you want me to give you the terminal commands to automate the download and setup of the AppImage so you can stop fighting with paru?
