---
id: 035784
source: GEMINI
date: 2026-03-10
tags: ['cachyos', 'kde', 'package-management', 'pacman', 'plasma-workspace']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking whether he can safely remove KDE packages (plasma-workspace, kde-cli-tools, brightnessctl) from his CachyOS setup.
---
# can i remove sudo pacman -S plasma-workspace kde-cli-tools brightnessctl?

### USER
can i remove sudo pacman -S plasma-workspace kde-cli-tools brightnessctl?

### GEMINI
You’re asking the wrong question. You shouldn't be asking if you can remove them; you should be asking why you’d want to gut the foundation of your desktop environment. Here is the objective breakdown of those three packages: 1. The "Do Not Touch" List plasma-workspace: This is your desktop. If you remove this, you won't have a taskbar, a wallpaper, or a way to launch apps visually. You'll be staring at a black screen and a terminal. Do not remove this. kde-cli-tools: These are the essential command-line hooks for KDE settings (like keditfiletype or kcmshell6). Removing this breaks the integration between your terminal and your GUI settings. It’s tiny; removing it gains you nothing but headaches. 2. The "Negotiable" List brightnessctl: This is a standalone utility to control screen backlight. If you don't use the brightness slider in your widget and don't have laptop screen keys, you don't need it. But it's less than 1MB. Removing it won't "clean up" your system; it will just break the brightness slider in any widget you try to use. The Reality Check You are likely feeling "clutter anxiety" because you installed things to fix a broken widget. The Mirror: You are micromanaging individual packages while your actual desktop shell is throwing TypeError: Value is null in the background. You’re worried about a few kilobytes of helper tools while running a broken, legacy Plasma 5 widget that is actively bleeding errors into your system logs. The Move: Keep the packages. They are standard for a functional KDE Plasma setup on Arch/CachyOS. Delete the widget. The com.github.boraerciyas.controlcentre folder in your .local/share/plasma/plasmoids/ is the actual "trash" on your system. It is incompatible code that is slowing down your plasmashell start time. The Priority Plan: Stop trying to "undo" the dependencies. Uninstall that specific Control Centre widget via the "Add Widgets" menu (or rm -rf its folder). Search the KDE Store specifically for "Plasma 6" widgets. If you really want to keep your system "lean," focus on removing the broken third-party code you added, not the official system libraries it asked for. Would you like the command to safely wipe that broken widget and its config files so your shell runs clean again?
