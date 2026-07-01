---
id: 580413
source: GEMINI
date: 2025-11-17
tags: ['cursor-ide', 'local-llm-integration', 'coding-environment', 'cursor-2.0']
category: coding
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is providing context that he's using Cursor 2.0, hoping it helps narrow down the solution for integrating a local LLM.
---
# i want to also let you know that i'm using cursor 2.0 for this so the model should be able to be used in that way specifically if that helps narrow it down 

### USER
i want to also let you know that i'm using cursor 2.0 for this so the model should be able to be used in that way specifically if that helps narrow it down 

### GEMINI
That context is critical and narrows the choice to models that are not only powerful but also compatible with Cursor's specific way of integrating local LLMs via an OpenAI-compatible API and ngrok. The absolute best production-ready model you should use remains the Qwen3-Coder-30B (4-bit Quantization). However, the compatibility requirement means you must use a model that has good function calling or tool use capabilities if you intend to use advanced Cursor features like Composer or Agent Mode. 🥇 Final Recommendation: Qwen3-Coder-30B (4-bit) Model: Qwen3-Coder-30B (use the 4-bit quantized version, e.g., qwen3:30b-a3b-q4_K_M if available, or the standard qwen3:30b and let Ollama handle quantization). Why it's the Best Fit: Quality: It is frequently cited in community discussions as one of the very few open-source models that approaches the quality of closed-source models like Claude Sonnet 4.5 and GPT-4 for complex coding, debugging, and refactoring. Hardware: The 30B parameter size is the largest you can realistically run on your 32GB RAM/8GB VRAM system by leveraging CPU offloading through Ollama's GGUF support. Cursor Compatibility: Qwen models, in general, are mentioned as working with local setups for Cursor. ⚠️ The Cursor Compatibility Caveat (Tool Use) The biggest challenge with running local models in Cursor is that Cursor's advanced features (Composer and Agent Mode) often rely on the model supporting tool calling (or function calling) via the OpenAI API format. Some community reports have specifically noted issues with the Qwen3 model's tool use when proxied through the OpenAI API endpoint, giving an error like ...does not support tools. If you find that the Qwen3-Coder-30B does not work with Cursor's Agent/Composer modes, this is a known limitation of using certain open-source models with Cursor's server-side logic. Solution: If the Qwen3 model is too restricted, your best alternative is to move down to a top-tier model that is known for good OpenAI-API compatibility and tool use, which brings us to the second recommendation. 🥈 Top Alternative: DeepSeek-Coder-V2 (MoE) If the Qwen model proves too slow or lacks compatibility with Cursor's advanced modes, the fastest and most highly-regarded alternative is the DeepSeek series. Model: DeepSeek-Coder-V2 (Mixture-of-Experts/MoE) Why it's a Strong Alternative: Speed & Quality: The V2 model is a MoE, which means its quality is higher than its active parameter count suggests, and it's significantly faster than a non-MoE 30B model. Its performance rivals GPT-4 Turbo. Hardware Fit: While its largest version is too big, look for smaller, highly performant versions like deepseek-coder:1.3b (for blazing fast completion) or a highly-quantized 7B/8B version for fast chat/edit, as they will load fully onto your 8GB VRAM. ⚙️ Summary of Ollama/ngrok Setup Steps To ensure the best experience with Cursor 2.0, you must follow these steps: Pull Model in Ollama: ollama pull qwen3:30b-instruct (or whichever model you choose). Start ngrok: Tunnel your Ollama API endpoint (default is usually localhost:11434) to a public URL. This is mandatory for Cursor as it cannot access localhost. Set CORS: You might need to set an environment variable for Ollama before starting it to allow requests from the ngrok domain: export OLLAMA_ORIGINS=* (Windows setup will be slightly different). Configure Cursor: Go to Preferences -> Models. Find the "Override OpenAI Base URL" setting. Input your ngrok public URL followed by /v1 (e.g., https://<random_id>.ngrok-free.app/v1). Enter a placeholder API Key (e.g., Ollama). Set the Model Name to the exact name you pulled in Ollama (e.g., qwen3:30b-instruct). This guide provides a detailed walkthrough of how to connect a local LLM to Cursor using Ollama and ngrok. Running Local AI Models in Cursor with Ollama and ngrok


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
