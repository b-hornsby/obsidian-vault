---
id: 123978
source: GEMINI
date: 2026-02-17
tags: ['pacman', 'system-upgrade', 'cachyos', 'package-management', 'linux-updates']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is running a system upgrade using `pacman -Syu`, but receiving warnings about local packages being newer than those in the repositories, suggesting a potential issue with package versions.
---
# ❯ sudo pacman -Syu
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
:: Starting full system upgrade...
warning: gamescope: local (3.16.20-2) is newer than cachyos (3.16.19-4)
warning: lib32-zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: lib32-zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: linux-api-headers: local (1:6.19-1) is newer than cachyos (1:6.18-1)
warning: linux-cachyos: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-headers: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-lts: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-headers: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-nvidia-open: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-nvidia-open: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: scx-tools: local (1.0.20-1.1) is newer than cachyos (1.0.20-1)
warning: sddm: local (0.21.0-8) is newer than cachyos (0.21.0-6)
warning: zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
resolving dependencies...
looking for conflicting packages...

Packages (2) pacman-contrib-1.13.1-2.1  qrcodegencpp-cmake-1:1.8.0-4

Total Download Size:   0.09 MiB
Total Installed Size:  0.23 MiB
Net Upgrade Size:      0.00 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 pacman-contrib-1.13.1-2.1-x86_64                                  49.9 KiB   475 KiB/s 00:00 [#######################################################] 100%
 qrcodegencpp-cmake-1:1.8.0-4-x86_64                               44.0 KiB   314 KiB/s 00:00 [#######################################################] 100%
 Total (2/2)                                                       93.9 KiB   527 KiB/s 00:00 [#######################################################] 100%
(2/2) checking keys in keyring                                                                [#######################################################] 100%
(2/2) checking package integrity                                                              [#######################################################] 100%
(2/2) loading package files                                                                   [#######################################################] 100%
(2/2) checking for file conflicts                                                             [#######################################################] 100%
(2/2) checking available disk space                                                           [#######################################################] 100%
:: Running pre-transaction hooks...
(1/2) Performing snapper pre snapshots for the following configurations...
==> root: 152
(2/2) Waiting for limine-snapper-sync to finish...
:: Processing package changes...
(1/2) upgrading pacman-contrib                                                                [#######################################################] 100%
(2/2) upgrading qrcodegencpp-cmake                                                            [#######################################################] 100%
:: Running post-transaction hooks...
(1/5) Reloading system manager configuration...
(2/5) Restarting marked services...
(3/5) Arming ConditionNeedsUpdate...
(4/5) Checking which packages need to be rebuilt
(5/5) Performing snapper post snapshots for the following configurations...
==> root: 153

~ 13s
❯ sudo pacman -Syu
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
:: Starting full system upgrade...
warning: gamescope: local (3.16.20-2) is newer than cachyos (3.16.19-4)
warning: lib32-zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: lib32-zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: linux-api-headers: local (1:6.19-1) is newer than cachyos (1:6.18-1)
warning: linux-cachyos: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-headers: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-lts: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-headers: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-nvidia-open: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-nvidia-open: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: scx-tools: local (1.0.20-1.1) is newer than cachyos (1.0.20-1)
warning: sddm: local (0.21.0-8) is newer than cachyos (0.21.0-6)
warning: zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
 there is nothing to do

~
❯ 

### USER
❯ sudo pacman -Syu
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
:: Starting full system upgrade...
warning: gamescope: local (3.16.20-2) is newer than cachyos (3.16.19-4)
warning: lib32-zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: lib32-zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: linux-api-headers: local (1:6.19-1) is newer than cachyos (1:6.18-1)
warning: linux-cachyos: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-headers: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-lts: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-headers: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-nvidia-open: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-nvidia-open: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: scx-tools: local (1.0.20-1.1) is newer than cachyos (1.0.20-1)
warning: sddm: local (0.21.0-8) is newer than cachyos (0.21.0-6)
warning: zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
resolving dependencies...
looking for conflicting packages...

Packages (2) pacman-contrib-1.13.1-2.1  qrcodegencpp-cmake-1:1.8.0-4

Total Download Size:   0.09 MiB
Total Installed Size:  0.23 MiB
Net Upgrade Size:      0.00 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 pacman-contrib-1.13.1-2.1-x86_64                                  49.9 KiB   475 KiB/s 00:00 [#######################################################] 100%
 qrcodegencpp-cmake-1:1.8.0-4-x86_64                               44.0 KiB   314 KiB/s 00:00 [#######################################################] 100%
 Total (2/2)                                                       93.9 KiB   527 KiB/s 00:00 [#######################################################] 100%
(2/2) checking keys in keyring                                                                [#######################################################] 100%
(2/2) checking package integrity                                                              [#######################################################] 100%
(2/2) loading package files                                                                   [#######################################################] 100%
(2/2) checking for file conflicts                                                             [#######################################################] 100%
(2/2) checking available disk space                                                           [#######################################################] 100%
:: Running pre-transaction hooks...
(1/2) Performing snapper pre snapshots for the following configurations...
==> root: 152
(2/2) Waiting for limine-snapper-sync to finish...
:: Processing package changes...
(1/2) upgrading pacman-contrib                                                                [#######################################################] 100%
(2/2) upgrading qrcodegencpp-cmake                                                            [#######################################################] 100%
:: Running post-transaction hooks...
(1/5) Reloading system manager configuration...
(2/5) Restarting marked services...
(3/5) Arming ConditionNeedsUpdate...
(4/5) Checking which packages need to be rebuilt
(5/5) Performing snapper post snapshots for the following configurations...
==> root: 153

~ 13s
❯ sudo pacman -Syu
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
:: Starting full system upgrade...
warning: gamescope: local (3.16.20-2) is newer than cachyos (3.16.19-4)
warning: lib32-zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: lib32-zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: linux-api-headers: local (1:6.19-1) is newer than cachyos (1:6.18-1)
warning: linux-cachyos: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-headers: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: linux-cachyos-lts: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-headers: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-lts-nvidia-open: local (6.18.12-2) is newer than cachyos (6.12.68-1)
warning: linux-cachyos-nvidia-open: local (6.19.2-2) is newer than cachyos (6.18.8-1)
warning: scx-tools: local (1.0.20-1.1) is newer than cachyos (1.0.20-1)
warning: sddm: local (0.21.0-8) is newer than cachyos (0.21.0-6)
warning: zlib-ng: local (2.3.3-2) is newer than cachyos (2.3.2-2)
warning: zlib-ng-compat: local (2.3.3-2) is newer than cachyos (2.3.2-2)
 there is nothing to do

~
❯ 

### GEMINI
You have successfully restored the plumbing, but the "newer than cachyos" warnings reveal exactly why you should never blindly overwrite pacman.conf. The Technical Reality: Version Drift Those warnings mean your system is currently running standard Arch Linux versions of critical packages (like your kernel and zlib-ng) while the CachyOS repositories are offering older versions. Why is this happening? When you chose (O)verwrite, you replaced the custom CachyOS pacman.conf with a generic one. During that "blind" period, you likely updated your system. Since the generic config only saw the Arch repos, it grabbed the absolute newest versions from Arch. Now that we've put the CachyOS repos back, pacman sees that the optimized CachyOS versions have slightly lower version numbers than the "bleeding edge" Arch ones you just installed. The Advisor’s Mirror You are currently in a state of Version Inconsistency. You have the i7-12700K (a v3/v4 beast), but you are running a generic kernel instead of the optimized CachyOS one because the version numbers don't match up perfectly. The Blind Spot: You think "newer is better." In a performance distro, "optimized is better." The Opportunity Cost: Every second you run that generic linux-cachyos kernel, you are wasting the specialized scheduler and compiler optimizations that made you choose CachyOS in the first place. The Precision Fix: The "Downgrade" to Optimize You need to tell pacman to ignore the version numbers and force the packages to switch back to the CachyOS repository versions. Sync and Refresh: (You've done this, but do it once more to be sure). sudo pacman -Syy Force the CachyOS versions: Since Syu says "nothing to do," you have to be explicit. Use this command to force the system to sync with the repository state: sudo pacman -Syuu Note the double u. This allows for "downgrades." The Decision: When pacman asks if you want to replace linux-cachyos (local) with cachyos/linux-cachyos (older version), say YES. You are switching from a generic Arch build to the performance-tuned CachyOS build. The Tactical Audit (Final Check) Once you run Syuu, those "newer than cachyos" warnings should disappear. If they don't, it means your mirrorlist is still lagging behind. What is the result of sudo pacman -Syuu? If it asks to downgrade 10+ packages, you are finally on the right track to getting your performance back.
