---
id: 129169
source: GEMINI
date: 2026-02-02
tags: ['mouse-lock', 'window-focus', 'gaming', 'cachyos', 'input-confinement']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted to lock his mouse cursor to a specific game window on CachyOS to prevent it from leaving the game.
---
# how do i lock my mouse so its only focused on the window i play games in? im on cachyos

### USER
how do i lock my mouse so its only focused on the window i play games in? im on cachyos

### GEMINI
Since you’re on CachyOS, you’re likely using either KDE Plasma or Hyprland (their two most popular spins) on Wayland. The "cursor escaping" issue is a classic symptom of how Wayland handles window focus compared to X11. Here is the objective breakdown of how to fix this, depending on your setup. 1. The Wayland "Constraint" Reality In Wayland, the compositor (the thing drawing your desktop) manages the pointer. If a game isn't explicitly "locking" the pointer via the relative-pointer or pointer-constraints protocols, your mouse will drift. If you are on KDE Plasma (Wayland) KDE has a built-in "Legacy" toggle that often fixes this for games running via XWayland (which is most games on Steam/Proton). Go to System Settings > Input Devices > Mouse. Look for "Pointer Barrier" or "Lock cursor to window." The Pro-Move: Use a Window Rule. Press Alt + F3 while the game is open. Go to More Actions > Configure Special Window Settings. Add Property: Pointer Constraint. Set it to "Force" and "Confined to window." If you are on Hyprland (The CachyOS Default) Hyprland usually handles this well, but if it’s failing, you are likely playing in "Windowed" or "Borderless" mode. The Solution: Force the game into Fullscreen. If you need to lock it manually while windowed, you can use a bind in your hyprland.conf: bind = $mainMod, L, fakefullscreen This tricks the app into thinking it has total control of the geometry. 2. The "Gamescope" Solution (The Nuclear Option) If you want a professional-grade fix that works regardless of your desktop environment, use Gamescope. It’s a micro-compositor (the same one the Steam Deck uses). It creates a "sandbox" for your game where the mouse literally cannot leave the box unless you hit a shortcut. Install it: sudo pacman -S gamescope Launch your game with these arguments (Steam > Properties > Launch Options): gamescope -f -e -- %command% -f: Fullscreen. -e: Integration with Steam/Wayland. This forces a hardware-level lock on the cursor. 3. The Strategy: Stop the Drift Your reasoning for "locking" the mouse is likely a workaround for a bigger issue: Windowed Mode Latency. The Blind Spot: You are likely playing in "Borderless Windowed" because you want to Alt-Tab quickly. On Linux, this is the primary cause of cursor drift. The Correction: Use Fullscreen combined with Gamescope. It gives you the "instant" Alt-Tab feel of borderless but the hard cursor-lock of exclusive fullscreen. Your Next Step Tell me which Desktop Environment you chose during the CachyOS install (KDE, Hyprland, or GNOME). Once I know that, I can give you the exact terminal command or config line to permanently hard-lock that cursor.
