---
category: homelab
date: 2026-02-03
id: 054888
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to remove a Steam shortcut from his desktop on CachyOS.
tags:
- steam
- desktop-shortcut
- cachyos
- linux-desktop
---
# How do I get rid of the steam shortcut on my desktop cachyos?

### USER
How do I get rid of the steam shortcut on my desktop cachyos?

### GEMINI
If seeing a shortcut on your desktop already feels like "clutter," then your instinct for a clean system is finally kicking in. In KDE Plasma, the desktop isn't just a folder; it’s a coordinate-based space managed by the "Folder View" widget. To get rid of that Steam icon, you have two options depending on how "clean" you actually want to be. 1. The Quick Delete (The "Surface" Clean) Right-click the Steam icon. Select Move to Trash (or press Delete on your keyboard while it's highlighted). Note: This only deletes the shortcut file (.desktop file) located in your ~/Desktop folder. It does not uninstall Steam. 2. The Total Desktop Purge (The "Minimalist" Way) If you want a truly clean "fresh start" look, you shouldn't have any icons on your desktop. In KDE, you can disable icons entirely: Right-click any empty space on your desktop. Select Configure Desktop and Wallpaper. Under the Mouse Actions or Layout section, you can change the Layout from "Folder View" to "Desktop". The Result: Your desktop becomes a pure wallpaper zone. No files, no icons, no mess. You access everything via the Meta (Windows) key or the Taskbar. The "Advisor" Warning: The fact that Steam put a shortcut there in the first place means you probably checked a box during the Steam install or the CachyOS Welcome app. Watch your habits: As you install your library, launchers will try to litter your desktop with "quick access" icons. Stop clicking "Next" blindly. * Stop allowing installers to dictate your file structure. If you want this instance to stay fast, use the KRunner (Alt+Space or just start typing with the Start menu open) to launch apps. It’s faster than hunting for an icon with a mouse and keeps your workspace pristine. What's the next piece of "bloat" you've spotted? Let's kill it before it multiplies.
