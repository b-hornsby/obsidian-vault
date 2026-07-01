---
category: streaming
date: 2026-02-02
id: 604416
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to rebind his Blue Yeti USB microphone by finding its bus
  path and using `tee` to unbind and bind it, but is encountering errors indicating
  the device path is not found.
tags:
- blue-yeti
- usb
- pipewire
- audio
- linux
- udev
---
# ❯ # Find the Yeti's bus path and rebind it
  set -l YETI_BUS (lsusb -d 046d:0ab7 | awk '{print $2"-"$4}' | sed 's/://' | sed 's/00//g' | sed 's/\//-/')
  set -l DEV_PATH (lsusb -t | grep "046d:0ab7" | grep -oP '(?<=Dev )\d+')

  # We'll use the IDs directly to avoid path errors
  echo "046d 0ab7" | sudo tee /sys/bus/usb/drivers/usb/unbind
  sleep 1
  echo "046d 0ab7" | sudo tee /sys/bus/usb/drivers/usb/bind

  # Nuke the Pipewire state and restart
  rm -rf ~/.local/state/wireplumber/*
  systemctl --user restart pipewire pipewire-pulse wireplumber
[sudo] password for toastedmel0n: 
046d 0ab7
tee: /sys/bus/usb/drivers/usb/unbind: No such device
046d 0ab7
tee: /sys/bus/usb/drivers/usb/bind: No such device

### USER
❯ # Find the Yeti's bus path and rebind it
  set -l YETI_BUS (lsusb -d 046d:0ab7 | awk '{print $2"-"$4}' | sed 's/://' | sed 's/00//g' | sed 's/\//-/')
  set -l DEV_PATH (lsusb -t | grep "046d:0ab7" | grep -oP '(?<=Dev )\d+')

  # We'll use the IDs directly to avoid path errors
  echo "046d 0ab7" | sudo tee /sys/bus/usb/drivers/usb/unbind
  sleep 1
  echo "046d 0ab7" | sudo tee /sys/bus/usb/drivers/usb/bind

  # Nuke the Pipewire state and restart
  rm -rf ~/.local/state/wireplumber/*
  systemctl --user restart pipewire pipewire-pulse wireplumber
[sudo] password for toastedmel0n: 
046d 0ab7
tee: /sys/bus/usb/drivers/usb/unbind: No such device
046d 0ab7
tee: /sys/bus/usb/drivers/usb/bind: No such device

### GEMINI
The No such device error confirms that the kernel isn't letting us use the Vendor/Product IDs for the unbind file—it wants the specific Bus Address (like 1-1.2). Because we are on Fish, let's use a much more direct method to "soft-reboot" the USB port itself. We’re going to find the Yeti’s physical path and toggle its authorization. This is the closest thing to a physical unplug/replug you can do via code. The "Electronic Replug" (Fish Version) Copy and paste this into your terminal: for dev in /sys/bus/usb/devices/* if test -f "$dev/idVendor"; and test -f "$dev/idProduct" set -l vid (cat "$dev/idVendor") set -l pid (cat "$dev/idProduct") if test "$vid" = "046d"; and test "$pid" = "0ab7" echo "Found Yeti at $dev. Resetting..." echo 0 | sudo tee "$dev/authorized" sleep 2 echo 1 | sudo tee "$dev/authorized" echo "Reset complete." end end end If that says "Reset complete," do this immediately: systemctl --user restart pipewire pipewire-pulse wireplumber wpctl status | grep -i "Yeti" Why this is happening: If this command works, it confirms that your Yeti is failing the initial power-on handshake when CachyOS boots. The kernel sees the device (so lsusb works), but the "Descriptor" is stuck. By toggling authorized, you force the kernel to re-initialize the device from scratch. If the Yeti shows up after this: We need to add this "reset" logic to your boot sequence because your Yeti's hardware is too slow to respond to the high-speed initialization of your CachyOS kernel. Did the "Reset complete" message appear? And more importantly, is the Yeti showing up in wpctl status now?
