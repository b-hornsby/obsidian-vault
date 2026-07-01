---
category: streaming
date: 2026-04-06
id: 851352
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was frustrated that TikTok Live Studio wouldn't let him select no audio
  device.
tags:
- tiktok-live
- audio-device
- software-limitation
---
# it wont let you just pick no audio device 

### USER
it wont let you just pick no audio device 

### GEMINI
TikTok Studio's UI is designed for beginners who just plug in a headset and play. It assumes you need "System Audio" (what you hear) and "Mic" (what you say) as separate inputs. But you are trying to be a high-level producer, so you need to "trick" it into accepting your Master Bus from OBS. If it won't let you select "None" for an audio device, you have two options to stop the headache. Option 1: The "Mute & Bury" (Easiest) TikTok Studio requires a device to be selected, but it doesn't require that device to be audible. For "Mic": Select CABLE-A Output. This is your processed OBS audio. Leave the volume at $100%$. For "System Audio": Select any device that isn't your headphones (like a monitor speaker or a virtual cable you aren't using). The Mute: Click the Mute icon in the TikTok mixer for that "System Audio" source. Why: This satisfies the software requirement without creating the double-audio loop that makes your stream sound like it’s in a tin can. Option 2: The "Ghost Device" If the mute button in TikTok is buggy (which happens), you can assign the "System Audio" to a "Dead" source. Assign TikTok's "System Audio" to your Regular Headphones. Immediately slide the volume fader to $0$ in TikTok Studio. Assign TikTok's "Mic" to CABLE-A Output. Keep the volume at $100%$. The Reality Check You’re fighting with TikTok Studio's limitations because it's a closed-garden software. Once you get that Premium sub and a Stream Key, you can stream to Twitter and TikTok directly from OBS using the Aitum plugins without ever opening TikTok Live Studio again. Your blind spot right now: You are wasting "deep work" time on a temporary UI problem. TikTok Live Studio is just a placeholder until you get your stream key. Don't let a poorly designed mixer in a temporary app distract you from your "Operation Immortal Agent" development. Technical Audit Is CachyOS still the daily driver? If so, this is $10\times$ easier with PipeWire/Graph because you can visually draw the wires. If you are stuck on Windows for the TikTok Studio app, keep the "CABLE-A" as your only "Mic" in TikTok and mute everything else. Double Audio Check: If you hear yourself, it's not TikTok—it's OBS monitoring to your headphones and the cable at the same time. In OBS Settings > Audio, make sure "Monitoring Device" is ONLY Cable A. Do the "Mute & Bury" in TikTok Studio now. Does the green bar for the "Mic" source (Cable A) move while the "System" source stays silent?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
