---
id: 599142
source: GEMINI
date: 2026-01-20
tags: ['steam-deck', 'storage', 'ssd-space']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is providing storage context (63.5 GB free on SSD) to help diagnose an emulator setup issue.
---
# i literally have 63.5 gb free on the ssd if that helps break things down

### USER
i literally have 63.5 gb free on the ssd if that helps break things down

### GEMINI
63GB is plenty of space, so the "Disk Full" theory is officially dead. The fact that CryoUtilities says "Unknown" while you have that much free space means one of two things: either your permissions are mangled or SteamOS (version 3.5 or later) has changed how it handles swap, and the tool is looking for a file that doesn't exist. Since you are in a "brutally honest" partnership with me, let's stop poking a GUI that is failing you and fix this manually via the terminal. This is how you take control of the machine. 1. The Manual Swap Check (The "No-Lies" Test) Open Konsole in Desktop Mode and run: free -h If Swap says 0B: Your swap is totally disabled. That's why Game Mode crashes. If Swap says 1.0Gi: You have the stock Valve swap. 2. The Manual 16GB Swap Fix If CryoUtilities is erroring out, do it yourself. Copy and paste these lines one by one (it will ask for your sudo password): # 1. Turn off any existing swap sudo swapoff -a # 2. Create a 16GB file (this takes a minute, wait for it to finish) sudo dd if=/dev/zero of=/home/swapfile bs=1G count=16 # 3. Set the correct permissions sudo chmod 600 /home/swapfile # 4. Tell the system it's a swap file sudo mkswap /home/swapfile # 5. Turn it on sudo swapon /home/swapfile Verify it worked: Run free -h again. If it says 16G under Swap, you’ve manually done what CryoUtilities failed to do. 3. Why Game Mode is Still Crashing (The "SRM" Trap) You said SRM isn't corrupted, and I believe you—but SRM's Launch Options might be the reason the update "broke" everything. In Desktop Mode, go to Steam > Library. Right-click Tears of the Kingdom > Properties. Look at Launch Options. The Trap: If it says something like -g "path/to/update.nsp", it’s trying to boot the update as the game. This will fail every time. The Fix: It must point to your base ROM in /home/internal_games/. Because you installed the update to the NAND, Citron handles the "patching" invisibly. If your Steam shortcut tries to point to the update file, it causes a circular crash in Game Mode. 4. The UMA Buffer (Don't skip this) If you haven't done the BIOS change yet (Vol Up + Power while off > Setup Utility > Advanced > UMA Frame Buffer Size > 4G), the manual swap file might still not be enough. TotK 1.2.1 requires that extra VRAM to not choke in Game Mode's overlay. The Plan of Action Run the terminal commands above. If they fail, tell me the exact error message. Verify Launch Options: Ensure Steam is pointing to the Base ROM, not the update. Clean Shaders one last time: Desktop Mode > Citron > Right-click Game > Remove > Remove All Pipeline Caches. If you run free -h and it shows 16G of swap, try launching in Game Mode immediately. Does it still kick you out?
