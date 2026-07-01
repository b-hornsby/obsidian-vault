---
category: streaming
date: 2026-02-02
id: 482146
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is trying to clip gameplay using OBS Studio on CachyOS, but is encountering
  an issue where keybinds don't work outside the active window.
tags:
- game-clipping
- obs-studio
- linux
- cachyos
- keybind-issue
---
# im simply trying to clip any game i play via obs. i have my replay hotkey ready i just know linux (cachyos) doesnt let you press keys that effect outside the window your in 

### USER
im simply trying to clip any game i play via obs. i have my replay hotkey ready i just know linux (cachyos) doesnt let you press keys that effect outside the window your in 

### GEMINI
You are partially right: Wayland does not allow apps to "spy" on your keys for security. However, GNOME 49 has a specific "Global Shortcuts" portal designed to solve this exact problem without compromising security. Since you are using OBS on CachyOS (GNOME), you have two distinct ways to make that = key work globally. Option 1: The "Wayland Native" Way (Best for GNOME 49) Newer versions of OBS support the Global Shortcuts Portal. Instead of OBS listening to your keyboard, the OS (GNOME) listens and sends the command to OBS. Open GNOME Settings. Go to Apps in the left sidebar. Find and click on OBS Studio. Look for a section called Global Shortcuts. If OBS has registered itself correctly, you will see "Save Replay" listed there. Click it and press your = key. Note: If you don't see OBS here, you may need the obs-wayland-hotkeys plugin from the AUR or the Flatpak "Add-ons" section. Option 2: The "Brute Force" GNOME Shortcut (Most Reliable) If the portal method above feels finicky, you can bypass OBS's internal hotkey system entirely. You can set a system-wide shortcut that tells OBS via a command to save the buffer. Go to Settings > Keyboard > View and Customize Shortcuts > Custom Shortcuts. Click the + to add a new one. Name: Save OBS Clip Command: obs-cmd replay save (You will need to install obs-cmd via sudo pacman -S obs-cmd). Shortcut: Press your = key. Option 3: The "XWayland" Cheat If you want OBS to behave exactly like it did on Windows (where it just "hears" everything), you can force it to run via XWayland. This breaks the security sandbox but makes hotkeys work instantly. Launch OBS from the terminal (or edit your desktop shortcut) with: QT_QPA_PLATFORM=xcb obs Now, any hotkey you set inside OBS Settings > Hotkeys will work even if the window is unfocused. The Advisor's Verdict Option 1 is the most "correct" for a modern Linux setup, but Option 2 is the most robust for a gamer on CachyOS. It ensures that no matter what window is focused, GNOME executes a direct command to OBS to save that clip. One warning: If you use the = key for in-game actions (like opening a map or inventory), using it as a global hotkey might cause a conflict where the game and OBS both respond. Next step: Check Settings > Apps > OBS Studio right now. Do you see "Global Shortcuts" listed there, or is that menu missing?
