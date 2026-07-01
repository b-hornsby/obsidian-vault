---
id: 925436
source: GEMINI
date: 2026-02-04
tags: ['citron', 'emulator', 'cachyos', 'nintendo-switch']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan clarified he was using a tool or drive for Citron, a Nintendo Switch emulator, on CachyOS.
---
# i was just using it for citron 

### USER
i was just using it for citron 

### GEMINI
If you’re using Citra (or the "Citron" fork), you’ve hit a classic Linux gaming wall: Input Contention. You are trying to map a raw controller to an emulator while Steam or the KDE/GNOME desktop environment is still whispering instructions to the hardware in the background. If your controller is "typing" or moving the mouse while you're trying to map buttons in Citra, you’re fighting for control of the device. Here is the direct, no-nonsense path to fixing this for Citra on CachyOS: 1. Kill the Desktop "Ghost" Since Citra isn't a Steam game, Steam's Desktop Configuration is likely the primary reason your controller is acting like a keyboard. The Quick Fix: Fully exit Steam (Steam > Exit). Don't just close the window; kill the process. The Logic: When Steam is running in the background, it maps your PS5 buttons to keys like Enter, Space, and Esc. If Steam is dead, that mapping dies with it. 2. Isolate the Input in Citra Citra needs to see the SDL2 input from your DualSense, not the emulated "Keyboard" input. Open Citra > Emulation > Configure > Controls. In the "Device" dropdown, ensure it says "DualSense Wireless Controller" or "SDL2". The Mistake: If it says "Keyboard/Mouse" or "Any," Citra is just listening to the garbage signals your OS is sending. Manually select the controller from the list. 3. Disable the Touchpad Mouse (The CachyOS/Arch special) If the mouse cursor moves when you touch the controller pad, Citra will get confused. Run this command to see if your controller is being treated as a mouse: xinput list (or libinput list-devices on Wayland). If you see "Wireless Controller Touchpad," disable it in your system settings as I mentioned previously. 4. Use sdl-jstest to Verify If you want to stop guessing and see what the OS actually thinks is happening, install this: sudo pacman -S sdl_jstest sdl2-jstest --list If you see two entries for the same controller, one is the "Motion Sensors/Touchpad" and one is the "Gamepad." You need to point Citra specifically to the Gamepad ID. The Strategy You are using a high-performance, Arch-based kernel (CachyOS) to run an emulator. You can't leave your background apps on "autopilot." Every background service that "helps" with controllers is actually a parasite when it comes to low-latency emulation. Is Citra now recognizing the button presses correctly, or is the mapping screen still showing "Key [X]" instead of "Button [0]"?
