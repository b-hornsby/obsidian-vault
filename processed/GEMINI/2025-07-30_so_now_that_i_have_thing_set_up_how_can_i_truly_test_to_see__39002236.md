---
category: coding
date: 2025-07-30
id: 20746
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: executing
source: GEMINI
summary: Bryan is asking how to verify that his local LLM setup is working as intended
  and using the correct offline model.
tags:
- local-llm-testing
- offline-model-verification
---
# so now that i have thing set up, how can i truly test to see if its working as intended and using the offline model i want it to 

### USER
so now that i have thing set up, how can i truly test to see if its working as intended and using the offline model i want it to 

### GEMINI
Okay, great question! It's always good to verify your setup. Here's how you can truly test if Continue.dev is using your offline Ollama models (llama3.1:8b-instruct-q4_K_M for chat and qwen2.5-coder:1.5b for autocomplete) as intended: 1. Test Chat Model (llama3.1:8b-instruct-q4_K_M) Disconnect from the Internet (Crucial Test): The most definitive way to ensure it's using an offline model is to turn off your Wi-Fi or unplug your Ethernet cable. This forces Continue.dev to rely only on locally accessible models. Open Continue.dev Chat in VS Code: Go to the Continue.dev sidebar in VS Code. Make sure llama3.1 8b is selected as your "Chat" model in the dropdown. Ask a Question: In the chat input, ask a general knowledge question or a simple coding question that Llama 3.1 should be able to answer. Example: "Explain the concept of recursion in programming." or "What is the capital of France?" Observe the Response: If you get a coherent and relevant response while offline, it's definitively using your local Ollama model. Check Ollama Terminal Logs: Keep your Ollama terminal window open. When you send a chat message in Continue.dev, you should see new log entries appearing in the Ollama terminal. Look for [GIN] ... POST "/api/generate" or POST "/api/chat" with a 200 status code, followed by output from the model. This is your Llama 3.1 processing the request. 2. Test Autocomplete Model (qwen2.5-coder:1.5b) Disconnect from the Internet (Again, for a definitive test): Turning off your internet connection will ensure no cloud-based autocomplete services interfere. Open a Code File in VS Code: Create a new file (e.g., test.py or test.js) or open an existing one. Ensure Autocomplete is Enabled and Qwen is Selected: In the Continue.dev sidebar settings (the gear icon next to the model dropdowns), ensure "Autocomplete" is enabled and qwen2.5-coder 1.5b is selected as the "Autocomplete" model. Start Typing Code: Type a function signature or the beginning of a common code pattern. Example in Python: def factorial(n): if n == 0: return 1 # Type below this line: # return n * fac or class MyClass: def __init__(self, name): self.name = name # Type below this line: # def say_hello Observe for Autocompletion Suggestions: As you type, you should see grayed-out "ghost text" suggestions appearing automatically. These are the autocomplete suggestions from Qwen. Check Ollama Terminal Logs: When you type and trigger a completion, you should see [GIN] ... POST "/api/generate" or POST "/api/completions" entries in your Ollama terminal, indicating Qwen is being queried. What to look for if it's not working: No response/Long delay: If you're offline and get no response or a very long delay (and no Ollama logs), it's not connecting to your local model. Error messages in VS Code: Check the VS Code "Output" panel for "Continue" or "Ollama" specific errors. No new logs in Ollama terminal: If Ollama isn't showing new POST requests when you try to use the models, Continue.dev isn't reaching it. This could mean Ollama isn't running, or there's a port/address mismatch in Continue's config (though localhost:11434 is the default). "No suggestions" or default VS Code suggestions: If you only see VS Code's built-in Intellisense suggestions and no AI-powered "ghost text," the autocomplete model isn't active. By performing these tests, especially while disconnected from the internet, you can be confident that your Continue.dev setup is indeed using your local Ollama models.
