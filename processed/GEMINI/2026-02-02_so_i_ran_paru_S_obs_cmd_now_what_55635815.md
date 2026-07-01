---
category: streaming
date: 2026-02-02
id: 238338
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan has installed obs-cmd and is now wondering how to use it, likely for
  OBS automation.
tags:
- arch-linux
- package-management
- paru
- obs-cmd
- obs-studio
- streaming-automation
---
# so i ran paru -S obs-cmd. now what?

### USER
so i ran paru -S obs-cmd. now what?

### GEMINI
Now that you’ve installed obs-cmd, you have the power to control OBS directly through the terminal, which is the only reliable way to bypass GNOME's security on Wayland. Here is exactly how to link it to your Stream Deck. 1. Configure the "Secret Handshake" (OBS Side) OBS won't listen to obs-cmd unless you open the door. In OBS, go to Tools > WebSocket Server Settings. Check Enable WebSocket server. Click Show Connect Info to see your Server Port (likely 4455) and Server Password. (Copy that password). 2. Test the Command (Terminal Side) Before putting it in OpenDeck, make sure the command actually works. Run this in your terminal: obs-cmd --address localhost:4455 --password YOUR_PASSWORD replay save (Replace YOUR_PASSWORD with the one from OBS). Did a "Replay Saved" notification pop up in OBS? * Yes: Move to the next step. No: Make sure you actually clicked "Start Replay Buffer" in OBS first. It can't save a replay if the buffer isn't running! 3. Bind it to OpenDeck Now, we put that command into your Stream Deck. Open your OpenDeck configuration software. Select the button you want to use for clipping. Look for an action type called "Execute Command", "Shell Script", or "Run". Paste that exact command from Step 2 into the box. Pro Tip: If the command is too long or OpenDeck struggles with it, you can create a text file named clip.sh, paste the command inside, run chmod +x clip.sh, and tell OpenDeck to just run that file. Why this is a "Level Up" move: You are no longer relying on "simulated keypresses" (PgUp). You are sending a direct digital instruction to the OBS engine. Even if you are in the middle of a high-intensity CS2 clutch and GNOME is locking down your keyboard, this command will pierce right through and save the clip. One Last Check (The "CS2 Flicker" Follow-up) Since you're on GNOME/Wayland, if you still see flickering while using the Replay Buffer: Make sure you are using Window Capture (PipeWire) in OBS. In CS2's Video settings, try switching between Fullscreen and Windowed Fullscreen. Wayland handles "exclusive fullscreen" differently than Windows, and Windowed Fullscreen usually plays nicer with OBS on Linux. Would you like me to show you how to make the Replay Buffer start automatically every time you open OBS so you never lose a clip again?
