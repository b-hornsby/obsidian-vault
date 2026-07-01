---
id: 983908
source: GEMINI
date: 2025-07-30
tags: ['ollama', 'model-name', 'local-llm-setup']
category: coding
sentiment: executing
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is providing the exact name of the model he's using in his offline Ollama setup.
---
# this is the name of the model in my offline terminal/ollama setup:llama3.1:8b-instruct-q4_K_M 

### USER
this is the name of the model in my offline terminal/ollama setup:llama3.1:8b-instruct-q4_K_M 

### GEMINI
Got it, thank you for clarifying the exact name: llama3.1:8b-instruct-q4_K_M. This is crucial. The error message "Model 'llama3.1:8b' is not found in Ollama" means that Ollama didn't find a model with the tag llama3.1:8b. It was looking for that specific tag because that's what was in your config.yaml. Since your locally installed model is llama3.1:8b-instruct-q4_K_M, you need to update your config.yaml to use this exact name. Here's the corrected config.yaml snippet you should use: name: llama3.1 8b version: 1.0.1 schema: v1 models: - name: llama3.1 8b provider: ollama model: llama3.1:8b-instruct-q4_K_M # <-- **CHANGED THIS LINE** roles: - chat - edit - apply capabilities: - tool_use defaultCompletionOptions: contextLength: 128000 - name: qwen2.5-coder 1.5b provider: ollama model: qwen2.5-coder:1.5b # Assuming this is correct from your Ollama list roles: - autocomplete - chat # Optional: Add 'chat' here if you also want to use Qwen for regular chat defaultCompletionOptions: contextLength: 32768 Steps to fix: Open your ~/.continue/config.yaml file in VS Code. Change the model: line for your Llama 3.1 entry from model: llama3.1:8b to model: llama3.1:8b-instruct-q4_K_M. Save the config.yaml file. Ensure your Ollama terminal is running with llama3.1:8b-instruct-q4_K_M loaded. (Optional but recommended for a clean test) Disconnect from the internet. Go back to Continue.dev chat in VS Code and try asking your question again. Now, when Continue.dev sends a request to Ollama, it will ask for the exact model name that Ollama actually has installed, resolving the "not found" error.
