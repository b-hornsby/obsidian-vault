---
category: homelab
date: 2026-02-03
id: 621942
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan accidentally uninstalled Konsole on CachyOS and is seeking help to
  recover or reinstall it.
tags:
- konsole
- cachyos
- terminal-emulator
- accidental-removal
---
# accidentally uninstalled konsole?

### USER
accidentally uninstalled konsole?

### GEMINI
Don't panic. This is a rite of passage in Arch Linux. You removed the "GNOME" group, and since Konsole wasn't part of it, you likely accidentally included it in a "remove orphans" command or a recursive wipe. Since you are in KDE, you have three "backdoors" to get your terminal back without needing a terminal to do it. Method 1: The "Krunner" Trick (Easiest) KDE has a built-in runner that can execute commands directly. Press Alt + F2 (or just start typing on your empty desktop). Type this exactly: pkg_add konsole (If CachyOS has their helper active) OR kioclient5 exec "konsole" (To see if it's actually still there but just hidden). If that doesn't work, type this into the runner: systemsettings Navigate to Applications > Default Applications and see if "Terminal Emulator" has anything else listed (like xterm). If it does, open that. Method 2: The "TTY" (The Fail-Safe) Linux has a "hidden" text-only mode that exists underneath your desktop. Press Ctrl + Alt + F3 on your keyboard. The screen will go black and ask for a login. Type your username (toastedmel0n) and press Enter, then type your password. Now you are in a raw terminal. Run: sudo pacman -S konsole Once it's done, press Ctrl + Alt + F1 (or F2) to jump back to your colorful KDE desktop. Method 3: Use "Octopi" (The GUI Way) CachyOS usually comes with a graphical app store called Octopi or Discover. Open your Application Launcher (the "Start" menu). Search for Octopi or Discover. Search for "Konsole". Click Install or Apply. The Advisor's Brutal Truth You just learned why we check the "removal list" before hitting 'Y'. You likely ran sudo pacman -Rsc, which "cascades" and deletes everything that even thinks about the packages you named. Konsole probably shared a tiny library with a GNOME component you nuked. Go with Method 2 (Ctrl + Alt + F3). It’s the fastest way and it makes you look like a pro. Did you get back into the desktop with Konsole reinstalled? Once you're back, let's make sure you didn't accidentally delete networkmanager too (check if your internet still works).
