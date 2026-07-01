---
category: homelab
date: 2025-06-23
id: 814267
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: The user was checking the status of their WSL (Windows Subsystem for Linux)
  installation to see if their Ubuntu environment was running, likely as part of setting
  up or maintaining their homelab environment.
tags:
- WSL
- Ubuntu
- Windows
- virtualization
- environment-setup
---
# PS C:\Users\Bryan> wsl -l -v
  NAME      STATE           VERSION
* Ubuntu    Stopped         2
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> wsl -l -v
  NAME      STATE           VERSION
* Ubuntu    Stopped         2
PS C:\Users\Bryan>

### GEMINI
Excellent! Thank you for that output. From what you've provided: You have one WSL2 distribution named Ubuntu. Its state is Stopped. It's running WSL version 2, which is what we want for performance. Now that we know your distribution, let's get into it and figure out where your Nous-Hermes-2 Mistral 7B model is located. Step 2: Locate Your Nous-Hermes-2 Mistral 7B Model within Ubuntu WSL2 You mentioned the model runs in the terminal in WSL2, which is great, as it means the model files themselves are likely intact. The next step is to pinpoint their exact location within your Ubuntu file system. Action: We need to start your Ubuntu WSL2 distribution and navigate to where your model is. What I need you to do: Start your Ubuntu WSL2 distribution: Open a new PowerShell or Command Prompt window (if you closed the previous one) and simply type: wsl This will launch your default WSL2 distribution, which is Ubuntu in your case. You should see your Ubuntu terminal prompt appear (it might look something like your_username@your_computer_name:~$ or similar). Navigate to your model's directory: Once inside the Ubuntu terminal, you'll need to remember where you saved the Nous-Hermes-2 Mistral 7B model. Common places for models are often in a models directory, or within the directory of the software you used to download it (like text-generation-webui/models if you used oobabooga's download feature before, or a custom directory you created). Here are some common Linux commands to help you find it: ls: Lists the contents of the current directory. ls -l: Lists contents with more details (permissions, size, date). pwd: Prints the current working directory (tells you where you are). cd [directory_name]: Changes directory. cd ..: Goes up one directory. cd ~: Goes to your home directory. find . -name "*mistral*" -print: This command is a powerful way to search for files. It will search the current directory (.) and all subdirectories for anything with "mistral" in its name. It might take a moment if you're searching a large area. My suggestion: Start by typing pwd to see your current location. Then, try ls to see what's there. If you know you put it in a specific folder, cd into that folder. If you're unsure, try the find command. Confirm the model file name and path: Once you've navigated to the directory containing your Nous-Hermes-2 Mistral 7B model, use ls to list the files and note the exact filename (it will likely end in .gguf, .bin, or a similar extension). What I need from you: Confirm that you have successfully entered your Ubuntu WSL2 terminal. Tell me the full path to the directory where your Nous-Hermes-2 Mistral 7B model file is located within Ubuntu. For example, it might be /home/your_username/models/Nous-Hermes-2-Mistral-7B.gguf or /mnt/c/Users/Bryan/Documents/LLM_Models/Nous-Hermes-2-Mistral-7B.gguf (if you stored it on your Windows drive and accessed it via /mnt/c/). Tell me the exact filename of the model. Take your time with this step, exploring your file system. I'll wait for you to provide this information before we move on to setting up oobabooga.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]