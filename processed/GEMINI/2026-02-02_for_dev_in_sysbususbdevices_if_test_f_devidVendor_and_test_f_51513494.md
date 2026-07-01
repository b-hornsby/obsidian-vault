---
id: 662436
source: GEMINI
date: 2026-02-02
tags: ['usb-reset', 'blue-yeti', 'fish-script', 'cachyos', 'audio-troubleshooting']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan ran a Fish shell script to reset his Blue Yeti USB device by toggling its authorized state, though audio pickup was not confirmed afterward.
---
# ❯ for dev in /sys/bus/usb/devices/*
      if test -f "$dev/idVendor"; and test -f "$dev/idProduct"
          set -l vid (cat "$dev/idVendor")
          set -l pid (cat "$dev/idProduct")
          if test "$vid" = "046d"; and test "$pid" = "0ab7"
              echo "Found Yeti at $dev. Resetting..."
              echo 0 | sudo tee "$dev/authorized"
              sleep 2
              echo 1 | sudo tee "$dev/authorized"
              echo "Reset complete."
          end
      end
  end
Found Yeti at /sys/bus/usb/devices/1-3. Resetting...
0
1
Reset complete.

~
❯ wpctl status | grep -i "Yeti"

~
❯ 

### USER
❯ for dev in /sys/bus/usb/devices/*
      if test -f "$dev/idVendor"; and test -f "$dev/idProduct"
          set -l vid (cat "$dev/idVendor")
          set -l pid (cat "$dev/idProduct")
          if test "$vid" = "046d"; and test "$pid" = "0ab7"
              echo "Found Yeti at $dev. Resetting..."
              echo 0 | sudo tee "$dev/authorized"
              sleep 2
              echo 1 | sudo tee "$dev/authorized"
              echo "Reset complete."
          end
      end
  end
Found Yeti at /sys/bus/usb/devices/1-3. Resetting...
0
1
Reset complete.

~
❯ wpctl status | grep -i "Yeti"

~
❯ 

### GEMINI
Still nothing. Even after a forced electronic reset, PipeWire is refusing to map the Yeti into the audio stack. This means the kernel sees the "USB device" but the snd_usb_audio driver is failing to bind to it or is crashing silently. Let's look at the "black box" of the kernel to see the exact error that happened when we ran that reset. 1. The Evidence Run this now: dmesg | grep -i "usb" | tail -n 20 What we are looking for: New USB device found, idVendor=046d, idProduct=0ab7 (Good) config 1 interface 0 altsetting 0 bulk endpoint 0x82 has invalid maxpacket 64 (Bad - hardware failure) error -110 or error -71 (Physical connection/voltage issue) 2. The "Nuclear" ALSA Force Sometimes PipeWire won't see it because ALSA (the base layer) has it locked or misconfigured. Let's see if ALSA can see the hardware directly: arecord -l If the Yeti is NOT listed here: The driver didn't load. If the Yeti IS listed: PipeWire is definitely the culprit. 3. The "CachyOS" Performance Conflict CachyOS uses pipewire-launcher or specific session managers. If you have any other audio hardware (Stream Deck, OpenRGB-synced gear), they might be competing for the same USB bandwidth/interrupts. Try this "Blind" Fix: Since the reset "worked" at the USB level but didn't show up in wpctl, force-load the kernel module with a specific "delayed" parameter: sudo modprobe -r snd_usb_audio sudo modprobe snd_usb_audio index=1,2 model=yeti systemctl --user restart pipewire wireplumber Bottom Line: If arecord -l shows nothing, we are fighting a dying USB port or a bad cable that provides enough power for the "ID" to show up, but not enough for the "Audio Data" to stream. What does arecord -l say? If it's not in that list, no software command on earth will make it record.
