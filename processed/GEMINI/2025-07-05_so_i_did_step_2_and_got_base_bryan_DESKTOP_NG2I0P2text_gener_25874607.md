---
id: 235427
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'openai', 'gguf']
category: ai-tools
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# so i did step 2 and got: (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
11:37:28-342987 INFO     Starting Text generation web UI
11:37:28-344839 INFO     Loading settings from "user_data/settings.yaml"
11:37:28-347160 INFO     Loading the extension "openai"
11:37:28-429032 INFO     OpenAI-compatible API URL:

                         http://127.0.0.1:5000


Running on local URL:  http://127.0.0.1:7860
 

### USER
so i did step 2 and got: (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
11:37:28-342987 INFO     Starting Text generation web UI
11:37:28-344839 INFO     Loading settings from "user_data/settings.yaml"
11:37:28-347160 INFO     Loading the extension "openai"
11:37:28-429032 INFO     OpenAI-compatible API URL:

                         http://127.0.0.1:5000


Running on local URL:  http://127.0.0.1:7860
 

### GEMINI
Great! That's excellent progress. You successfully ran ./start_linux.sh and it launched Oobabooga. Importantly, it loaded the "openai" extension, and the API is running on http://127.0.0.1:5000. However, the key part we're missing is that it didn't explicitly load your model. When you run ./start_linux.sh without the --model flag, it starts the UI but doesn't necessarily load a specific model unless one is pre-selected in its settings. That's why you got the "No model loaded" error previously. Now we need to do the final step: stop Oobabooga in this window, and then restart it with your model explicitly specified. Step 1: Stop Oobabooga In the current WSL2 terminal window where Oobabooga is running (the one displaying the output you just shared), press Ctrl + C. You might need to press Ctrl + C a couple of times. Wait for the process to terminate and your command prompt (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ to reappear. Step 2: Restart Oobabooga with Your Model and API Now, use the full command to ensure your specific model is loaded, and the API is enabled. From your ~/text-generation-webui$ prompt, run: python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf --api Watch this terminal window closely. This time, you should see messages indicating the model is actually being loaded. It will take some time, with progress indicators (e.g., percentages, kv cache details). Wait patiently for the model to fully load. You will eventually see the familiar Uvicorn running on http://127.0.0.1:5000 message, which confirms the API is ready and the model is loaded. Step 3: Run Your Helpdesk AI Once Oobabooga is confirmed running with the model loaded in its terminal window, switch back to your other WSL2 terminal window (where you have ~/helpdesk_ai_rag$). Execute the rag_chat.py script: python rag_chat.py When prompted You: , ask your question again: my wifi drops frequently Please provide the complete output from both terminal windows (especially the Oobabooga one showing model loading) once you've performed these steps. This should finally get your RAG system working!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]