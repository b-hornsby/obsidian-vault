---
category: ai-tools
date: 2025-07-05
id: 940622
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan reported that even with only whisper_stt enabled (no TTS), the system
  was still slow even on the tiny model.
tags:
- whisper-stt
- slow-performance
- stt-latency
---
# no i did that and even with just whisper stt it still is pretty slow, even on tiny

### USER
no i did that and even with just whisper stt it still is pretty slow, even on tiny

### GEMINI
You're observing a critical point: even with only whisper_stt active and set to tiny.en, there's still a noticeable slowdown compared to direct text input. This means the bottleneck is specifically within the Speech-to-Text (STT) transcription process itself. Direct text input is "instant" because your computer sends the characters directly to the AI model. With STT, however, a series of complex steps occur: Audio Capture: Your microphone records your voice. Audio Transfer: This audio data is sent to the whisper_stt extension. Whisper Model Inference: The tiny.en Whisper model then performs the computationally intensive task of converting that raw audio waveform into text. Even tiny.en, while the smallest, is still a neural network running complex calculations. Text Display: The transcribed text is then passed back to the Gradio UI to be displayed in the input box. The delay you're experiencing is the sum of these steps. Here's the reality and what we can do: Inherent Latency: There will always be a delay when using STT compared to direct typing because of the audio processing and inference. It cannot be "instant" like typing. Optimization, Not Elimination: Our goal now is to minimize this inherent latency as much as possible for whisper_stt. Troubleshooting and Optimization Steps: Confirm GPU Usage for Whisper: Go to your Oobabooga UI settings, and expand the Whisper STT section. Double-check that Device is unequivocally set to cuda. If it's on cpu, it will be significantly slower. Also, ensure your system's NVIDIA drivers are up-to-date in WSL2. Minimal Whisper Model: You're already on tiny.en. This is the fastest available Whisper model. You cannot go faster than this. Short, Clear Phrases: When testing, try speaking very short, clear phrases (e.g., "Hello AI", "What is the capital of France?"). Does the transcription time feel more acceptable for these? Longer utterances naturally take longer to process. Monitor Resource Usage (Optional but Recommended): While Oobabooga is running and you are trying to use STT, open a separate terminal in WSL2. Run nvidia-smi to monitor your GPU usage. See if your GPU activity spikes significantly when you speak, indicating it's being actively used by Whisper. You can also run htop (you might need to sudo apt install htop) to monitor CPU and RAM usage. See if the CPU is maxing out during the transcription process. What this means for your "seamless and conversational" goal: For the STT input, tiny.en with GPU acceleration is the fastest you can get. If that's still too slow, the limitation might be your specific hardware's processing speed for even the smallest STT model. The "almost instant" feel of text input is a benchmark that STT, by its nature, cannot perfectly match. The aim is to make the STT delay as imperceptible as possible given the technology and your hardware. Let's confirm the cuda setting for Whisper STT and then assess if the delay changes with shorter inputs.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
