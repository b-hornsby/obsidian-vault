---
id: 344481
source: GEMINI
date: 2026-01-20
tags: ['steam-deck', 'citron', 'command-line', 'troubleshooting', 'file-system']
category: general
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan ran a command to remove files from a specific directory, but it returned no output, indicating either success or that the directory was already empty.
---
# Ran the rm -rf ~/.local/share/citron/nand/system/Contents/registered/* command it returned nothing

### USER
Ran the rm -rf ~/.local/share/citron/nand/system/Contents/registered/* command it returned nothing

### GEMINI
If the command returned nothing, it means one of two things: either the directory was already empty (unlikely given your issue) or—more likely—the AppImage is storing its data in a different hidden folder than the one we targeted. On Linux, "returning nothing" after a rm command actually means it successfully executed (it's called "silent success"). But if the game behavior hasn't changed, we hit the wrong target. 1. Find where the "Ghost" actually lives Since you are using an AppImage, it might be using the Flatpak-style path or a custom one if you used EmuDeck. Run this command in Konsole to find the real folder: find ~ -name "registered" -type d 2>/dev/null This will list every "registered" folder on your Deck. Look for the one that has citron in the path. Once you see that path, run the rm -rf command on that specific directory. 2. The "Game Mode" Loading Fix The reason it works in Desktop but not Game Mode is a Shader Cache or VRAM collision. In Desktop mode, the Deck has more overhead; in Game Mode, it tries to optimize and chokes on the TotK update's new shader requirements. Do this in Game Mode: Launch the game. When it gets stuck loading, hit the (...) button -> Performance (Battery icon). Turn OFF "Frame Limit" and OFF "Refresh Rate Limit" (set to 60). Scroll down to GPU Clock Frequency. If it's on, turn it off. If it's off, try manually setting it to 1600MHz just to force the hardware to max out for the initial boot. 3. Use the "Right-Click" GUI Shortcut If the terminal is being stubborn, do it manually in the file explorer (Dolphin): Open Dolphin (File Manager). Click the hamburger menu (top right) -> Show Hidden Files. Go to Home -> .var -> app. If you see org.citron_emu.citron, go inside: data -> citron -> nand -> system -> Contents -> registered. Delete everything inside registered. Now go back to citron folder -> shader. Delete everything inside here too. Why it says "No Update Installed" but it's there: The AppImage is likely failing to read the Title Metadata because of a permissions lock. When you "installed" the update, the AppImage created a folder that it now doesn't have "permission" to modify or delete. The Absolute Fix: Rename your citron folder to citron_old. Start the emulator fresh. It will be empty. Re-add your keys and the game. If it works now, the issue was a corrupted configuration file in your old folder. You can then move your saves folder from citron_old to the new citron folder. Did the find command from Step 1 show you a different path than the one we tried earlier?
