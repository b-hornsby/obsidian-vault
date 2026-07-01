---
id: 715777
source: GEMINI
date: 2026-03-07
tags: ['windows-10', 'operating-system', 'pc-build', 'dual-boot']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was mentioning his plan to use Windows 10 as part of his PC setup, likely for gaming or dual-boot purposes.
---
# I planned on using windows 10 as well if that helps

### USER
I planned on using windows 10 as well if that helps

### GEMINI
Using Windows 10 instead of Windows 11 changes the security and support landscape, but it actually makes the hard drive situation worse, not better. Here is the strategic breakdown of why "using what you have" with Windows 10 on an HDD in 2026 is a high-risk move for your specific setup. 1. The Support "Cliff" Windows 10 officially reached its End of Support on October 14, 2025. Security Risk: Since we are now in 2026, your Windows 10 install is no longer receiving free security patches. For a machine that you’ll be using for online multiplayer games like COD and Fortnite, this is a major vulnerability. The Paid Fix: Microsoft now charges roughly $30–$61 per year for "Extended Security Updates" (ESU) for home users. If you have to pay for updates just to keep an old OS safe, that money is better spent on a cheap SSD. 2. Windows 10 + HDD = "The 100% Bug" Windows 10 is notorious for a "100% Disk Usage" bug when paired with mechanical HDDs. Because Windows 10 (and 11) assumes you have an SSD, it runs aggressive background processes like SysMain (Superfetch), Windows Search indexing, and Antimalware Service Executable. On an HDD, these tasks will often peg your drive at 100% capacity for 10–20 minutes every time you boot up. This means even before you launch Fortnite, your PC will be sluggish and unresponsive. 3. Game-Specific Failures (2026 Edition) You mentioned Fortnite and COD. By 2026, these games have evolved significantly: Fortnite (UE5): Fortnite now uses Nanite and Lumen (high-end lighting and geometry). These technologies require assets to be pulled from storage almost instantly. On a SATA HDD, you will likely see "LOD bugs" where buildings look like melted marshmallows for the first 30 seconds of a landing. Call of Duty: Modern COD files are massive and highly compressed. The "de-shuffling" process of reading those files from a spinning platter during a match load will frequently result in you being kicked for "Server Timed Out" or "Timed Out Waiting for Achievements." 4. The Opportunity Cost You have an RTX 3070 and an i7-12700K. The Loss: By using an HDD, you are essentially "underclocking" your entire experience. You'll spend roughly 15–20% of your total gaming time just sitting at loading screens or waiting for the OS to stop lagging. The Math: If you play 5 hours a week, you're losing about an hour a week to the hard drive. Over a year, that's 50 hours of your life spent looking at a loading bar. My Brutal Recommendation Since you already have a 2TB Linux Drive, don't spend a dime on new hardware if you're tight on cash. Instead: Shrink your Linux partition by 200GB–300GB. Install Windows 11 (it’s free to use unactivated, and it’s actually supported) on that newly created space. Use the 1TB HDD as a "Game Library" drive for your Linux side or for older, lighter games that don't stream assets (like Valheim, Minecraft, or older Indies). Stop trying to revive 2014-era storage for 2026-era competitive gaming. It’s like buying a 4K monitor and only watching 480p videos. Would you like me to find a guide on how to safely resize your Linux partition to make room for Windows on your SSD?
