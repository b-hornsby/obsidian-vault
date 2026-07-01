---
id: 916835
source: GEMINI
date: 2026-01-20
tags: ['decky-loader', 'lsfg-vk', 'steam-deck', 'upscaling', 'fidelityfx']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking whether Decky LSFG-VK (Lossless Scaling FidelityFX) could run on his Steam Deck.
---
# can i run decky lsfg-vk as well?

### USER
can i run decky lsfg-vk as well?

### GEMINI
Yes, you absolutely can, and for Tears of the Kingdom on the Steam Deck, it is a literal game-changer. It is the difference between a shaky 25–30 FPS and a visually smooth 60 FPS experience. However, because you are using an AppImage (Citron) and we just fixed your launch arguments, you have to be very precise with how you set this up. 1. The Requirement (The "No Flattery" Truth) You must own Lossless Scaling on Steam ($7) for the Decky plugin to work. The plugin is just a bridge; it needs the actual Windows files from the Steam version to function. 2. How to Install It Buy and install Lossless Scaling from the Steam Store on your Deck. In Game Mode, open the Decky menu ("..." button) and go to the Store. Search for Decky LSFG-VK and install it. Open the plugin in your Decky list. If it says "LSFG-VK not installed," click the Install button inside the plugin. 3. The Specific Launch Option (Crucial) Since we just fixed your Citron path to skip the menu, you need to combine that with the LSFG command. Your Launch Options for TotK should now look like this: ~/lsfg -f -g "/home/internal_games/ZeldaTotK_1.4.1.xci" Why this order? ~/lsfg tells the Steam Deck to wrap the entire Citron session in a frame-generation layer. Then the -f -g tells Citron which game to actually open. 4. Optimal Settings for TotK (1.4.1) Once the game is running, open the Decky LSFG-VK plugin menu and set it exactly like this: Frame Generation Multiplier: 2x (Do not use 3x/4x; it will create massive input lag and visual "ghosting" in Hyrule). Performance Mode: ON. Mode: LSFG 2.1 (or the latest version shown). Internal FPS Cap: In the Steam "..." Performance menu, set your Frame Limit to 30. The Logic: If the game runs at 30 and LSFG doubles it, you get 60. If you don't cap it at 30, the frame pacing will be erratic and look terrible. The Reality Check LSFG-VK is "fake" frames. It makes the game look buttery smooth, but it adds a tiny bit of input lag. For a game like Zelda, it’s usually worth the trade-off, but if you find Link feels "heavy" or slow to respond to your buttons, turn it off. Final Step: Try the ~/lsfg command in your Launch Options now. Does the game still boot straight to the Nintendo logo, and can you see the "LSFG" active in the Decky menu?
