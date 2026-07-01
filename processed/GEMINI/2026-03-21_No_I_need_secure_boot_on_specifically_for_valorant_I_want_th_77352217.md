---
category: homelab
date: 2026-03-21
id: 066907
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan needs secure boot enabled for Valorant and wants to restore his system
  to its previous working state.
tags:
- secure-boot
- valorant
- system-configuration
- gaming
---
# No I need secure boot on specifically for valorant. I want things back as they were

### USER
No I need secure boot on specifically for valorant. I want things back as they were

### GEMINI
If you want things exactly as they were—Secure Boot on, Valorant working, and Minegrub/Tiny 11 accessible—you have a fundamental conflict: The update replaced your signed bootloader with an unsigned one. Your BIOS is blocking GRUB because it isn't "signed" with a key it recognizes. To fix this without turning Secure Boot off, you have to manually bridge that trust gap. The "Brutally Honest" Reality You can't just "wish" it back from that blue screen. You have to perform a manual "Enrollment" in your BIOS. If you don't do this, you will never see Minegrub again as long as Secure Boot is active. 1. Identify your Motherboard Since you have a 12700K, you're likely on an ASUS, MSI, or Gigabyte board. The steps vary slightly: ASUS: Go to Boot > Secure Boot > Key Management > Append Default Key (or Enroll EFI Image). MSI: Go to Settings > Advanced > Windows OS Configuration > Secure Boot > Enroll EFI Image. Gigabyte: Go to Boot > Secure Boot > Key Management. 2. The Enrollment Procedure Once you find the "Enroll EFI Image" (or similar) option: A file browser will appear. Select your main boot drive. Navigate to: EFI -> GRUB -> grubx64.efi. Select that file and confirm you want to Trust/Enroll it. Crucial Step: You also need to enroll the kernel. Navigate to EFI -> linux-cachyos -> vmlinuz-linux-cachyos and enroll that too. Save and Exit (F10). What if my BIOS doesn't have "Enroll EFI Image"? If your motherboard is one of the annoying ones that doesn't allow manual file enrollment, you have to use a Shim. Temporarily Disable Secure Boot just to get into CachyOS. (Don't worry, we'll turn it back on in 5 minutes). Open the terminal and install shim and preloader: sudo pacman -S shim-signed preloader-signed Re-install GRUB using the shim: sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB --modules="tpm" --disable-shim-lock Re-enable Secure Boot in the BIOS. The Opportunity Cost If you keep staring at the "Secure Boot Violation" screen without taking one of these actions, you are essentially locked out of your own machine. You have to either make the BIOS trust the new files or downgrade the security temporarily to fix it from the inside. Which motherboard brand are you using? I can give you the exact menu path so we can get this done.
