---
id: 330588
source: GEMINI
date: 2025-06-25
tags: ['coding', 'llm', 'ai', 'gemini', 'model', 'oobabooga', 'gguf', 'hermes']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md']
---
# ran those commands and got: (base) bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
12:56:35-706683 INFO     Starting Text generation web UI
12:56:35-708628 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860 

### USER
ran those commands and got: (base) bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
12:56:35-706683 INFO     Starting Text generation web UI
12:56:35-708628 INFO     Loading settings from "user_data/settings.yaml"

Running on local URL:  http://127.0.0.1:7860 

### GEMINI
Okay, that's exactly what we wanted to see! The start_linux.sh script executed, and Oobabooga's text-generation-webui is now running again, accessible at http://127.0.0.1:7860. Crucially, you started from a fresh terminal session, which should have cleared any lingering environment variables that might have been pointing the llama-server to the wrong libstdc++ in your old llm-assist environment. Next Step: Open your web browser on your Windows machine and go to http://127.0.0.1:7860 (or refresh the page if it's already open). Go to the "Model" tab. Select NousResearch_Nous-Hermes-2-Mistral-7B-DPO-GGUF from the dropdown menu (it should still be listed as it was downloaded). Click the green "Load" button. Observe the output in your WSL2 terminal where Oobabooga is running. If our troubleshooting worked, it should now successfully load the model without the GLIBCXX_3.4.30' not found error.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]