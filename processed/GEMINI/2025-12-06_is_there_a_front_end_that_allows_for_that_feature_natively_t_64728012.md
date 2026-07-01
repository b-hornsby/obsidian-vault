---
category: ai-tools
date: 2025-12-06
id: 573004
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if there's a front-end other than LM Studio that natively
  supports web search for local LLMs.
tags:
- local-llm
- front-end
- web-search
- alternative-ui
---
# is there a front end that allows for that feature natively that isn't lm studio? 

### USER
is there a front end that allows for that feature natively that isn't lm studio? 

### GEMINI
The assumption that a local LLM runner will be an all-in-one assistant is what is hindering your progress. Yes, there are front-ends that integrate the speech-to-text (STT) feature natively to create a seamless experience, but you must understand that "natively" in this context usually means the front-end has integrated an existing STT tool (like Whisper) into its core architecture, not that it somehow magically added the capability to the LLM itself. Here are the most relevant, non-LM Studio front-ends that allow for native STT integration: 1. The Power User's Interface: SillyTavern This is the most direct answer for a robust, customizable, integrated solution. Key Feature: SillyTavern is a highly flexible, open-source web UI primarily focused on roleplay and advanced conversational features, but it is built to be a central hub for multiple AI models. STT Integration: It has a dedicated Speech Recognition Extension that allows for native integration of high-quality, local STT models: Whisper/Vosk: You can configure it to use the excellent Whisper model locally via an accompanying "extras server" script. This is the most accurate, fully local option. Browser STT: It also supports the browser's built-in, but less powerful, speech recognition feature. How it Connects to LLMs: SillyTavern acts as the true front-end. It can connect to local LLM backends like KoboldAI/KoboldCPP and, crucially, to LM Studio's Local Server API (the service you were planning to set up in Phase 2 of the previous advice). 2. The RAG-Focused Interface: AnythingLLM If your primary goal is to chat with your documents using voice input, this is a strong contender. Key Feature: AnythingLLM is a full-stack application focused on RAG (Retrieval Augmented Generation), allowing you to easily chat with PDFs, documents, and other file types using a local or cloud LLM. STT Integration: It has explicit support for audio transcription models: Local Transcription: It can use a built-in local transcription model (often Xenova's version of Whisper) for STT. External APIs: It also supports cloud APIs like OpenAI for transcription. Caveat: The documentation suggests the microphone input feature might be more readily available in the Docker/Server versions, and less so in the desktop application, so verify this for your specific use case. 3. The Easy Button: Backyard AI This option aims for out-of-the-box simplicity, though often with a focus on character chat. Key Feature: Backyard AI is a platform designed for engaging with AI-driven characters with a strong emphasis on privacy by running locally. STT Integration: The platform explicitly touts allowing users to engage with AI characters through both text and voice interactions. Because it's designed to run on the desktop and be user-friendly, the voice feature is likely a core, "natively" implemented feature to simplify the user experience. 💡 Strategic Takeaway Your initial instinct to find a "native" solution was correct, but you were looking in the wrong place. LM Studio is an engine; you need a dashboard. The strategic move is not to try and shoehorn a microphone feature into LM Studio's chat box, but to start LM Studio as an API server (its true function for integration) and then use a feature-rich front-end like SillyTavern or AnythingLLM to handle the complex, real-time STT pipeline. Which of these front-ends—the highly customizable SillyTavern or the RAG-focused AnythingLLM—better aligns with what you want to achieve with your voice-enabled local LLM?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/tech/homelab|Homelab]]
