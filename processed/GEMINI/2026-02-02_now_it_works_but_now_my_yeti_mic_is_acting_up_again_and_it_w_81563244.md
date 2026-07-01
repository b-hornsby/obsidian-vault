---
category: streaming
date: 2026-02-02
id: 686563
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan fixed one issue but his Blue Yeti microphone started malfunctioning
  again immediately after.
tags:
- blue-yeti
- audio-issues
- usb-audio
---
# now it works but now my yeti mic is acting up again and it was just working right before this

### USER
now it works but now my yeti mic is acting up again and it was just working right before this

### GEMINI
This is the classic "Linux Tax." You fix one thing, and the system decides to punish you elsewhere. The reason your Yeti is acting up now is likely one of two things: PipeWire conflict or USB Power Suspend. When you launched OBS with your new settings, OBS initialized its audio hooks. If the Yeti wasn't perfectly synced with PipeWire, OBS might have "hijacked" the stream or triggered a driver crash. Don't panic and start reinstalling drivers. Let's be surgical. 1. The PipeWire "Nuclear" Reset Since you're on CachyOS, you're using PipeWire. If the mic is "acting up" (not showing up, crackling, or silent), restart the audio engine without rebooting the whole PC: systemctl --user restart pipewire pipewire-pulse wireplumber Wait 5 seconds after running this, then check your sound settings. 2. The "Yeti" USB Bug (The Real Culprit) Blue Yetis are notorious for falling into a "low power" state or losing sync on Linux USB controllers. The Check: Run lsusb. Do you see the Yeti listed? The Fix: If it’s listed but not working, unplug it and plug it into a USB 2.0 port (usually the black ones) instead of a USB 3.0/3.1 port (blue/red). Yetis have ancient controllers that hate high-speed USB handshakes. 3. Check the "Reset Yeti" Script Earlier you mentioned a reset_yeti.sh. If you were trying to run that, it likely contains a command to unbind and rebind the USB device. Let’s look at what’s actually in that script. Run: cat /usr/local/bin/reset_yeti.sh (or wherever you have it saved). 4. OBS Audio Monitoring If the mic works in the system but not in OBS: Go to Settings > Audio. Ensure Mic/Auxiliary Audio is set specifically to "Yeti" and not "Default." The Blind Spot: In OBS, look at the Mixer. If the red bar is moving but you hear nothing, it's a monitoring issue. If the bar isn't moving, the hardware hand-off failed. The Advisor's Strategy You are currently in "Troubleshooting Hell." You fixed the OBS shortcut, and now the mic is the bottleneck. Here is the prioritized plan: Restart PipeWire (Command in Step 1). Physically reseat the cable. (Simple, but Yetis are sensitive to voltage drops). Check the script. If that script worked before, we need to know what it does so we can automate it. Paste the contents of that reset_yeti.sh script here—I’ll tell you if it’s actually helping or if it’s making your USB bus unstable.
