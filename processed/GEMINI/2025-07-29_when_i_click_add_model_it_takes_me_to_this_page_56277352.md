---
category: coding
date: 2025-07-29
id: 672391
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is encountering an issue where clicking 'add model' in Continue.dev
  leads to an unexpected page.
tags:
- continue.dev
- model-configuration
- local-llm-setup
---
# when i click add model it takes me to this page 

### USER
when i click add model it takes me to this page 

### GEMINI
I see. Thank you for the new screenshot. This is a bit of a loop, and it indicates that "Add Model" from that specific "Models" overview within the Hub is actually leading you to "Create a new block," which is not what we want for a simple Ollama connection. The "Create a new block" page is for defining new, complex "blocks" that might use a model, but not for simply adding a pre-existing local Ollama model to your assistant. We need to find a different way to add the model to your "LocalCode" assistant. Given this new information, let's try a different path from the main "LocalCode" assistant view. Here's the revised strategy: Go back to the "LocalCode" assistant overview in the Continue Hub. If you're currently on the "Create a new block" page, use your browser's back button or navigate back to the main "LocalCode" assistant page. You know you're on the right page if you see the "LocalCode" name in the top right sidebar, and the central content is about the assistant itself, rather than creating a new block. Look for an "Edit" or "Configure" option for your "LocalCode" assistant. Once you are on the "LocalCode" assistant overview page, scan for options to edit its configuration or settings. This might be a pencil icon, an "Edit" button, or something similar. Within the Assistant's Configuration, look for a way to add models. When you're editing the "LocalCode" assistant directly, there should be a section or tab for "Models" or "Blocks." This is where you should find the option to add an Ollama model. Think of it like this: You've created a container (your "LocalCode" assistant). You now need to put a specific item (your llama3.1:8b-instruct-q4_K_M model) into that container. The "Create a new block" page is like building a new type of item, not selecting an existing one. If you can get to the main "LocalCode" assistant page, please send a screenshot of that page. This will help me guide you to the exact button or link to add the model to it. We need to find the specific UI element that lets you select existing models (like those you saw listed under Ollama previously) and associate them with your "LocalCode" assistant. It's likely within the assistant's own settings/edit page.
