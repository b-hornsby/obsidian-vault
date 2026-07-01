---
id: 110671
source: GEMINI
date: 2026-03-07
tags: ['120gb-ssd', 'limited-storage', 'dual-boot', 'windows-install']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan noted he only has a 120GB SSD available for a Windows dual-boot setup.
---
# This is the ssd that I have to work with. Only 120gb tho

### USER
This is the ssd that I have to work with. Only 120gb tho

### GEMINI
You have the right parts; you just need to arrange them correctly. Your 120GB SanDisk SSD PLUS is the missing link that makes this build viable. By 2026 standards, 120GB is considered "marginal" for a modern OS, but it is infinitely better than a mechanical HDD. Using it as your boot drive will prevent the 100% disk usage bugs common in Windows 10/11 on HDDs. The 2026 "Dual-Drive" Strategy DriveRoleContents120GB SanDisk SSDBoot DriveWindows 10/11 OS, Drivers, Browser.1TB Seagate HDDGame LibraryCOD, Fortnite, and bulk storage. Step 1: The SSD Space Optimization Since you have 32GB of RAM, Windows will automatically create a "Hibernation" file of roughly that same size on your 120GB SSD. This will eat 25% of your drive immediately. Action: Once Windows is installed, open Command Prompt (Admin) and type: powercfg /hibernate off Result: This instantly deletes the hiberfil.sys file, reclaiming ~25GB to 32GB of space. Step 2: Offloading Games to the HDD Windows and its updates will take about 30–40GB. With hibernation disabled, you'll have about 70GB free on the SSD. Fortnite: At ~30–50GB, this could fit on the SSD for better performance. Call of Duty: Because COD can exceed 150GB, you must install it on the 1TB HDD. How to do it: In the Battle.net or Steam settings, create a new "Library Folder" on the D: Drive (your HDD). Step 3: The Reality Check Even with this setup, your RTX 3070 and i7-12700K are still being held back by the HDD's seek times. The Compromise: You will still see "LOD issues" (blurry textures/marshmallow buildings) in Fortnite and COD because a 7200RPM drive cannot feed assets to your high-end GPU fast enough in 2026. The OS Benefit: Because the OS is on the SanDisk SSD, the rest of your computer won't freeze up or lag while the game is loading. Summary of the Plan Wipe the 120GB SSD and install Windows. Disable Hibernation immediately to save 30GB. Point your game launchers to the 1TB HDD for the heavy lifting. Would you like me to walk you through how to set up a secondary Steam or Battle.net library on that HDD once your Windows install is finished?
