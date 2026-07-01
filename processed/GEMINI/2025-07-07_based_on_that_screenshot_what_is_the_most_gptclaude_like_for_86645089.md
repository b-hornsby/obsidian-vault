---
category: ai-tools
date: 2025-07-07
id: 16445
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking which local LLM model is most similar to GPT/Claude based
  on a screenshot he shared.
tags:
- model-selection
- gpt-claude-alternative
- local-llm
- model-comparison
---
# based on that screenshot what is the most gpt/claude like for that model? 

### USER
based on that screenshot what is the most gpt/claude like for that model? 

### GEMINI
Okay, looking specifically at the screenshot you provided, and given the options visible, there isn't a directly labeled preset like "GPT-like" or "Claude-like." However, we can infer the best choice from the common understanding of how these parameters influence model behavior, and based on what those top-tier models prioritize: coherence, instruction following, and less "random" output. Given the screenshot, if there is a dropdown menu that contains presets, you'll need to select one that typically emphasizes: Lower Temperature: To make the output more deterministic and factual. Moderate Top P: To maintain diversity without going off the rails. Stronger Repetition Penalties: To prevent repetitive phrases, which GPT and Claude models are generally very good at avoiding. Based on common naming conventions for presets in tools like Oobabooga's Text Generation WebUI (which this interface strongly resembles), the most "GPT/Claude-like" preset you're likely to find or aim for would be one that is described as: "Precise" "Instruction-tuned" "Coherent" "Llama-Precise" (if present, this is a common one) "Divine Intellect" (if present, often aims for logical, coherent responses) If those specific names aren't visible in the dropdown, look for a preset that, when selected, results in the following initial parameter values (or as close as possible): Temperature: Around $0.7$ to $0.8$ (lower is generally more "factual" for instruction following). Top P: Around $0.8$ to $0.9$. Repetition Penalty: $1.1$ or higher. Frequency Penalty / Presence Penalty: Often set to $0$ in many presets, but if one has them slightly above $0$, that's a good sign for reducing verbosity and repetition. Actionable Steps: Locate the Presets Dropdown: In your screenshot, it's not immediately obvious where the preset dropdown is, but it's typically within the "Generation" tab, often near the top under "Sampling options" or in its own "Presets" section. Experiment: Select a preset that sounds like it would prioritize precision or instruction following. Inspect and Adjust: After selecting a preset, immediately look at the values for Temperature, Top P, Repetition Penalty, Frequency Penalty, and Presence Penalty. Adjust them manually to the values I recommended in the previous answer if the preset doesn't quite match. For example, if a "Precise" preset sets Temperature to $0.7$, that's good. But if it has Repetition Penalty at $1.0$, you'll want to manually increase it to $1.15$ or $1.2$. Without seeing the list of available presets in your dropdown, I can only guide you on what to look for and how to manually adjust after selecting one. The manual adjustments are often the most crucial step to fine-tune the behavior for your specific model and desired output.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
