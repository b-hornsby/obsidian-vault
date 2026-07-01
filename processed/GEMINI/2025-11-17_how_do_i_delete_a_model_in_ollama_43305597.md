---
category: ai-tools
date: 2025-11-17
id: 541984
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to delete a model in Ollama, likely to manage resources
  or test different models.
tags:
- ollama
- model-management
- local-llm
- resource-optimization
---
# how do i delete a model in ollama? 

### USER
how do i delete a model in ollama? 

### GEMINI
The easiest and recommended way to delete a model in Ollama is by using the Command Line Interface (CLI) command ollama rm. Here are the steps: 1. List Your Installed Models First, you should list all the models you have installed to get the exact name (including the tag, like :latest or :7b): ollama list This will output a table of your models. Note the NAME of the model you wish to delete (e.g., llama3:8b). 2. Remove the Model Use the ollama rm command followed by the exact model name. ollama rm <model-name> Example: To delete the model named llama3:8b: ollama rm llama3:8b Ollama will then confirm that the model has been deleted, and the associated files will be removed (note that shared model components, called "blobs," will only be deleted if no other installed model is using them). 3. Verify the Deletion You can run the ollama list command again to confirm that the model no longer appears in your list. ollama list Note: If the model is currently running or in use, you may need to stop it before deleting it. You can try stopping the model first with ollama stop <model-name> and then running the ollama rm command.
