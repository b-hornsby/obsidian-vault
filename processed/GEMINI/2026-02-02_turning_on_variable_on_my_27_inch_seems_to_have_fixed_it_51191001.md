---
id: 998841
source: GEMINI
date: 2026-02-02
tags: ['monitor-settings', 'variable-refresh-rate', 'display-fix']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan reported that enabling a variable setting on his 27-inch monitor seemed to fix an unspecified display issue.
---
# turning on variable on my 27 inch seems to have fixed it?

### USER
turning on variable on my 27 inch seems to have fixed it?

### GEMINI
It worked because you inadvertently synced the Wayland compositor’s clock with your monitor’s hardware clock. When VRR (Variable Refresh Rate) is off, Gnome’s compositor (Mutter) and Pipewire are fighting to decide which "frame" to send to OBS. If the game is pushing 144 FPS but the compositor is fixed at 60Hz (or vice versa), you get "buffer desync," which manifests as that annoying flickering or strobe effect. By enabling VRR, you forced the entire pipeline to follow the game's heartbeat. The Advisor’s Mirror You got lucky. You "fixed" it by flipping a switch without knowing why, which is a dangerous way to manage a Linux system. If your FPS drops below your monitor's VRR range in a heavy area, the flickering will return. To make this setup "bulletproof" and reach that next level of reliability, you need to finish the job: Set a Frame Cap: In your game settings, cap your FPS to 3 frames below your monitor's max refresh rate (e.g., 141 FPS for a 144Hz screen). This keeps VRR active 100% of the time and prevents OBS from choking on "overfill" frames. Verify the Hotkey: Now that the video is clean, does the obs-cmd replay save command we set up actually work when you hit PgUp? Check for "Direct Scanout" Flips: If you see the screen blink once when tabbing into a game, that’s Gnome handing control to the GPU. If OBS goes black then, you’ll need to switch the game to "Borderless Window" to keep the capture stream alive. Your High-Level Status Video: Fixed (for now). Input/Hotkey: Pending (needs obs-cmd verification). Optimization: Missing (need FPS caps to prevent future flicker). Does hitting PgUp now save the clip without you having to alt-tab out of the game?
