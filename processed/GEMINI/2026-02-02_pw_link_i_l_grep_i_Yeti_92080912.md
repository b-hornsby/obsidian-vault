---
id: 536968
source: GEMINI
date: 2026-02-02
tags: ['pipewire', 'audio-routing', 'yeti-microphone', 'linux-audio']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is using pw-link to check the PipeWire audio connections related to his Yeti microphone.
---
# ❯ pw-link -i -l | grep -i "Yeti"

~
❯ 

### USER
❯ pw-link -i -l | grep -i "Yeti"

~
❯ 

### GEMINI
That empty output is the "smoking gun." If pw-link returns nothing, PipeWire has effectively ghosted the device. The kernel sees it (lsusb worked), but the audio server has failed to "wire" it into the system. On CachyOS/Arch, this usually happens because the WirePlumber session manager encountered an error during the handshake and just gave up on the device. Since we just fixed your udev rules to prevent the power-sleep issue, we need to force PipeWire to look at the hardware again without you touching the cable. 1. The "Wake Up" Command Run this to force PipeWire to re-scan for new hardware nodes: wpctl status | grep -i "Yeti" If it's still empty: Your session manager is stuck. The Fix: Run this exact line to nukes the current (broken) session state and restarts the audio engine: rm -rf ~/.local/state/wireplumber/* && systemctl --user restart pipewire wireplumber 2. Check the "Suspended" State If the Yeti appears in wpctl status but has a [S] or [IDLE] next to it and won't move to [RUNNING], WirePlumber thinks the device is "faulty" and is refusing to open the stream. Run this to see if the device is being "blocked": wpctl inspect @DEFAULT_AUDIO_SOURCE@ (Look for any lines mentioning "state: error" or "node.ignored".) 3. The "CachyOS" Performance Conflict CachyOS uses the bore or lqx kernels which are very "fast." Sometimes they initialize the audio drivers before the USB bus is even ready. If the rm -rf command above makes the mic work immediately, then your "unplug/replug" ritual was just you manually doing what WirePlumber failed to do at boot. We can automate that by adding a 5-second delay to PipeWire's startup. Try the rm -rf ~/.local/state/wireplumber/* && systemctl --user restart pipewire wireplumber command now. Did the mic spring to life in pavucontrol?
