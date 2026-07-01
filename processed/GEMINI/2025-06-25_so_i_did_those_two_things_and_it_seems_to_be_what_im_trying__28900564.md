---
id: 555257
source: GEMINI
date: 2025-06-25
tags: ['oobabooga-tabs', 'ui-navigation', 'feature-discovery', 'llm-ui']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan confirmed he was on the right track with oobabooga configuration and was asking about the purpose/function of a specific tab in the UI.
---
# so i did those two things and it seems to be what i'm trying to build here. what about this tab? : 

### USER
so i did those two things and it seems to be what i'm trying to build here. what about this tab? : 

### GEMINI
You're referring to the tab in image_39e1a7.jpg. This tab is the "Training" tab in Oobabooga's web UI. Specifically, this tab provides options for LoRA training (Low-Rank Adaptation), which is a form of fine-tuning. What this tab is for: This tab allows you to: Take an existing pre-trained LLM (like Nous-Hermes-2 Mistral 7B DPO that you've downloaded). Train a small adapter layer (LoRA) on top of it using your own custom dataset. This allows the model to learn new patterns, facts, or styles without retraining the entire huge model. Save this LoRA adapter. You can then load it alongside your base model to imbue it with the new knowledge or behavior you've trained it on. When you would use this tab for your helpdesk AI: If you have a large, specific dataset of helpdesk interactions: This means actual conversations between users and helpdesk agents, or structured Q&A pairs directly related to your private, internal, or highly specific helpdesk information. This data needs to be formatted in a way suitable for training. If you want the model to learn a very specific tone, jargon, or way of structuring answers that is unique to your helpdesk and cannot be adequately achieved through just prompt engineering. If you want the model to "know" specific facts or procedures directly without needing to retrieve them via RAG every time. However, for factual knowledge, RAG is usually more scalable and easier to update. What you would put here (high-level): Data Format: You would need to prepare your training data (e.g., helpdesk conversations) in a specific format (e.g., text files with prompt/response pairs, or JSONL files). Dataset: You'd upload or specify the path to this prepared dataset. LoRA Rank / Alpha: These are parameters that control the size and strength of the LoRA adapter. Higher values mean a more powerful (but larger) adapter that can learn more, but might also lead to "catastrophic forgetting" of the base model's general knowledge if pushed too far. Epochs: How many times the model goes through your entire dataset during training. Learning Rate: How quickly the model adjusts its weights during training. Many other advanced training parameters. Is this tab something you need to use right now for your personal helpdesk AI? Probably not immediately. As we discussed earlier, prompt engineering (setting the "System prompt" and adjusting basic parameters) is your first and most powerful tool. It's much easier, faster, and requires no special data or training. Retrieval Augmented Generation (RAG) is the next step if you want your AI to answer questions based on your specific, private knowledge base (like internal documents, unique procedures, etc.). This doesn't involve the "Training" tab directly; it's an external system that feeds context to the LLM. Fine-tuning (using this "Training" tab) is an advanced step. It's typically considered when: You've exhausted the possibilities of prompt engineering and RAG. You have a truly unique dataset of interactions that you want the model to learn from directly. You have the computational resources (VRAM, time) to perform training, which is much more demanding than just running inference. You are comfortable with the complexities of data preparation for training and monitoring training progress. Recommendation: For now, focus on mastering prompt engineering and interacting with your Nous-Hermes-2 Mistral 7B DPO model in the "Chat" tab, combined with the "Deterministic" preset and adjusted parameters. This will get you 90% of the way to a great personal helpdesk AI. Keep the "Training" tab in mind for the future, but it's not a beginner-friendly feature and might not even be necessary for your specific goal if RAG proves sufficient later on.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
