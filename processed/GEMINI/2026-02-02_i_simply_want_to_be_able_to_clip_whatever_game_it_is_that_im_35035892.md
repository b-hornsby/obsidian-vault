---
category: streaming
date: 2026-02-02
id: 976908
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated with his inability to clip gameplay using OBS Studio
  on Linux and is seeking a solution to make it work.
tags:
- game-clipping
- obs-studio
- linux
- troubleshooting
---
# i simply want to be able to clip whatever game it is that i'm playing. tell me what to delete and what i need to do to achieve this 

### USER
i simply want to be able to clip whatever game it is that i'm playing. tell me what to delete and what i need to do to achieve this 

### GEMINI
To achieve a seamless clipping experience on CachyOS (GNOME/Wayland), you need to strip away the "over-engineering" that’s causing lag and use a tool built for high-performance recording. Here is exactly what to delete and exactly what to do. 1. The Clean Slate (Delete the Junk) Gamescope is great for the Steam Deck, but on a powerful desktop running GNOME, it’s adding unnecessary latency and breaking your cursor. Remove Launch Options: 1. Open Steam > Right-click Halo MCC > Properties. 2. Delete everything in the "Launch Options" box. Uninstall Gamescope (Optional but recommended): Open your terminal and run: sudo pacman -Rns gamescope Reset In-Game Settings: * Launch the game and set it to Exclusive Fullscreen or Borderless Windowed. Turn Vsync OFF (we will handle syncing elsewhere). 2. The Solution: GPU Screen Recorder This is the "ShadowPlay" of Linux. It is significantly faster than OBS because it does 99% of the work directly on your GPU. It supports "Instant Replay" (clipping the last X minutes). Step A: Install it CachyOS has this in its main repository. Open your terminal and run: sudo pacman -S gpu-screen-recorder-gtk Step B: Configure for Clipping Open GPU Screen Recorder from your app drawer. Record Mode: Set to "Screen" or "Follow Focused Window." Video Quality: Set to "Very High." Audio: Select your Desktop Audio (and Mic if you want your voice). Replay Settings: * Turn on Replay. Set the time (e.g., 60 seconds). Folder: Choose where you want the clips to go. Hotkeys: Set a hotkey for "Save Replay" (e.g., Alt + F10). Step C: Enable "Direct Capture" To prevent the lag you were feeling with Gamescope: In GPU Screen Recorder settings, ensure "Advanced" is checked. Make sure "Force Nvenc/VAAPI" is active so it uses your hardware encoder. 3. Fixing the Mouse (The GNOME Way) Since you are no longer using Gamescope to "trap" the mouse, use the native GNOME solution so it doesn't leak to your other monitors: Search for "Extensions" in your app drawer. Install the Mousetrap or Lock Cursor extension. Toggle it on when you play Halo. This locks the cursor to the screen without the overhead of a second compositor. Why this is better No Lag: GPU Screen Recorder has near-zero impact on FPS (unlike OBS or Gamescope). Native Performance: Halo runs directly on your GPU/Wayland without being "wrapped" in a Gamescope window. Reliability: You’ll get a consistent cursor and a high-quality video file every time you hit that hotkey. Would you like me to walk you through setting up a script that automatically starts the clipping service every time you boot your PC?
