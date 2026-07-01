---
category: streaming
date: 2026-03-09
id: 722847
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble with OBS hotkeys for clipping not working when a
  game is running on his primary monitor and OBS is on the secondary monitor in CachyOS.
tags:
- obs-studio
- hotkeys
- replay-buffer
- cachyos
- game-capture
- streaming-setup
---
# im on cachyos and whenever i press my hotkey for clips via replay buffer in obs it doesnt work because im in another game while obs is running on my secondary monitor. how do i fix this? 

### USER
im on cachyos and whenever i press my hotkey for clips via replay buffer in obs it doesnt work because im in another game while obs is running on my secondary monitor. how do i fix this? 

### GEMINI
The reason your hotkey isn't working is that Wayland, the display protocol used by default in CachyOS, blocks applications from "listening" to your keyboard while they aren't in focus. This is a security feature to prevent keylogging, but it breaks global hotkeys for apps like OBS. Since OBS still hasn't fully implemented the native Wayland "Global Shortcuts Portal," you have three main ways to fix this. Option 1: The "XWayland" Workaround (Easiest) You can force OBS to run as an X11 application. Wayland has a "Legacy X11 Support" mode that allows these older apps to read global hotkeys. Open System Settings → Security & Privacy → Legacy X11 App Support. Set it to "Allow legacy X11 apps to read every key" (or similar, depending on your version of KDE/GNOME). Restart OBS. If it doesn't work, you may need to launch it with an environment variable by running this in your terminal: QT_QPA_PLATFORM=xcb obs Option 2: The WebSocket + System Shortcut Method (Best Performance) This is the most reliable "Linux" way to do it. You tell your Desktop Environment (KDE or GNOME) to listen for the key and send a command directly to OBS via its built-in WebSocket. Enable WebSocket in OBS: Go to Tools → WebSocket Server Settings → Enable WebSocket Server. Take note of the Port (usually 4455) and Password. Install obs-cmd: Open your terminal and run: sudo pacman -S obs-cmd Test the command: Try running this in the terminal while the Replay Buffer is active: obs-cmd replay save (If you set a password, use: obs-cmd --password YOURPASSWORD replay save) Bind it to a Hotkey: Go to System Settings → Shortcuts → Commands (or Custom Shortcuts). Add a new shortcut and paste that obs-cmd command as the action. Assign your favorite keybind. Option 3: The Portal Plugin There is a specific plugin designed to bridge this gap for Wayland users. Install the obs-wayland-hotkeys plugin. On CachyOS/Arch, you can find this in the AUR: yay -S obs-wayland-hotkeys-git Restart OBS. Upon launch, you should see a system pop-up asking to register shortcuts. You will then manage these hotkeys through your System Settings (under the "Shortcuts" or "Global Shortcuts" section) rather than inside the OBS settings menu. Which should you use? If you want it to just work right now without extra software, Option 1 is the way. If you want a setup that won't break when X11 support eventually fades, Option 2 is the professional choice. Would you like me to walk you through the specific syntax for a script to automate starting the Replay Buffer on boot as well?
