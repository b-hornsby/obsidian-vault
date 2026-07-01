---
category: streaming
date: 2026-02-04
id: 007708
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was troubleshooting OBS not working with QT_QPA_PLATFORM=xcb via command
  line arguments and Stream Deck keybind assignment.
tags:
- obs
- qt
- wayland
- cachyos
- stream-deck
- keybind
---
# it worked when i ran the QT_QPA_PLATFORM=xcb obs command but when i add it to the command line arguments it doesnt? i tried adding the custom command via step 3 but it wont let me assign page down?

### USER
it worked when i ran the QT_QPA_PLATFORM=xcb obs command but when i add it to the command line arguments it doesnt? i tried adding the custom command via step 3 but it wont let me assign page down?

### GEMINI
The reason it failed when you added it as a "command line argument" is because QT_QPA_PLATFORM=xcb is an environment variable, not an argument. It tells the system how to launch the app before the app even starts. Putting it in the "Arguments" box is like trying to put the car's fuel in the trunk instead of the gas tank. Here is exactly how to fix the shortcut and why Step 3 (the KDE shortcut) is fighting you. 1. The Correct Way to Edit the Shortcut In KDE Plasma (CachyOS), you need to format the "Command" field specifically so the system knows to apply the environment variable. Right-click your Application Launcher (Start button) > Edit Applications. Find OBS Studio (usually under Multimedia). Look at the Command field. It likely says obs. Change it to exactly this: env QT_QPA_PLATFORM=xcb obs %U Save it. Crucial: Close all running instances of OBS before launching it from the menu again. Why env? The env command tells the shell to set the following variable (QT_QPA_PLATFORM) for the duration of the program's life. This forces OBS to run as an X11 app, which allows it to "hook" your keyboard even when you're focused on a game. 2. Why Step 3 (Page Down) Failed KDE likely won't let you assign Page Down as a global shortcut because it’s considered a "Standard Key" that is usually reserved for navigation. Wayland/KDE is protective of keys that could interfere with typing or scrolling. The Reality: Even if you forced it to work, using a single key like PgDn is a bad strategic move. If you're typing in a game chat or scrolling a menu, you'll trigger a recording and waste disk space/write cycles. The Fix: Use a combo. If you absolutely want a "one-tap" feel, use a Function key like F10 or F12. 3. The "CachyOS" Performance Warning By forcing xcb (X11 mode) on Wayland, you are using XWayland. The Risk: You might see a tiny bit more input lag or "stutter" in the OBS preview compared to native Wayland. The Trade-off: If your clips are saving and the game feels smooth, ignore the purists. Functionality beats "theoretical performance" every time. Final Check If you’ve updated the shortcut with env QT_QPA_PLATFORM=xcb obs %U and it still won't work: Open your terminal. Type which obs. If it says /usr/bin/obs, ensure your shortcut points to that path. Is OBS now launching correctly from your menu with the hotkeys working, or is it giving you an error when you click the icon?
