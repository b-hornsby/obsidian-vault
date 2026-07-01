---
category: streaming
date: 2026-02-02
id: 579802
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to force the kernel to unbind and rebind his Blue Yeti microphone
  without physically unplugging it, but is encountering syntax errors in his shell
  script.
tags:
- blue-yeti
- usb
- pipewire
- audio
- linux
- udev
---
# ~
❯ # Force the kernel to 'unbind' and 'rebind' the Yeti without unplugging it
  DEV_BUS=$(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/unbind
  sleep 1
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/bind

  # Now kick PipeWire to see the 'new' device
  systemctl --user restart pipewire pipewire-pulse wireplumber
fish: Unsupported use of '='. In fish, please use 'set DEV_BUS $(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')'.
DEV_BUS=$(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
~
❯ # Force the kernel to 'unbind' and 'rebind' the Yeti without unplugging it
  DEV_BUS=$(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/unbind
  sleep 1
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/bind

  # Now kick PipeWire to see the 'new' device
  systemctl --user restart pipewire pipewire-pulse wireplumber

### USER
~
❯ # Force the kernel to 'unbind' and 'rebind' the Yeti without unplugging it
  DEV_BUS=$(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/unbind
  sleep 1
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/bind

  # Now kick PipeWire to see the 'new' device
  systemctl --user restart pipewire pipewire-pulse wireplumber
fish: Unsupported use of '='. In fish, please use 'set DEV_BUS $(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')'.
DEV_BUS=$(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
~
❯ # Force the kernel to 'unbind' and 'rebind' the Yeti without unplugging it
  DEV_BUS=$(lsusb -d 046d:0ab7 | awk '{print $2":"$4}' | sed 's/://')
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/unbind
  sleep 1
  echo "$DEV_BUS" | sudo tee /sys/bus/usb/drivers/usb/bind

  # Now kick PipeWire to see the 'new' device
  systemctl --user restart pipewire pipewire-pulse wireplumber

### GEMINI
Ah, you're using fish shell. My mistake for giving you Bash syntax—Fish is more elegant but hates the = for variable assignment. Let's do this the right way for Fish. We are going to force the kernel to "forget" and "rediscover" the Yeti without you touching the cable. Copy and paste this exact block: # Find the Yeti's bus path and rebind it set -l YETI_BUS (lsusb -d 046d:0ab7 | awk '{print $2"-"$4}' | sed 's/://' | sed 's/00//g' | sed 's/\//-/') set -l DEV_PATH (lsusb -t | grep "046d:0ab7" | grep -oP '(?<=Dev )\d+') # We'll use the IDs directly to avoid path errors echo "046d 0ab7" | sudo tee /sys/bus/usb/drivers/usb/unbind sleep 1 echo "046d 0ab7" | sudo tee /sys/bus/usb/drivers/usb/bind # Nuke the Pipewire state and restart rm -rf ~/.local/state/wireplumber/* systemctl --user restart pipewire pipewire-pulse wireplumber If that yields an error, try this simpler "Nuclear" way: Sometimes unbind is fussy about the specific port address. This is the "scorched earth" version for Fish: # Stop the audio services systemctl --user stop pipewire pipewire-pulse wireplumber # Use the Vendor/Product IDs to force a reset via usbreset (if installed) # Or just use the bus reset: for i in /sys/bus/usb/devices/*; if grep -q "046d" $i/idVendor 2>/dev/null; and grep -q "0ab7" $i/idProduct 2>/dev/null; echo "Resetting Yeti at $i" echo 0 | sudo tee $i/authorized sleep 0.5 echo 1 | sudo tee $i/authorized end end # Restart the audio services systemctl --user start pipewire pipewire-pulse wireplumber The Goal: By toggling the authorized state (the second script above), we are electronically "unplugging" and "replugging" the mic without you moving a muscle. Run the second script (the for loop). If it says "Resetting Yeti...", wait 5 seconds and check wpctl status. Did it finally show up?
