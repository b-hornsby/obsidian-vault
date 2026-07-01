---
id: 615250
source: GEMINI
date: 2025-07-29
tags: ['continue.dev', 'ollama', 'status-update']
category: ai-tools
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is providing a status update on where he stands with the continue.dev and Ollama setup process.
---
# this is where i am now 

### USER
this is where i am now 

### GEMINI
Excellent! This is precisely the page we needed to get to. You're now on the configuration page for your "LocalCode" assistant. Here's how to add your llama3.1:8b-instruct-q4_K_M model from this page: Locate the "Models" section: You'll see a section titled "Models" with an icon of a cube and the text "No models have been configured." Click the "Explore" button within the "Models" section: Directly under the "No models have been configured" text, you'll see two buttons: "Create" and "Explore." Click "Explore." Why "Explore"? "Explore" here means "explore existing model blocks" that you can add to your assistant. "Create" would take you back to the "Create a new block" page, which is not what we want. Search for Ollama Models (if necessary): Clicking "Explore" should take you to a page similar to the one you were on before, where you saw all the model cards (Claude, Gemini, etc.), but now specifically for adding to this assistant. You can use the search bar at the top of that page to type "ollama" to quickly filter the results. Click the "+" button next to "llama3.1:8b": Once you find the llama3.1:8b card (or similar llama3.1 variant), click the "+" button on that card. Confirm the Addition: You might get a small confirmation prompt. Confirm that you want to add this model. What happens next: Model will appear in "LocalCode" assistant: After adding it, you should be redirected back to this "LocalCode" assistant configuration page, and your llama3.1:8b model will now be listed under the "Models" section. Synchronization with VS Code: The Continue.dev VS Code extension should then sync this change, and you'll be able to select your Llama 3.1 model within the extension's settings. Final Check in VS Code: Open VS Code, go to the Continue.dev sidebar, and navigate to the "Models" settings to confirm that llama3.1:8b is now an available option for your "Chat" and/or "Autocomplete" model. This is the correct path to associate a pre-defined model (like your local Ollama Llama 3.1) with your custom assistant.
