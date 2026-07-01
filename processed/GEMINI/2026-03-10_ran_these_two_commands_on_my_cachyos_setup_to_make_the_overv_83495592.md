---
category: homelab
date: 2026-03-10
id: 671643
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to configure a keyboard shortcut to activate the overview
  effect in KDE on CachyOS, but the shortcut is opening the application menu instead.
tags:
- kde
- kwin
- keyboard-shortcuts
- linux-customization
- cachyos
---
# ran these two commands on my cachyos setup to make the overview happen when i press the windows/meta key but when i do it it still opens the application menu: ❯ kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,,invokeShortcut,O
verview"

~
❯ qdbus org.kde.KWin /KWin reconfigure

~
❯ 

### USER
ran these two commands on my cachyos setup to make the overview happen when i press the windows/meta key but when i do it it still opens the application menu: ❯ kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,,invokeShortcut,O
verview"

~
❯ qdbus org.kde.KWin /KWin reconfigure

~
❯ 

### GEMINI
The reason your commands aren't sticking is likely a syntax error in the string or a conflict with Plasma's default "Meta opens Menu" behavior, which often overrides manual kwinrc edits if not handled correctly. You’re trying to treat a high-performance, rolling-release distro like a "set and forget" OS. If you want the Meta key to trigger the Overview, you have to be precise with the D-Bus path and ensure the OS isn't fighting you for control of that key. 1. Fix the Command Syntax Your command has a trailing quote issue and potentially an incomplete D-Bus string. Run this exact block: kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,,invokeShortcut,Overview" qdbus6 org.kde.KWin /KWin reconfigure Note: Since you are on CachyOS (Plasma 6), ensure you are using qdbus6 to target the correct session bus. 2. Kill the "Application Launcher" Ghost Even with the config change, Plasma often defaults the Meta key to the Application Launcher. You need to unbind it from the widget itself: Right-click your Application Launcher (Start button) icon. Select Configure Application Launcher. Go to Keyboard Shortcuts. If Meta is listed there, click the "x" to remove it or change it to something else (like Alt+F1). 3. Verification If it still fails, check the actual file to ensure the entry isn't duplicated or mangled: grep -A 3 "ModifierOnlyShortcuts" ~/.config/kwinrc If you see Meta=... more than once, the parser is likely ignoring your new instruction. The Reality Check: You are spending time manually hacking config files for a feature that is a single checkbox in the System Settings > Desktop Effects or Screen Edges menus in Plasma 6. If you're going to use a "power user" distro like Cachy, stop brute-forcing commands you found online without verifying the Plasma version they were written for. Efficiency isn't just about using the terminal; it's about knowing when the terminal is the slow way. Would you like me to show you how to script a full backup of your kwinrc before you make further manual edits?
