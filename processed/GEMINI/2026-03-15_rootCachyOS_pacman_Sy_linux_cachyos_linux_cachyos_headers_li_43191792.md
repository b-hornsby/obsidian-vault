---
id: 207829
source: GEMINI
date: 2026-03-15
tags: ['cachyos', 'kernel-reinstall', 'nvidia-drivers', 'pacman']
category: homelab
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan reinstalled the CachyOS kernel, headers, and NVIDIA open drivers to fix boot issues.
---
# [root@CachyOS /]# pacman -Sy linux-cachyos linux-cachyos-headers linux-cachyos-nvidia-open nvidia-utils
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
warning: linux-cachyos-6.19.6-1 is up to date -- reinstalling
warning: linux-cachyos-headers-6.19.6-1 is up to date -- reinstalling
warning: linux-cachyos-nvidia-open-6.19.6-1 is up to date -- reinstalling
warning: nvidia-utils-590.48.01-6 is up to date -- reinstalling
resolving dependencies...
looking for conflicting packages...

Packages (4) linux-cachyos-6.19.6-1  linux-cachyos-headers-6.19.6-1  linux-cachyos-nvidia-open-6.19.6-1
             nvidia-utils-590.48.01-6

Total Installed Size:  1161.61 MiB
Net Upgrade Size:         0.00 MiB

:: Proceed with installation? [Y/n] y
(4/4) checking keys in keyring                                     [####################################] 100%
(4/4) checking package integrity                                   [####################################] 100%
(4/4) loading package files                                        [####################################] 100%
(4/4) checking for file conflicts                                  [####################################] 100%
(4/4) checking available disk space                                [####################################] 100%
:: Running pre-transaction hooks...
(1/3) Performing snapper pre snapshots for the following configurations...
==> root: 264
(2/3) Waiting for limine-snapper-sync to finish...
(3/3) Remove upgraded DKMS modules
==> dkms remove --no-depmod openrazer-driver/3.11.0 -k 6.19.6-1-cachyos
:: Processing package changes...
(1/4) reinstalling linux-cachyos                                   [####################################] 100%
(2/4) reinstalling linux-cachyos-headers                           [####################################] 100%
(3/4) reinstalling nvidia-utils                                    [####################################] 100%
(4/4) reinstalling linux-cachyos-nvidia-open                       [####################################] 100%
:: Running post-transaction hooks...
( 1/12) Creating system user accounts...
( 2/12) Reloading system manager configuration...
  Skipped: Running in chroot.
( 3/12) Restarting marked services...
  Skipped: Running in chroot.
( 4/12) Reloading device manager configuration...
  Skipped: Running in chroot.
( 5/12) Arming ConditionNeedsUpdate...
( 6/12) Updating module dependencies...
( 7/12) Install DKMS modules
==> dkms install --no-depmod openrazer-driver/3.11.0 -k 6.19.6-1-cachyos
==> depmod 6.19.6-1-cachyos
( 8/12) Updating linux initcpios...
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
Kernel stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos
Initramfs stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/initramfs-linux-cachyos
Updated: /boot/limine.conf
( 9/12) Check if user should be informed about rebooting after certain system package upgrades.
==> INFO: Reboot is recommended due to the upgrade of core system package(s).
(10/12) Reloading system bus configuration...
  Skipped: Running in chroot.
(11/12) Checking which packages need to be rebuilt
(12/12) Performing snapper post snapshots for the following configurations...
==> root: 265
[root@CachyOS /]# mkinitcpio -P
==> ERROR: No presets found in /etc/mkinitcpio.d
==> WARNING: This does not update Limine boot entries.
    Use 'limine-mkinitcpio' or 'limine-update' instead.
==> Would you like to run 'limine-mkinitcpio' now? [Y/n]: 

### USER
[root@CachyOS /]# pacman -Sy linux-cachyos linux-cachyos-headers linux-cachyos-nvidia-open nvidia-utils
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
warning: linux-cachyos-6.19.6-1 is up to date -- reinstalling
warning: linux-cachyos-headers-6.19.6-1 is up to date -- reinstalling
warning: linux-cachyos-nvidia-open-6.19.6-1 is up to date -- reinstalling
warning: nvidia-utils-590.48.01-6 is up to date -- reinstalling
resolving dependencies...
looking for conflicting packages...

Packages (4) linux-cachyos-6.19.6-1  linux-cachyos-headers-6.19.6-1  linux-cachyos-nvidia-open-6.19.6-1
             nvidia-utils-590.48.01-6

Total Installed Size:  1161.61 MiB
Net Upgrade Size:         0.00 MiB

:: Proceed with installation? [Y/n] y
(4/4) checking keys in keyring                                     [####################################] 100%
(4/4) checking package integrity                                   [####################################] 100%
(4/4) loading package files                                        [####################################] 100%
(4/4) checking for file conflicts                                  [####################################] 100%
(4/4) checking available disk space                                [####################################] 100%
:: Running pre-transaction hooks...
(1/3) Performing snapper pre snapshots for the following configurations...
==> root: 264
(2/3) Waiting for limine-snapper-sync to finish...
(3/3) Remove upgraded DKMS modules
==> dkms remove --no-depmod openrazer-driver/3.11.0 -k 6.19.6-1-cachyos
:: Processing package changes...
(1/4) reinstalling linux-cachyos                                   [####################################] 100%
(2/4) reinstalling linux-cachyos-headers                           [####################################] 100%
(3/4) reinstalling nvidia-utils                                    [####################################] 100%
(4/4) reinstalling linux-cachyos-nvidia-open                       [####################################] 100%
:: Running post-transaction hooks...
( 1/12) Creating system user accounts...
( 2/12) Reloading system manager configuration...
  Skipped: Running in chroot.
( 3/12) Restarting marked services...
  Skipped: Running in chroot.
( 4/12) Reloading device manager configuration...
  Skipped: Running in chroot.
( 5/12) Arming ConditionNeedsUpdate...
( 6/12) Updating module dependencies...
( 7/12) Install DKMS modules
==> dkms install --no-depmod openrazer-driver/3.11.0 -k 6.19.6-1-cachyos
==> depmod 6.19.6-1-cachyos
( 8/12) Updating linux initcpios...
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
Kernel stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos
Initramfs stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/initramfs-linux-cachyos
Updated: /boot/limine.conf
( 9/12) Check if user should be informed about rebooting after certain system package upgrades.
==> INFO: Reboot is recommended due to the upgrade of core system package(s).
(10/12) Reloading system bus configuration...
  Skipped: Running in chroot.
(11/12) Checking which packages need to be rebuilt
(12/12) Performing snapper post snapshots for the following configurations...
==> root: 265
[root@CachyOS /]# mkinitcpio -P
==> ERROR: No presets found in /etc/mkinitcpio.d
==> WARNING: This does not update Limine boot entries.
    Use 'limine-mkinitcpio' or 'limine-update' instead.
==> Would you like to run 'limine-mkinitcpio' now? [Y/n]: 

### GEMINI
Look at the output from your pacman command—it actually worked! Even though mkinitcpio -P is acting confused, the post-transaction hooks (Hook 8/12) already built your images. You can see it right there: Initcpio image generation successful Kernel stored in /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos The reason mkinitcpio -P is failing now is because CachyOS is using a specific "Machine ID" folder structure (that long string of numbers). Don't worry about the Limine prompt—answer n. We just need to tell the Minegrub (GRUB) menu exactly where those files are so it can put CachyOS on the list. 1. The Final Menu Update Run this command. It is the most important one because it will scan those new folders and find your kernel: grub-mkconfig -o /boot/grub/grub.cfg Watch for this specific line: Found linux image: /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos 2. If it still doesn't find it: If the command above finishes and only shows Windows, it means GRUB is being lazy. We'll force it by copying the kernel to the main /boot folder where GRUB expects it: cp /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/vmlinuz-linux-cachyos /boot/ cp /boot/6cd86a12288e4089802591bd1a9a39ce/linux-cachyos/initramfs-linux-cachyos.img /boot/ grub-mkconfig -o /boot/grub/grub.cfg The Finish Line: Once grub-mkconfig says "Found linux image," you are golden. Type exit. Reboot your PC. Check your BIOS to ensure "GRUB" is still #1. Does the terminal finally show "Found linux image" when you run that grub-mkconfig command?
