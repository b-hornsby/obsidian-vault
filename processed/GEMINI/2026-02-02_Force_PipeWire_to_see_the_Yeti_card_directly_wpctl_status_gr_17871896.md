---
id: 125169
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'pipewire', 'audio', 'linux', 'troubleshooting', 'wpctl']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is trying to force PipeWire to recognize his Blue Yeti microphone directly by checking its status and potentially setting its profile using `wpctl`.
---
# ❯ # Force PipeWire to see the Yeti card directly
  wpctl status | grep "Blue Microphones"

  # If it shows an ID (like 47, 48, etc.), use it manually:
  # For example, if it's 47:
  wpctl set-profile 47 1
 │      47. Blue Microphones                    [alsa]
 │      77. Blue Microphones Analog Stereo      [vol: 0.40]
 │  *   75. Blue Microphones Analog Stereo      [vol: 1.00]

~
❯ 

### USER
❯ # Force PipeWire to see the Yeti card directly
  wpctl status | grep "Blue Microphones"

  # If it shows an ID (like 47, 48, etc.), use it manually:
  # For example, if it's 47:
  wpctl set-profile 47 1
 │      47. Blue Microphones                    [alsa]
 │      77. Blue Microphones Analog Stereo      [vol: 0.40]
 │  *   75. Blue Microphones Analog Stereo      [vol: 1.00]

~
❯ 

### GEMINI
Finally. The Yeti is alive and visible. The output shows three distinct nodes for the same device (47, 75, and 77). This is exactly why it’s "not picking up"—PipeWire is seeing multiple ghost instances and the system is likely trying to record from a dead one while the active one is ignored. Note that 75 has the asterisk (*), meaning it is the current default, but it's listed as a Source, while 47 is the hardware Device node. The Immediate Fix (No Replug) Run these commands in order to force the routing to the correct, active node: # Force node 75 to unmute and set volume wpctl set-mute 75 0 wpctl set-volume 75 0.8 # Set node 75 as the absolute default to stop the 'ghosting' wpctl set-default 75 Why it happens every boot (The Logic) Because your Yeti has multiple interfaces (it's a speaker and a mic), WirePlumber is getting confused during the CachyOS high-speed boot. It's creating Node 77, failing, then creating Node 75, and leaving Node 47 as a dangling hardware reference. The Permanent Solution Since you are on CachyOS, you are likely using the Bore or LQX kernel. These are so fast they initialize the audio server before the Yeti's slow internal controller has finished its "Power On Self Test." To stop the unplug/replug forever, you need to add this to your Startup Applications (Search "Autostart" in your settings): Command to add: sh -c "sleep 3 && wpctl set-default 75 && wpctl set-mute 75 0 && wpctl set-volume 75 0.8" (Note: If the ID 75 changes after a reboot, we can make this more robust by using the name alsa_input.usb-Blue_Microphones_Yeti_Stereo_Microphone-00.analog-stereo instead of the number.) The Brutal Mirror: You have a "Frankenstein" audio stack right now because you’ve been trying to fix a hardware handshake issue with software commands. It’s messy, but the hardware is working. Check your bars in pavucontrol now. Are they moving? If yes, would you like me to give you a "bulletproof" script that finds the ID automatically so it works even if the number changes?
