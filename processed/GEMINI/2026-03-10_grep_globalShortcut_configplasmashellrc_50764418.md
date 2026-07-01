---
id: 538740
source: GEMINI
date: 2026-03-10
tags: ['kde', 'plasma', 'global-shortcuts', 'linux-customization']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is using grep to search for global shortcut configurations in his Plasma environment, likely to customize or troubleshoot them.
---
# ❯ grep "globalShortcut" ~/.config/plasmashellrc

~
❯ 

### USER
❯ grep "globalShortcut" ~/.config/plasmashellrc

~
❯ 

### GEMINI
The fact that grep returned nothing means the shortcut isn't explicitly defined in your plasmashellrc, which is actually the problem. In Plasma, if a shortcut isn't defined there, it often defaults to the internal hard-coded behavior: Meta = Application Launcher. You are currently stuck in a loop of configuring the "Receiver" (KWin) without properly disabling the "Interrupter" (Plasma Shell). The Direct Action Since you are on CachyOS (Arch-based), the version of Plasma 6 you’re running has a specific way of handling "Modifier Only" keys. If the shell thinks it owns the Meta key, your kwinrc edit is just background noise. Run these two commands to explicitly kill the default assignment and force the refresh: # 1. Clear any latent Meta-to-Launcher binding in the global settings kwriteconfig6 --file kdglobalsrc --group ModifierOnlyShortcuts --key Meta "" # 2. Re-apply the Overview binding to ensure it's the primary listener kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,,invokeShortcut,Overview" # 3. Reload KWin and Plasma Shell (The Nuclear Option) qdbus6 org.kde.KWin /KWin reconfigure plasmashell --replace & disown The Strategic Blind Spot You are verifying the files, but you aren't verifying the state. If the commands above don't work, the "Overview" effect itself is likely disabled in your Desktop Effects settings. CachyOS sometimes ships with specific performance presets that disable certain heavy animations like Overview. Check if the effect is even active: qdbus6 org.kde.KWin /Effects activeEffects | grep overview If that returns nothing, no amount of kwriteconfig6 will help you because you're trying to map a key to a ghost. You'll need to enable the effect first: kwriteconfig6 --file kwinrc --group Plugins --key overviewEnabled true qdbus6 org.kde.KWin /KWin reconfigure The Mirror You're treating this like a syntax error, but it's a logic error. You are focused on the "how" (the commands) while ignoring the "what" (the system's actual state). On a high-speed distro like Cachy, things move fast—if you want to be a "high-level advisor" to your own system, stop guessing with grep and start querying the live D-Bus session to see what's actually running. Would you like the D-Bus command to see exactly which component is currently intercepting your Meta key presses?
