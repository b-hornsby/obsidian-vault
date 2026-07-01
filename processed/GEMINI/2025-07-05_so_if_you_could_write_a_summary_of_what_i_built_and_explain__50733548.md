---
id: 201127
source: GEMINI
date: 2025-07-05
tags: ['rag', 'local-llm', 'project-summary', 'troubleshooting', 'helpdesk-ai']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is requesting a summary of his RAG project and an explanation of the challenges encountered during its development.
---
# so if you could write a summary of what i built and explain the troubles you noticed we had setting this whole thing up? 

### USER
so if you could write a summary of what i built and explain the troubles you noticed we had setting this whole thing up? 

### GEMINI
You've built a customized, voice-enabled AI helpdesk assistant designed for quick, knowledgeable text responses. This project demonstrates a strong understanding of integrating and optimizing various AI components for practical application. Project Summary: Voice-Enabled Helpdesk AI You've successfully engineered a conversational AI assistant that operates locally on your system, bypassing cloud services for enhanced privacy and control. Key features include: Real-time Voice Input (Speech-to-Text - STT): You can speak naturally to the AI, and your words are converted into text using the Whisper STT extension (specifically optimized with base.en model running on cuda for efficiency). Intelligent Knowledge Retrieval (Retrieval-Augmented Generation - RAG): The AI enhances its responses by pulling information from two sources: Local Documents (superboogav2): It can search and retrieve context from your private helpdesk knowledge base. Web Search (web_rag): It can access current information from the internet via DuckDuckGo Lite to answer queries that require up-to-date or broader knowledge. Optimized Language Model (LLM): The core intelligence is powered by a Large Language Model (LLM), specifically Phi-3-mini-4k-instruct.Q4_K_M.gguf. This model was chosen and configured to run primarily on your GPU (using CUDA and --n-gpu-layers 999) for the fastest possible text output. Text-Only Output: The system is configured to provide responses solely in plain text, prioritizing speed and avoiding automatic voice playback overhead. Local Deployment: The entire setup runs within a WSL2 environment, demonstrating competence in local AI deployment and resource management. Troubleshooting Journey: Overcoming Setup Challenges Setting up and optimizing this system presented several key challenges that you systematically addressed: Initial Speed Bottleneck with Text-to-Speech (TTS): Problem: Early on, the AI's responses were slow, even if the audio wasn't played automatically. Solution: We identified that the Coqui TTS extension, even when just active in the background for audio synthesis, consumed significant resources. The solution was to completely disable the Coqui TTS extension, removing all audio generation overhead. RAG-Induced Latency: Problem: Even after disabling TTS, queries that required the AI to gather external information (like "My PC keeps crashing..." or "Setting up a VPN") were very slow (e.g., 24+ seconds for an initial short response). This pointed to Retrieval-Augmented Generation (RAG) as the primary cause. Solution: The core issue was the sheer volume of context being retrieved by both superboogav2 and web_rag and then fed into the LLM. We dramatically reduced the amount of data processed by adjusting settings: superboogav2 Context length: Reduced from 250,800 to much smaller values (e.g., 100,200). web_rag Maximum characters of retrieved data to keep: Reduced from 5000 to 1000-1500. web_rag Number of pages to retrieve: Reduced from 3 to 1 or 2. LLM Inference Speed as the Core Bottleneck: Problem: Even with TTS and RAG disabled, the AI was still slow (e.g., 16.46 seconds for a simple question) when using the Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf model. This revealed that the Language Model itself was the ultimate bottleneck for achieving fast responses on your hardware. Solution: To significantly improve the LLM's response speed, we opted to switch to a smaller, more efficient model: Phi-3-mini-4k-instruct.Q4_K_M.gguf. This model, when fully offloaded to your GPU (--n-gpu-layers 999), drastically cut down the LLM's processing time (to around 10 seconds for a core LLM response), striking the best balance of speed and helpdesk-level intelligence for your system. UI Settings Visibility: Problem: At one point, the settings for superboogav2 and web_rag weren't appearing in the UI even though the extensions were loading. Solution: This was resolved by ensuring the extensions were properly enabled and that the browser cache was cleared with a hard refresh, confirming it was a UI/loading order issue rather than a functional problem with the extensions. Through these steps, you transformed a slow, potentially frustrating setup into a functional and significantly faster voice-controlled AI assistant, showcasing strong debugging and optimization skills.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
