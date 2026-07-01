---
id: 138340
source: GEMINI
date: 2026-02-03
tags: ['neofetch', 'system-info', 'cachyos', 'ascii-art']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan shared his neofetch/system stats output, likely seeking help or validation about his CachyOS setup.
---
# these are my stats if that helps: toastedmel0n@toastedPC
          .+=========================.                    -
---
-
---
-
---
-
---
-
---
--
         :++===++==================-       :++-           OS: CachyOS x86_64
        :*++====+++++=============-        .==:           Kernel: Linux 6.18.8-3-cachyos
       -*+++=====+***++==========:                        Uptime: 19 mins
      =*++++========
---
-
---
-
---
-:                         Packages: 1285 (pacman)
     =*+++++=====-                     ...                Shell: fish 4.3.3
   .+*+++++=-===:                    .=+++=:              Display (DEL41D9): 1440x2560 @ 1.78x in 27", 165 Hz [External]
  :++++=====-==:                     -*****+              Display (DELD10F): 2560x1440 in 32", 165 Hz [External] *
 :++========-=.                      .=+**+.              DE: GNOME 49.3
.+==========-.                          .                 WM: Mutter (Wayland)
 :+++++++====-                                .--==-.     WM Theme: Tahoe-Dark
  :++==========.                             :+++++++:    Theme: Tahoe-Dark [GTK2/3/4]
   .-===========.                            =*****+*+    Icons: MacTahoe-dark [GTK2/3/4]
    .-===========:                           .+*****+:    Font: Adwaita Sans (11pt) [GTK2/3/4]
      -=======++++:::::::::::::::::::::::::-:  .
---
:      Cursor: MacTahoe-dark (24px)
       :======++++====+++******************=.             Terminal: GNOME Console 49.2
        :=====+++==========++++++++++++++*-               Terminal Font: Adwaita Mono (11pt)
         .====++==============++++++++++*-                CPU: 12th Gen Intel(R) Core(TM) i7-12700K (20) @ 5.00 GHz
          .===+==================+++++++:                 GPU: NVIDIA GeForce RTX 3070 Lite Hash Rate [Discrete]
           .-=======================+++:                  Memory: 5.47 GiB / 31.08 GiB (18%)
             ..........................                   Swap: 0 B / 31.08 GiB (0%)
                                                          Disk (/): 1021.13 GiB / 1.82 TiB (55%) - btrfs
                                                          Local IP (enp6s0): 192.168.1.162/24
                                                          Locale: en_US.UTF-8

                                                                                  
                                                                                  
~

### USER
these are my stats if that helps: toastedmel0n@toastedPC
          .+=========================.                    -
---
-
---
-
---
-
---
-
---
--
         :++===++==================-       :++-           OS: CachyOS x86_64
        :*++====+++++=============-        .==:           Kernel: Linux 6.18.8-3-cachyos
       -*+++=====+***++==========:                        Uptime: 19 mins
      =*++++========
---
-
---
-
---
-:                         Packages: 1285 (pacman)
     =*+++++=====-                     ...                Shell: fish 4.3.3
   .+*+++++=-===:                    .=+++=:              Display (DEL41D9): 1440x2560 @ 1.78x in 27", 165 Hz [External]
  :++++=====-==:                     -*****+              Display (DELD10F): 2560x1440 in 32", 165 Hz [External] *
 :++========-=.                      .=+**+.              DE: GNOME 49.3
.+==========-.                          .                 WM: Mutter (Wayland)
 :+++++++====-                                .--==-.     WM Theme: Tahoe-Dark
  :++==========.                             :+++++++:    Theme: Tahoe-Dark [GTK2/3/4]
   .-===========.                            =*****+*+    Icons: MacTahoe-dark [GTK2/3/4]
    .-===========:                           .+*****+:    Font: Adwaita Sans (11pt) [GTK2/3/4]
      -=======++++:::::::::::::::::::::::::-:  .
---
:      Cursor: MacTahoe-dark (24px)
       :======++++====+++******************=.             Terminal: GNOME Console 49.2
        :=====+++==========++++++++++++++*-               Terminal Font: Adwaita Mono (11pt)
         .====++==============++++++++++*-                CPU: 12th Gen Intel(R) Core(TM) i7-12700K (20) @ 5.00 GHz
          .===+==================+++++++:                 GPU: NVIDIA GeForce RTX 3070 Lite Hash Rate [Discrete]
           .-=======================+++:                  Memory: 5.47 GiB / 31.08 GiB (18%)
             ..........................                   Swap: 0 B / 31.08 GiB (0%)
                                                          Disk (/): 1021.13 GiB / 1.82 TiB (55%) - btrfs
                                                          Local IP (enp6s0): 192.168.1.162/24
                                                          Locale: en_US.UTF-8

                                                                                  
                                                                                  
~

### GEMINI
You have an NVIDIA RTX 3070 and you're running GNOME 49 (Wayland) on CachyOS. The flickering you're seeing in the Browser Source is the "NVIDIA-Wayland Flicker." It happens because Chromium (the engine behind the Browser Source) and the Wayland compositor are arguing over who gets to finish "drawing" the frame first. Switching to KDE won't magically solve this because both desktops use Wayland by default now, and the issue is at the driver/protocol level, not the desktop interface level. The Brutal Plan to Stop the Flicker 1. The "10-Second" Fix (Highest Success Rate) NVIDIA + Wayland + Hardware Acceleration is the recipe for flickers. Turn off the acceleration for just the browser. Open OBS. Go to Settings -> Advanced. Scroll down to the Sources section. Uncheck "Enable Browser Source Hardware Acceleration." Restart OBS. Since a music overlay is just a tiny bit of text and an image, your i7-12700K won't even feel the load. This is the smartest move. 2. The "Wayland is Too New" Fix (Zero Flicker Guaranteed) If you want to keep hardware acceleration on for other things but hate the flicker, stop using Wayland for your stream sessions. Log out of CachyOS. At the login screen, click your name. Click the gear icon in the bottom right corner. Select GNOME on Xorg. Log in. X11 is "old," but it is rock-solid for NVIDIA. There is zero flickering on X11. 3. The "CachyOS Optimization" Check You are on Kernel 6.18, which is very recent. Ensure your NVIDIA drivers are actually the latest (560+). Open your terminal. Run nvidia-smi. If your version is lower than 555, you are missing "Explicit Sync"—the technology designed to stop this exact flickering. Update your system: sudo pacman -Syu. Why KDE isn't the Answer If you hop to KDE, you’ll spend two hours setting up your desktop only to find that Kwin (KDE's compositor) has its own set of flickering issues with NVIDIA on Wayland. You’re trading one headache for another. Stop "hoping" and start "fixing": Step 1: Disable Browser Hardware Acceleration in OBS. Step 2: If it still flickers, log into an Xorg session. Did unchecking "Hardware Acceleration" in the OBS Advanced settings work? That usually kills the flicker instantly for 90% of Linux streamers.
