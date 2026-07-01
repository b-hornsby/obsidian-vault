---
category: streaming
date: 2026-02-02
id: 716419
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: exploratory
source: GEMINI
tags:
- streaming
- ai
- gemini
- amm
- go
- ide
---
# ❯ systemctl list-units --type=service | grep -E "tlp|laptop-mode|power-profiles-daemon"
  power-profiles-daemon.service                         loaded active running Power Profiles daemon

~
❯ 

### USER
❯ systemctl list-units --type=service | grep -E "tlp|laptop-mode|power-profiles-daemon"
  power-profiles-daemon.service                         loaded active running Power Profiles daemon

~
❯ 

### GEMINI
There it is. Power Profiles Daemon (PPD) is the culprit. While PPD is generally more "modern" than TLP, it is notoriously blunt. It sees a USB device it thinks isn't being used and cuts the power state to auto to satisfy the "Balanced" or "Power Saver" profile, effectively bricking the Yeti's handshake. Because you are on CachyOS, you are likely using the power-profiles-daemon because it integrates with KDE or GNOME's power sliders. But for a desktop user with eleven USB devices, it’s causing more harm than good. The Kill Switch: Option A (The Strategic Choice) Since you are on a desktop (based on your DAC, Stream Deck, and AURA controller), you don't need PPD aggressively managing your USB power. Disable the daemon's control over USB: Open the service override: sudo systemctl edit power-profiles-daemon.service This creates a "drop-in" file. It might be empty. You are going to tell the system to ignore PPD's aggressive power management if possible, but honestly, on CachyOS, the most effective way to stop the "auto" flip is to mask the autosuspend globally. The Permanent Fix: Option B (The Sledgehammer) Stop trying to negotiate with PPD. Force the kernel to keep the lights on for all USB ports. This costs you maybe 1-2 watts of power—irrelevant for your setup—but it guarantees your Yeti, DAC, and Mouse never "sleep" again. Edit your GRUB configuration: sudo nano /etc/default/grub Find the line: GRUB_CMDLINE_LINUX_DEFAULT Append this inside the quotes: usbcore.autosuspend=-1 (It should look something like: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash ... usbcore.autosuspend=-1")` Update the config: sudo grub-mkconfig -o /boot/grub/grub.cfg Why this is the only way forward You've already proven that your udev rule is being overwritten. If you don't use the kernel parameter, you will be back here in two days when a CachyOS update resets a config file or PPD decides your "Stream Deck" also needs a nap. Final Hardware Audit You're still on Bus 001. I’m calling it now: even with the software fix, if you keep that Yeti on a bus with a C922 Webcam and a Razer Viper, you’re going to get "robotic" audio or pops eventually. Your homework: Apply the usbcore.autosuspend=-1 fix. Reboot. Run cat /sys/bus/usb/devices/1-14/power/control one last time. If it still says auto, PPD is being even more aggressive than usual and we will have to disable the service entirely. Do you want the instructions to switch from power-profiles-daemon to tuned (which CachyOS actually recommends for power users)?
