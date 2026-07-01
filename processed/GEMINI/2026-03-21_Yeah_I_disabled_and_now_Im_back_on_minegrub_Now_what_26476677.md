---
id: 026380
source: GEMINI
date: 2026-03-21
tags: ['grub', 'dual-boot', 'bootloader', 'troubleshooting']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan disabled something and is back on the default GRUB, asking what to do next.
---
# Yeah I disabled and now I’m back on minegrub. Now what?

### USER
Yeah I disabled and now I’m back on minegrub. Now what?

### GEMINI
Now that you're back in Minegrub, you're at the crossroads. You have the look you want, but Valorant will not launch because Secure Boot is currently disabled. To get things back to "exactly as they were" (Minegrub working + Secure Boot on for Valorant), you have to fix the "trust" issue. The update changed your files, so your BIOS no longer recognizes their signatures. The Strategic Plan You have two ways to fix this. Choose the one that matches your BIOS capability: Option A: The "Manual Enroll" (If your BIOS allows it) This is the cleanest way. You are telling the BIOS, "I know these new files are mine, trust them." Reboot and enter your BIOS. Go to the Security/Secure Boot tab and look for "Key Management" or "Enroll EFI Image". You need to enroll three specific files from your EFI partition (usually a file browser pops up): EFI/GRUB/grubx64.efi (This makes Minegrub/GRUB "legal") vmlinuz-linux-cachyos (The actual Linux kernel) initramfs-linux-cachyos.img (The boot RAM disk) Re-enable Secure Boot in the BIOS. Save and Exit. Option B: The sbctl Route (The "Pro" Linux Way) If your BIOS is being difficult or won't let you pick files, use sbctl. This tool creates your own custom keys and signs your files so the BIOS accepts them automatically. In your CachyOS terminal, install the tool: sudo pacman -S sbctl Check your status (it should say Setup Mode: Enabled if you clear keys, but let's try signing first): sudo sbctl status Create your own keys and enroll them: sudo sbctl create-keys sudo sbctl enroll-keys -m Sign your bootloader and kernel: sudo sbctl sign -s /boot/EFI/GRUB/grubx64.efi sudo sbctl sign -s /boot/vmlinuz-linux-cachyos Reboot, enter BIOS, and Re-enable Secure Boot. The "Brutally Honest" Warning: Tiny 11 & Valorant Since you are using Tiny 11, ensure that your Windows Boot Manager is also "Trusted" in your BIOS. Usually, Windows is signed by Microsoft, so the BIOS trusts it by default—but if you messed with the keys in the past, you might need to "Restore Factory Keys" or "Append Microsoft Default Keys" in the BIOS Secure Boot menu to ensure Valorant's Vanguard doesn't kick you for a "System Requirement" error. Which path feels more comfortable for you: digging through the BIOS menus again (Option A) or running the signing commands in the terminal (Option B)?
