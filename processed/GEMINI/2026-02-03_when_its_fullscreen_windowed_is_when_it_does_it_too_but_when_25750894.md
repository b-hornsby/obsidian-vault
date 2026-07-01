---
category: streaming
date: 2026-02-03
id: 780324
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is troubleshooting a problem that occurs only when his game is in fullscreen
  windowed mode, likely related to streaming or display settings.
tags:
- obs-studio
- game-capture
- streaming-setup
- troubleshooting
- fullscreen-windowed
---
# when its fullscreen windowed is when it does it too but when its windowed it doesnt?

### USER
when its fullscreen windowed is when it does it too but when its windowed it doesnt?

### GEMINI
That distinction is the "smoking gun." When you go Fullscreen Windowed (Borderless), GNOME 49 triggers a feature called "Direct Scanout" (or Fullscreen Unredirect). It essentially tries to bypass the compositor to give you better latency. On NVIDIA 30-series cards, this hand-off between the compositor and the GPU is currently broken in Wayland, causing that strobe-light flicker. When you are in a normal Window, the compositor (Mutter) stays in control of the frame timing, which is why it stays stable. The "Advisor" Plan: Stop the Borderless Flicker 1. The "Window Capture" Absolute Rule Since "Windowed" mode works and "Fullscreen Windowed" doesn't, you need to change how OBS "sees" the game. Do not use "Screen Capture" (the whole monitor). Use "Window Capture (PipeWire)" specifically for the game window. Even if the game is in Fullscreen Windowed, PipeWire can often "grab" the stable window buffer before the compositor tries to "unredirect" it and cause the flicker. 2. Disable "Direct Scanout" (The Nuclear Fix) If you want to play in Fullscreen Windowed without the flicker, you have to tell GNOME to stop trying to be "efficient." Open your terminal. Run this command to disable the experimental unredirection (this varies by GNOME version, but is the standard for Cachy/Arch): gsettings set org.gnome.mutter unredirect-vblank-windows false Why: This forces GNOME to keep compositing the window even when it's fullscreen, which stops the NVIDIA "sync-miss" flicker. 3. Match the Refresh Rates (Again) If your game is running at 165Hz in Borderless but OBS is trying to render at 60fps, the "Direct Scanout" will flicker every time the two numbers don't divide perfectly. The Fix: Go to OBS Settings -> Video. Set your Integer FPS Value to 165 (to match your monitor) or 82.5. Alternatively, cap your game at 144Hz and match OBS to 60 or 120. Mismatched high refresh rates are the fuel for this fire. The Brutal Truth You are discovering why most pro streamers on Linux eventually switch to KDE Plasma or go back to X11. GNOME's Wayland implementation for NVIDIA is very aggressive with "optimizations" (like Direct Scanout) that NVIDIA's drivers simply aren't ready for yet. Your immediate fix: Run the gsettings command above to disable unredirection. Did that command stop the flickering in Fullscreen Windowed mode? If not, your only choice is to play in standard Windowed mode (and just maximize it manually) until the next GNOME/NVIDIA driver update.
