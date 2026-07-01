---
id: 692521
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'embedding', 'text-generation']
category: ai-tools
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# Closing server running on port: 7860
13:30:37-143605 INFO     Loading the extension "superboogav2"
13:30:37-144523 INFO     Loading the extension "web_rag"
13:30:37-145073 INFO     Loading the extension "whisper_stt"
13:30:40-356504 INFO     Loading the extension "coqui_tts"
[XTTS] Loading XTTS...
100%|█████████████████████████████████████████████████████████████████████████| 1.87G/1.87G [-1:59:17<00:00, -43.2MiB/s]
4.37kiB [00:00, 41.7kiB/s]
361kiB [00:00, 2.94MiB/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 32.0/32.0 [00:00<00:00, 211iB/s]
100%|█████████████████████████████████████████████████████████████████████████████| 7.75M/7.75M [01:02<00:00, 26.8MiB/s][XTTS] Done!

Running on local URL:  http://127.0.0.1:7860

13:31:22-345608 INFO     Saved "/home/bryan_/text-generation-webui/user_data/settings.yaml".

### USER
Closing server running on port: 7860
13:30:37-143605 INFO     Loading the extension "superboogav2"
13:30:37-144523 INFO     Loading the extension "web_rag"
13:30:37-145073 INFO     Loading the extension "whisper_stt"
13:30:40-356504 INFO     Loading the extension "coqui_tts"
[XTTS] Loading XTTS...
100%|█████████████████████████████████████████████████████████████████████████| 1.87G/1.87G [-1:59:17<00:00, -43.2MiB/s]
4.37kiB [00:00, 41.7kiB/s]
361kiB [00:00, 2.94MiB/s]
100%|█████████████████████████████████████████████████████████████████████████████████| 32.0/32.0 [00:00<00:00, 211iB/s]
100%|█████████████████████████████████████████████████████████████████████████████| 7.75M/7.75M [01:02<00:00, 26.8MiB/s][XTTS] Done!

Running on local URL:  http://127.0.0.1:7860

13:31:22-345608 INFO     Saved "/home/bryan_/text-generation-webui/user_data/settings.yaml".

### GEMINI
Fantastic! This is exactly what we wanted to see! Let's break down that latest output: 13:30:37-145073 INFO Loading the extension "whisper_stt" - Success! Whisper STT loaded without errors. 13:30:40-356504 INFO Loading the extension "coqui_tts" - Success! Coqui TTS started loading. [XTTS] Loading XTTS... and the progress bars (100%|████████...) - This means coqui_tts is downloading its default XTTS model. This is a large file (1.87GB!), and it completed successfully. [XTTS] Done! - Confirmation that the Coqui TTS model is loaded and ready. And finally, Running on local URL: http://127.0.0.1:7860 means your Oobabooga server is fully up, and all your desired extensions (superboogav2, web_rag, whisper_stt, and coqui_tts) are loaded without errors! Next Steps: Configure and Test Voice Interaction Now that everything is loaded, let's configure and test it in the web UI. Open your web browser and go to http://127.0.0.1:7860. Navigate to the "Extensions" tab: Ensure that whisper_stt and coqui_tts are both checked and enabled. If you haven't saved settings since enabling them, click "Save settings" and restart if prompted. Explore the "Whisper STT" Tab: You should now have a dedicated "Whisper STT" tab. Click on it. Model selection: You'll likely see a dropdown for "Whisper model." Smaller models (tiny, base) are faster but less accurate. Larger models (small, medium, large) are more accurate but require more VRAM/RAM and are slower. For a balance of speed and accuracy, base or small is a good starting point. You may also need to download the model if it's not already cached. Language: Set this to English or en. Adjust any other settings like Beam size if you experience issues, but defaults are usually fine to start. Explore the "Coqui TTS" Tab: You should have a dedicated "Coqui TTS" tab. Click on it. Model Selection: The XTTS model you just saw downloading (tts_models/en/ljspeech/vits or similar XTTS path) should now be available in a dropdown. Select it. Speaker: For most XTTS models, you'll need to select a speaker from a list or provide a speaker embedding. Start with a default speaker if one is offered. Voice Sample: You might be able to play a test voice sample here to ensure it's working and sounds good. Test Voice Chat in the "Chat" Tab: Go to the "Chat" tab. You should now see microphone icons (for STT) near the input box and speaker icons (for TTS) near the AI's response area. To speak to the AI: Click the microphone icon near the input text box. Speak your question clearly into your microphone. Watch as your speech is transcribed into the text input area. To hear the AI: After the AI generates its text response, click the speaker icon next to its message. The AI should speak its reply. Congratulations! You're very close to having a fully voice-enabled AI assistant. Let me know if you encounter any issues during the configuration in the UI or during testing.