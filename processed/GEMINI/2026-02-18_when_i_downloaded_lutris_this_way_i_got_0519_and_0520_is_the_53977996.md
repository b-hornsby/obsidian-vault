---
category: homelab
date: 2026-02-18
id: 815284
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is checking if the Lutris version he installed (0.5.19 or 0.5.20) is
  the latest, indicating he wants to ensure he has the most up-to-date version.
tags:
- lutris
- version-check
- game-launcher
- linux-gaming
---
# when i downloaded lutris this way i got 0.5.19 and 0.5.20 is the latest version?

### USER
when i downloaded lutris this way i got 0.5.19 and 0.5.20 is the latest version?

### GEMINI
Lutris 0.5.20 was released literally yesterday (February 17, 2026). The reason you have 0.5.19 is that you are on a rolling-release distro (CachyOS/Arch), and new releases usually sit in the testing repositories for 24–48 hours to ensure they don't break your system before hitting the stable repos. The Advisor's Reality Check You are experiencing the "Update Fever" common in Linux users. 0.5.20 is a major release because it makes umu-launcher the default, which significantly improves how Lutris handles Proton. However, forcing an update 24 hours after release is how people break their dependencies. If your games are running fine right now, wait 24 hours. It will show up in a standard sudo pacman -Syu naturally. If You Can't Wait (The Options) If you absolutely must have the latest features (like the new Steam Family support or the better Wayland driver) right now: 1. The "Safety First" Way (Flatpak) If you need 0.5.20 today without touching your system libraries, use the Flatpak version. It updates independently of the CachyOS repositories. flatpak install flathub net.lutris.Lutris 2. The "Cutting Edge" Way (Lutris-Git) You can install the development version from the CachyOS repositories, which is already at 0.5.20 levels. sudo pacman -S lutris-git Note: This will replace your current Lutris installation. Your games and configs will stay, but the binary changes. 3. The "Impatience" Way (Extra-Testing) You can pull the package directly from Arch's testing repo, but I advise against this for a beginner because it might require updated libraries your system hasn't cleared for stable yet. My Recommendation Do nothing for one day. CachyOS maintainers are fast, but they have to recompile the package for the v3 architecture you're using. The Opportunity Cost: If you force the update now and it has a bug, you'll spend 2 hours troubleshooting why your games won't launch. If you wait 24 hours, you spend 0 minutes. Would you like me to check again tomorrow to see if the stable v3 build is live, or do you want the instructions to switch to lutris-git right now?
