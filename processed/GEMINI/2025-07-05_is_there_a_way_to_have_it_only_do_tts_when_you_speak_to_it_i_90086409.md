---
category: ai-tools
date: 2025-07-05
id: 403119
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wanted TTS to activate only when the user speaks to the AI, not for
  text input, to avoid slowing down responses.
tags:
- conditional-tts
- stt-triggered-tts
- performance-optimization
---
# is there a way to have it only do tts when you speak to it? i feel like becuase its enabled at all it slows down the answers

### USER
is there a way to have it only do tts when you speak to it? i feel like becuase its enabled at all it slows down the answers

### GEMINI
No, unfortunately, there isn't a direct setting within Oobabooga's coqui_tts extension to only activate TTS output when the input was spoken. The Play TTS automatically checkbox either enables automatic speech playback for all AI responses, or it disables it, requiring a manual click. Here's why it's behaving this way and the limitations: Separate Functions: Speech-to-Text (STT) and Text-to-Speech (TTS) are treated as distinct functionalities within the web UI. Your voice input goes through STT to become text, and the AI then processes that text input. The TTS output is triggered by the AI's text response, not by the origin of the user's input. Gradio Interface Limitations: The underlying Gradio framework, while flexible, doesn't inherently provide a direct, simple way to link the input method (typed vs. spoken) to the output method (text vs. spoken) for every single response without custom coding. Why it "feels like because it's enabled at all it slows down the answers": You're absolutely right in your observation. When TTS is active, even if "Play TTS automatically" is unchecked, the system still goes through the TTS synthesis process in the background to generate the audio file for the speaker icon. This generation takes time. So, if you're waiting for the AI's text response to appear, it might still be waiting for the TTS audio to be ready before it fully displays, giving the impression of a slowdown even if you don't play the audio. Current Options: Manual Playback (Current Recommended): This is what we just set up. You speak, the AI responds in text, and then you manually click the speaker icon if you want to hear it. This gives you control and avoids the perceived slowdown for those who prefer to read. Fully Automatic Playback (If Speed is Acceptable): If you find a fast-enough TTS voice, you could re-enable "Play TTS automatically" for a completely hands-free experience. Advanced: Custom Code (Not recommended for most users): To achieve what you're asking for (TTS output only on spoken input), you would likely need to delve into Oobabooga's modules/chat.py or the coqui_tts extension's script.py and modify the code. This would involve adding logic to check if the last user input came from the STT microphone and then conditionally trigger the TTS output. This is a complex undertaking, as it requires Python programming knowledge and understanding of Oobabooga/Gradio's internals. For now, sticking with the manual TTS playback option (where you click the speaker icon) is the most practical way to have TTS available without slowing down every text response.
