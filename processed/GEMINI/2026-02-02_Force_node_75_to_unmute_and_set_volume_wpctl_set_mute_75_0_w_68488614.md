---
id: 831446
source: GEMINI
date: 2026-02-02
tags: ['blue-yeti', 'pipewire', 'audio', 'linux', 'troubleshooting', 'wpctl']
category: streaming
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is attempting to unmute and set the volume for a specific PipeWire node (75) associated with his Blue Yeti microphone, and set it as the default to prevent 'ghosting'.
---
# ❯ # Force node 75 to unmute and set volume
  wpctl set-mute 75 0
  wpctl set-volume 75 0.8

  # Set node 75 as the absolute default to stop the 'ghosting'
  wpctl set-default 75

~
❯ 

### USER
❯ # Force node 75 to unmute and set volume
  wpctl set-mute 75 0
  wpctl set-volume 75 0.8

  # Set node 75 as the absolute default to stop the 'ghosting'
  wpctl set-default 75

~
❯ 

### GEMINI
Since there was no error message this time, Node 75 is officially engaged. Open Pavucontrol or your sound settings. If you see the bars moving, we’ve won the battle. But because you are on CachyOS, the next time you reboot, that "75" might become "82" or "40," and you'll be right back to unplugging the cable to force a reset. The "Advisor" Move: Automate the Handshake To stop the "unplug/replug" cycle forever, you need a startup command that doesn't care about ID numbers. It needs to find the Yeti by name and force it to wake up. Do this once, and you’ll never have to touch the cable again: Open your System Settings -> Autostart (or "Startup Applications"). Add a "Login Script" or "Command." Paste this exact command (it works in both Fish and Bash): sh -c "sleep 5; wpctl set-default (wpctl status | grep -i 'Yeti' | grep -oP '(?<= )\d+(?=\. )' | head -n 1); wpctl set-mute @DEFAULT_AUDIO_SOURCE@ 0; wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.6" Why this is the "Brutally Honest" fix: The Problem: Your Yeti is a legacy USB 2.0 device trying to talk to a high-performance CachyOS kernel. It's too slow to "check in" during the initial boot, so PipeWire ignores it or gives it a "ghost" ID. The Fix: We let the system boot, wait 5 seconds for the Yeti to finally "wake up" on the USB bus, then programmatically tell PipeWire: "Hey, find the thing named Yeti, make it the boss, and unmute it." Is the mic actually working right now? Scratch the grill and check your levels. If it's working, set that autostart command and consider the case closed.
