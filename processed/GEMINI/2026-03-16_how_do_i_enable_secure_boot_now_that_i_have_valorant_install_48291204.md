---
category: homelab
date: 2026-03-16
id: 190098
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wanted to enable secure boot while keeping Valorant (which requires
  secure boot via Vanguard) working.
tags:
- secure-boot
- valorant
- cachyos
- vanguard-anti-cheat
---
# how do i enable secure boot now that i have valorant installed? i know cachyos needs to be added to bios im pretty sure

### USER
how do i enable secure boot now that i have valorant installed? i know cachyos needs to be added to bios im pretty sure

### GEMINI
To play Valorant, you've reached the point where you can no longer avoid the "final boss." Valorant's Vanguard anti-cheat on Windows 11 is non-negotiable: it must see Secure Boot as "Enabled." Since you are on CachyOS, you have a massive advantage: CachyOS includes a tool called sbctl that makes this process much easier than on standard Arch. The Game Plan We are going to "sign" your Linux bootloader so the BIOS thinks CachyOS is just as "official" as Windows. Step 1: Install the Signing Tool Open your terminal in CachyOS and run: sudo pacman -S sbctl Step 2: Check your Status Run this to see if your BIOS is ready: sbctl status It should say Setup Mode: Enabled (This means your BIOS is currently "open" to learning new keys). It should say Secure Boot: Disabled. Step 3: Create and Enroll Your Own Keys This tells the motherboard to trust you instead of just Microsoft. sudo sbctl create-keys sudo sbctl enroll-keys -m (The -m includes Microsoft’s keys so Windows still boots!) Step 4: Sign the Boot Files Now you need to sign the Minecraft menu (GRUB) and your Kernel so they can pass the security check. Run these one by one: sudo sbctl sign -s /boot/EFI/CachyOS/grubx64.efi sudo sbctl sign -s /boot/vmlinuz-linux-cachyos Note: If those paths aren't exactly right, run sbctl verify and it will tell you exactly which files are missing signatures. Step 5: The BIOS Flip Now, the moment of truth: Reboot and enter your BIOS. Go to Boot -> Secure Boot. Change it to Enabled (or "Windows UEFI Mode"). Save and Exit. What should happen: The Minecraft Menu should appear like normal. CachyOS should boot without a "Security Violation." Windows should boot, and Valorant should finally let you past the loading screen. The "Emergency Exit" If you get a black screen or a red "Violation" box: Go back into BIOS. Turn Secure Boot OFF. You’ll be right back into CachyOS, and we can check which file we missed signing. Would you like me to help you verify the exact file paths for your signatures before you reboot?
