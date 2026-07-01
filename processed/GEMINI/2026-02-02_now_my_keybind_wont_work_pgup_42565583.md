---
category: streaming
date: 2026-02-02
id: 861245
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's OBS replay buffer keybind (PgUp) stopped working and he was trying
  to fix it.
tags:
- obs-keybind
- pgup
- replay-buffer-hotkey
---
# now my keybind wont work? pgup

### USER
now my keybind wont work? pgup

### GEMINI
On CachyOS (Wayland), standard "Hotkey" behavior in OBS is broken by design. Wayland treats every app as a secure island; it prevents OBS from "listening" to your keyboard when you are focused on another window (like CS2) to prevent keylogging. Since you switched to Page Up (PgUp), here is why it's failing and exactly how to fix it. 1. The Wayland Security Barrier In Windows, OBS can "hook" the keyboard globally. On Wayland, once you click into CS2, OBS becomes "blind" to your keypresses. The Fix: You need to use Global Shortcuts. If you are on KDE Plasma (default for CachyOS): Go to System Settings > Shortcuts > Global Shortcuts. Click Add New or look for OBS Studio in the list. You should see an entry for Save Replay. Bind PgUp here. Why: This tells the desktop environment (KDE) to intercept the key and pass it to OBS, bypassing the security restriction. 2. The "Numpad" Trap On many Linux distros, PgUp and Numpad 9 are interpreted differently depending on whether NumLock is on. The Check: Did you bind PgUp while NumLock was OFF, but now you're playing with it ON? The Fix: Try pressing the key both ways. If it only works when NumLock is off, re-bind it in OBS (or the Global Shortcut menu) while NumLock is in the state you usually play with. 3. Permission to "See" the Keyboard If you are using the Flatpak version of OBS (very common on Arch-based distros like Cachy), it is sandboxed. It literally cannot hear your keyboard outside of its own window without specific permissions. The Fix: Install Flatseal from the CachyOS repos/Octopi. Open Flatseal, select OBS, and look for Bus Talk or Inter-process communication. Ensure org.freedesktop.portal.Desktop is enabled. 4. Direct Plugin Fix (The "Pro" Route) If the above feels like a headache, install the obs-wayland-shortcuts-git package from the AUR. This plugin specifically bridges the gap between Wayland's security and OBS's need for global hotkeys. After installing, restart OBS, and it should "hear" PgUp even while you're flicking heads in CS2. The Advisor's Verdict Stop fighting the keyboard. If you are using a Stream Deck (as you mentioned earlier), ignore the hotkey entirely. Go back to the Stream Deck software and use the Direct OBS Integration (Option 2 from my previous message). Because that uses a websocket (a network connection) to talk to OBS, it doesn't care about Wayland's keyboard security or what window is focused. It will work 100% of the time. Would you like the specific terminal commands to install the Wayland shortcut fix from the AUR?
