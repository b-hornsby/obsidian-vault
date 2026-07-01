---
category: coding
date: 2025-06-23
id: 804876
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user is working on building an extension for the operation-immortal-agent
  project and has reached the extension UI part but is stuck because they only see
  a blank or incomplete visual output and need guidance on what should appear there.
tags:
- extension development
- UI implementation
- stuck on visual layout
- frontend debugging
- partial progress
---
# im at the extension part. this is all i see: 

### USER
im at the extension part. this is all i see: 

### GEMINI
Thanks for providing that screenshot, Bryan! You're right, looking at that "Available extensions" list, I don't see a clearly named RAG extension like rag_agent, simple_rag, or document_loader that is typically used for directly integrating your knowledge base in Oobabooga. While superbooga and superboogav2 are powerful, they don't usually act as the primary, dedicated RAG system. This suggests that your Oobabooga installation might be a slightly older version, or configured in a way that doesn't expose those specific RAG extensions. To get the dedicated RAG capabilities we discussed (which will make your help desk AI truly stand out by using your documents), the most straightforward solution is to update your Oobabooga text-generation-webui installation. Updating will pull down the latest features, bug fixes, and usually, the dedicated RAG extensions we're looking for. Next Step: Update Your Oobabooga Installation Goal: Get access to the latest extensions, including the RAG ones. Estimated Time: 5-15 minutes, depending on your internet speed and the size of the update. Here's how to do it in your WSL2 Ubuntu terminal: Go back to your Ubuntu WSL2 terminal. Make sure Oobabooga is running in that terminal (or any other terminal). Stop the Oobabooga server first: Press Ctrl + C repeatedly in the terminal where Oobabooga is running until you see your command prompt (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Ensure you are in the text-generation-webui directory: cd ~/text-generation-webui Pull the Latest Changes from GitHub: This command fetches the newest code from the Oobabooga project. git pull You'll see output about files being updated. Update Python Dependencies: After pulling the code, you need to update any Python libraries that the new version might require. pip install -r requirements.txt --upgrade This command tells pip (Python's package installer) to read the requirements.txt file (which lists all necessary libraries) and upgrade them to the versions specified, installing any new ones. Restart Oobabooga: Once the pip install command finishes, you can restart Oobabooga using your script: ./start_ooba.sh Wait for it to fully load in your browser. After Oobabooga has restarted, go back to the "Settings" tab (or if a new "Extensions" tab appears on the left, go there!) and check the "Available extensions" list again. You should now see a wider range of extensions, hopefully including explicit RAG-related ones. This update should provide you with the necessary tools for RAG. Let me know how the update goes and what you see in the extensions list afterward!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]