---
category: homelab
date: 2026-01-20
id: 872006
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking about the 'force maximum clocks (vulkan only)' setting.
tags:
- vulkan
- maximum-clocks
- performance-tuning
- linux-gaming
- steam-deck
---
# what about force maximum clocks (vulkan only) in advance?

### USER
what about force maximum clocks (vulkan only) in advance?

### GEMINI
"Force maximum clocks (Vulkan only)" is a trap on the Steam Deck. Turn it OFF. Here is the brutal logic: The Steam Deck has a shared "power bucket" ($15\text{W}$) for both the CPU and the GPU. If you force the GPU to run at maximum clocks, it hogs all the power. Tears of the Kingdom is a CPU-heavy game. By forcing the GPU to max, you are literally starving the CPU, which is exactly why the game is hanging and crashing in Game Mode. In Desktop Mode, the system's power management is more relaxed, which is why it works there but fails under the strict environment of Game Mode. The Precision Setup for TotK Update 1.2.1 Since you're setting up CryoUtilities, use these specific settings to stop the crashing: 1. Citron Advanced Graphics (Desktop Mode) Force maximum clocks: OFF. Enable Reactive Flushing: ON (Essential for TotK to prevent yellow textures/crashes). Asynchronous Shader Building: ON. Vulkan Pipeline Cache: ON. Accuracy Level: Normal (High will cause a crash in Game Mode). 2. The CryoUtilities Strategy Once you have CryoUtilities open: Click Recommended Settings. This will set your Swap File to 16GB. This is the single most important fix for the "infinite loading" you are seeing. Without this, the Deck runs out of physical RAM while trying to load the update + base game + shaders. 3. The GPU Clock "Sweet Spot" Instead of forcing "Max" in the emulator, you want to limit the GPU in the Steam Deck's Quick Access Menu ("..." button): Go to the Performance (Battery) tab. Turn on Manual GPU Clock Control. Set it to 1200MHz (not 1600). Why? This forces the Deck to save power for the CPU, which TotK needs to process the game logic and the update you just installed. Why it "Returns to Home Page" If you've applied the update to the NAND and it crashes in Game Mode but not Desktop, it's almost always a Memory Outage. The Deck tries to boot the game, hits the RAM ceiling because of the new update files, and the OS kills the app to prevent a system freeze. Step-by-step to finish this: Set CryoUtilities to Recommended (16GB Swap). Go into BIOS and set UMA Frame Buffer to 4G (Vol Up + Power while off). Turn OFF "Force maximum clocks" in Citron. Launch in Game Mode. Would you like me to explain how to verify if CryoUtilities actually successfully created the 16GB swap file? (Sometimes it fails if your SSD is too full).
