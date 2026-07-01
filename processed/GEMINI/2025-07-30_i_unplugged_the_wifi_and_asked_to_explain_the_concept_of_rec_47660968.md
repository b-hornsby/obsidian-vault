---
id: 818362
source: GEMINI
date: 2025-07-30
tags: ['local-llm-testing', 'offline-mode', 'recursion']
category: coding
sentiment: executing
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is testing his local LLM in offline mode by asking it to explain recursion.
---
# i unplugged the wifi and asked to explain the concept of recursion in programming and got this

### USER
i unplugged the wifi and asked to explain the concept of recursion in programming and got this

### GEMINI
Okay, this is extremely helpful! The image shows a clear error message: "Model 'llama3.1:8b' is not found in Ollama. You need to install it." Below that, there's an "Install Model" button. This means that while your config.yaml is correctly telling Continue.dev to use llama3.1:8b from Ollama, Ollama itself does not have the model downloaded on your machine. Even though you saw llama3.1:8b in the Continue Hub, that only tells you it's available on Ollama's public library, not that you've downloaded it locally. The previous terminal logs showing POST "/api/show" might have been Ollama just confirming that a model could exist, but it wasn't actually ready to serve it for generation. What you need to do is physically download the llama3.1:8b model using Ollama in your terminal. Steps to fix this: Reconnect to the Internet. (You need an internet connection to download the model). Open your terminal (the one where you usually run Ollama). Run the Ollama pull command for Llama 3.1: ollama pull llama3.1:8b This command will start the download process for the llama3.1:8b model. It will show you progress bars. Note: You previously mentioned llama3.1:8b-instruct-q4_K_M. The ollama pull llama3.1:8b command will typically pull the default/recommended tag (often an instruct variant like the q4_K_M if that's the common one for 8b). If you want to be super specific, you could try ollama pull llama3.1:8b-instruct-q4_K_M, but often llama3.1:8b is sufficient. Let's start with llama3.1:8b. Wait for the download to complete. This model is larger than Qwen 1.5B, so it might take a while depending on your internet speed. Verify the model is installed: Once the download is finished, you can run ollama list in your terminal to confirm that llama3.1:8b (or its specific variant) appears in the list. After the download is complete: You can then disconnect from the internet again (for the true offline test). Go back to VS Code and the Continue.dev chat. Try asking your question again: "Explain the concept of recursion in programming." You should now see the llama3.1:8b model processing the request in your Ollama terminal, and Continue.dev should display the generated response. This "Model not found in Ollama" error is very common when first setting up local models, as the configuration tells the client (Continue.dev) what to ask for, but the server (Ollama) still needs the actual model files.
