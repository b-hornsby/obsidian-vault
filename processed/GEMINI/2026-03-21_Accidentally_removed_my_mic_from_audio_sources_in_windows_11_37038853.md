---
category: homelab
date: 2026-03-21
id: 520926
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan accidentally removed his Yeti microphone from audio sources in Windows
  11 and is seeking help to restore it.
tags:
- windows-11
- audio-input
- microphone-setup
- yeti-microphone
---
# Accidentally removed my mic from audio sources in windows 11? I had my yeti but I clicked don’t allow audio from it 

### USER
Accidentally removed my mic from audio sources in windows 11? I had my yeti but I clicked don’t allow audio from it 

### GEMINI
It happens. When you click "Don't Allow," Windows essentially disables the device at the driver level rather than just muting it. It’s a quick fix to bring it back. Here is the step-by-step to re-enable your Blue Yeti: 1. Re-enable via Windows Settings Press Win + I to open Settings. Go to System > Sound. Scroll down to the Input section. Click on All sound devices (under the "Advanced" header). Look for your Yeti under the "Input devices" list. It will likely be in a separate section for disabled/disallowed devices. Click on the Yeti, and you will see an Allow button next to "Allow apps and Windows to use this device for audio." Click Allow. 2. The "Old School" Control Panel Method If the Yeti doesn't show up in the modern Settings menu, the classic Sound dialog usually catches it: Press Win + R, type mmsys.cpl, and hit Enter. Click the Recording tab. Right-click anywhere in the white space of the list and ensure "Show Disabled Devices" and "Show Disconnected Devices" are both checked. Your Yeti should appear (likely greyed out). Right-click it and select Enable. 3. Privacy Settings Check If it’s enabled but still not picking up sound, Windows might be blocking app access: Go to Settings > Privacy & security > Microphone. Ensure Microphone access is toggled On. Ensure Let apps access your microphone is also toggled On. Would you like me to help you set the Yeti as your default communication device so your apps prioritize it automatically?
