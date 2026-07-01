---
id: 150106
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'llm', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'openai']
category: ai-tools
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$
./start_linux.sh
11:07:51-230506 INFO     Starting Text generation web UI
11:07:51-232459 INFO     Loading settings from "user_data/settings.yaml"
11:07:51-236944 INFO     Loading the extension "openai"
11:07:51-318630 INFO     OpenAI-compatible API URL:

                         http://127.0.0.1:5000


Running on local URL:  http://127.0.0.1:7860

### USER
(base) bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$
./start_linux.sh
11:07:51-230506 INFO     Starting Text generation web UI
11:07:51-232459 INFO     Loading settings from "user_data/settings.yaml"
11:07:51-236944 INFO     Loading the extension "openai"
11:07:51-318630 INFO     OpenAI-compatible API URL:

                         http://127.0.0.1:5000


Running on local URL:  http://127.0.0.1:7860

### GEMINI
Excellent! That's precisely what we needed to see. You've successfully: Navigated to your text-generation-webui directory in the new WSL2 terminal window. Started Oobabooga using ./start_linux.sh (which, on your setup, appears to automatically enable the OpenAI API extension, as indicated by Loading the extension "openai"). Confirmed that the OpenAI-compatible API is running at http://127.0.0.1:5000. This is the crucial address rag_chat.py needs! Now, leave that Oobabooga terminal window open and running. Do not close it. Final Step: Run Your Helpdesk AI (rag_chat.py) Switch back to your original WSL2 terminal window (the one where your prompt is (base) bryan_@DESKTOP-NG2I0P2:~/helpdesk_ai_rag$). Ensure you are in your ~/helpdesk_ai_rag directory. Your prompt should be: (base) bryan_@DESKTOP-NG2I0P2:~/helpdesk_ai_rag$ Execute the rag_chat.py script: python rag_chat.py What to expect: The script will print messages like "Loading embedding model...", "ChromaDB loaded.", "Retriever initialized.", and "LLM connection established." Then, it will present a prompt: You: Now, you can type your helpdesk questions! Try asking questions based on the documents you put in your knowledge_base folder. For example, you could ask: How do I fix a paper jam? What are the steps to connect to the VPN? My mouse is not working. Can you explain password best practices? What should I do if my system is freezing? When you're done, type exit and press Enter to quit the chat. Please run python rag_chat.py in your first terminal, and then paste the output of the script's startup and your first question and its answer. We're very close to seeing your RAG system in action!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]