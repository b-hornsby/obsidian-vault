---
id: 483483
source: GEMINI
date: 2025-11-18
tags: ['ai-tools', ''ollama'', ''ai'', ''gpt'', ''gemini'', ''grok'', ''model'', ''cursor'']
category: general
sentiment: frustrated
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/ai-tools.md', 'nodes/topics/general.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is providing context, likely to a previous question or problem.
---
# for better context this is what i have going on: 

### USER
for better context this is what i have going on: 

### GEMINI
This image is extremely helpful because it confirms that your entire setup looks correct on the surface! Here is what the image shows: ComponentStatus (Confirmed in Image)Issue/SolutionOllama ServerRunning (ollama serve logs visible)✅ngrok TunnelRunning and Forwarding✅ URL: https://delena-ungrinned-lemuel.ngrok-free.devCursor Base URLCorrectly set with /v1✅ Base URL: https://delena-ungrinned-lemuel.ngrok-free.dev/v1Cursor API KeySet to Ollama✅Custom Model NameSet to qwen2.5-coder:14b-instruct-q4_K_M✅Model IsolationThe most likely culprit.❌ Crucial Misconfiguration (See below) 💥 The Confirmed Issue: Model Isolation Looking at the Cursor settings in the image, here is the problem: The models Sonnet 4.5, Sonnet 4.7, and your custom model qwen2.5-coder:14b... are all toggled ON. When you have multiple models toggled on, Cursor's verification process tries to check all of them against the overridden Base URL and API Key. The Sonnet models are expecting the real Anthropic API, but they are hitting your Ollama/ngrok URL instead, which causes the generic "The model does not work with your current plan or API key" error. The Immediate Fix You must disable all other models. In the Cursor settings panel (where you have the screenshot open): Find the toggles for Sonnet 4.5 and Sonnet 4.7 (and any other default models like GPT-4 or DeepSeek). Toggle them OFF. Ensure that only the qwen2.5-coder:14b-instruct-q4_K_M toggle is ON. Click Save and then Verify again. If the verification passes, try the chat window immediately. ⚠️ Secondary Check: Ollama CORS (Just in Case) Although you ran the command, if you did not restart the ollama serve process after setting the environment variable, it is still running without CORS enabled. Go to the terminal running ollama serve. Press Ctrl+C to stop the server. Run the restart command: ollama serve (You should not need to restart ngrok unless it disconnected, but leave it running.) Once you have isolated the model and restarted Ollama, the connection should succeed. Let me know if you are still stuck after making the model isolation change!
