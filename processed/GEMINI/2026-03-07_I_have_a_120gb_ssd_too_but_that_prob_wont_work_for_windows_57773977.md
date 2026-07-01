---
id: 643569
source: GEMINI
date: 2026-03-07
tags: ['windows-10', 'ssd', 'storage', 'pc-build']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was considering whether his 120GB SSD could work for a Windows 10 installation.
---
# I have a 120gb ssd too but that prob won’t work for windows

### USER
I have a 120gb ssd too but that prob won’t work for windows

### GEMINI
Actually, that 120GB SSD is your secret weapon. Using it for your Windows dual-boot is a significantly smarter move than using the HDD, provided you understand the storage math for 2026. Here is the objective reality of why the 120GB SSD is better than the 1TB HDD, and how to make it work. 1. The "Performance vs. Capacity" Trade-off Windows 10/11 requires about 30–40GB for a clean installation with drivers and basic updates. The SSD (120GB): You’ll have roughly 70–80GB of usable free space. The HDD (1TB): You’ll have 1,000GB, but the OS will be perpetually sluggish. 2. The "Hybrid" Strategy (Best of both worlds) You don't have to choose one or the other. You can use both to solve your problem: Install Windows on the 120GB SSD: This ensures your PC boots in 10 seconds, the Start menu is instant, and Windows background tasks don't lag your game. Install the Games on the 1TB HDD: Both Steam and the Battle.net launcher allow you to set a "Library Folder" on a different drive. Fortnite is currently ~30–50GB. Call of Duty (Warzone + Multiplayer) can exceed 150GB–200GB. The Result: Your OS stays snappy on the SSD, while your massive games live on the HDD. You’ll have "slow" loading screens, but the Windows OS itself won't be fighting the game for disk priority. 3. Why Windows 10 is a "Tight Fit" In 2026, Windows 10 is no longer receiving free security updates. If you use it, you must be extremely disciplined: Disable Hibernation: Run powercfg -h off in the command prompt. This can save you 16GB–32GB of space (since you have 32GB of RAM). Clear "Delivery Optimization" files: Windows stores update caches that can eat 10GB easily. The Prioritized Plan Boot Drive: Install Windows 10 (or 11) on the 120GB SSD. It is enough for the OS and one small game (like Fortnite). Game Drive: Plug in the 1TB HDD and format it as NTFS. Optimization: * Move your Windows Page File to the SSD (it likely already is). Tell Steam/Battle.net to install Call of Duty to the HDD. Keep 20GB free on that 120GB SSD at all times, or Windows will slow to a crawl. The Opportunity Cost Warning Even with the OS on an SSD, Call of Duty on a mechanical HDD in 2026 will still cause texture streaming issues. You will see "clay buildings" and stuttering because the 3070 wants data faster than the HDD can spin. It is "playable," but it is the weakest link in your $1,500+ build. Would you like me to show you the command to disable the hibernation file to save that extra 30GB on your small SSD?
