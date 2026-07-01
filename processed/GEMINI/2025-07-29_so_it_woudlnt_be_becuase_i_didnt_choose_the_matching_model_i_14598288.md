---
id: 080653
source: GEMINI
date: 2025-07-29
tags: ['continue.dev', 'model-selection', 'ollama', 'configuration']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking whether the issue is caused by not selecting the matching model name in continue.dev's configuration.
---
# so it woudln't be becuase i didn't choose the matching model in here? 

### USER
so it woudln't be becuase i didn't choose the matching model in here? 

### GEMINI
No, it wouldn't be because you didn't choose the matching model in that "Add Chat model" dialog. Here's why: You already have a config.yaml: Your config.yaml file (seen in image_987f22.png and image_98dcb4.png) is already correctly set up to define your llama3.1:8b-instruct-q4_K_M model. The "Add Chat model" dialog updates your config.yaml: That dialog is designed to help users create or modify their config.yaml file. If your config.yaml is already correct, that dialog isn't necessary for the model to be recognized. The core problem is the extension itself: The primary issue is that the continue.dev extension isn't fully initializing. This is indicated by two key symptoms: The "Continue" output channel is missing from the VS Code Output dropdown. The continue.dev sidebar still says "No models configured," implying it hasn't even read your existing config.yaml yet. If the extension were working properly, it would automatically detect and display your "Llama 3.1 8B Local (Ollama)" model from your config.yaml in the "Select model" dropdown, without you needing to interact with the "Add Chat model" dialog. So, the problem isn't the model choice; it's the extension's ability to operate at a fundamental level in your VS Code environment. Given that all standard troubleshooting has failed and you prefer not to use VS Code Insiders, filing a detailed bug report on the continue.dev GitHub page remains the most effective next step. You've gathered excellent diagnostic information for them.
