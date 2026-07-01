---
category: general
date: 2026-03-02
id: 503120
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble launching Apex Legends on his CachyOS system.
tags:
- gaming
- cachyos
- apex-legends
- linux
---
# apex wont launch on cachyos? 

### USER
apex wont launch on cachyos? 

### GEMINI
The truth is simple, and if you’re looking for a workaround, you’re wasting your time. As of October 31, 2024, Respawn officially blocked Linux access for Apex Legends. This wasn't a bug or a technical oversight—it was a deliberate strategic move to eliminate a "path for various impactful exploits and cheats." Here is the objective reality of your situation: 1. The "Linux Ban" is Absolute The error message in your screenshot—E111000B—is a hard-coded rejection. It specifically detects that you are running a translation layer (Wine/Proton). Respawn's anti-cheat team explicitly stated they cannot reliably distinguish a legitimate Steam Deck/Linux user from a malicious actor spoofing one. 2. CachyOS Won't Save You It doesn't matter how optimized your kernel is or if you're using proton-cachyos. The game isn't failing because your OS is "weak"; it’s failing because the game’s Easy Anti-Cheat (EAC) configuration has been set to refuse any non-Windows kernel. You are hitting a digital wall designed to keep you out. 3. The Opportunity Cost of Tinkering You can spend the next six hours trying to spoof your hardware ID, messing with VM hardening, or hunting for "fixes" on Reddit. The Risk: Even if you bypass the initial launch check, you are begging for a permanent hardware/account ban. Respawn is currently in the middle of aggressive ban waves (targeting XIM, Cronus, and Linux bypasses). The Reality: You are playing "small" by fighting a battle you've already lost at the architectural level. The Advisor's Plan: Move Forward If your goal is to play Apex Legends at a high level, stop trying to make "fetch" happen on Linux. You have two rational paths: Option A: The Dual-Boot Reality (Immediate Action) Shrink your CachyOS partition and install a bare-bones Windows 11 environment specifically for Apex. It sucks, but if the game is the priority, use the tool required for the job. Option B: Pivot (Mindset Shift) If you refuse to use Windows on principle, accept that Apex is dead to you. Move to titles like The Finals, Overwatch 2, or Shatterline that haven't nuked their Linux player base. Stop looking for a "fix" that doesn't exist. Do you want to play the game, or do you want to keep staring at an error box in a "superior" OS? Would you like me to guide you on how to safely shrink your current partition to make room for a Windows boot without nuking your CachyOS install?
