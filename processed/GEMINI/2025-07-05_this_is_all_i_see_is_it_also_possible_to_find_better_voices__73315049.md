---
category: ai-tools
date: 2025-07-05
id: 420840
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking about improving TTS voice quality for his AI assistant and
  reporting what he currently sees in the UI.
tags:
- tts
- voice-quality
- ai-assistant
- webui
---
# this is all i see? is it also possible to find better voices for the ai assistant? 

### USER
this is all i see? is it also possible to find better voices for the ai assistant? 

### GEMINI
You're seeing the "Whisper STT" and "Coqui TTS (XTTSv2)" sections in the settings, which is great! That screenshot (image_cb3d37.png) confirms that both extensions are loaded into the UI. Yes, it is absolutely possible to find better voices for the AI assistant, particularly with Coqui TTS. Coqui TTS Voice Selection The screenshot you provided for image_cb3d37.png shows the "Coqui TTS (XTTSv2)" configuration. Here's how to access and find better voices: "Voice wav" Dropdown: You'll see a dropdown menu labeled "Voice wav". This is where you select the specific voice model to use. Click on this dropdown. You should see a list of available voice models. If you just ran the server and it downloaded the XTTS model (as indicated by your previous terminal output), you should now see options like tts_models/en/ljspeech/vits or vits/en_US/vctk/p225 (these are common XTTS models) in this list. Select one of them. Downloading More Voices (If Desired): The Coqui TTS extension typically provides a mechanism (often a separate tab like "Coqui TTS" or a section within the current tab) where you can browse and download additional voice models. Look for a section or button that allows you to download more TTS models. These models vary in quality, accent, and speaker. Coqui-TTS has a wide range of pre-trained models. Downloading a new model will happen in the background and might take some time, similar to when the default XTTS model was downloaded upon server start. Once downloaded, it will appear in the "Voice wav" dropdown. "Preview text" and "Preview" Button: Once you've selected a voice model from the "Voice wav" dropdown, type some text into the "Preview text" box (e.g., "Hello, this is a test voice."). Click the "Preview" button. This will generate and play a short audio clip of the selected voice speaking your text, allowing you to audition different voices without having to go back to the chat. "Activate TTS" and "Play TTS automatically": Ensure "Activate TTS" is checked. "Play TTS automatically" is a convenient option if you want the AI to speak its responses without you having to click the speaker icon every time. You can leave this checked. Whisper STT Configuration While your screenshot (image_cb3d37.png) also shows the "Whisper STT" section, it's collapsed. You'll want to expand that section to configure the Whisper model. Expand "Whisper STT": Click the dropdown arrow next to "Whisper STT" to reveal its settings. Model Selection: Just like with Coqui TTS, Whisper has different model sizes (tiny, base, small, medium, large). Smaller models are faster but less accurate, while larger models are more accurate but slower and require more resources. Recommendation: For a balance of performance and accuracy, start with base or small. You may need to download the chosen Whisper model if it's not already on your system. Language: Ensure "English" or "en" is selected for transcription. After configuring both, remember to go to the Chat tab to test the full voice interaction using the microphone and speaker icons.
