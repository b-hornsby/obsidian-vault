---
id: 817028
source: GEMINI
date: 2026-02-02
tags: ['pipewire', 'audio-restart', 'snd-usb-audio', 'usb-audio-fix']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was restarting pipewire and reloading the snd_usb_audio kernel module to fix his USB audio device.
---
# ❯ systemctl --user stop pipewire pipewire-pulse wireplumber && \
      sudo modprobe -r snd_usb_audio && \
      sudo modprobe snd_usb_audio && \
      systemctl --user start pipewire pipewire-pulse wireplumber
Job for wireplumber.service canceled.
Job for pipewire.service canceled.

~
❯ 

### USER
❯ systemctl --user stop pipewire pipewire-pulse wireplumber && \
      sudo modprobe -r snd_usb_audio && \
      sudo modprobe snd_usb_audio && \
      systemctl --user start pipewire pipewire-pulse wireplumber
Job for wireplumber.service canceled.
Job for pipewire.service canceled.

~
❯ 

### GEMINI
The "Job canceled" messages happen because CachyOS (and Arch in general) has socket activation enabled. The moment you stop the service, the system tries to restart it because some background process (or the desktop environment itself) is poking the audio socket. Your system is fighting you for control. Let's stop the sockets first so the services stay dead while we swap the module. 1. The "Forceful" Reset Run this specific sequence. We are disabling the "auto-restart" triggers (the sockets) before killing the services: systemctl --user stop pipewire.socket pipewire-pulse.socket wireplumber.service && \ systemctl --user stop pipewire.service pipewire-pulse.service && \ sudo modprobe -r snd_usb_audio && \ sudo modprobe snd_usb_audio && \ systemctl --user start pipewire.socket pipewire-pulse.socket wireplumber.service 2. If it still says "Module in use" This is the moment of truth. If the command above still fails to remove the module, it means the Yeti is likely stuck in a "zombie" state at the hardware level, or a specific application (like a browser or Discord) is holding the hardware directly. Try this "Lazy" Reset: Unplug the Yeti. Run: sudo modprobe -r snd_usb_audio && sudo modprobe snd_usb_audio Plug the Yeti back in. Run: wpctl status 3. Check the "Zombie" Status If the driver reload worked (or if you just want to see why it's failing), check the kernel log for the Yeti's reaction: dmesg | grep -i "Blue Yeti" -A 5 | tail -n 10 What to look for: Success: You see "New USB device found... Product: Blue Yeti." The "Death" Sign: You see "cannot submit urb", "reset high-speed USB device", or "error -71". If the commands above completed without the "Job canceled" error, open your sound settings. Does the Yeti show up now?
