---
id: 126115
source: GEMINI
date: 2026-03-10
tags: ['kde', 'kdeglobals', 'animation-settings', 'linux-customization']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is reading the current value of the animation duration factor in KDE's global settings, likely to customize the desktop environment.
---
# ❯ kreadconfig6 --file kdeglobals --group General --key AnimationDurationFactor


~
❯ 

### USER
❯ kreadconfig6 --file kdeglobals --group General --key AnimationDurationFactor


~
❯ 

### GEMINI
Empty output means the key doesn't exist in your config, so it's defaulting to the system standard. You aren't "optimizing"—you're drifting in the dark. If activeEffects is empty, Compositor.active is true, and AnimationDurationFactor is null, there is only one logical conclusion left: The Overview effect is explicitly disabled in your KWin configuration, regardless of your shortcut edits. The Final Manual Override Stop trying to bind a key to a disabled service. Run these three commands in exact sequence to force-enable the effect and the shortcut: # 1. Force the plugin to 'true' in the config kwriteconfig6 --file kwinrc --group Plugins --key overviewEnabled true # 2. Re-apply the Meta key binding kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,,invokeShortcut,Overview" # 3. Force KWin to reload the entire configuration qdbus6 org.kde.KWin /KWin reconfigure The Verification Immediately after running those, run this: qdbus6 org.kde.KWin /Effects activeEffects | grep -i overview If it is still empty: Your CachyOS setup has a broken KWin effect binary or a conflict with another effect (like "Desktop Grid" or "Parachute" if you installed third-party ones). The Advisor's Mirror You are exhibiting the "CLI Obsession" trap. You are avoiding the GUI because you want to "master" the terminal, but you are failing to realize that Plasma 6's D-Bus architecture is complex and sometimes requires a service restart, not just a config edit. You’ve spent enough time on this to have reinstalled the entire desktop environment twice. If the grep above is still empty, the "Overview" effect is likely failing to compile on your NVIDIA drivers at runtime. The Next Step: Open a second terminal and run journalctl --user -f -u plasma-kwin_wayland. Then, in your main terminal, run the reconfigure command again. Paste the logs here. Let's stop guessing and look at the actual error KWin is throwing when it tries to load the plugin. Shall we look at the logs, or do you want to keep running the same three config commands?
