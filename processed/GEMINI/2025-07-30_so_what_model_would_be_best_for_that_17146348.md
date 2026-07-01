---
category: coding
date: 2025-07-30
id: 973364
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for a recommendation on the best model to use for a specific
  purpose (unspecified in this turn).
tags:
- local-llm-model-selection
---
# so what model would be best for that? 

### USER
so what model would be best for that? 

### GEMINI
Based on your question "what model would be best for that?" and the previous context about "rerank," you're asking about which model is best to use for the Rerank capability within Continue.dev. Currently, Continue.dev typically uses a built-in, client-side model for reranking (like the "Transformers.js (Built-In)" option you saw). This is generally the recommended and easiest approach for a local setup like yours for the following reasons: Efficiency and Speed: These built-in models are often highly optimized to run directly in your VS Code environment or browser. This means very low latency for reranking operations, which is crucial for features like instant code suggestions or quick search refinement. No Additional Setup: You don't need to download another large model via Ollama or configure another API key. It just works out of the box with the extension. Specialized for Reranking: While small, these models are specifically trained for the task of semantic similarity and relevance ranking, making them very effective for their purpose. Therefore, for the "Rerank" capability, the "Transformers.js (Built-In)" model is generally the best and most practical choice for most users with your setup. To clarify further: You don't typically run a "rerank" model via Ollama. Ollama is designed for running large language models (LLMs) like Llama 3.1 and Qwen for generation tasks (chat, autocomplete). The "rerank" model is distinct from your main LLM. Your Llama 3.1 or Qwen model will be doing the actual text generation, while the rerank model helps filter the context before it gets to them. Unless you have a very specific advanced use case that requires a custom, external reranker model (which is usually for much larger, enterprise-level RAG systems), sticking with the built-in option in Continue.dev is the way to go for "Rerank." You likely don't need to change anything for that setting.
