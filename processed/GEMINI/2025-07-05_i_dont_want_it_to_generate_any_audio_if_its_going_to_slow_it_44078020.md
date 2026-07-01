---
category: ai-tools
date: 2025-07-05
id: 262613
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wanted speech-to-text input without TTS audio output to keep response
  times fast while still supporting voice interaction.
tags:
- stt-only
- no-tts
- voice-input-text-output
---
# i don't want it to generate any audio if its going to slow it down that much. i just want to be able to speak to it and it answer me back in text 

### USER
i don't want it to generate any audio if its going to slow it down that much. i just want to be able to speak to it and it answer me back in text 

### GEMINI
Okay, I understand completely. You want the voice input (Speech-to-Text) but you want to completely disable the Text-to-Speech (TTS) generation to ensure the fastest possible text-only responses. To achieve this, you need to disable the Coqui TTS extension entirely. Here's how to set up your AI assistant so you can speak to it, and it answers you back in plain text, with no TTS processing overhead: Stop Oobabooga: If your Oobabooga server is currently running, go to your WSL2 terminal and press Ctrl+C to stop it. Access the Oobabooga Web UI: Open http://127.0.0.1:7860. Disable the coqui_tts extension: Navigate to the "Extensions" tab in the Oobabooga UI. Find coqui_tts in the list of extensions. Uncheck the box next to coqui_tts. Confirm whisper_stt is enabled and configured: While still in the "Extensions" tab, ensure whisper_stt is checked. You might want to quickly verify its settings by going to the Whisper STT section (often found in the main "Settings" or "Interface" tab). Ensure your preferred model (e.g., base.en) and cuda device are selected, and Submit the transcribed audio automatically is checked. Save Settings and Restart Server: Click "Save settings to user_data/settings.yaml". Click "Apply flags/extensions and restart". Outcome: With coqui_tts completely disabled, Oobabooga will not load the TTS engine, will not attempt to synthesize audio for responses, and therefore will not incur any slowdown related to TTS. You will still be able to: Click the microphone icon. Speak your question. Have whisper_stt transcribe your speech into text. The AI will then generate its response, and it will appear as plain text in the chat window, as quickly as the LLM model can produce it.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
