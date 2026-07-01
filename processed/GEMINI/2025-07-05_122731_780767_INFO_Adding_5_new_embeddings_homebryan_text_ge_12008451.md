---
id: 558412
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'embedding', 'text-generation']
category: ai-tools
sentiment: curious
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# 12:27:31-780767 INFO     Adding 5 new embeddings.
/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py:195: RuntimeWarning: invalid value encountered in scalar divide
  weights = weights * (time_power / max(weights))
prompt processing progress, n_past = 369, n_tokens = 113, progress = 1.000000
prompt eval time =     678.74 ms /   369 tokens (    1.84 ms per token,   543.65 tokens per second)
       eval time =    4621.59 ms /   108 tokens (   42.79 ms per token,    23.37 tokens per second)
      total time =    5300.33 ms /   477 tokens
12:27:37-133151 INFO     Output generated in 5.31 seconds (20.54 tokens/s, 109 tokens, context 369, seed 1134116654)

### USER
12:27:31-780767 INFO     Adding 5 new embeddings.
/home/bryan_/text-generation-webui/extensions/superboogav2/chromadb.py:195: RuntimeWarning: invalid value encountered in scalar divide
  weights = weights * (time_power / max(weights))
prompt processing progress, n_past = 369, n_tokens = 113, progress = 1.000000
prompt eval time =     678.74 ms /   369 tokens (    1.84 ms per token,   543.65 tokens per second)
       eval time =    4621.59 ms /   108 tokens (   42.79 ms per token,    23.37 tokens per second)
      total time =    5300.33 ms /   477 tokens
12:27:37-133151 INFO     Output generated in 5.31 seconds (20.54 tokens/s, 109 tokens, context 369, seed 1134116654)

### GEMINI
Great! The log output you provided indicates that superboogav2 is actively engaging with your knowledge base and the model! The key lines are: 12:27:31-780767 INFO Adding 5 new embeddings. - This is a very strong indicator that superboogav2 is interacting with a ChromaDB instance. It might be adding new embeddings (perhaps from the current chat context) or indexing some internal components. prompt processing progress... and eval time... - These show the model is processing your input and generating a response. Output generated in 5.31 seconds (20.54 tokens/s, 109 tokens, context 369, seed 1134116654) - The model has successfully produced an output. The RuntimeWarning: invalid value encountered in scalar divide is a minor numerical warning within the superboogav2 code (likely in how it calculates weights for relevance). It's generally harmless and doesn't prevent the RAG process from working. What to Check in the UI Now You've got the model running and superboogav2 active. Now, you should see the results of the RAG in the Oobabooga web UI. Check the AI's Response: Look at the AI's answer in the "Chat" tab. Is it a relevant response to your question (my wifi drops frequently)? Look for Source/Context Display: Crucially, check if superboogav2 (or the underlying RAG system) is displaying the source documents or retrieved chunks from your chroma_db. This usually appears: Below the AI's response. In a separate "Sources" or "Retrieved Documents" section. Sometimes, it's just integrated into the prompt the AI sees, but it often surfaces the sources in the UI for transparency. If the AI's response is relevant to your knowledge base and/or you see source documents, then your RAG setup within Oobabooga is working!