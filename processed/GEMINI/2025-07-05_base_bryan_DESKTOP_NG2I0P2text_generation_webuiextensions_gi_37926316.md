---
id: 941848
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'ollama', 'ai', 'gemini', 'model', 'oobabooga', 'rag', 'gguf']
category: ai-tools
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ git clone https://github.com/oobabooga/text-generation-webui/tree/main/extensions/rag
Cloning into 'rag'...
fatal: repository 'https://github.com/oobabooga/text-generation-webui/tree/main/extensions/rag/' not found
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$ git clone https://github.com/oobabooga/text-generation-webui/tree/main/extensions/rag
Cloning into 'rag'...
fatal: repository 'https://github.com/oobabooga/text-generation-webui/tree/main/extensions/rag/' not found
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$

### GEMINI
You're absolutely correct to point out that error, Bryan! My apologies. I made a mistake in the git clone command. When you use git clone, you need the raw Git repository URL, not the URL of a specific folder within the GitHub web interface. The URL https://github.com/oobabooga/text-generation-webui/tree/main/extensions/rag is a web page URL, not a cloneable Git URL. To clone just the rag extension directly into your extensions folder, it's actually a bit more complex because Git is designed to clone entire repositories, not just subdirectories. The easiest and most common way to get a specific extension that's part of the main text-generation-webui repository is to download it as a ZIP file or copy its contents manually, then install its requirements. Let's use the manual copy method from the GitHub page. Corrected Steps to Get the rag Extension Files Ensure you are in your extensions directory: cd ~/text-generation-webui/extensions Your prompt should be (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui/extensions$. Manually Download the rag Extension (from your Windows browser): Go to the rag extension's folder on GitHub: https://github.com/oobabooga/text-generation-webui/tree/main/extensions/rag On that page, look for a green "Code" button. Click it. In the dropdown, choose "Download ZIP". This will download the entire text-generation-webui-main.zip file. You only need the contents of the extensions/rag folder from within that ZIP. Extract and Copy rag folder into WSL2: On your Windows desktop, open the downloaded text-generation-webui-main.zip. Inside the ZIP file, navigate to text-generation-webui-main/extensions/rag/. Extract the entire rag folder to a temporary location on your Windows desktop (e.g., C:\Users\Bryan\Desktop\temp_rag). Now, in your WSL2 terminal, copy this extracted rag folder from your Windows filesystem into your WSL2 ~/text-generation-webui/extensions/ directory. Assuming you're still in ~/text-generation-webui/extensions: cp -r /mnt/c/Users/Bryan/Desktop/temp_rag/rag . (Make sure to replace /mnt/c/Users/Bryan/Desktop/temp_rag/rag with the actual path where you extracted it on your Windows side. The . at the end means "copy it to the current directory"). After this, you should have a new folder named rag within ~/text-generation-webui/extensions/. You can verify this with ls -l. Go back to the Oobabooga root directory: cd .. Your prompt should be (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$. Install rag Extension Dependencies: Now that the rag folder is in place, you can install its dependencies. ./installer_files/env/bin/pip install -r extensions/rag/requirements.txt This command should now successfully find and process the requirements.txt file. Let it complete fully. Copy Your Knowledge Base (if not already done): If you haven't copied your db folder from ~/helpdesk_ai_rag/ to ~/text-generation-webui/user_data/ yet, do so now: cp -r ~/helpdesk_ai_rag/db user_data/ Restart Oobabooga: ./installer_files/env/bin/python server.py --model user_data/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf Wait for Oobabooga to fully load the model and display its URL. Enable and Configure the rag Extension in the Web UI: Open http://127.0.0.1:7860 in your web browser. Go to the "Extensions" tab. You should now see "rag" listed as an available extension. Check its box. Click "Save settings" and restart the server via the UI prompt. After restart, a new "RAG" tab should appear. Click on it. Configure the "Knowledge base path" to user_data/db. Configure the embedding model if prompted (e.g., "Ollama" and nomic-embed-text). Save settings within the "RAG" tab. This is a more involved set of steps due to the git clone limitation, but it should ensure the rag extension files are correctly placed. Please let me know the output as you go through these steps.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]