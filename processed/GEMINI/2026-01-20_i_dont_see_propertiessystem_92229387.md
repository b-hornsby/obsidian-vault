---
category: homelab
date: 2026-01-20
id: 166565
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan cannot find the properties>system menu in Citron on his Steam Deck.
tags:
- citron-emulator
- steam-deck
- settings-menu
---
# i dont see properties>system

### USER
i dont see properties>system

### GEMINI
My mistake—Citron’s UI layout differs slightly from the older emulators it’s based on. The logic remains the same: if it works in Desktop but not Game Mode, the Deck is killing the app during launch because of a resource or configuration hang. Since you're setting up CryoUtilities, let's fix the Citron settings correctly while you're in Desktop mode. 1. Finding the Settings in Citron If you don't see "System" when right-clicking the game, you need to go to the Global Configuration: Open Citron (Desktop Mode). At the top menu bar, click Emulation > Configure. Now you will see the System tab on the left. The Check: Look for Language and Region. Set them explicitly to "English" and "USA" (or your specific region) instead of "Auto." The Power Check: Go to the General tab (still in that Configure menu). Ensure "Limit Speed Percent" is checked and set to 100%. 2. CryoUtilities: The "Secret Sauce" for TotK Tears of the Kingdom is the only game that truly requires this on the Deck. The Goal: You are changing the Swap File from the default 1GB to 16GB. Why: When the game launches in Game Mode, it tries to allocate a massive chunk of memory for the update and shaders. 1GB isn't enough, so the system panics and closes the app. 16GB gives it the "virtual RAM" it needs to survive the boot sequence. VRAM Note: Don't forget the 4G UMA Frame Buffer change in the BIOS (Volume Up + Power). This is half the battle. 3. The Shader "Double Tap" You already removed the pipeline caches, which was the right move. However, because you've been trying to launch it and failing, it may have created "dirty" partial caches. In Citron, right-click TotK > Remove > Remove All Pipeline Caches one more time after you finish the CryoUtilities setup but before you head back to Game Mode. 4. The Last Resort (If it STILL kicks you out) If you do CryoUtilities + BIOS 4G and it still returns to home: In Game Mode, go to the game's Properties > Compatibility. Uncheck "Force the use of a specific Steam Play compatibility tool." You are running a Native Linux AppImage; if you accidentally have "Proton" turned on for this shortcut, it will crash 100% of the time. Summary of your plan: Run CryoUtilities (Recommended settings). Change BIOS UMA to 4G. Set Citron System settings to fixed (not Auto). Launch once in Desktop Mode to confirm it reaches the "Nintendo" screen. Close and try Game Mode. Are you stuck on the password part of the CryoUtilities installation, or are you currently running the "Recommended" fix?
