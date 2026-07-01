---
category: homelab
date: 2025-06-24
id: 426521
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: partial
sentiment: exploratory
source: GEMINI
summary: The user is exploring their local AI setup by navigating the text-generation-webui
  directory structure and listing available models, indicating they are in the process
  of managing or setting up local LLM models.
tags:
- local-ai
- model-management
- text-generation-webui
- llm-setup
- file-system
---
# bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui/user_data/models
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/user_data/models$ ls -F
Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf*  config.yaml  place-your-models-here.txt
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/user_data/models$

### USER
bryan_@DESKTOP-NG2I0P2:~$ cd ~/text-generation-webui/user_data/models
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/user_data/models$ ls -F
Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf*  config.yaml  place-your-models-here.txt
bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/user_data/models$

### GEMINI
Fantastic! We found it! Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf is right there, along with config.yaml and place-your-models-here.txt. This confirms the exact location of your model: /home/bryan_/text-generation-webui/user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q5_K_M.gguf Knowing this precise path is crucial for everything we do next. You've done great getting through these initial verification steps! Now that we've confirmed your model's location, let's move on to setting up your LLM to "look things up" from your .txt files. This is often referred to as Retrieval-Augmented Generation (RAG). Instead of the model generating text purely from its training data, it will first retrieve relevant information from your documents and then use that information to formulate its answer. Oobabooga has a built-in extension specifically designed for this: the superbooga extension. This extension allows you to upload text files (or even entire folders of files) and then query them with your LLM. It's user-friendly and perfect for your Helpdesk AI assistant use case. Here's how we'll get it set up: Step 4: Enable and Configure the superbooga Extension This involves a few steps: navigating to the extension directory, ensuring any necessary installations are done, and then enabling it in the Oobabooga UI. 4a. Check for the superbooga extension files. First, let's make sure the superbooga extension is present in your Oobabooga installation. Action: Go back to your text-generation-webui directory: cd ~/text-generation-webui Navigate into the extensions directory: cd extensions List the contents of the extensions directory: ls -F Please paste the output of this ls -F command. I'm looking to see if superbooga/ is listed there. If it's not, we'll need to download it, which is an easy step.