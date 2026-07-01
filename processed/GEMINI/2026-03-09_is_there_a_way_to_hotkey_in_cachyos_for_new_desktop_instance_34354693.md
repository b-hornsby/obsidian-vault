---
category: general
date: 2026-03-09
id: 049145
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if there's a way to set up a hotkey in CachyOS to create
  new desktop instances.
tags:
- cachyos
- hotkeys
- desktop-management
- window-management
- productivity
---
# is there a way to hotkey in cachyos for new desktop instances? 

### USER
is there a way to hotkey in cachyos for new desktop instances? 

### GEMINI
Depending on which desktop environment or window manager you chose when you installed CachyOS, the hotkeys for managing virtual desktops (workspaces) vary. Since you've recently migrated to CachyOS, here are the standard hotkeys for the most likely setups: KDE Plasma (Common CachyOS Default) KDE doesn't always have a "create new" hotkey enabled by default, but it has excellent management: Switch Desktops: Ctrl + F1 through F4 (or Meta + Arrow Keys). Show All Desktops (Grid): Meta + G or Ctrl + F8. Move Window to Next Desktop: Meta + Shift + Arrow Keys. To Add a New Desktop: You can create a custom shortcut in System Settings > Shortcuts > KWin for "Create New Desktop." Hyprland (Tiling WM Option) Hyprland uses "dynamic" workspaces—they exist as soon as you move a window to them or focus them: Switch Workspaces: Super + 1-9. Move Window to Workspace: Super + Shift + 1-9. Next/Previous Workspace: Super + Left/Right Arrow. Customization: Edit your config at ~/.config/hypr/hyprland.conf to add specific "new desktop" logic. GNOME Switch Workspaces: Super + Page Up/Down or Ctrl + Alt + Up/Down. Move Window: Super + Shift + Page Up/Down. Activities Overview: Super (Windows key) allows you to drag windows into the "+" area at the top to create a new one. Pro-Tip for CachyOS If you are using a tiling manager like i3 or Hyprland, the concept of "creating" a instance is usually replaced by simply navigating to a number that isn't currently in use. The system generates it on the fly. If the default keys aren't working, check your specific config files: KDE: System Settings UI. Hyprland: ~/.config/hypr/hyprland.conf i3: ~/.config/i3/config Would you like me to help you write a custom script or bind a specific key combo to automate creating and switching to a new desktop instance?
