---
id: 987518
source: GEMINI
date: 2025-06-25
tags: ['oobabooga-presets', 'model-parameters', 'generation-settings']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was asking about the preset options available in oobabooga's parameters tab for configuring model generation settings.
---
# what about the preset in parameters? 

### USER
what about the preset in parameters? 

### GEMINI
Based on the screenshot image_39cf39.png, you're asking about the "Preset" dropdown in Oobabooga's "Parameters" tab. The presets are pre-configured sets of generation parameters designed for specific types of outputs or model behaviors. Given your use case (a personal helpdesk AI assistant) and your desire for accurate, consistent, and non-creative responses, the Deterministic preset is likely the most suitable choice among the ones shown. Here's why: Deterministic: This preset is specifically designed to minimize randomness in the model's output. It typically sets parameters like Temperature to very low values (e.g., 0.1 or 0.0), Top P very high, and Top K to a low but reasonable number. This forces the model to choose the most probable next tokens, leading to highly consistent and predictable responses. For a helpdesk, this means less "creativity" and more factual, repeatable answers, which is exactly what you want. Other presets and why they might be less suitable for a helpdesk: Creative: This preset would likely increase Temperature and other randomness parameters, encouraging the model to generate more imaginative and varied text. This is generally not desirable for a helpdesk, where factual accuracy and consistency are paramount. Instruct: While your model is an instruct-tuned model, and your use case is instruction-following, this preset might focus more on general instruction adherence rather than the specific non-creative, deterministic output you need for a helpdesk. It might still allow for more variability than Deterministic. min_p: This likely configures parameters related to min_p sampling, which can be useful but might not inherently lead to the "deterministic" behavior you're aiming for without further tweaking. Qwen3 - Thinking / Qwen3 - No Thinking: These are likely presets specific to the Qwen3 family of models. Since you are using Nous-Hermes-2 Mistral 7B DPO, these Qwen3-specific presets are unlikely to be optimized for your chosen model and might not yield the best results. Recommendation: Start by selecting the Deterministic preset from the dropdown menu shown in image_39cf39.png. After selecting it, still double-check the individual parameters (like Temperature, Repetition Penalty, Max New Tokens) on the "Parameters" tab. You may want to slightly adjust Max New Tokens to ensure responses are sufficiently long for helpdesk solutions (e.g., 256-512 tokens), as a strictly deterministic preset might sometimes favor very short answers. This combination of the Deterministic preset and a strong system prompt should give you an excellent foundation for your helpdesk AI.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
