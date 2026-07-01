---
id: 158346
source: GEMINI
date: 2025-07-29
tags: ['continue.dev', 'vs-code', 'configuration']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking whether any additional configuration is needed in VS Code for continue.dev to work with his Ollama model.
---
# do i need to do anything here? 

### USER
do i need to do anything here? 

### GEMINI
No, you do not need to do anything in that "Add Chat model" dialog. You've already correctly configured your llama3.1:8b-instruct-q4_K_M model directly in the config.yaml file, which is the preferred and most robust way to manage your models in Continue.dev. That "Add Chat model" dialog is an alternative, more guided way to add models, but it ultimately does the same thing: it tries to update your config.yaml file for you. Since you've already done that manually and correctly, there's no need to use this dialog. What you should see now (and your next step): Close that "Add Chat model" dialog. Just click the 'x' in the top right corner. Look at the "Select model" dropdown directly above it in the Continue.dev sidebar. Click on that "Select model" dropdown. You should now see "Llama 3.1 8B Local (Ollama)" (or whatever title you gave it in config.yaml) as an option. Select "Llama 3.1 8B Local (Ollama)" from the dropdown. Once that model is selected, the "Ask anything..." input box will become active, and you can start interacting with Llama 3.1 for your scaffolding tasks!
