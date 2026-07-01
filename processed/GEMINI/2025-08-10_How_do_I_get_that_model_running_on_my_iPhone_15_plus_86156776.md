---
id: 793573
source: GEMINI
date: 2025-08-10
tags: ['iphone-15-plus', 'pocketpal', 'ios', 'local-llm']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking how to run a local LLM on his iPhone 15 Plus using Pocket Pal.
---
# How do I get that model running on my iPhone 15 plus?

### USER
How do I get that model running on my iPhone 15 plus?

### GEMINI
Getting a GGUF model like Llama 3 8B Instruct running on your iPhone 15 Plus via PocketPal is a straightforward process that takes advantage of the app's integration with Hugging Face. Here's a step-by-step guide: Step 1: Install PocketPal AI First, if you haven't already, download the PocketPal AI app from the Apple App Store. Step 2: Navigate to the Model Download Section Open the PocketPal app. Look for a menu or settings icon (often a hamburger menu or gear icon). Navigate to the "Models" or "Local Models" section. Step 3: Search for Llama 3 on Hugging Face PocketPal has a built-in feature to search for and download GGUF models directly from Hugging Face. In the Models section, look for an option to "Add from Hugging Face" or a similar button with a "+" icon. In the search bar, type "Llama 3 8B Instruct GGUF." You'll see a list of results from various contributors. The key is to find a reputable quantizer or a widely-used version. For example, you might see models from users like "bartowski" or "MaziyarPanahi." Step 4: Choose the Right Quantization This is the most crucial step for balancing performance and quality on your device. When you find the Llama 3 8B Instruct model, you'll see different GGUF files with names like: Meta-Llama-3-8B-Instruct-Q4_K_M.gguf Meta-Llama-3-8B-Instruct-Q5_K_M.gguf Meta-Llama-3-8B-Instruct-Q8_0.gguf The number after the Q represents the quantization level. Q4_K_M: A good balance of file size and quality. This is often the best all-around choice for a powerful phone like the iPhone 15 Plus. It will run quickly and still provide high-quality responses. Q5_K_M: Slightly larger file size and a bit slower, but with a marginal improvement in quality. If you want to push for the best possible quality, this is a great option. Q8_0: A much larger file with the best quality but will be the slowest to run. You can try it, but the performance might not be as snappy as the Q4 or Q5 versions. For a great all-around experience, I recommend starting with the Q4_K_M or Q5_K_M versions. Step 5: Download the Model Once you've selected the GGUF file you want, tap on the "Download" button. The app will then download the model weights to your phone's local storage. This may take a few minutes, depending on the file size and your internet connection. Important: Keep the PocketPal app open and your phone awake during the download to avoid any interruptions. Some users have reported issues with downloads getting stuck if the app is closed or the screen locks. Step 6: Load the Model After the download is complete, the model will appear in your list of local models. Tap the "Load" button next to the Llama 3 model you just downloaded. This loads the model into your phone's memory, making it ready to use. Step 7: Start Chatting! Go to the "Chat" screen in the app. You should now be able to use the Llama 3 8B Instruct model for all your conversations, directly on your iPhone, without an internet connection. By following these steps, you'll have the best all-around local model up and running on your iPhone 15 Plus, providing you with a powerful and private AI assistant.
