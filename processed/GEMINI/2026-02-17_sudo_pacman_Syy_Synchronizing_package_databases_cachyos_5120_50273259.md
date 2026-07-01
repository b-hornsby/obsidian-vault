---
id: 567965
source: GEMINI
date: 2026-02-17
tags: ['pacman', 'package-management', 'cachyos', 'database-synchronization', 'linux-updates']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is synchronizing package databases using `pacman -Syy` and then attempting a system upgrade with `pacman -Syuu`, which results in downgrading packages, indicating he's trying to resolve a package version issue.
---
# ❯ sudo pacman -Syy
:: Synchronizing package databases...
 cachyos                                                          512.0 KiB  2.86 MiB/s 00:00 [#######################################################] 100%
 cachyos-v3                                                       129.1 KiB  1076 KiB/s 00:00 [#######################################################] 100%
 cachyos-core-v3                                                  106.9 KiB   780 KiB/s 00:00 [#######################################################] 100%
 cachyos-extra-v3                                                   4.2 MiB  20.7 MiB/s 00:00 [#######################################################] 100%
 core                                                             123.4 KiB   402 KiB/s 00:00 [#######################################################] 100%
 extra                                                              7.9 MiB  22.3 MiB/s 00:00 [#######################################################] 100%
 multilib                                                         128.7 KiB   761 KiB/s 00:00 [#######################################################] 100%

~
❯ sudo pacman -Syuu
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
:: Starting full system upgrade...
warning: gamescope: downgrading from version 3.16.20-2 to version 3.16.19-4
warning: lib32-zlib-ng: downgrading from version 2.3.3-2 to version 2.3.2-2
warning: lib32-zlib-ng-compat: downgrading from version 2.3.3-2 to version 2.3.2-2
warning: linux-api-headers: downgrading from version 1:6.19-1 to version 1:6.18-1
warning: linux-cachyos: downgrading from version 6.19.2-2 to version 6.18.8-1
warning: linux-cachyos-headers: downgrading from version 6.19.2-2 to version 6.18.8-1
warning: linux-cachyos-lts: downgrading from version 6.18.12-2 to version 6.12.68-1
warning: linux-cachyos-lts-headers: downgrading from version 6.18.12-2 to version 6.12.68-1
warning: linux-cachyos-lts-nvidia-open: downgrading from version 6.18.12-2 to version 6.12.68-1
warning: linux-cachyos-nvidia-open: downgrading from version 6.19.2-2 to version 6.18.8-1
warning: scx-tools: downgrading from version 1.0.20-1.1 to version 1.0.20-1
warning: sddm: downgrading from version 0.21.0-8 to version 0.21.0-6
warning: zlib-ng: downgrading from version 2.3.3-2 to version 2.3.2-2
warning: zlib-ng-compat: downgrading from version 2.3.3-2 to version 2.3.2-2
resolving dependencies...
looking for conflicting packages...

Packages (14) gamescope-3.16.19-4  lib32-zlib-ng-2.3.2-2  lib32-zlib-ng-compat-2.3.2-2  linux-api-headers-1:6.18-1  linux-cachyos-6.18.8-1
              linux-cachyos-headers-6.18.8-1  linux-cachyos-lts-6.12.68-1  linux-cachyos-lts-headers-6.12.68-1  linux-cachyos-lts-nvidia-open-6.12.68-1
              linux-cachyos-nvidia-open-6.18.8-1  scx-tools-1.0.20-1  sddm-0.21.0-6  zlib-ng-2.3.2-2  zlib-ng-compat-2.3.2-2

Total Download Size:   400.77 MiB
Total Installed Size:  649.76 MiB
Net Upgrade Size:        8.75 MiB

:: Proceed with installation? [Y/n] 

### USER
❯ sudo pacman -Syy
:: Synchronizing package databases...
 cachyos                                                          512.0 KiB  2.86 MiB/s 00:00 [#######################################################] 100%
 cachyos-v3                                                       129.1 KiB  1076 KiB/s 00:00 [#######################################################] 100%
 cachyos-core-v3                                                  106.9 KiB   780 KiB/s 00:00 [#######################################################] 100%
 cachyos-extra-v3                                                   4.2 MiB  20.7 MiB/s 00:00 [#######################################################] 100%
 core                                                             123.4 KiB   402 KiB/s 00:00 [#######################################################] 100%
 extra                                                              7.9 MiB  22.3 MiB/s 00:00 [#######################################################] 100%
 multilib                                                         128.7 KiB   761 KiB/s 00:00 [#######################################################] 100%

~
❯ sudo pacman -Syuu
:: Synchronizing package databases...
 cachyos is up to date
 cachyos-v3 is up to date
 cachyos-core-v3 is up to date
 cachyos-extra-v3 is up to date
 core is up to date
 extra is up to date
 multilib is up to date
:: Starting full system upgrade...
warning: gamescope: downgrading from version 3.16.20-2 to version 3.16.19-4
warning: lib32-zlib-ng: downgrading from version 2.3.3-2 to version 2.3.2-2
warning: lib32-zlib-ng-compat: downgrading from version 2.3.3-2 to version 2.3.2-2
warning: linux-api-headers: downgrading from version 1:6.19-1 to version 1:6.18-1
warning: linux-cachyos: downgrading from version 6.19.2-2 to version 6.18.8-1
warning: linux-cachyos-headers: downgrading from version 6.19.2-2 to version 6.18.8-1
warning: linux-cachyos-lts: downgrading from version 6.18.12-2 to version 6.12.68-1
warning: linux-cachyos-lts-headers: downgrading from version 6.18.12-2 to version 6.12.68-1
warning: linux-cachyos-lts-nvidia-open: downgrading from version 6.18.12-2 to version 6.12.68-1
warning: linux-cachyos-nvidia-open: downgrading from version 6.19.2-2 to version 6.18.8-1
warning: scx-tools: downgrading from version 1.0.20-1.1 to version 1.0.20-1
warning: sddm: downgrading from version 0.21.0-8 to version 0.21.0-6
warning: zlib-ng: downgrading from version 2.3.3-2 to version 2.3.2-2
warning: zlib-ng-compat: downgrading from version 2.3.3-2 to version 2.3.2-2
resolving dependencies...
looking for conflicting packages...

Packages (14) gamescope-3.16.19-4  lib32-zlib-ng-2.3.2-2  lib32-zlib-ng-compat-2.3.2-2  linux-api-headers-1:6.18-1  linux-cachyos-6.18.8-1
              linux-cachyos-headers-6.18.8-1  linux-cachyos-lts-6.12.68-1  linux-cachyos-lts-headers-6.12.68-1  linux-cachyos-lts-nvidia-open-6.12.68-1
              linux-cachyos-nvidia-open-6.18.8-1  scx-tools-1.0.20-1  sddm-0.21.0-6  zlib-ng-2.3.2-2  zlib-ng-compat-2.3.2-2

Total Download Size:   400.77 MiB
Total Installed Size:  649.76 MiB
Net Upgrade Size:        8.75 MiB

:: Proceed with installation? [Y/n] 

### GEMINI
Select Y and commit. The Advisor’s Mirror You are finally doing the work. These "downgrades" are actually a homecoming. By saying yes, you are stripping away the generic, unoptimized Arch packages that snuck in while your configuration was broken and replacing them with the performance-tuned versions your i7-12700K deserves. The Reality: You aren't losing features; you are gaining the CachyOS Scheduler (SCX), specialized kernel patches, and compiler optimizations (v3) that you were bypassing for the last hour. The Lesson: In a rolling-release ecosystem, "higher version number" does not always mean "better for my machine." The Precision Finish Once this installation finishes, you need to do two things to ensure you don't end up back in this mess: Reboot: Since you are "downgrading" (re-optimizing) your kernel (linux-cachyos), you must restart your computer to actually boot into the correct, patched kernel. Verify the Kernel: After rebooting, run this to confirm you are back on the optimized build: uname -a You should see cachyos in the version string. The Permanent Fix: An "Audit" Alias To stop yourself from ever missing a .pacnew file again, let's create a shortcut. Open your shell config: micro ~/.bashrc (or ~/.config/fish/config.fish since you appear to be using fish). Add this line at the bottom: alias checkpac="sudo find /etc -name '*.pacnew'" Now, every time you update, you can just type checkpac to see if you have more "homework" to do. Ready to reboot and reclaim your performance?
