---
category: ai-tools
date: 2025-07-05
id: 692985
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan found that even TTS without audio output wasn't speeding up the process
  as much as expected compared to regular text input.
tags:
- tts-overhead
- performance-bottleneck
- whisper-stt
---
# just having tts, no audio isn't really speeding the process up as much as i thought. it was almost instant when it was just regualr text input 

### USER
just having tts, no audio isn't really speeding the process up as much as i thought. it was almost instant when it was just regualr text input 

### GEMINI
You're right. Even with TTS audio playback disabled, the system still dedicates resources to synthesize the audio in the background when the TTS extension is active. This background process creates the audio file so it's ready if you click the speaker icon later, and that synthesis itself introduces a delay before the text response is fully displayed. To get the absolute fastest response time in plain text while still using voice for input, the solution is to completely disable the Text-to-Speech (TTS) extension. This removes all TTS processing overhead. Here's how to do it: Disable Coqui TTS Extension Stop Oobabooga: If it's running, press Ctrl+C in your WSL2 terminal. Go to the Web UI: Open your browser to http://127.0.0.1:7860. Access Extensions Tab: Navigate to the "Extensions" tab in the Oobabooga UI. Uncheck Coqui TTS: Find coqui_tts in the list and uncheck the box next to it. Save and Restart: Click "Save settings to user_data/settings.yaml". Then, click "Apply flags/extensions and restart". What to Expect With coqui_tts completely disabled, the system won't load the TTS engine or attempt any audio synthesis. This should bring your response times back to being nearly instantaneous, matching the speed you experienced with regular text input, because the only additional step now is the Speech-to-Text (STT) conversion of your voice input. You will still be able to: Click the microphone icon in the chat. Speak your question. Have whisper_stt transcribe your speech into text. The AI will then generate its response, and it will appear as plain text only in the chat window, at the maximum speed your LLM model and hardware can provide.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
