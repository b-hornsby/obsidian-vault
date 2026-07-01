---
id: 611674
source: GEMINI
date: 2025-07-30
tags: ['local-llm-performance', 'recursion', 'response-time']
category: coding
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is comparing the response time of his local LLM for the same query about recursion.
---
# i asked the same Explain the concept of recursion in programming question and now the response is 19sec

### USER
i asked the same Explain the concept of recursion in programming question and now the response is 19sec

### GEMINI
That's fantastic news! A drop from 1 minute 12 seconds to 19 seconds for an 8B model on your RTX 3070 is a significant and expected performance improvement. This strongly suggests that: Ollama is now successfully utilizing your RTX 3070 GPU. This is the biggest factor in performance for LLMs. The contextLength adjustment (if you made it) also likely played a role, helping to reduce the memory footprint and processing overhead. The model is now properly loaded and ready to serve requests from your Ollama instance. While 19 seconds might still feel a bit slow for a very short answer, it's a completely different league from over a minute, and much closer to what's expected for that model size and hardware. The exact speed can vary based on: The complexity and length of the response. Other background processes on your system. The specific quantization of the model (q4_K_M is good, but slight variations can exist). What to do now: Continue using it! Experience the difference in your daily workflow. Keep an eye on your Ollama terminal. You should see consistent POST "/api/generate" or POST "/api/chat" entries with 200 status codes and much faster response times in milliseconds/seconds (...ms or ...s). Test Autocomplete: Try typing code in VS Code to see how qwen2.5-coder:1.5b performs for real-time suggestions. It should be very fast due to its smaller size. You've successfully overcome the initial hurdles and optimized your local LLM setup. Great work!
