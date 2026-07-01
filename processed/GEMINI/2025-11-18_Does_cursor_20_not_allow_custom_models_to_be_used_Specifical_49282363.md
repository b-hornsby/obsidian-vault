---
category: ai-tools
date: 2025-11-18
id: 676288
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if Cursor 2.0 allows the use of custom models, specifically
  open-source models like Qwen 2.5.
tags:
- cursor-ide
- custom-models
- local-llm
- qwen-2.5
- cursor-2.0
---
# Does cursor 2.0 not allow custom models to be used? Specifically open source models like qwen 2.5

### USER
Does cursor 2.0 not allow custom models to be used? Specifically open source models like qwen 2.5

### GEMINI
It appears that Cursor 2.0 does allow the use of custom models, including open-source ones like the Qwen 2.5 series, though it often requires using a third-party API service that acts as a proxy. Cursor 2.0 is primarily built around its proprietary model, Composer, but it maintains compatibility with external models. 🛠️ How to Use Custom/Open-Source Models While Cursor 2.0 has its own models, you can integrate other models, including open-source ones, by configuring a custom API endpoint that follows the OpenAI API schema: Third-Party Proxy Services: Many users connect open-source models, like Qwen 2.5 Coder 32B Instruct, by using services like OpenRouter. This service provides an API key and a custom base URL that can be entered into Cursor's settings. Custom API Endpoint: In Cursor's settings, under the Models or API Keys tab, you can often find an option to "Override OpenAI Base URL" or "Add Custom Model". This allows you to point Cursor to an API endpoint that hosts the model you want to use. Local LLMs: Running an LLM locally (e.g., using Ollama or another server) is also possible, but it usually requires using a tunneling service (like ngrok) to make your local endpoint publicly accessible so Cursor can connect to it. In short, while Cursor 2.0's native focus is on Composer, its architecture still supports integrating open-source models like Qwen 2.5 via external APIs. Would you like a step-by-step guide on how to try connecting a custom model via a service like OpenRouter?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
