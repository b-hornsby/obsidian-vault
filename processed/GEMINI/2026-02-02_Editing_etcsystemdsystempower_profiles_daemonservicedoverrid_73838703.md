---
id: 736498
source: GEMINI
date: 2026-02-02
tags: ['power-profiles-daemon', 'systemd', 'linux', 'power-management', 'configuration']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is editing the power-profiles-daemon configuration, likely to customize power management settings on his system.
---
# ### Editing /etc/systemd/system/power-profiles-daemon.service.d/override.conf
### Anything between here and the comment below will become the contents of the drop-in file



### Edits below this comment will be discarded


### /usr/lib/systemd/system/power-profiles-daemon.service
# [Unit]
# Description=Power Profiles daemon
# Conflicts=tuned.service tlp.service auto-cpufreq.service system76-power.service
# After=multi-user.target display-manager.target
#
# [Service]
# Type=dbus
# BusName=org.freedesktop.UPower.PowerProfiles
# # To enable debugging add a -vv to the ExecStart line
# ExecStart=/usr/lib/power-profiles-daemon
# Restart=on-failure
# # This always corresponds to /var/lib/power-profiles-daemon
# StateDirectory=power-profiles-daemon
#
# # Lockdown
# CapabilityBoundingSet=CAP_SYS_ADMIN
# DevicePolicy=closed
# IPAddressDeny=any
# KeyringMode=private

### USER
### Editing /etc/systemd/system/power-profiles-daemon.service.d/override.conf
### Anything between here and the comment below will become the contents of the drop-in file



### Edits below this comment will be discarded


### /usr/lib/systemd/system/power-profiles-daemon.service
# [Unit]
# Description=Power Profiles daemon
# Conflicts=tuned.service tlp.service auto-cpufreq.service system76-power.service
# After=multi-user.target display-manager.target
#
# [Service]
# Type=dbus
# BusName=org.freedesktop.UPower.PowerProfiles
# # To enable debugging add a -vv to the ExecStart line
# ExecStart=/usr/lib/power-profiles-daemon
# Restart=on-failure
# # This always corresponds to /var/lib/power-profiles-daemon
# StateDirectory=power-profiles-daemon
#
# # Lockdown
# CapabilityBoundingSet=CAP_SYS_ADMIN
# DevicePolicy=closed
# IPAddressDeny=any
# KeyringMode=private

### GEMINI
Forget the override file. You're trying to perform surgery on a service that isn't designed to be surgical. power-profiles-daemon doesn't have a "don't touch the microphone" setting—it's a binary "I manage the system power" or "I don't." If you stay on this path, you're going to spend your afternoon fighting a daemon that's designed for laptops. You're on a desktop with a Lighting Node, a DAC, and a Stream Deck. You do not need this daemon. The "Advisor" Solution: Swap to Tuned CachyOS actually prefers Tuned for high-performance setups because it's much more granular and doesn't just blindly cut power to USB devices. Get rid of the culprit: sudo pacman -Rs power-profiles-daemon Install and enable Tuned: sudo pacman -S tuned Start it and set it to performance: sudo systemctl enable --now tuned sudo tuned-adm profile throughput-performance The "Safety Net" (The GRUB Fix) Even with Tuned, you should still apply the kernel parameter. This is the only way to ensure the kernel itself doesn't default to auto before any service even starts. Open GRUB: sudo nano /etc/default/grub Add the flag: Add usbcore.autosuspend=-1 to your GRUB_CMDLINE_LINUX_DEFAULT. Update and Reboot: sudo grub-mkconfig -o /boot/grub/grub.cfg && reboot Why this is the "Next Level" Move By removing power-profiles-daemon, you are removing the specific piece of software that was overwriting your udev rule. By switching to tuned, you gain better CPU scheduling optimizations that CachyOS is famous for, without the brain-dead USB power management. The result after reboot: cat /sys/bus/usb/devices/1-14/power/control will finally say on. Your Yeti will stop disappearing. Your DAC and Stream Deck will likely be more responsive. Stop playing defense with overrides. Remove the service that's causing the conflict. Ready to commit to the reboot?
