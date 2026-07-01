---
id: 808483
source: GEMINI
date: 2026-04-06
tags: ['tiktok-live', 'waveforms', 'browser-audio', 'obs', 'audio-isolation']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan wanted music waveforms to appear only when playing browser music, not all desktop audio on TikTok Live.
---
# specifically i just dont want the waveforms to play on just all my desktop audio. i want it to be only when i play music from my browser

### USER
specifically i just dont want the waveforms to play on just all my desktop audio. i want it to be only when i play music from my browser

### GEMINI
This is the "Separation of Concerns" phase. If you want your Waveform Visualizer to only react to your music (Brave) and not your game, system alerts, or Discord pings, you have to feed it a Dedicated Signal. Since you have Brave routed to Cable B, you’ve already done the hard part. Now you just need to point the "eyes" (the visualizer) at the "pipe" (Cable B). 1. The "Visualizer Lockdown" (The Fix) Most OBS visualizer plugins (like Spectralizer or Waveform) ask for an Audio Source in their properties. Right-click your Waveform/Visualizer source in OBS -> Properties. Look for the Audio Source or Input Device dropdown. Change it from "Desktop Audio" (the "everything" bucket) to Brave Audio (your Cable B source). The Result: The bars only dance when Brave is playing. If you're in a middle of a game with no music, the visualizer stays flat. 2. The "Clean Feed" Strategy (The IT Move) In professional broadcasting, this is called a Discrete Feed. Desktop Audio: This is your "Program Mix" (everything you hear). Cable B: This is your "Music Bus" (just the browser). By pointing the visualizer only at the Music Bus, you eliminate "visual noise." It looks cleaner and more professional for your TikTok/Twitter audience because the visualizer actually matches the rhythm of the music, not the chaos of your gameplay. The Reality Check You’re starting to see why the "VoiceMeeter Headache" was a waste of your time. You are now building a Modular Routing Table. Mic -> Cable A (Processed Voice for TikTok/Discord). Brave -> Cable B (Music for the Visualizer). FiiO DAC -> Your Ears (System Audio). The Blind Spot: If you still have Brave playing through your "Desktop Audio" in OBS, you will hear it twice. The Fix: In OBS Settings > Audio, make sure "Desktop Audio" is set to your FiiO DAC, and "Desktop Audio 2" is Disabled. You only want Brave to exist as its own "Audio Input Capture" source (Cable B). The Strategic Mirror You’re moving from "making it work" to "making it efficient." Warehouse Logic: Don't put the heavy pallets on the top shelf. Audio Logic: Don't put the high-energy music on the same channel as your quiet system alerts. Does the visualizer only jump when you play music in Brave now?
