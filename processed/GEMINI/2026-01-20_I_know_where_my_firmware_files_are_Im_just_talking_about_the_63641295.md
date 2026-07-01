---
id: 895961
source: GEMINI
date: 2026-01-20
tags: ['steam-deck', 'citron', 'tears-of-the-kingdom', 'game-update', 'firmware', 'clarification']
category: general
sentiment: frustrated
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan clarifies that he's referring to the game update file, not the firmware files.
---
# I know where my firmware files are I’m just talking about the update file for the game itself

### USER
I know where my firmware files are I’m just talking about the update file for the game itself

### GEMINI
I understand. You don't want a lecture on file paths; you want that specific, corrupted update file gone so the game stops hanging in Game Mode. Because the GUI "Delete" button and the standard "nuke" commands failed, it’s because the update is buried in a specific Title ID subfolder that the emulator has locked or hidden. 1. The Direct Manual Delete Instead of using commands, we're going to use the Dolphin File Manager to find the exact "junk" file. Open Dolphin in Desktop Mode. Go to the Hamburger Menu (top right) and check "Show Hidden Files". Navigate to exactly here: /home/deck/.local/share/citron/nand/user/Contents/registered/ (Note: If you don't see this, look in /home/deck/.var/app/org.citron_emu.citron/data/citron/nand/user/Contents/registered/). Inside registered, you will see a bunch of folders with long, random names (like 000000A1...). Change the View to "Details" and sort by "Date Modified." The folder at the very top (the most recent one) is your corrupted TotK update. Delete that folder. 2. The "Update Registry" Kill (Why it still shows in Properties) The emulator keeps a "memory" of the update in a file called records.bin. Even if you delete the file, the GUI will say it's there until you kill the record. In that same citron folder, go to the system folder. Look for a file named records.bin. Delete it. Restart Citron. The "Properties" should now finally show no update. 3. The "Game Mode" Fix (The real reason it hangs) If you delete the update and it still won't load in Game Mode, the problem isn't the update anymore—it's the Shader Cache. A failed update attempt "poisons" the shaders. Open Citron in Desktop Mode. Right-click Tears of the Kingdom -> Remove -> Remove All Pipeline Caches. Now, switch to Game Mode. Wait 3 minutes. The first launch after a cache wipe looks like a hang, but it's just the Steam Deck rebuilding the game's startup engine. The Advisor's Bottom Line You are likely dealing with a Region Mismatch. If your base game is the US version and you tried to install a European update, it creates exactly the "No update installed" error you're seeing while still clogging up your storage. Try deleting that most recent folder in the registered directory now. Does the game finally boot in Game Mode without the update?
