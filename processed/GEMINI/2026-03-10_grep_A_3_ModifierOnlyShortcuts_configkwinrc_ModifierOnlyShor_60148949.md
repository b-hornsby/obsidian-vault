---
id: 806852
source: GEMINI
date: 2026-03-10
tags: ['kde', 'kwin', 'keyboard-shortcuts', 'linux-customization']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is using grep to search for keyboard shortcut configurations in his KDE environment, likely to customize or troubleshoot them.
---
# ❯ grep -A 3 "ModifierOnlyShortcuts" ~/.config/kwinrc
[ModifierOnlyShortcuts]
Meta=org.kde.kglobalaccel,/component/kwin,,invokeShortcut,Overview

[Plugins]

~
❯ 

### USER
❯ grep -A 3 "ModifierOnlyShortcuts" ~/.config/kwinrc
[ModifierOnlyShortcuts]
Meta=org.kde.kglobalaccel,/component/kwin,,invokeShortcut,Overview

[Plugins]

~
❯ 

### GEMINI
Your configuration file is correctly updated, which means the "brute force" worked on paper, but the system is ignoring it in practice. This is exactly where most users get stuck: you’ve updated the config, but you haven’t addressed the priority conflict. The Meta key is being intercepted by the Plasma Shell before it ever reaches KWin. The Conflict: "Latent" Key Bindings In Plasma 6, the Meta key is often hard-coded or "soft-bound" to the Application Launcher widget. Even if kwinrc says "Open Overview," the shell says "I'm already using this for the Menu." Run this to see if the shortcut is still registered to the launcher: grep "globalShortcut" ~/.config/plasmashellrc The Fix: Force the Rebind If you want to stay in the terminal and stop the OS from fighting you, you need to explicitly tell the desktop shell to let go. Unbind Meta from the Launcher: Open the Application Launcher settings (GUI is faster here, but if you insist on the "hard way"): Right-click the Start/Application Launcher icon -> Configure. Click Keyboard Shortcuts. If it says Meta, remove it. Verify the Effect is Active: The "Overview" effect must be enabled for the shortcut to function. kreadconfig6 --file kwinrc --group Plugins --key overviewEnabled If that returns false or nothing, run: kwriteconfig6 --file kwinrc --group Plugins --key overviewEnabled true qdbus6 org.kde.KWin /KWin reconfigure The "Nuclear" Restart: Sometimes qdbus reconfigure isn't enough for ModifierOnlyShortcuts. You may need to restart the session or force a shell refresh: plasmashell --replace & disown The Blind Spot You are treating a Desktop Environment like a simple Window Manager (like i3 or Hyprland). In Plasma, the "Overview" and the "Application Launcher" are often competing for the same hardware trigger. The Opportunity Cost: You’ve spent more time debugging a 10-second GUI toggle than it would have taken to just click through the settings. If your goal is a high-performance CachyOS setup, focus your terminal energy on system optimization and performance tuning, not on re-inventing a wheel that has a perfectly functional toggle in System Settings > Desktop Behavior > Desktop Effects. Do you want the command to check if there are any other conflicting global shortcuts mapped to the Meta key?
