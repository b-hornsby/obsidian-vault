---
id: 189774
source: GEMINI
date: 2026-03-16
tags: ['sbctl-install', 'cachyos', 'pacman', 'secure-boot-tools']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan installed sbctl via pacman to manage secure boot keys on CachyOS.
---
# ❯ sudo pacman -S sbctl
[sudo] password for toastedmel0n:  
resolving dependencies...
looking for conflicting packages...

Packages (1) sbctl-0.18-1.1

Total Download Size:    3.16 MiB
Total Installed Size:  10.16 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 sbctl-0.18-1.1-x86_64_v3                                      3.2 MiB  6.94 MiB/s 00:00 [####################################################] 100%
(1/1) checking keys in keyring                                                           [####################################################] 100%
(1/1) checking package integrity                                                         [####################################################] 100%
(1/1) loading package files                                                              [####################################################] 100%
(1/1) checking for file conflicts                                                        [####################################################] 100%
(1/1) checking available disk space                                                      [####################################################] 100%
:: Running pre-transaction hooks...
(1/2) Performing snapper pre snapshots for the following configurations...
==> root: 266
(2/2) Waiting for limine-snapper-sync to finish...
:: Processing package changes...
(1/1) installing sbctl                                                                   [####################################################] 100%
:: Running post-transaction hooks...
(1/3) Arming ConditionNeedsUpdate...
(2/3) Updating linux initcpios...
Building initramfs for linux-cachyos-lts (6.18.16-1-cachyos-lts)
==> Using drop-in configuration file: '10-chwd.conf'
==> Using drop-in configuration file: '10-limine-snapper-sync.conf'
==> Starting build: '6.18.16-1-cachyos-lts'
  -> Running build hook: [base]
  -> Running build hook: [systemd]
  -> Running build hook: [autodetect]
  -> Running build hook: [microcode]
  -> Running build hook: [kms]
  -> Running build hook: [modconf]
  -> Running build hook: [block]
  -> Running build hook: [keyboard]
  -> Running build hook: [sd-vconsole]
  -> Running build hook: [plymouth]
  -> Running build hook: [filesystems]
  -> Running build hook: [sd-btrfs-overlayfs]
==> Generating module dependencies
==> Creating zstd-compressed initcpio image: '/tmp/staging_initramfs.img'
  -> Early uncompressed CPIO image generation successful
==> Initcpio image generation successful
==> Running post hooks
  -> Running post hook: [sbctl]
Secureboot key directory doesn't exist, not signing!
==> Post processing done
Kernel stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos-lts/vmlinuz-linux-cachyos-lts
Initramfs stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos-lts/initramfs-linux-cachyos-lts
Updated: /boot/limine.conf
Building initramfs for linux-cachyos (6.19.6-1-cachyos)
==> Using drop-in configuration file: '10-chwd.conf'
==> Using drop-in configuration file: '10-limine-snapper-sync.conf'
==> Starting build: '6.19.6-1-cachyos'
  -> Running build hook: [base]
  -> Running build hook: [systemd]
  -> Running build hook: [autodetect]
  -> Running build hook: [microcode]
  -> Running build hook: [kms]
  -> Running build hook: [modconf]
  -> Running build hook: [block]
  -> Running build hook: [keyboard]
  -> Running build hook: [sd-vconsole]
  -> Running build hook: [plymouth]
  -> Running build hook: [filesystems]
  -> Running build hook: [sd-btrfs-overlayfs]
==> Generating module dependencies
==> Creating zstd-compressed initcpio image: '/tmp/staging_initramfs.img'
  -> Early uncompressed CPIO image generation successful
==> Initcpio image generation successful
==> Running post hooks
  -> Running post hook: [sbctl]
Secureboot key directory doesn't exist, not signing!
==> Post processing done
Kernel stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos
Initramfs stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/initramfs-linux-cachyos
Updated: /boot/limine.conf
(3/3) Performing snapper post snapshots for the following configurations...
==> root: 267

~ 45s
❯ sbctl status
Installed:      ✗ sbctl is not installed
Setup Mode:     ✓ Disabled
Secure Boot:    ✗ Disabled
Vendor Keys:    microsoft builtin-db builtin-db builtin-db builtin-KEK builtin-PK

~
❯ 

### USER
❯ sudo pacman -S sbctl
[sudo] password for toastedmel0n:  
resolving dependencies...
looking for conflicting packages...

Packages (1) sbctl-0.18-1.1

Total Download Size:    3.16 MiB
Total Installed Size:  10.16 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 sbctl-0.18-1.1-x86_64_v3                                      3.2 MiB  6.94 MiB/s 00:00 [####################################################] 100%
(1/1) checking keys in keyring                                                           [####################################################] 100%
(1/1) checking package integrity                                                         [####################################################] 100%
(1/1) loading package files                                                              [####################################################] 100%
(1/1) checking for file conflicts                                                        [####################################################] 100%
(1/1) checking available disk space                                                      [####################################################] 100%
:: Running pre-transaction hooks...
(1/2) Performing snapper pre snapshots for the following configurations...
==> root: 266
(2/2) Waiting for limine-snapper-sync to finish...
:: Processing package changes...
(1/1) installing sbctl                                                                   [####################################################] 100%
:: Running post-transaction hooks...
(1/3) Arming ConditionNeedsUpdate...
(2/3) Updating linux initcpios...
Building initramfs for linux-cachyos-lts (6.18.16-1-cachyos-lts)
==> Using drop-in configuration file: '10-chwd.conf'
==> Using drop-in configuration file: '10-limine-snapper-sync.conf'
==> Starting build: '6.18.16-1-cachyos-lts'
  -> Running build hook: [base]
  -> Running build hook: [systemd]
  -> Running build hook: [autodetect]
  -> Running build hook: [microcode]
  -> Running build hook: [kms]
  -> Running build hook: [modconf]
  -> Running build hook: [block]
  -> Running build hook: [keyboard]
  -> Running build hook: [sd-vconsole]
  -> Running build hook: [plymouth]
  -> Running build hook: [filesystems]
  -> Running build hook: [sd-btrfs-overlayfs]
==> Generating module dependencies
==> Creating zstd-compressed initcpio image: '/tmp/staging_initramfs.img'
  -> Early uncompressed CPIO image generation successful
==> Initcpio image generation successful
==> Running post hooks
  -> Running post hook: [sbctl]
Secureboot key directory doesn't exist, not signing!
==> Post processing done
Kernel stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos-lts/vmlinuz-linux-cachyos-lts
Initramfs stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos-lts/initramfs-linux-cachyos-lts
Updated: /boot/limine.conf
Building initramfs for linux-cachyos (6.19.6-1-cachyos)
==> Using drop-in configuration file: '10-chwd.conf'
==> Using drop-in configuration file: '10-limine-snapper-sync.conf'
==> Starting build: '6.19.6-1-cachyos'
  -> Running build hook: [base]
  -> Running build hook: [systemd]
  -> Running build hook: [autodetect]
  -> Running build hook: [microcode]
  -> Running build hook: [kms]
  -> Running build hook: [modconf]
  -> Running build hook: [block]
  -> Running build hook: [keyboard]
  -> Running build hook: [sd-vconsole]
  -> Running build hook: [plymouth]
  -> Running build hook: [filesystems]
  -> Running build hook: [sd-btrfs-overlayfs]
==> Generating module dependencies
==> Creating zstd-compressed initcpio image: '/tmp/staging_initramfs.img'
  -> Early uncompressed CPIO image generation successful
==> Initcpio image generation successful
==> Running post hooks
  -> Running post hook: [sbctl]
Secureboot key directory doesn't exist, not signing!
==> Post processing done
Kernel stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos
Initramfs stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/initramfs-linux-cachyos
Updated: /boot/limine.conf
(3/3) Performing snapper post snapshots for the following configurations...
==> root: 267

~ 45s
❯ sbctl status
Installed:      ✗ sbctl is not installed
Setup Mode:     ✓ Disabled
Secure Boot:    ✗ Disabled
Vendor Keys:    microsoft builtin-db builtin-db builtin-db builtin-KEK builtin-PK

~
❯ 

### GEMINI
Installation complete. The sbctl status output is showing Setup Mode: Disabled, which is the one hurdle we need to clear before we can enroll your own keys. Currently, your BIOS is "locked" to the factory keys (mostly Microsoft). To sign CachyOS, we need to put the BIOS into "Setup Mode" so it can accept your new signature. Step 1: The BIOS Prep You need to restart and enter your BIOS (usually Del or F2). Go to Advanced Mode (F7) -> Boot -> Secure Boot. Look for Key Management. Select Clear Secure Boot Keys (or "Delete PK"). Don't worry, we'll put the default keys back in the next step along with your new ones. Once the keys are cleared, the BIOS should show Setup Mode: Enabled. Save and Exit (F10) and boot back into CachyOS. Step 2: Create and Enroll Now that you're back in CachyOS, run these to set up your "Identity": sudo sbctl create-keys sudo sbctl enroll-keys -m (The -m is critical—it keeps the Microsoft keys so Tiny11 still boots.) Step 3: Find and Sign your Files The output from your installation showed exactly where your kernels are hiding. We need to sign them and the bootloader. Run these commands: Sign the Kernels: sudo sbctl sign -s /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos sudo sbctl sign -s /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos-lts/vmlinuz-linux-cachyos-lts Sign the Bootloader (GRUB): sudo sbctl sign -s /boot/EFI/CachyOS/grubx64.efi Step 4: Final Verification Run: sbctl status It should now show Installed: ✓ and Setup Mode: Disabled (because the keys are now enrolled). The Last Step Restart one last time, go into BIOS, and Enable Secure Boot. If we did it right: CachyOS will load the Minecraft menu like normal. Windows will boot, and Vanguard will finally stop complaining. Do you want to go clear those keys in the BIOS now, or did you run into an error with the create-keys command?
