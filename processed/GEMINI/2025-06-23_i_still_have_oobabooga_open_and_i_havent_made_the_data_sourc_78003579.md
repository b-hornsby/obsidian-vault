---
category: ai-tools
date: 2025-06-23
id: 946596
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is trying to set up a data_sources folder within the oobabooga interface
  but is unsure how to navigate to the correct directory or configure the required
  folder structure.
tags:
- oobabooga
- data_sources
- folder setup
- local AI
- initial configuration
---
# i still have oobabooga open and i havent made the data_sources folder yet. how do i get to where i need to be? 

### USER
i still have oobabooga open and i havent made the data_sources folder yet. how do i get to where i need to be? 

### GEMINI
Okay, no problem at all! You can do this without closing Oobabooga. You need to switch from your web browser (where Oobabooga's UI is) back to your Ubuntu WSL2 terminal. Here's how to get to where you need to be: Locate your Ubuntu WSL2 Terminal: You likely have it open already from where you launched Oobabooga. Just click on its window if it's minimized or in the background. If you closed it, open a new Ubuntu terminal from your Windows Start Menu. Navigate to the Oobabooga Directory: Once in your Ubuntu terminal, make sure you are in the text-generation-webui directory. Type: cd ~/text-generation-webui Press Enter. Create the data_sources Folder: Now, you can create the folder where your documents will go. Type: mkdir data_sources Press Enter. That's it for the terminal part! You've now created the folder. To put your .txt files into it: Open Windows File Explorer. In the address bar at the top, type the exact path: \\wsl$\Ubuntu\home\bryan_\text-generation-webui\data_sources *Press Enter. This will open the data_sources folder in Windows File Explorer, and you can simply drag and drop the .txt files you create (using Notepad as discussed) directly into this folder.