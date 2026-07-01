---
id: 076605
source: GEMINI
date: 2025-07-05
tags: ['text-generation-webui', 'speech-to-text', 'feature-addition']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is considering adding speech-to-text functionality to the AI assistant.
---
# for sure. thinking about adding the ability to talk with the ai assistant for those who don't want to type. is that doable here?

### USER
for sure. thinking about adding the ability to talk with the ai assistant for those who don't want to type. is that doable here?

### GEMINI
Yes, adding the ability to talk with the AI assistant (speech-to-text, STT, for input and text-to-speech, TTS, for output) is definitely doable within the Oobabooga text-generation-webui. Oobabooga supports several extensions for both STT and TTS. Looking at your extensions directory listing, I see a couple that are directly relevant: whisper_stt: This extension would allow users to speak their input, and the system would convert it to text for the AI to process. Whisper is a highly capable STT model from OpenAI. silero_tts: This extension provides text-to-speech capabilities, allowing the AI's responses to be spoken aloud. coqui_tts: Another option for text-to-speech, often providing high-quality voices. You can enable these extensions, and once configured, users would interact with the AI using their voice.
