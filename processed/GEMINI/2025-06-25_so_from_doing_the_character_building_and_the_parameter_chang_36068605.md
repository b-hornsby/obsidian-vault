---
id: 786820
source: GEMINI
date: 2025-06-25
tags: ['oobabooga-character', 'model-parameters', 'next-steps', 'llm-configuration']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan had completed character building and parameter changes in oobabooga and was asking what the next step should be.
---
# so from doing the character building and the parameter changes, whats next?

### USER
so from doing the character building and the parameter changes, whats next?

### GEMINI
Now that you've done the character building (setting the system prompt in the "Context" box) and adjusted the generation parameters (like setting "Deterministic" preset and adjusting Temperature, Top P, etc.), you're ready for the most important step: testing and iterating! Here's what's next: Go to the "Chat" Tab in Oobabooga. This is where you'll interact directly with your AI helpdesk assistant. Start asking questions as if you were a user needing helpdesk support. Common Scenarios: "My printer isn't working. It says 'Error 404'." (Test its troubleshooting steps for a common, but slightly nonsensical, error). "How do I connect to the Wi-Fi?" "I forgot my password for [example software], what should I do?" "My computer is running very slow." "Can you help me install [example software]?" Test its limitations: Ask questions that require external knowledge not in its training data (e.g., "What's the latest update to our company's VPN policy from yesterday?"), or that require personal information it shouldn't ask for. See how it handles these (it should ideally state its limitations and suggest contacting a human). Test its persona: See if it maintains the polite, patient, and thorough tone you defined in the system prompt. Evaluate its responses. Are the answers clear and easy to understand? Are the instructions step-by-step and logical? Does it maintain the helpdesk persona? Does it avoid making things up (hallucinations)? Does it appropriately admit when it doesn't know something or needs more information? Iterate and Refine (The Ongoing Process): Based on your testing, go back to the "Character" tab (Context) or the "Parameters" tab. If the tone or general behavior isn't right: Tweak your system prompt in the "Context" box. Add more specific instructions, refine existing ones, or emphasize certain aspects (e.g., "Be extremely concise," or "Always provide numbered lists for steps"). If the output is too creative/random, too repetitive, or too short/long: Adjust the parameters on the "Parameters" tab. Too random/creative: Lower Temperature further (e.g., to 0.6 or 0.5). Too repetitive: Slightly increase Repetition Penalty (e.g., from 1.1 to 1.15 or 1.2). Too short: Increase Max New Tokens. Too long: Decrease Max New Tokens. After making changes, remember to click the "Save character" button (if you changed the context) and then test again. This iterative process of testing, evaluating, and refining your system prompt and parameters is key to making your LLM truly shine as a customized helpdesk assistant.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
