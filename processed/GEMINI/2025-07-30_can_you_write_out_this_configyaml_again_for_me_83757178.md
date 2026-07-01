---
category: coding
date: 2025-07-30
id: 044283
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan is asking for the config.yaml file to be rewritten, likely due to errors
  or needing a fresh start.
tags:
- continue.dev
- yaml-configuration
- local-llm-setup
---
# can you write out this config.yaml again for me? 

### USER
can you write out this config.yaml again for me? 

### GEMINI
name: llama3.1 version: 1.0.1 schema: v1 models: - name: llama3.1 8b provider: ollama model: llama3.1:8b-instruct-q4_K_M roles: - chat - edit - apply capabilities: - tool_code defaultCompletionOptions: contextLength: 8192 - name: qwen2.5-coder 1.5b provider: ollama model: qwen2.5-coder:1.5b roles: - autocomplete defaultCompletionOptions: contextLength: 4096
