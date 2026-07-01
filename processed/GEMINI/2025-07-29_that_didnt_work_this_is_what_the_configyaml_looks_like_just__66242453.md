---
category: ai-tools
date: 2025-07-29
id: 190439
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is sharing his continue.dev config.yaml to troubleshoot why the Ollama
  model connection isn't working.
tags:
- continue.dev
- config.yaml
- ollama
- configuration
---
# that didn't work. this is what the config.yaml looks like just to confirm: 

### USER
that didn't work. this is what the config.yaml looks like just to confirm: 

### GEMINI
Thank you for the updated screenshot of your config.yaml. You're very close! The issue is with the indentation and the model: AUTODETECT entry you've added. In YAML, indentation is extremely important. It defines the structure and hierarchy of the data. Your llama3.1 model configuration is currently indented one level too far, making it a sub-item of AUTODETECT which isn't what we want. Also, AUTODETECT is a separate provider configuration, not part of the llama3.1 model entry. Let's correct it. Here's how your config.yaml should look, with the corrected indentation and structure: name: Local Assistant version: 1.0.0 schema: v1 models: - title: Llama 3.1 8B Local (Ollama) provider: ollama model: llama3.1:8b-instruct-q4_K_M apiBase: http://localhost:11434 - title: Autodetect provider: ollama model: AUTODETECT context: - provider: code - provider: docs - provider: diff - provider: terminal - provider: problems - provider: folder - provider: codebase Key changes and why: Line 5: models: This is the top-level list where all your model configurations go. Line 6: - title: Llama 3.1 8B Local (Ollama) Crucial: This line needs to be indented with two spaces from the models: line. The hyphen - signifies an item in a list. All the properties underneath it (provider, model, apiBase) must be indented four spaces from the models: line (or two spaces from the - title: line). Lines 10-12: The Autodetect Model (Optional but good to have) I've added back the Autodetect model configuration. This is usually helpful as a fallback or for when you want Ollama to try to automatically pick a model. Crucial: This Autodetect entry also needs to start with a hyphen - and be indented two spaces from the models: line, just like your Llama 3.1 entry. They are both separate items in the models list. What to do now: Carefully copy the corrected YAML code above. Paste it into your config.yaml file in VS Code, overwriting the current models section. Save the config.yaml file. (Ctrl + S on Windows). Check the Continue.dev sidebar again. It should now properly recognize and list "Llama 3.1 8B Local (Ollama)" in its model dropdown. The ! exclamation mark and red squiggly under name: Autodetect in your screenshot confirm that the YAML parser in VS Code detected an indentation error there. Correcting the indentation will resolve that.
