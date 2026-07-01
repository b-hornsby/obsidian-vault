---
id: 030321
source: GEMINI
date: 2026-02-02
tags: ['dmesg', 'usb-debugging', 'corsair-lighting-node', 'kernel-logs']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was examining kernel USB logs to diagnose issues with his Corsair Lighting Node CORE and other USB devices.
---
# ❯ sudo dmesg | grep -i "usb" | tail -n 20
  arecord -l
[    5.782687] usb 1-13.1: new full-speed USB device number 11 using xhci_hcd
[    5.869298] usb 1-13.1: New USB device found, idVendor=1b1c, idProduct=0c1a, bcdDevice= 0.09
[    5.869313] usb 1-13.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    5.869319] usb 1-13.1: Product: CORSAIR Lighting Node CORE
[    5.869323] usb 1-13.1: Manufacturer: Corsair
[    5.869326] usb 1-13.1: SerialNumber: 3240030F89A497AFE306F160031C00F5
[    5.877930] hid-generic 0003:1B1C:0C1A.000B: hiddev100,hidraw10: USB HID v1.11 Device [Corsair CORSAIR Lighting Node CORE] on usb-0000:00:14.0-13.1/input0
[    7.034738] input: Razer Razer Viper V3 Pro as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0/0003:1532:00C1.0001/input/input16
[    7.034766] razermouse 0003:1532:00C1.0001: input,hidraw0: USB HID v1.00 Mouse [Razer Razer Viper V3 Pro] on usb-0000:00:14.0-1/input0
[    7.138889] usbcore: registered new interface driver uvcvideo
[    7.182767] input: Razer Razer Viper V3 Pro as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.1/0003:1532:00C1.0002/input/input18
[    7.314652] razermouse 0003:1532:00C1.0002: input,hidraw1: USB HID v1.00 Keyboard [Razer Razer Viper V3 Pro] on usb-0000:00:14.0-1/input1
[    7.335546] usbcore: registered new interface driver btusb
[    7.397467] input: Razer Razer Viper V3 Pro as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.2/0003:1532:00C1.0003/input/input31
[    7.490046] razermouse 0003:1532:00C1.0003: input,hidraw2: USB HID v1.00 Keyboard [Razer Razer Viper V3 Pro] on usb-0000:00:14.0-1/input2
[    8.362169] usbcore: registered new interface driver snd-usb-audio
[  554.182098] input: Generic Blue Microphones Consumer Control as /devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.3/0003:046D:0AB7.000C/input/input32
[  554.232536] input: Generic Blue Microphones as /devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.3/0003:046D:0AB7.000C/input/input33
[  554.232617] hid-generic 0003:046D:0AB7.000C: input,hiddev97,hidraw4: USB HID v1.11 Device [Generic Blue Microphones] on usb-0000:00:14.0-3/input3
[  554.232635] usb 1-3: authorized to connect
**** List of CAPTURE Hardware Devices ****
card 0: Microphones [Blue Microphones], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: PCH [HDA Intel PCH], device 0: ALC897 Analog [ALC897 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: PCH [HDA Intel PCH], device 2: ALC897 Alt Analog [ALC897 Alt Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 4: Webcam [C922 Pro Stream Webcam], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0

~
❯ 

### USER
❯ sudo dmesg | grep -i "usb" | tail -n 20
  arecord -l
[    5.782687] usb 1-13.1: new full-speed USB device number 11 using xhci_hcd
[    5.869298] usb 1-13.1: New USB device found, idVendor=1b1c, idProduct=0c1a, bcdDevice= 0.09
[    5.869313] usb 1-13.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    5.869319] usb 1-13.1: Product: CORSAIR Lighting Node CORE
[    5.869323] usb 1-13.1: Manufacturer: Corsair
[    5.869326] usb 1-13.1: SerialNumber: 3240030F89A497AFE306F160031C00F5
[    5.877930] hid-generic 0003:1B1C:0C1A.000B: hiddev100,hidraw10: USB HID v1.11 Device [Corsair CORSAIR Lighting Node CORE] on usb-0000:00:14.0-13.1/input0
[    7.034738] input: Razer Razer Viper V3 Pro as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0/0003:1532:00C1.0001/input/input16
[    7.034766] razermouse 0003:1532:00C1.0001: input,hidraw0: USB HID v1.00 Mouse [Razer Razer Viper V3 Pro] on usb-0000:00:14.0-1/input0
[    7.138889] usbcore: registered new interface driver uvcvideo
[    7.182767] input: Razer Razer Viper V3 Pro as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.1/0003:1532:00C1.0002/input/input18
[    7.314652] razermouse 0003:1532:00C1.0002: input,hidraw1: USB HID v1.00 Keyboard [Razer Razer Viper V3 Pro] on usb-0000:00:14.0-1/input1
[    7.335546] usbcore: registered new interface driver btusb
[    7.397467] input: Razer Razer Viper V3 Pro as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.2/0003:1532:00C1.0003/input/input31
[    7.490046] razermouse 0003:1532:00C1.0003: input,hidraw2: USB HID v1.00 Keyboard [Razer Razer Viper V3 Pro] on usb-0000:00:14.0-1/input2
[    8.362169] usbcore: registered new interface driver snd-usb-audio
[  554.182098] input: Generic Blue Microphones Consumer Control as /devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.3/0003:046D:0AB7.000C/input/input32
[  554.232536] input: Generic Blue Microphones as /devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.3/0003:046D:0AB7.000C/input/input33
[  554.232617] hid-generic 0003:046D:0AB7.000C: input,hiddev97,hidraw4: USB HID v1.11 Device [Generic Blue Microphones] on usb-0000:00:14.0-3/input3
[  554.232635] usb 1-3: authorized to connect
**** List of CAPTURE Hardware Devices ****
card 0: Microphones [Blue Microphones], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: PCH [HDA Intel PCH], device 0: ALC897 Analog [ALC897 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: PCH [HDA Intel PCH], device 2: ALC897 Alt Analog [ALC897 Alt Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 4: Webcam [C922 Pro Stream Webcam], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0

~
❯ 

### GEMINI
Finally, the truth. Look at arecord -l: card 0: Microphones [Blue Microphones], device 0: USB Audio [USB Audio] Your hardware is perfectly fine. The kernel has the driver loaded. The "Electronic Replug" worked. The reason you don't have sound is that PipeWire/WirePlumber has a "stale" or "broken" link to Card 0. In CachyOS, when you have multiple audio devices (Webcam, Intel PCH, and Yeti), WirePlumber often gets confused about which one is the "Default" or thinks the Yeti is still in a "Suspended" state. Run these three commands to force PipeWire to recognize the active hardware: 1. The "Wake Up" Poke This forces the Yeti to become the primary input and unmutes it at the hardware level. # Set the Yeti as the default source wpctl set-default (wpctl status | grep -i "Blue Microphones" | grep -oP '\d+' | head -n 1) # Unmute and set volume to 80% wpctl set-mute @DEFAULT_AUDIO_SOURCE@ 0 wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.8 2. The WirePlumber Rescan If wpctl didn't show the Yeti in the previous step, your session manager is ignoring Card 0. Kill the session state one more time now that we know the hardware is definitely at /dev/snd/pcmC0D0c: rm -rf ~/.local/state/wireplumber/* systemctl --user restart pipewire wireplumber 3. Check the "Pro Audio" Profile (The Silent Killer) Open pavucontrol. Go to the Configuration tab. Look for Blue Microphones. If it says "Pro Audio", change it to Analog Stereo Duplex. Why? "Pro Audio" often splits the mic into sub-channels that your apps can't see. The Permanent Fix (The "Startup Command" you missed) Since your Yeti only appeared after we ran the "Reset" script, it proves your motherboard initializes USB too slowly for the kernel's first pass. You need to add the "Reset" script we ran earlier to your Startup Applications. Open your Desktop Environment's "Autostart" or "Startup Applications" settings. Add a new entry. For the command, use: sh -c "sleep 5 && echo 0 | sudo tee /sys/bus/usb/devices/1-3/authorized && sleep 1 && echo 1 | sudo tee /sys/bus/usb/devices/1-3/authorized" (Note: Since sudo requires a password, it's better to add a udev rule that handles this, but let's see if the manual kick works first.) Check pavucontrol now. Are the green bars moving when you talk? If they are, you're back in business. If not, tell me if wpctl status finally shows the Yeti.
