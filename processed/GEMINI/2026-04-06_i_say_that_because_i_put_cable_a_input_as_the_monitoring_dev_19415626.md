---
category: streaming
date: 2026-04-06
id: 953648
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan's OBS mic monitoring through Cable A input wasn't being picked up by
  TikTok Live Studio.
tags:
- obs-monitoring
- vb-cable
- tiktok-live
- echo
- audio-routing
---
# i say that because i put cable a input as the monitoring device in obs and cable a output in tiktok and it still wont work

### USER
i say that because i put cable a input as the monitoring device in obs and cable a output in tiktok and it still wont work

### GEMINI
If the meters are moving in OBS but not in TikTok, you are dealing with a Direct Signal Interruption. This isn't a "settings" problem; it’s a device-in-use or sample rate mismatch problem. Since you just uninstalled VoiceMeeter, Windows might still be trying to hand off audio to a driver that no longer exists, or VoiceMeeter's "exclusive mode" is still locking the cables. The "IT Specialist" Diagnostic (Do this in order) 1. The Exclusive Mode "Kill" (The most likely culprit) VoiceMeeter often toggles a setting called "Allow applications to take exclusive control of this device." If OBS has "captured" Cable A, it might be refusing to let TikTok "hear" it. Right-click the Speaker icon > Sound Settings > More sound settings (Control Panel). Recording Tab: Right-click CABLE-A Output > Properties > Advanced. UNCHECK both boxes under Exclusive Mode. Playback Tab: Right-click CABLE-A Input > Properties > Advanced. UNCHECK both boxes under Exclusive Mode. Restart OBS. 2. The Sample Rate "Handshake" If OBS is sending audio at $44100\text{Hz}$ and Cable A is set to $48000\text{Hz}$, the pipe will literally stay silent or "glitch" into nothingness. In the same Advanced tab from Step 1, ensure every single device (Your Blue Yeti, CABLE-A Input, CABLE-A Output, and your FiiO DAC) is set to the exact same frequency (e.g., 24-bit, 48000Hz). If one is different, the "handshake" fails. 3. The "Ghost" Monitoring Device Sometimes OBS "locks" the monitoring device to the last one used. In OBS Settings > Audio > Advanced, change the Monitoring Device to your FiiO DAC. Click Apply. Then, change it back to CABLE-A Input. Click Apply. Why: This forces OBS to re-initialize the connection to the virtual cable. The Strategic Mirror You’re frustrated because you want a "plug and play" experience, but you're working on a Windows machine that just had its core audio mixer (VoiceMeeter) ripped out. You're dealing with "registry residue." The Truth: You are in a "Troubleshooting Loop." In your warehouse job, if a scanner stops working, you don't just keep pulling the trigger; you check the battery, the connection, and the signal. The Battery: Is the Mic actually getting power? (You said OBS sees it, so yes). The Connection: Is the Monitor set to Cable A? (You said yes). The Signal: Is the sample rate identical across the board? (Check this now). The Opportunity Cost: If you don't master this "signal chain" logic now, your "Operation Immortal Agent" bot's API calls will feel just as "wack" when they fail for no apparent reason. This is the same logic: Input -> Process -> Output. The "Nuclear" Test Close TikTok. Close Discord. Open OBS. Speak. Make sure the green bars move. Open the Windows Sound Control Panel > Recording Tab. Look at CABLE-A Output. Do the tiny grey bars next to it move when you speak into the OBS mic? If those grey bars in the Windows menu are moving, the problem is TikTok. If they are NOT moving, the problem is OBS Monitoring. Which one is it?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
