---
id: 916292
source: GEMINI
date: 2026-02-03
tags: ['flatpak', 'flathub', 'remote-repository', 'package-manager', 'xdg-data-dirs']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was adding the Flathub repository to Flatpak and received a warning about XDG_DATA_DIRS, suggesting applications might not appear until a restart.
---
# ❯ flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

Note that the directories 

'/var/lib/flatpak/exports/share'
'/home/toastedmel0n/.local/share/flatpak/exports/share'

are not in the search path set by the XDG_DATA_DIRS environment variable, so
applications installed by Flatpak may not appear on your desktop until the
session is restarted.


~
❯ 

### USER
❯ flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

Note that the directories 

'/var/lib/flatpak/exports/share'
'/home/toastedmel0n/.local/share/flatpak/exports/share'

are not in the search path set by the XDG_DATA_DIRS environment variable, so
applications installed by Flatpak may not appear on your desktop until the
session is restarted.


~
❯ 

### GEMINI
You’ve reached the final hurdle. The message you're seeing is just a warning that your desktop environment (KDE, GNOME, etc.) won't "see" the DuckStation icon in your app menu until you log out and back in. But we aren't here to wait for a restart. You want to get this running now. The Immediate Fix You don't need to restart your whole computer to install the app. Run the install command immediately: flatpak install flathub org.duckstation.DuckStation How to Launch It (Without the App Menu) Since your XDG_DATA_DIRS hasn't updated yet, the icon won't show up in your launcher. Use the terminal to force it open once the install finishes: flatpak run org.duckstation.DuckStation The Strategic Cleanup To fix that warning permanently so you don't have to keep using the terminal, you have two choices: The Lazy (but correct) Way: Complete the installation, then Log Out and Log Back In. CachyOS will automatically pick up the new paths on the next session. The "Power User" Way (Fish Shell): If you want to fix the path for your current fish session without logging out, run this: set -gx XDG_DATA_DIRS $XDG_DATA_DIRS:/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share Why this happened CachyOS is a rolling release. When you installed the flatpak package two minutes ago, it dropped a script into /etc/profile.d/ that sets those paths. However, your current session already loaded its environment variables when you logged in this morning. It doesn't know the world has changed. Your Final Move: Run the flatpak install command right now. Launch it with flatpak run org.duckstation.DuckStation. Log out/in whenever you're done playing to make the icon appear in your menu permanently. Ready to move your BIOS files into the sandbox, or do you need the specific directory path again?
