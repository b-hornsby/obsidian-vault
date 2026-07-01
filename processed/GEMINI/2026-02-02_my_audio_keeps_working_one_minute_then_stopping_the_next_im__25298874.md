---
category: homelab
date: 2026-02-02
id: 731120
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was troubleshooting intermittent audio dropouts in VLC on CachyOS where
  audio works briefly then stops and requires manual re-selection.
tags:
- audio-dropout
- vlc
- cachyos
- pipewire
---
# my audio keeps working one minute then stopping the next? im on cachyos and this only seems to happen when watching videos via vlc? it'll work for a few videos then stop and i have to manually click the audio source to fix it

### USER
my audio keeps working one minute then stopping the next? im on cachyos and this only seems to happen when watching videos via vlc? it'll work for a few videos then stop and i have to manually click the audio source to fix it

### GEMINI
This isn't a "broken" system; it's a classic conflict between VLC’s legacy handling of audio and the modern PipeWire stack that CachyOS uses. CachyOS is built for performance, but VLC often tries to "be the boss" of the audio hardware, leading to the exact dropping or "stuck" state you’re describing. When you manually click the source, you’re forcing a re-handshake between VLC and the audio server (WirePlumber). Here is the direct, BS-free path to fixing it. 1. The "VLC Logic" Fix (Immediate Action) VLC often defaults to its own internal "PipeWire" or "ALSA" modules which can be buggy. You want it to use the PulseAudio compatibility layer, which is the most stable bridge for VLC on Arch-based systems. Open VLC and go to Tools > Preferences (Ctrl+P). Switch to the Audio tab. Change Output module from "Automatic" to PulseAudio audio output. Save and restart VLC. [!NOTE] Even though CachyOS uses PipeWire, it uses pipewire-pulse to handle most apps. Forcing VLC to use this specific "language" usually stops the device from dropping when you switch videos. 2. Disable Audio Power Saving (The Strategic Fix) If the audio works for a few videos then dies, your kernel might be "suspending" your audio hardware during the micro-silence between files to save power. When VLC starts the next video, the hardware doesn't wake up fast enough, causing the stream to "orphan." Run this command to disable PipeWire's node suspension: mkdir -p ~/.config/wireplumber/wireplumber.conf.d echo 'monitor.alsa.rules = [ { matches = [ { node.name = "~alsa_output.*" } ]; actions = { update-props = { session.suspend-on-idle = false } } } ]' > ~/.config/wireplumber/wireplumber.conf.d/disable-suspension.conf Then restart the audio service: systemctl --user restart pipewire wireplumber 3. The "Blind Spot" Check If you are using HDMI audio or a USB DAC, these are notoriously finicky with "stream discontinuities" (the gap between videos). Check for PipeWire-ALSA conflicts: Ensure you don't have a rogue .asoundrc in your home folder trying to hijack the hardware. The "Pro" Alternative: If VLC continues to be a headache, try MPV. On CachyOS, MPV is generally better optimized for the kernel's scheduling and handles PipeWire natively without the legacy baggage VLC carries. What to do next Start with Step 1 (changing the output module in VLC). It fixes 90% of these cases on Arch-based distros. Would you like me to show you how to check your system logs (journalctl) specifically for audio "Xrun" errors to see if your hardware is actually crashing?
