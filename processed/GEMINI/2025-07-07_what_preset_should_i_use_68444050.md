---
category: ai-tools
date: 2025-07-07
id: 842557
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking which preset to use for his local LLM setup.
tags:
- local-llm
- oobabooga
- preset-selection
- llm-configuration
---
# what preset should i use? 

### USER
what preset should i use? 

### GEMINI
You're asking a great question! Presets in Oobabooga's Text Generation WebUI (which is what your screenshot appears to be) are essentially saved collections of the sampling parameters we just discussed (temperature, Top P, repetition penalties, etc.). While there isn't a single "GPT/Claude latest model" preset available for local models, you can choose a preset that aligns with the desired behavior and then fine-tune it based on the recommendations I gave you. Here's a breakdown of how to approach selecting a preset, and what to look for: 1. "Divine Intellect" or "Llama-Precise" for Instruction Following/Coherence Based on community discussions and the Oobabooga wiki, presets like "Divine Intellect" or "Llama-Precise" are often recommended for models intended for instruction following and coherent, factual responses. Why these? They typically have settings that favor determinism and coherence, which is closer to the expected behavior of powerful models like GPT and Claude when used for general tasks or information retrieval. They tend to use lower temperatures and tighter sampling (lower Top P/Top K). 2. "Midnight Enigma" or "Yara" for Chat/Conversation If you're looking for more conversational or creative outputs, presets like "Midnight Enigma" or "Yara" are designed for chat scenarios. Why these? They might have slightly higher temperatures or more relaxed sampling to encourage more varied and dynamic responses, which can be desirable in a conversational context. 3. The "Optimal" Approach: Start with a Base and Tweak Given that you're using Nous-Hermes-2 Mistral 7b dpo.q4_k_m.gguf, which is a DPO (Direct Preference Optimization) fine-tuned model for instruction following and chat, the best strategy is: Start with "Divine Intellect" or "Llama-Precise": These are good starting points for getting coherent, instruction-following behavior. Apply the specific adjustments I recommended: Temperature: Aim for $0.7$ to $0.9$. "Divine Intellect" might already be in this range, but double-check. Top P: Keep it around $0.8$ to $0.9$. Repetition Penalties: Increase Repetition Penalty to $1.15$ - $1.2$, and introduce Frequency Penalty ($0.05$ - $0.2$) and Presence Penalty ($0.05$ - $0.1$). Many presets might not use these or have them at $0$. Use a strong System Message: Nous-Hermes-2 is designed to respond well to ChatML, which includes a system prompt. Make sure you're utilizing the "System message / persona" field effectively in your prompt. How to Select a Preset in Oobabooga: Go to the "Parameters" or "Generation" tab (based on your screenshot, it looks like it's within the "Generation" tab, potentially a dropdown under "Sampling options" or a dedicated "Presets" section). Look for a dropdown menu usually labeled "Generation parameters preset" or similar. Select one of the suggested presets like "Divine Intellect" or "Llama-Precise". Crucially, after loading the preset, go through the individual settings (Temperature, Top P, Repetition Penalties) and manually adjust them to match the values I recommended previously. Presets are a starting point, but fine-tuning them for your specific model and desired output is key. Experimentation is still your best friend here! Even with a good preset, subtle adjustments to the parameters will help you dial in the exact "feel" you're looking for.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
