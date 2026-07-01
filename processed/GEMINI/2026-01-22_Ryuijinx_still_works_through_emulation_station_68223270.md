---
id: 392580
source: GEMINI
date: 2026-01-22
tags: ['ryujinx', 'emulationstation', 'steam-deck']
category: homelab
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking whether Ryujinx still works through EmulationStation on his Steam Deck.
---
# Ryuijinx still works through emulation station?

### USER
Ryuijinx still works through emulation station?

### GEMINI
Yes, Ryujinx still works and is fully supported by EmulationStation (ES-DE). However, since the original Ryujinx project was shut down in late 2024, the community has migrated to forks like Ryubing. If you choose to use a Ryujinx-based emulator instead of a Yuzu fork (like Eden or Citron), you just need to tell EmulationStation which "Alternative Emulator" to use. Since you want a clean start on your internal SSD, here is the exact path to set up your "All-in-One" system today. 1. Clear the Old Mess Delete the broken shortcuts: In Steam, remove your old "Tears of the Kingdom" and "Citron" entries. Wipe the "NAND" bloat: Since your original issue was the "Update Manager" bricking things, you must clear the emulator's internal update folder so it doesn't conflict with your SAK-merged files. Path: /home/deck/.var/app/org.ryujinx.Ryujinx/config/Ryujinx/sdcard/ (or similar for Citron). Just delete the contents of the registered folder inside the system directory. 2. Move ROMs to the SSD Open Dolphin (File Manager). Navigate to your Internal SSD: /home/deck/Emulation/roms/nswitch/. Move your SAK-merged games here. 3. The "Ghost Link" for EmulationStation You mentioned you need to link the SSD folder to the SD card path so ES-DE picks it up. Do this exactly: Go to your SD card roms folder (/run/media/mmcblk0p1/Emulation/roms/). Delete the empty nswitch folder on the SD card. Right-click and drag the nswitch folder from your Internal SSD into that empty spot on the SD card. Select "Link Here". Now, when ES-DE looks at the SD card, it is instantly redirected to your high-speed SSD. 4. Setting Ryujinx as the Default in ES-DE If you prefer Ryujinx's accuracy over Eden's speed: Open EmulationStation. Press Start > Other Settings > Alternative Emulators. Find Nintendo Switch and change it to RYUJINX (Standalone). Why this will actually work this time: No "Update Manager" bricks: By using SAK-merged files on the SSD, the emulator sees the game and update as one single entity. No more installing to NAND. No more "Substantiate" errors: By moving to the SSD and manually setting the "Start In" field to blank in Steam ROM Manager, you remove the permission hurdles that the SD card was causing. Internal Speed: Tears of the Kingdom shader compilation is significantly faster on the internal SSD than on an SD card. The Advisor's Next Step If you want to move forward with Eden instead (because it generally runs TOTK with better frame pacing on the Deck), you need the Eden AppImage. Would you like me to provide the configuration settings to ensure your SAK-merged files show up with the correct icons in Steam after you move them to the SSD?
