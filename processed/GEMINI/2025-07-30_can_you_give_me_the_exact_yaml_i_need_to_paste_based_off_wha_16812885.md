---
id: 092813
source: GEMINI
date: 2025-07-30
tags: ['continue.dev', 'yaml-configuration', 'llama3', 'local-llm-setup']
category: coding
sentiment: executing
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is requesting the correct YAML configuration for Continue.dev based on his existing configuration for a Llama3 model.
---
# can you give me the exact yaml i need to paste based off what i have in there now? ---
name: llama3.1 8b
version: 1.0.1
schema: v1
models:
  - name: llama3.1 8b
    provider: ollama
    model: llama3.1:8b
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    defaultCompletionOptions:
      contextLength: 128000
      

### USER
can you give me the exact yaml i need to paste based off what i have in there now? ---
name: llama3.1 8b
version: 1.0.1
schema: v1
models:
  - name: llama3.1 8b
    provider: ollama
    model: llama3.1:8b
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    defaultCompletionOptions:
      contextLength: 128000
      

### GEMINI
Certainly! Based on your existing config.yaml and the goal of adding qwen2.5-coder:1.5b for autocomplete, here's the exact YAML you need to paste. I've added the qwen2.5-coder:1.5b model entry to your models list, specifically assigning it the autocomplete role. I've also set a reasonable contextLength for it (you can adjust this if needed, check Ollama's model card for specifics). Copy and paste this entire block into your ~/.continue/config.yaml file, overwriting your current content. name: llama3.1 8b version: 1.0.1 schema: v1 models: - name: llama3.1 8b provider: ollama model: llama3.1:8b roles: - chat - edit - apply capabilities: - tool_use defaultCompletionOptions: contextLength: 128000 - name: qwen2.5-coder 1.5b provider: ollama model: qwen2.5-coder:1.5b # This must exactly match the model tag in your Ollama install roles: - autocomplete - chat # Optional: Add 'chat' here if you also want to use Qwen for regular chat defaultCompletionOptions: contextLength: 32768 # Common context length for smaller models, adjust if needed Before you save this file, please double-check one thing: Confirm the exact model name for Qwen in Ollama: In your terminal, run ollama list. Make sure the name of the Qwen model is precisely qwen2.5-coder:1.5b. If it's something slightly different (e.g., qwen2.5-coder-1.5b without the colon, or a different tag), adjust the model: line in the YAML accordingly. After pasting and saving the file, your VS Code Continue.dev extension should refresh, and you'll be able to select "qwen2.5-coder 1.5b" for your autocomplete model.
