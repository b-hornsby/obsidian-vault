---
category: homelab
date: 2026-02-08
id: 698553
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to play Tears of the Kingdom on Steam Deck via the Eden
  emulator but it froze and crashed after the loading screen.
tags:
- tears-of-the-kingdom
- eden-emulator
- steam-deck
- nintendo-switch
- gaming
---
# Trying to play tears of the kingdom on steam deck via Eden and it boots up, shows the loading screen, freezes and then boots out of the game? 

### USER
Trying to play tears of the kingdom on steam deck via Eden and it boots up, shows the loading screen, freezes and then boots out of the game? 

### GEMINI
Look, if your game is crashing at the loading screen, you're usually looking at a configuration conflict or a botched update path. "Eden" is a fork of Yuzu, and it inherits the same quirks—specifically how it handles Shader Caches and Update Files. Here is the objective reality of why your game is booting you out and exactly how to fix it. 1. The "Zelda Update" Loophole The most common cause for a crash-on-load in Tears of the Kingdom is a corrupted or improperly mounted update file (v1.1.0 – v1.2.1). The Fix: Open Eden in Desktop Mode. Right-click Tears of the Kingdom and select Remove -> Remove All Pipeline Caches. Then, right-click it again, go to Properties, and uncheck the Update file. Try booting the base game (v1.0.0). If it works, re-enable the update. If it crashes again, your update file is likely a bad dump. 2. Shader Cache Corruption If the game freezes specifically during the "Building Shaders" phase of the loading screen, your cache is poisoned. The Fix: In Eden, right-click the game -> Open Transferable Pipeline Cache. Delete everything in that folder. The next boot will be slower while it rebuilds, but it should actually finish. 3. VRAM & CryoUtilities Tears of the Kingdom is a memory hog. If your Steam Deck is set to the default 1GB VRAM in the BIOS, it will often crash during the heavy asset load of the opening sequence. The Fix: Shut down your Deck. Hold Volume Up + Power to enter the BIOS. Go to Setup Utility -> Advanced -> UMA Frame Buffer Size and set it to 4G. Priority Action Plan StepActionWhy?1Disable ModsMany "60FPS" or "Dynamic FPS" mods for TOTK are version-specific. If your mod is for v1.1.2 and you're running v1.2.1, it will crash the boot.2Switch to VulkanEnsure your Graphics API is set to Vulkan, not OpenGL. Handheld mode should be On.3Check Keys/FirmwareIf the loading screen shows but the game never actually starts "rendering," your Keys or Firmware (ensure you're on at least 18.0.0+) might be mismatched.4Reset ConfigIf you used EmuDeck to install, open the EmuDeck app -> Manage Emulators -> Eden -> Reset Configuration. This wipes any "bad" settings you might have toggled. Stop playing small with the settings: If you haven't installed CryoUtilities yet, you are wasting the Steam Deck's potential on this specific game. It manages the swap file size which prevents these exact "out of memory" crashes. Would you like me to walk you through how to verify if your Firmware version matches your Game Update version?
