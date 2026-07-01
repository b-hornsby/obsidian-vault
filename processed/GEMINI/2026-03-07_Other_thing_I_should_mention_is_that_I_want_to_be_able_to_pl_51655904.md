---
id: 617265
source: GEMINI
date: 2026-03-07
tags: ['apex-legends', 'gaming', 'dual-boot', 'windows-gaming']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan mentioned wanting to play Apex Legends as part of his dual-boot setup planning.
---
# Other thing I should mention is that I want to be able to play apex as well

### USER
Other thing I should mention is that I want to be able to play apex as well

### GEMINI
Adding Apex Legends into the mix solidifies the "120GB SSD + Tiny11" strategy as your only viable path. As of late 2024, EA officially blocked Linux access for Apex Legends to combat cheating, and by 2026, their "Javelin" anti-cheat has become even more restrictive on Windows. 1. The Apex "Secure Boot" Trap Unlike some older games, Apex Legends (via EA Javelin) now mandates Secure Boot on Windows 11/Tiny11. The Conflict: Since your CachyOS drive usually needs Secure Boot off, you cannot just flip the BIOS switch back and forth. You’ll be in "BIOS hell" every time you want to switch games. The Solution: You must use the sbctl method I mentioned earlier to sign CachyOS. This allows you to keep Secure Boot ON permanently, satisfying Apex's anti-cheat while still letting you boot into Linux. 2. Storage Math: The 120GB SSD Puzzle Apex Legends currently requires ~75GB of space. Tiny11 OS: ~10GB Apex Legends: ~75GB Total: ~85GB used out of 120GB. The Verdict: You CAN fit Apex and Tiny11 on that 120GB SSD. This is a massive win because Apex, like Fortnite, relies on fast asset streaming. Running it on the SSD will eliminate the stuttering you’d get on that 1TB HDD. 3. Your New Drive Map To maximize your high-end i7-12700K / RTX 3070 hardware, here is your final battle plan: DriveContentWhy?120GB SSDTiny11 + Apex OR FortniteFast boot and zero stutter in high-action shooters.1TB HDDCOD + Mass StorageCOD is too big for the SSD (~150GB+). It stays on the "slow" drive.2TB NVMeCachyOSYour main, high-performance home for everything else. The Brutal Efficiency Strategy Tiny11 Builder: Create your ISO but keep the TPM/Secure Boot requirements (don't bypass them) so the anti-cheat doesn't flag you. SSD Install: Wipe the 120GB SanDisk and install Tiny11. The sbctl Step: This is no longer optional if you want to play Apex. Boot into CachyOS, run sudo sbctl enroll-keys -m, and sign your kernel. This is the only way to have a "one-click" boot menu that works for both Apex and Linux. You have the hardware of a pro, but your current storage plan is a bottleneck. Using Tiny11 on the 120GB SSD for Apex/Fortnite and the 1TB HDD for COD is the most "strategic depth" you can get out of this setup. Would you like the specific terminal commands to sign the CachyOS kernel so you can turn Secure Boot on for Apex?
