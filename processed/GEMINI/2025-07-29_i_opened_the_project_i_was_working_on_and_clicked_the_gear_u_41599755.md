---
id: 680150
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ollama', 'ai', 'gemini', 'model', 'defi', 'go', 'code']
category: coding
sentiment: exploratory
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
---
# i opened the project i was working on and clicked the gear under the select model tab and it opened the config.yaml (path looks like users>Bryan>.continue>config.yaml)

### USER
i opened the project i was working on and clicked the gear under the select model tab and it opened the config.yaml (path looks like users>Bryan>.continue>config.yaml)

### GEMINI
Okay, this is excellent progress! You've found the correct configuration file, and it's good that it's config.yaml as Continue also supports YAML, which can be a bit cleaner to read than JSON sometimes. The screenshot shows that your models section is currently empty: models: []. This is why it says "No models configured" in the Continue sidebar. You just need to add the Llama 3.1 model configuration into that models section. Here's how to edit your config.yaml file: Locate the models: line. It's on line 5 in your screenshot. Add the Llama 3.1 model configuration underneath it. Make sure the indentation is correct (it's crucial in YAML!). There should be two spaces of indentation before the hyphen - that starts the model definition, and then more spaces for the key-value pairs. Here's the exact content you should paste into your config.yaml: name: Local Assistant version: 1.0.0 schema: v1 models: - title: Llama 3.1 8B Local (Ollama) provider: ollama model: llama3.1:8b-instruct-q4_K_M apiBase: http://localhost:11434 context: - provider: code - provider: docs - provider: diff - provider: terminal - provider: problems - provider: folder - provider: codebase Explanation of the changes: - title: Llama 3.1 8B Local (Ollama): This defines a new model entry. title is what you'll see in the dropdown in Continue. provider: ollama: Specifies that this model uses the Ollama backend. model: llama3.1:8b-instruct-q4_K_M: This is the exact name of the model you downloaded and want to use. apiBase: http://localhost:11434: This tells Continue where your Ollama server is running (the default local address). After you paste this into config.yaml: Save the config.yaml file. (Ctrl + S on Windows, or File > Save). Check the Continue Sidebar in VS Code. It should automatically update. You might see a small "Reload" button or it might refresh instantly. The "Select model" dropdown should now show "Llama 3.1 8B Local (Ollama)" as an option. Make sure that model is selected. Once you see your model in the dropdown, you're all set! You can then start typing your scaffolding prompts in the "Ask anything..." box.