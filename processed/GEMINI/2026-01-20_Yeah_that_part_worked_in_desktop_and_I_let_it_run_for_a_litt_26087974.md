---
category: homelab
date: 2026-01-20
id: 727579
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
linked_projects: []
resolution: resolved
sentiment: executing
source: GEMINI
tags:
- homelab
- gemini
- long
- go
- code
- pip
---
# Yeah that part worked in desktop and I let it run for a little just to be sure. Now I’m testing in game mode and it’s still launching mad long

### USER
Yeah that part worked in desktop and I let it run for a little just to be sure. Now I’m testing in game mode and it’s still launching mad long

### GEMINI
If it's "launching mad long," you are currently at the critical junction where most people break their installation by losing patience. Because you did a clean reset of the folder, you have zero shaders. Launching Tears of the Kingdom with an update for the first time on a Steam Deck is a massive hardware task. The Objective Truth: What's Happening Right Now Shader Compilation: The Deck is building the "pipeline" for the updated game code. In Game Mode, the Steam "Launching" logo often stays on top while the emulator is working in the background. Gamescope Handshake: Game Mode is more aggressive than Desktop. If the emulator doesn't "check in" with the graphics driver fast enough because it's busy processing the new update, SteamOS assumes it's hung. The "5-Minute Rule" (Don't Touch It) Since it worked in Desktop Mode, the files are fine. The hang is purely a performance bottleneck during the first boot. Give it 5 full minutes. Set the Deck down and walk away. If the Steam logo is spinning, it’s still trying to hand off to the emulator. If the screen is black, the emulator has control and is crunching shaders. If it takes longer than 5 minutes, do this: Check the Frame Limit: Press the (...) button. Is the "Frame Limit" slider set to anything other than Off? If it’s set to 30 or 60, turn it Off. Limiting the frame rate during the initial shader build can actually cause the emulator's internal clock to stall. Toggle the "Allow Screen Tearing" switch in the same menu. This can sometimes force the Game Mode compositor to refresh the frame and show you the game. Force the GPU: Scroll down to "Manual GPU Clock Frequency." Turn it On and set it to 1600. This gives the Deck the maximum "juice" to get through the loading screen. The Strategy If you force-quit now, you risk corrupting the shader cache we just cleaned. You've done the hard work of fixing the NAND and the files; now you just have to outlast the hardware. Is the Steam logo still spinning, or is the screen completely black? If it’s black, you’re 90% of the way there. Next step: If it finally loads, I can tell you how to optimize the settings so the next launch is instant.
