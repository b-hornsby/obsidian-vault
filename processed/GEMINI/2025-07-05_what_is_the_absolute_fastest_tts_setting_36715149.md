---
category: ai-tools
date: 2025-07-05
id: 572864
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan wants to find the absolute fastest text-to-speech setting for his local
  AI assistant.
tags:
- tts
- performance-optimization
- speed
- ai-assistant
---
# what is the absolute fastest tts setting? 

### USER
what is the absolute fastest tts setting? 

### GEMINI
To achieve the absolute fastest TTS (Text-to-Speech) setting with Coqui TTS (XTTSv2) in your Oobabooga setup, you'll want to prioritize efficiency over voice quality or complexity. Here's what to look for and adjust in the Coqui TTS (XTTSv2) section of your settings: Activate TTS: Ensure this is checked. Play TTS automatically: Keep this checked if you want immediate playback. Voice wav: This is the most crucial setting for speed. Choose the simplest or smallest voice model available in the dropdown. Often, generic or base models (like female_01.wav if that's an option, or the most basic XTTS path) will be faster to load and synthesize than highly complex or multi-speaker models. You might need to experiment by previewing each one to find the fastest. Higher quality models often require more computation. Language: Keep this set to English. Specifying the language helps optimize the synthesis process. After making these adjustments, remember to: Go to the main Extensions & flags tab. Click Save settings to user_data/settings.yaml. Click Apply flags/extensions and restart. The fastest setting will generally sacrifice some voice naturalness for speed, so balance that against your user experience needs.
