---
category: ai-tools
date: 2025-07-29
id: 080316
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is describing the error message he sees when trying to add an assistant
  in Continue.dev, indicating a problem with model configuration or detection.
tags:
- continue-dev-configuration
- assistant-setup
- local-llm-integration
- troubleshooting
---
# no when i press the plus the no assistants yet pops up and it also says this when i hover over the + 

### USER
no when i press the plus the no assistants yet pops up and it also says this when i hover over the + 

### GEMINI
Ah, thank you for the clarification and the new image! Now I see the pop-up message: "You must create or select an assistant before adding blocks." This changes the approach slightly, as Continue.dev wants you to associate models with an "assistant" first. Here's the updated strategy: Understanding the "No Assistants Yet" Message: The right sidebar in your image clearly states "No Assistants Yet. Get started by exploring existing assistants or creating your own custom assistant." This means the Continue Hub is designed around the concept of "assistants," and models are "blocks" that are added to an assistant. Steps to get your llama3.1:8b-instruct-q4_K_M model connected: Create a New Assistant: On the right sidebar, you'll see "No Assistants Yet." Below that, there should be a link or button to "creating your own custom assistant" (or similar wording like "Create Assistant"). Click this. Name Your Assistant: You'll likely be prompted to give your new assistant a name (e.g., "My Llama 3.1 Assistant," "Code Helper," "Local AI"). Choose a descriptive name. (Optional) Choose a Template: Some platforms offer assistant templates (e.g., "Code Assistant," "Chatbot"). If presented with options, you can choose one that aligns with your primary use case, or simply start with a blank one if that's an option. Add Your Llama 3.1 Model as a "Block" to the Assistant: Once you've created the assistant, you should be taken to its configuration page. On this page, you will then be able to add "blocks" (which are the models, rules, tools, etc.). Look for a section or button to "Add Model" or "Add Block." When you click "Add Model/Block," you should then be able to search for and select "llama3.1:8b" (or "Ollama" as a provider, then specify "llama3.1:8b"). This is where the "+" button for the llama3.1:8b model will now function correctly. To summarize the flow: Hub Page (current) -> Create Custom Assistant (right sidebar) -> Name Assistant -> Go to Assistant Configuration -> Add Block/Model -> Select llama3.1:8b (Ollama) Crucial Reminders: Ollama Running: Ensure your Ollama server is running and llama3.1:8b-instruct-q4_K_M is downloaded and available in Ollama before you attempt to use it. Synchronization: After you've successfully added the model to your assistant on the Continue Hub, allow a moment for the VS Code extension to synchronize. You might need to refresh the Continue.dev sidebar in VS Code or even restart VS Code if it doesn't appear immediately under your "Chat model" options. Let me know if you encounter any other pop-ups or if the process deviates from these steps.
