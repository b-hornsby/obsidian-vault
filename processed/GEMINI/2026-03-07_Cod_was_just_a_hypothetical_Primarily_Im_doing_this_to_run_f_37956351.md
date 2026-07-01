---
id: 565135
source: GEMINI
date: 2026-03-07
tags: ['gaming', 'fortnite', 'apex-legends', 'valorant', 'pc-gaming']
category: general
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was clarifying that his gaming PC build was primarily for Fortnite, Apex Legends, and possibly Valorant, not Call of Duty.
---
# Cod was just a hypothetical. Primarily I’m doing this to run fort and apex and maybe valorant

### USER
Cod was just a hypothetical. Primarily I’m doing this to run fort and apex and maybe valorant

### GEMINI
Adding Valorant into the mix changes the math because of Vanguard, Riot’s aggressive kernel-level anti-cheat. In 2026, Valorant on Windows 11/Tiny11 is the most demanding game you've mentioned regarding system integrity. If your BIOS or OS is "tweaked" incorrectly, Vanguard will simply refuse to let the game launch. 1. The Valorant "Dealbreaker" Vanguard mandates Secure Boot and TPM 2.0 on Windows 11 systems. Tiny11 Warning: If you use a version of Tiny11 that strips out Windows Security or User Account Control (UAC), Vanguard will likely trigger a "VAN9001" or "VAN9003" error. The Solution: When building your Tiny11 image, you must ensure you do not remove the TPM/Secure Boot requirements or core security libraries. Your Asus Z790-P motherboard supports these natively—use them. 2. Storage Triage: 120GB is Tight but Doable With Valorant added, your storage strategy must be surgical: Tiny11 OS: ~10GB Fortnite (Base): ~30GB Apex Legends: ~75GB Valorant: ~35GB Total: ~150GB The Reality: You cannot fit all three on the 120GB SSD. The Strategic Move: 1. SSD (120GB): Install Tiny11 and Valorant. Valorant is the most sensitive to drive speed and anti-cheat interference; it must be on the boot drive. 2. HDD (1TB): Install Apex Legends and Fortnite. * Note: You will experience the "blurry textures" (LOD pop-in) in Fortnite and Apex for the first 20 seconds of a match, but since your OS is on the SSD, the games won't crash or stutter as badly. 3. The CachyOS / Secure Boot Conflict Since Valorant requires Secure Boot to be enabled in the BIOS to run on Windows 11, you are officially forced into the sbctl path I mentioned earlier. Without signing your CachyOS kernel with sbctl, you will have to go into your BIOS and manually toggle Secure Boot every single time you switch between Linux and Valorant. This is a massive waste of time and wears down your CMOS. Final Recommended Setup (2026 Competitive Build) BIOS: Enable TPM 2.0, Secure Boot, and IOMMU (required for Vanguard in 2026). Linux: Boot CachyOS and use sbctl to sign your kernel so it boots with Secure Boot ON. Windows: Install Tiny11 on the 120GB SSD. Pro-Tip: Disable Hibernation (powercfg /hibernate off) to save ~30GB immediately. Install Map: SSD: Valorant (Needs the SSD for Vanguard stability). HDD: Fortnite & Apex (They can survive the HDD, even if textures are slow to load). The Bottom Line: You have an i7-12700K and an RTX 3070. Playing Valorant on a "broken" or "hacked" version of Windows is an invitation for a Vanguard ban or constant errors. Would you like the step-by-step terminal commands for sbctl so you can get CachyOS and Valorant working under Secure Boot today?
