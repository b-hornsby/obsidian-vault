---
category: ai-tools
date: 2025-07-05
id: 672000
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wanted TTS to be an optional feature rather than always-on, so non-typing
  users could benefit without slowing everyone down.
tags:
- tts-optional
- selective-tts
- accessibility
---
# i don't want every question to be answered in tts though. i just wanted it to be an option for all my non typing people out there

### USER
i don't want every question to be answered in tts though. i just wanted it to be an option for all my non typing people out there

### GEMINI
To make TTS an option rather than mandatory for every response, you just need to uncheck one specific setting in the Coqui TTS configuration. Making TTS Optional for Responses By default, when you enable "Play TTS automatically," every AI response will be spoken aloud. To make it an option: Access Coqui TTS Settings: Go to your Oobabooga web UI. Navigate to your settings, and find the "Coqui TTS (XTTSv2)" section. Uncheck "Play TTS automatically": Uncheck the box next to "Play TTS automatically". Save and Restart: Go to the main "Extensions & flags" tab. Click "Save settings to user_data/settings.yaml". Click "Apply flags/extensions and restart". How it Will Work Now After this change, when the AI generates a response: No Automatic Playback: The AI's response will not be automatically spoken aloud. Manual Playback Option: For users who prefer to listen, a speaker icon will appear next to the AI's response in the chat tab. Clicking this icon will play the audio for that specific response. This gives your "non-typing people" the option to listen, while those who prefer to read can do so without unnecessary audio.
