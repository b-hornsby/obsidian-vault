---
category: homelab
date: 2026-02-02
id: 179431
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is trying to set his Blue Yeti as the default audio source via PipeWire/wpctl
  on CachyOS but getting 'Node not found'.
tags:
- blue-yeti
- pipewire
- audio-source
- wpctl
- cachyos
---
# ❯ # Set the Yeti as the default source
  wpctl set-default (wpctl status | grep -i "Blue Microphones" | grep -oP '\d+' | head -n 1)

  # Unmute and set volume to 80%
  wpctl set-mute @DEFAULT_AUDIO_SOURCE@ 0
  wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.8
Node '47' not found

~
❯ 

### USER
❯ # Set the Yeti as the default source
  wpctl set-default (wpctl status | grep -i "Blue Microphones" | grep -oP '\d+' | head -n 1)

  # Unmute and set volume to 80%
  wpctl set-mute @DEFAULT_AUDIO_SOURCE@ 0
  wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.8
Node '47' not found

~
❯ 

### GEMINI
The Node '47' not found error means PipeWire assigned an ID to the Yeti, but by the time the command ran, the node vanished or wasn't fully "initialized." This confirms that on CachyOS, your Yeti and PipeWire are having a timing race condition. PipeWire sees the hardware, tries to build a map, and then the map collapses. Let's bypass the "search" and force the configuration. 1. The Direct Hardware Binding Since we know the Yeti is Card 0, we are going to tell PipeWire to forget the dynamic IDs and look at the hardware index. Run this: # Force PipeWire to see the Yeti card directly wpctl status | grep "Blue Microphones" # If it shows an ID (like 47, 48, etc.), use it manually: # For example, if it's 47: wpctl set-profile 47 1 2. The "Profile" Nuclear Reset The most common reason a node "disappears" immediately is that it's stuck in a "Pro Audio" profile that has no valid routes. Open pavucontrol. Go to the Configuration tab. Find Blue Microphones. Even if it says Analog Stereo Duplex, click the dropdown, change it to Off, wait 2 seconds, and change it back to Analog Stereo Duplex. 3. Check for "Suspending" in WirePlumber WirePlumber might be suspending the node because it thinks it's idle/broken. Run: wpctl inspect @DEFAULT_AUDIO_SOURCE@ | grep state If it says state: suspended, it won't pick up audio. The Permanent Strategic Fix Since your Yeti is consistently failing to initialize at boot but exists as Card 0, you need to automate the "kick" you gave it earlier. Do this to fix it for every future boot: We will create a script that waits for the desktop to load, then forces the Yeti to wake up. Create the script: nano ~/.yeti-fix.sh Paste this in: #!/bin/bash sleep 5 # Toggle authorization to force a clean USB handshake echo 0 | sudo tee /sys/bus/usb/devices/1-3/authorized sleep 1 echo 1 | sudo tee /sys/bus/usb/devices/1-3/authorized sleep 2 # Restart the audio stack one last time systemctl --user restart pipewire wireplumber Make it executable: chmod +x ~/.yeti-fix.sh Add it to your Startup Applications in your CachyOS settings. The Mirror Moment: You are fighting a battle against aging hardware (Yeti's USB 2.0 controller) and a bleeding-edge OS (CachyOS). The "unplug/replug" was your manual work-around; the script above is the automated version. Did the "Off -> Analog Stereo Duplex" toggle in pavucontrol make the bars move? That is the final bridge.
