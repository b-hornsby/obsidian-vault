---
category: coding
date: 2025-07-17
id: 970419
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan wants instructions formatted as a prompt to feed into Cursor for automated
  changes.
tags:
- cursor-ide
- prompt-formatting
- workflow-automation
---
# can you explain that in prompt format so i can feed that to cursor and have it make those changes?

### USER
can you explain that in prompt format so i can feed that to cursor and have it make those changes?

### GEMINI
Here's how you can phrase that as a prompt for Cursor (or any similar AI coding assistant), assuming it has access to your Python workflow file: Cursor Prompt: "Please modify the current Python script to configure it for use with a local Oobabooga text-generation-webui instance acting as an OpenAI-compatible API. Here are the specific changes to implement: Add import os at the very top of the file if it's not already present. Before any CrewAI agents or tasks are defined, add the following lines to set environment variables: os.environ["OPENAI_API_BASE"] = "http://localhost:5000/v1" Important: If your Oobabooga API is on a different port or IP, change http://localhost:5000/v1 to your correct Oobabooga API endpoint (e.g., http://127.0.0.1:5001/v1). os.environ["OPENAI_API_KEY"] = "sk-not-needed-for-local" (This can be a dummy key as Oobabooga's local API doesn't require a real one). os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo" (This is the model name your workflow will request, which Oobabooga will receive but then use its currently loaded model). Context: These changes ensure that any openai library calls made by CrewAI within this script will be directed to your local Oobabooga server, effectively using your loaded model (e.g., Phi-3-mini-4k-instruct-q4) under the gpt-3.5-turbo alias."
