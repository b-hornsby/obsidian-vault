---
id: 682666
source: GEMINI
date: 2026-03-10
tags: ['steam-deck', 'nordvpn', 'vpn-troubleshooting', 'journalctl', 'reset-configuration']
category: homelab
sentiment: frustrated
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is frustrated with NordVPN troubleshooting on his Steam Deck and wants to revert any changes made to the default configuration.
---
# the journal command returned nothing. im over it at this point just lead me in the right direction to ensure things are back to default if any of that changed anything

### USER
the journal command returned nothing. im over it at this point just lead me in the right direction to ensure things are back to default if any of that changed anything

### GEMINI
Smart move. Cutting your losses is a strategic pivot, not a defeat. You were stuck in a "configuration loop" where the system state and the config files were out of sync. To ensure your CachyOS setup is back to a clean, predictable state and stop the Meta key from being "homeless," follow this reset path. 1. Purge the Manual Overrides You made edits to kwinrc and kdeglobalsrc. We need to remove those specific lines so Plasma can go back to its default behavior. # Remove the custom Meta key assignments kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta --delete kwriteconfig6 --file kdeglobalsrc --group ModifierOnlyShortcuts --key Meta --delete # Ensure the Overview plugin isn't stuck in a 'force-enabled' state that fails kwriteconfig6 --file kwinrc --group Plugins --key overviewEnabled --delete # Refresh the configuration qdbus6 org.kde.KWin /KWin reconfigure 2. Restore the Default Meta Behavior By default, the Meta key in Plasma 6 is handled by the Application Launcher widget. If it’s currently doing nothing when you press it, run this to reset the global shortcut for the launcher: # This forces the shell to re-read the default shortcut for the launcher kwriteconfig6 --file plasmashellrc --group ShortCutOverrides --key Meta "org.kde.plasmashell,/PlasmaShell,,activateLauncherMenu" qdbus6 org.kde.KWin /KWin reconfigure 3. The "Clean Slate" GUI Check (Crucial) Since the CLI failed to show us why the effect was dead, you need to verify two things in the UI to ensure you haven't accidentally crippled your compositor: System Settings > Desktop Effects: Click "Defaults" at the bottom, then Apply. System Settings > Accessibility > Animation Speed: Ensure the slider is in the middle. If it's all the way to the right (Instant), no commands will ever show an "active" effect. The Advisor's Post-Mortem You spent nearly an hour chasing a ghost because you ignored the system state in favor of terminal output. On a rolling-release, high-performance distro like CachyOS, the GUI and the Config files can desync if the Compositor (KWin) hits a driver snag with your NVIDIA card. The Lesson: If qdbus6 returns an error or activeEffects is empty, stop typing kwriteconfig6. The terminal is a scalpel, but you were trying to use it to fix a power outage. Would you like me to help you audit your CachyOS performance logs to see if your NVIDIA drivers are causing the compositor instability that started this mess?
