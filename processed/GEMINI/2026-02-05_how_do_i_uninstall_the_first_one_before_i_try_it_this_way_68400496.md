---
category: general
date: 2026-02-05
id: 268190
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to uninstall a previously installed package before trying
  a different installation method.
tags:
- package-uninstall
- software-management
---
# how do i uninstall the first one before i try it this way?

### USER
how do i uninstall the first one before i try it this way?

### GEMINI
You’re asking to clean up the mess before making a new one. That's a rare moment of discipline—good. Since you used paru (which is just a wrapper for pacman), you need to strip out the package you installed and its unnecessary dependencies. 1. The Clean Sweep Run this to remove the package and any "orphaned" dependencies that nothing else on your system is using: paru -Rs shadps4-bin (If you installed the -git version, use shadps4-git instead.) -R: Remove the package. -s: Remove dependencies that aren't needed by other installed packages. This keeps your Arch install from becoming a graveyard of unused libraries. 2. Verify It’s Gone To make sure you aren't clicking a ghost icon, run: which shadps4 If it returns nothing, the "engine" is gone. If it returns a path, you didn't uninstall the right package. The Tactical Pivot Now that the slate is clean, don't repeat the mistake. Most people in the Arch/shadPS4 community are moving toward the Qt version because it bundles the GUI and the engine together correctly. Do this now: paru -S shadps4-qt-bin Note: Using the -qt-bin version (if available) specifically targets the Graphical User Interface build. This should give you the "clickable experience" you’ve been chasing without the CLI warning. The Opportunity Cost of "Messy" Installs Every time you install/uninstall/reinstall without knowing exactly what the package contains, you risk "Configuration Drift"—where your ~/.config folder fills up with junk files from failed attempts. Pro Tip: After you uninstall, check ~/.config/shadps4. If it exists, delete it (rm -rf ~/.config/shadps4) so your next install starts with a truly clean state. Next Step: Once the new version is in, do you want me to explain how to symlink your controllers, or are you going to see if they "just work" first?
