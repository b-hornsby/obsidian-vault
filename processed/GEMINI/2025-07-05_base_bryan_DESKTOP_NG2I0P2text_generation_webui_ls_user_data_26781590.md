---
id: 509222
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'gguf', 'hermes']
category: ai-tools
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf  config.yaml  place-your-models-here.txt(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ls user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf  config.yaml  place-your-models-here.txt(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Great! That's exactly what we needed. You have found your model: Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf. This model is located inside the user_data/models/ directory. Step 1: Restart Oobabooga with the Correct Model Path Now that we know the exact path, let's restart Oobabooga so it loads the model properly. Ensure you are in your second WSL2 terminal window (the one running Oobabooga). Stop Oobabooga by pressing Ctrl + C (you might need to press it a couple of times). Run the following command to start Oobabooga, including the full path to your model: python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf --api Crucially, watch this terminal window. It will now show messages indicating it's loading the model. This will take a moment (you'll see progress bars or percentages). Wait until you see messages like: INFO: Started server process [xxxxx] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit) Step 2: Try Your Helpdesk AI Again Once Oobabooga has successfully loaded the model and is running (as indicated by the Uvicorn messages), switch back to your first WSL2 terminal window (where your prompt is (base) bryan_@DESKTOP-NG2I0P2:~/helpdesk_ai_rag$). Run the rag_chat.py script: python rag_chat.py When prompted, ask your question again: my wifi drops frequently Please execute these steps, and then paste the entire output from your terminal after asking the question. We've fixed the "No model loaded" issue on Oobabooga's side, so this should resolve the Internal Server Error.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]