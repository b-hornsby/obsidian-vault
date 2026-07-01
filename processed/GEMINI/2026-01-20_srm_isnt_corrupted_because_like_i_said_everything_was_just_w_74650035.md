---
id: 988317
source: GEMINI
date: 2026-01-20
tags: ['steam-rom-manager', 'cryoutilities', 'steam-deck', 'emulator-setup']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan disputes that SRM is corrupted and asks how to set up CryoUtilities.
---
# srm isn't corrupted because like i said everything was just working literally right before the update and i JUST set srm up. how do i set cryoutilities? 

### USER
srm isn't corrupted because like i said everything was just working literally right before the update and i JUST set srm up. how do i set cryoutilities? 

### GEMINI
If SRM was working a second ago and now it’s not, it's not "corrupted," but it is conflicted. Tears of the Kingdom on Version 1.0.0 vs. Version 1.2.1 is a different beast for the Steam Deck’s RAM. In Game Mode, the Deck is more aggressive about memory management. If the game spikes during the "update check" launch, SteamOS kills it. CryoUtilities is the standard fix for this because it expands your "Swap File" (emergency RAM), which TotK desperately needs to stop those Game Mode crashes. Phase 1: Install CryoUtilities Switch to Desktop Mode. Open Konsole (the terminal). Set a password if you haven't (type passwd, enter it, then confirm it). Copy and paste this exact command to download and run the installer: curl -L https://raw.githubusercontent.com/CryoByte33/steam-deck-utilities/main/install.sh | bash -s -- Once finished, you'll have an icon on your desktop called CryoUtilities. Phase 2: Apply the "Safe" Boost Open CryoUtilities and enter your password. Click the Recommended button. This will set your Swap File to 16GB. It may take a few minutes as it has to "carve" that space out of your SSD. Don't touch it while it works. The VRAM Tweak (Do not skip this): Shut down your Deck. Hold Volume Up and press Power. Select Setup Utility (bottom right) > Advanced. Find UMA Frame Buffer Size and change it from 1G to 4G. Save and Exit (Select button). Phase 3: The "Tears of the Kingdom" Specific Check Since it works in Desktop but not Game Mode, and you've already done the NAND update and cleared shaders, check this one last thing in Citron before going back to Game Mode: Properties > System: Ensure "Limit Speed Percent" is at 100%. Properties > Graphics > Advanced: Vulkan Pipeline Cache: ON. Enable Reactive Flushing: ON. Use Asynchronous Shader Building: ON. Launch it once in Desktop Mode until you are standing in the game world. Close it. Why this fixes it In Desktop Mode, the Deck allows the emulator to "hang" for a few seconds while it figures out the memory address changes from the update. In Game Mode, if the app hangs for more than a second during that "Launch" screen, SteamOS assumes it's crashed and force-closes it. Increasing your Swap to 16GB and VRAM to 4G gives the Deck enough "breathing room" to pass that check. One final reality check: Is your internal SSD almost full? If you have less than 10GB free, CryoUtilities will fail to create the 16GB swap file, and you'll be right back where you started. Try launching it in Game Mode after the CryoUtilities "Recommended" settings are applied. Does it still kick you back to the home screen instantly, or does it hang on a black screen first?
