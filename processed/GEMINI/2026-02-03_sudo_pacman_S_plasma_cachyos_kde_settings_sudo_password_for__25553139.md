---
id: 929280
source: GEMINI
date: 2026-02-03
tags: ['kde', 'plasma', 'cachyos', 'pacman', 'desktop-environment']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is installing KDE Plasma and CachyOS KDE settings via pacman and is being prompted to select packages.
---
# ❯ sudo pacman -S plasma cachyos-kde-settings
[sudo] password for toastedmel0n: 
:: There are 64 members in group plasma:
:: Repository cachyos-extra-v3
   1) aurorae  2) bluedevil  3) breeze  4) breeze-plymouth  5) discover  6) drkonqi  7) flatpak-kcm
   8) kactivitymanagerd  9) kde-cli-tools  10) kde-gtk-config  11) kdecoration  12) kdeplasma-addons  13) kgamma
   14) kglobalacceld  15) kinfocenter  16) kmenuedit  17) knighttime  18) kpipewire  19) krdp  20) kscreen
   21) kscreenlocker  22) ksshaskpass  23) ksystemstats  24) kwallet-pam  25) kwayland  26) kwin  27) kwin-x11
   28) kwrited  29) layer-shell-qt  30) libkscreen  31) libplasma  32) milou  33) oxygen  34) plasma-activities
   35) plasma-activities-stats  36) plasma-browser-integration  37) plasma-desktop  38) plasma-disks
   39) plasma-firewall  40) plasma-integration  41) plasma-nm  42) plasma-pa  43) plasma-sdk  44) plasma-systemmonitor
   45) plasma-thunderbolt  46) plasma-vault  47) plasma-welcome  48) plasma-workspace  49) plasma5support
   50) plymouth-kcm  51) polkit-kde-agent  52) powerdevil  53) print-manager  54) qqc2-breeze-style  55) sddm-kcm
   56) spectacle  57) systemsettings  58) wacomtablet  59) xdg-desktop-portal-kde
:: Repository extra
   60) breeze-gtk  61) libksysguard  62) ocean-sound-theme  63) oxygen-sounds  64) plasma-workspace-wallpapers

Enter a selection (default=all): 

### USER
❯ sudo pacman -S plasma cachyos-kde-settings
[sudo] password for toastedmel0n: 
:: There are 64 members in group plasma:
:: Repository cachyos-extra-v3
   1) aurorae  2) bluedevil  3) breeze  4) breeze-plymouth  5) discover  6) drkonqi  7) flatpak-kcm
   8) kactivitymanagerd  9) kde-cli-tools  10) kde-gtk-config  11) kdecoration  12) kdeplasma-addons  13) kgamma
   14) kglobalacceld  15) kinfocenter  16) kmenuedit  17) knighttime  18) kpipewire  19) krdp  20) kscreen
   21) kscreenlocker  22) ksshaskpass  23) ksystemstats  24) kwallet-pam  25) kwayland  26) kwin  27) kwin-x11
   28) kwrited  29) layer-shell-qt  30) libkscreen  31) libplasma  32) milou  33) oxygen  34) plasma-activities
   35) plasma-activities-stats  36) plasma-browser-integration  37) plasma-desktop  38) plasma-disks
   39) plasma-firewall  40) plasma-integration  41) plasma-nm  42) plasma-pa  43) plasma-sdk  44) plasma-systemmonitor
   45) plasma-thunderbolt  46) plasma-vault  47) plasma-welcome  48) plasma-workspace  49) plasma5support
   50) plymouth-kcm  51) polkit-kde-agent  52) powerdevil  53) print-manager  54) qqc2-breeze-style  55) sddm-kcm
   56) spectacle  57) systemsettings  58) wacomtablet  59) xdg-desktop-portal-kde
:: Repository extra
   60) breeze-gtk  61) libksysguard  62) ocean-sound-theme  63) oxygen-sounds  64) plasma-workspace-wallpapers

Enter a selection (default=all): 

### GEMINI
Press Enter (for the default "all" selection). On CachyOS, when you install the plasma group, you want every one of those 64 members to ensure the desktop functions exactly like the "flagship" experience they intend. Missing even one (like kscreen or plasma-nm) will result in your monitors not saving settings or your Wi-Fi icon disappearing. The Critical "Post-Install" Steps Once the installation finishes, do not just reboot. We have to tell your computer to stop using the GNOME login screen and start using the new KDE one. Switch the Login Manager: CachyOS recently moved away from SDDM and now uses the Plasma Login Manager for its 2026 releases. Run these commands: sudo systemctl disable gdm sudo systemctl enable plasma-login-manager (If that returns an error, it means you're on a slightly older build—use sudo systemctl enable sddm instead). Reboot: sudo reboot Your New "Streaming Ready" Setup When you land at the new login screen, look for a small icon or dropdown (usually in the bottom-left or center). Select "Plasma (X11)": Since Wayland was the source of all your flickering, start here. X11 is the "old reliable" that handles OBS and NVIDIA 30-series cards perfectly. Select "Plasma (Wayland)": If you want to try Wayland again, KDE’s version is much better at preventing the "strobe light" effect than GNOME was, especially since you already disabled GSP and locked your clocks. The Advisor's Truth You just made the smartest move for your stream. GNOME is beautiful, but it's a locked-down vault. KDE is a workshop; if something flickers, KDE actually gives you the tools to fix it without having to hack your kernel every time. Is the installation finished? Once you reboot and get into the KDE desktop, open OBS. You’ll notice the flickering is likely gone immediately on X11, and we can tune the Wayland session from there if you prefer it.
