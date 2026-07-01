---
category: coding
date: 2025-07-29
id: 176086
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is having trouble setting up a chat model in Continue.dev and is stuck
  on the 'how to' page.
tags:
- continue.dev
- chat-model-setup
- local-llm-setup
---
# when i clicked setup chat model it took me to the how to page and i went to the continue hub and this is where i am

### USER
when i clicked setup chat model it took me to the how to page and i went to the continue hub and this is where i am

### GEMINI
Got it. So when you clicked "Setup Chat model" in the VS Code extension, it directed you to the Continue Hub (the webpage in your second image) instead of directly letting you configure the model within VS Code. This usually means that the VS Code extension is designed to use the Continue Hub as the central place for model management, especially for discovering and adding models. Here's how you should proceed from the Continue Hub to get your llama3.1:8b-instruct-q4_K_M model working: Goal: Get your llama3.1:8b-instruct-q4_K_M model (running locally via Ollama) recognized and usable by the Continue.dev extension in VS Code. Steps from the Continue Hub: Look for an "Add Custom Model" or "Self-Hosted Model" Option: On the Continue Hub page (where you are currently), carefully scan the interface for a button or link that says something like: "Add Custom Model" "Self-Hosted Model" "Local Model" "Add Your Own Model" There might also be a "More" or "..." menu that contains this option. Why? The models shown on the main page (Claude, Codestral, Gemini, etc.) are typically integrated models that Continue.dev provides or has direct partnerships with. For a local model like Llama 3.1 running on Ollama, you'll need to specify its details. Select Ollama as the Provider: Once you find the option to add a custom/self-hosted model, you'll likely be prompted to choose a "provider" or "platform." Select "Ollama" from the list of options. Enter Your Llama 3.1 Model Name: After selecting Ollama, you will be asked to provide the "Model Name." Enter the exact name: llama3.1:8b-instruct-q4_K_M Configure Ollama Host (if necessary): There might be an option to specify the "Ollama Host" or "API Base URL." If your Ollama instance is running on the default address, http://localhost:11434, you might not need to change anything, or it might be pre-filled. If you're running Ollama on a different IP address or port, enter that here (e.g., http://192.168.1.100:11434). Save/Add Model: Once you've entered the necessary information, click a "Save," "Add Model," or "Connect" button. What Happens Next (and Back to VS Code): Synchronization: The Continue Hub (being web-based) and the Continue.dev VS Code extension are designed to synchronize. After you've successfully added your Ollama model via the Hub, the VS Code extension should automatically pick up this configuration. You might see a notification in VS Code, or the "Setup Chat model" link might change to show your llama3.1:8b-instruct-q4_K_M model. Verify in VS Code: Go back to VS Code. Open the Continue.dev extension sidebar. Check the "Models" section in the extension settings (the one from your first image). You should now see llama3.1:8b-instruct-q4_K_M listed under "Chat" (or "Autocomplete" if you added it there) instead of "Setup Chat model." Important Reminder: Ensure your Ollama server is running and the llama3.1:8b-instruct-q4_K_M model is downloaded and ready to be served by Ollama before you try to use it with Continue.dev. If you still have trouble finding the "Add Custom Model" option on the Continue Hub, a screenshot of the current Continue Hub page would be helpful for more specific guidance.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
