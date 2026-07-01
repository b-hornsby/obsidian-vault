---
id: 532753
source: GEMINI
date: 2025-07-05
tags: ['text-generation-webui', 'speech-to-text', 'plain-text-output']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking if it's possible to configure the system to provide plain text output after speech input.
---
# can i just have it set up where i can talk to it and it spits out the answer in plain text? 

### USER
can i just have it set up where i can talk to it and it spits out the answer in plain text? 

### GEMINI
Yes, absolutely! You can have your AI assistant set up so that you can talk to it (using speech-to-text input), and it provides its answers in plain text only (without automatically speaking them aloud). Here's how to configure Oobabooga for this specific setup: Enable and Configure whisper_stt (Speech-to-Text Input): Goal: To allow you to speak to the AI. Settings: Navigate to your Oobabooga UI settings, find the "Whisper STT" section. Ensure it's loaded and enabled. Device: Set to cuda (for GPU acceleration). Whisper Model: Choose a balance of speed and accuracy. base.en is a good starting point. If base.en is too slow, try tiny.en but be aware of accuracy trade-offs. Whisper Language: Set to english. Submit the transcribed audio automatically: Check this box for seamless conversation flow. Disable Automatic Text-to-Speech Output: Goal: To ensure the AI's answers are only in plain text. Settings: Navigate to the "Coqui TTS (XTTSv2)" section in your Oobabooga settings. Activate TTS: Keep this checked. (You still need the extension loaded to process any TTS if you manually click the speaker icon). Play TTS automatically: Uncheck this box. This is the crucial setting that prevents the AI from automatically speaking every response. Save and Restart: After making these changes, go to the main "Extensions & flags" tab. Click "Save settings to user_data/settings.yaml". Click "Apply flags/extensions and restart". Result: With this setup, you will be able to click the microphone icon in the chat tab, speak your question, and your words will be transcribed into the input box. The AI will then process your request and provide its answer as plain text only in the chat window, without generating any audio unless you specifically click the speaker icon next to its response.
