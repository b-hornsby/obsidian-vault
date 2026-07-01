---
category: homelab
date: 2026-03-16
id: 802189
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan asked for a complete step-by-step plan to set up secure boot from scratch.
tags:
- secure-boot
- cachyos
- setup-guidance
---
# So from the start and now knowing what we know, what do I do?

### USER
So from the start and now knowing what we know, what do I do?

### GEMINI
To get Minegrub working with Secure Boot (and Valorant) without that "prohibited by policy" error, we have to strip out the Microsoft "Shim" that GRUB is trying to use. Since you have already enrolled your own keys into the BIOS hardware, we are going to make GRUB rely only on your keys. The Master Plan (No more "Shim" errors) Step 1: Prep the BIOS (One last time) Reboot into BIOS. Disable Secure Boot so you can get into CachyOS. Keep your keys enrolled (Don't clear them this time). Step 2: Configure GRUB for Direct Boot Open your terminal in CachyOS and run: Edit the GRUB config: sudo micro /etc/default/grub Find the line: GRUB_CMDLINE_LINUX_DEFAULT="..." Add module_blacklist=shim_lock inside the quotes. Save and exit (Ctrl+S, Ctrl+Q). Re-Install GRUB (The "Secret Sauce"): This command installs GRUB without the "Shim" dependency that is causing your black screen error. sudo grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=CachyOS --no-uefi-secure-boot Update the Minecraft Menu: sudo grub-mkconfig -o /boot/grub/grub.cfg Step 3: Sign the New Bootloader Now we need to make sure the BIOS trusts the new file you just created. Sign the GRUB binary: sudo sbctl sign -s /boot/EFI/CachyOS/grubx64.efi Verify the chain: sudo sbctl verify Ensure /boot/EFI/CachyOS/grubx64.efi and /boot/vmlinuz-linux-cachyos are both Green ✓. Step 4: The Final Lock-In Reboot into BIOS. Enable Secure Boot (Standard or Windows UEFI Mode). Save and Exit. Why this works: The Error Fix: By using --no-uefi-secure-boot, you told GRUB: "Don't look for the Microsoft Shim middleman." The Security: Because you signed the file with sbctl, the BIOS still verifies the file is safe before it lets it run. The Game: Windows will see the BIOS is in Secure Boot mode, and Valorant will launch perfectly. The Vibe: Since we only updated the GRUB "engine" and not the theme files, your Minegrub menu will look exactly the same. Run those three commands in Step 2 and 3. Do you get a "Green ✓" for the /boot/EFI/CachyOS/grubx64.efi file when you run verify?
