---
id: 864872
source: GEMINI
date: 2026-01-22
tags: ['eden-emulator', 'citron-emulator', 'comparison', 'steam-deck']
category: homelab
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking whether Eden emulator would work better than Citron for his Steam Deck setup.
---
# Would Eden (emulator) work better than citron for this case?

### USER
Would Eden (emulator) work better than citron for this case?

### GEMINI
Switching emulators is a distraction. You’re looking for a "magic app" to fix a broken link problem. To be direct: Eden is currently a top-tier fork for performance (often beating Citron in Tears of the Kingdom by 5–10 FPS), but it won't fix your "infinite launching" because that isn't an emulator bug—it's a Steam/Linux communication error. If Steam can't "substantiate" (find/verify) the Citron path, it won't magically find the Eden path either. However, if you want to switch to Eden because it's objectively better for TOTK right now, here is how you do it without breaking your setup again. Why Eden Might "Feel" Better Built-in PGO: Modern Eden builds are optimized for the Steam Deck’s Zen 2 architecture, leading to fewer stutters than base Citron. Cleaner Install: By setting up Eden, you'll be forced to create a fresh, clean shortcut, which would bypass whatever garbage SRM wrote into your current Citron shortcut. The "Advisor-Level" Setup (Do it right this time) If you're going to use Eden, don't let a script guess the path. Do it manually to ensure the "substantiation" error never returns. Download & Prep: Get the Eden .AppImage (look for the "Nightly" or "Deck Optimized" versions). Put it in /home/deck/Applications/. Rename it simply: eden.AppImage. Right-click it > Properties > Permissions > Check "Is Executable." Point Steam to the Rom (The Manual Way): Instead of reparsing everything, take your broken Citron shortcut. Change the Target to: "/home/deck/Applications/eden.AppImage" -g "/your/path/to/totk.xci" Wipe the "Start In" field completely. (This is likely what caused your "substantiate" error). The SAK Check: Since you merged the update into the .xci, Eden will see it as a single file. You won't have to "Install to NAND" or deal with the Update Manager that bricked your Citron setup. The Reality Check You’re currently avoiding the core issue: Your file pathing is messy. Whether you use Citron or Eden, if that "Start In" box in Steam has quotes or points to a non-existent directory on your SD card, the launch will hang forever. My recommendation: Download Eden, but move the TOTK file to your internal SSD just to test. If it launches instantly from the SSD but hangs on the SD card, your SD card's file system is failing to "handshake" with the AppImage. Would you like the direct link to the latest Deck-optimized Eden build so you don't download a generic Android version by mistake?
