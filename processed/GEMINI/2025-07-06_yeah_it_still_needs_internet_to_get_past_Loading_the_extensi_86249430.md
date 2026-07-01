---
category: ai-tools
date: 2025-07-06
id: 484976
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan confirms that Superbooga v2 still requires internet to load the extension,
  preventing fully offline operation.
tags:
- superboogav2
- internet-dependency
- extension-loading
- offline-issue
---
# yeah it still needs internet to get past  Loading the extension "superboogav2" 

### USER
yeah it still needs internet to get past  Loading the extension "superboogav2" 

### GEMINI
You're right to be persistent about this. If superboogav2 is still requiring an internet connection every time you launch Oobabooga, even after a previous successful download, it means the necessary embedding model (usually all-MiniLM-L6-v2) isn't being cached reliably, or something is forcing a re-download/online verification every time. This is unusual behavior for a cached model, as they're designed to run offline once downloaded. The persistent NameResolutionError suggests a fundamental issue with your WSL2's ability to consistently resolve domain names, or that the cache is being invalidated. Let's try a more robust approach to diagnose and fix this: Deeper Troubleshooting for Persistent Online Requirement Step 1: Verify WSL2 Network Configuration Consistency Even if you set DNS manually before, let's confirm it's truly persistent. Close all WSL2 terminals. Open PowerShell or Command Prompt (on Windows) as Administrator. Run: wsl --shutdown Verify/Create .wslconfig: Navigate to your Windows user profile folder: C:\Users\YourUserName\ (replace YourUserName with your actual Windows username). Look for a file named .wslconfig. If it exists, open it with Notepad. If it doesn't exist, create a new text file and save it as .wslconfig in that exact folder. Make sure it's not .wslconfig.txt. Add or ensure the following content is in the file: [wsl2] dns=8.8.8.8 This forces WSL2 to use Google's highly reliable DNS server. Restart WSL2: Just open a new WSL2 terminal. Verify DNS in WSL2: In your WSL2 terminal, run: cat /etc/resolv.conf It should show nameserver 8.8.8.8. If it doesn't, the .wslconfig isn't being read correctly or something else is overriding it. Step 2: Clear and Force a Fresh Download/Cache If the DNS is stable, the problem might be with the cache itself. Ensure you have an active internet connection. Stop Oobabooga (Ctrl+C in your WSL2 terminal). Navigate to the Hugging Face cache directory and delete the problematic model: cd ~/.cache/huggingface/hub rm -rf models--sentence-transformers--all-MiniLM-L6-v2 You previously confirmed this folder exists. Deleting it ensures a clean download. Go back to your Oobabooga directory: cd ~/text-generation-webui/ Run Oobabooga: ./installer_files/env/bin/python server.py Observe the output carefully. You should see it actively downloading all-MiniLM-L6-v2. This needs to complete successfully. Step 3: Test Offline Loading Once Oobabooga has successfully loaded with superboogav2 (and internet was active for that specific boot where it downloaded), try this: Stop Oobabooga. Disconnect your PC from the internet (turn off Wi-Fi, unplug Ethernet). Restart WSL2: wsl --shutdown from Windows PowerShell (as Admin). Open your WSL2 terminal. Run Oobabooga: cd ~/text-generation-webui/ ./installer_files/env/bin/python server.py Observe the output carefully. If it still gets stuck at superboogav2 with a NameResolutionError, then: Your .wslconfig isn't fully guaranteeing consistent DNS/network. OR, there's an unusually aggressive online verification step by the library that somehow doesn't recognize a cached version as valid for offline use. This is less common but possible in some very specific setups or library versions. If the above steps don't work, consider reinstalling sentence-transformers within your Oobabooga environment. Stop Oobabooga. cd ~/text-generation-webui/installer_files/env/ pip uninstall sentence-transformers pip install sentence-transformers Then retry booting Oobabooga with internet.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
