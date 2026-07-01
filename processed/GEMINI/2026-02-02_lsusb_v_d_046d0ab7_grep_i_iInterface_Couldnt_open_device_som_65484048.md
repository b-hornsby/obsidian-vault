---
id: 851457
source: GEMINI
date: 2026-02-02
tags: ['usb-debugging', 'blue-yeti', 'device-descriptors']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was querying USB descriptor information for his Blue Yeti microphone (046d:0ab7) to diagnose a device recognition issue.
---
# ❯ lsusb -v -d 046d:0ab7 | grep -i "iInterface"
Couldn't open device, some information will be missing
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              0 

~
❯ 

### USER
❯ lsusb -v -d 046d:0ab7 | grep -i "iInterface"
Couldn't open device, some information will be missing
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              5 
      iInterface              0 

~
❯ 

### GEMINI
The "Couldn't open device" warning is just a permissions thing (needs sudo), but the output confirms the system sees the interfaces. The Yeti is connected, it's powered, and the kernel is talking to it. If you still don't have green bars moving, we are down to a Routing or Mute issue in PipeWire. Run this specific command to see exactly how PipeWire is treating the Yeti's input: pw-link -i -l | grep -i "Yeti" The Final "Software" Hurdles: The "Pro Audio" Trap (Again): On Arch/CachyOS, if the Yeti is set to "Pro Audio" in your settings, it creates separate nodes for every single channel. Most apps (Discord, Browser) will see this and just give up, resulting in "no audio." Fix: Open pavucontrol, go to Configuration, and ensure it is Analog Stereo Duplex. If it's on Pro Audio, change it. The ALSA Hardware Mute: Sometimes the hardware mixer is muted even if the software says 100%. Run alsamixer. Press F6, select the Yeti. Press F4 to see "Capture." If you see MM under the bar, press Space or M to turn it into CAPTUR (red). The Strategy: You've cleaned up the udev rules, so the "disappearing" act should be over. Now we just need to confirm it's not being silenced by the mixer stack. Do this: Open pavucontrol to the Input Devices tab. Scratch the grill of the mic. Do you see the blue/gray bar move at all? If yes: The mic is working; your specific app (Discord/OBS) just needs to be pointed to the right device. If no: Run the alsamixer check I mentioned above. Is the bar moving in pavucontrol? If not, tell me what alsamixer shows for the "Capture" column.
