---
id: 123795
source: GEMINI
date: 2025-06-25
tags: ['llm-parameters', 'hardware-optimization', 'local-llm', 'rtx-3070']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md', 'nodes/projects/private-ai-consulting.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan asked about the best LLM parameters for his specific hardware use case.
---
# What would be the best parameters to use for this specific use case  given my specs? 

### USER
What would be the best parameters to use for this specific use case  given my specs? 

### GEMINI
You've asked about the "best parameters" for your specific use case (personal helpdesk AI) given your specs, which include a working CUDA setup for GPU acceleration. The Oobabooga UI (as shown in image_397582.jpg) offers many parameters. Here's a breakdown of the most impactful parameters and recommended settings for a helpdesk AI, explaining why each setting is chosen for this specific use case: Key Principle for Helpdesk AI Parameters: You want responses that are accurate, consistent, factual, clear, and non-creative. This means favoring settings that reduce randomness and steer the model towards reliable, instruction-following behavior. On the "Parameters" Tab in Oobabooga (image_397582.jpg) 1. Temperature (Most Important) Location: Under "Curve shape" Recommended Value: 0.5 to 0.7 (Start at 0.7 and go lower if responses are still too creative/unreliable). Why: Temperature controls the randomness of the output. For a helpdesk, you want deterministic, factual, and consistent answers, not creative ones. Lower temperatures lead to more focused and predictable responses, reducing the chance of "hallucinations" or imaginative solutions. 2. Top P Location: Under "Curve cutoff" Recommended Value: 0.9 to 0.95 (Default is often fine, or slightly lower than 1.0) Why: Top P (nucleus sampling) selects tokens whose cumulative probability exceeds a threshold. A lower Top P restricts the model to more probable (and thus often more factual/reliable) words, reducing diversity. 3. Top K Location: Under "Curve cutoff" Recommended Value: 40 to 50 (Default is usually good, or slightly lower than 100) Why: Top K selects from the K most probable next tokens. Similar to Top P, restricting this number (but not too much) can help focus the model on more sensible outputs. Too low can make it repetitive. 4. Repetition Penalty Location: Under "Repetition suppression" Recommended Value: 1.1 to 1.15 Why: This prevents the model from repeating words, phrases, or even entire sentences, which is common in generated text and especially undesirable in step-by-step instructions. 5. Max New Tokens (Response Length) Location: Top right, under "Filter by length" Recommended Value: 256 to 512 (adjust as needed) Why: This sets the maximum length of the AI's response. For helpdesk, you want sufficiently detailed answers but not excessively long ramblings. 256 tokens is often enough for a concise solution, while 512 provides room for more detailed explanations or multi-step processes. Adjust based on how verbose you need the answers to be. 6. Min P (Optional, Can Experiment) Location: Under "Curve cutoff" Recommended Value: 0.0 to 0.05 (If you want to filter out very low probability tokens that might be nonsensical) Why: This prunes tokens below a certain probability. It can help filter out truly random or irrelevant words. Other Parameters (Generally Leave Defaults or Keep Disabled): ** mirostat / dynamic_temperature / typical_p / tfs / custom_token_presence / frequency / presence_penalty / temperature_last / do_sample / early_stopping / num_beams / no_repeat_ngram_size / encoder_repetition_penalty / do_sample / length_penalty / num_return_sequences / output_scores / output_attentions / output_hidden_states / return_dict_in_generate / min_length / max_length / seed / max_time / num_beams:** These often relate to more advanced or creative generation techniques (like beam search for higher quality outputs, but slower; or specific sampling methods). For a helpdesk, the primary parameters above are usually sufficient. Keep do_sample enabled if it's there (it's essential for any form of temperature/top_p/top_k sampling). Combined with your System Prompt: Remember, these parameters work in conjunction with your system prompt. The parameters control how the model picks words, while the system prompt tells the model what persona to adopt and what kind of information to prioritize. For example, a low temperature will make the model more likely to follow your system prompt's instructions about "clear, concise, and accurate solutions." Actionable Steps: Open Oobabooga's web UI. Go to the "Parameters" tab. Adjust the Temperature, Top P, Top K, Repetition Penalty, and Max New Tokens sliders/input boxes to the recommended values. Go back to the "Chat" tab and ensure your strong system prompt (as discussed in the previous response) is active. Test the model with various helpdesk queries and fine-tune these parameters slightly based on its performance. You might slightly increase temperature if it's too rigid, or decrease it if it's too creative. By combining well-chosen parameters with a robust system prompt, you'll optimize Nous-Hermes-2 Mistral 7B DPO to perform as an effective personal helpdesk AI.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
