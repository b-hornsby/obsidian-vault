---
id: 705914
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ollama', 'ai', 'gemini', 'model', 'defi', 'go', 'shell']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
---
# PS C:\Users\Bryan> tasklist /fi "PID eq 27296"

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
ollama.exe                   27296 Console                    1     51,164 K
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> tasklist /fi "PID eq 27296"

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
ollama.exe                   27296 Console                    1     51,164 K
PS C:\Users\Bryan>

### GEMINI
Excellent! We have a clear culprit: ollama.exe with PID 27296 is indeed the process holding the port. This confirms that Ollama is running in the background, likely as a Windows Service, which is why it keeps starting up automatically after a restart. Now, let's stop it so you can take control: Step 1: Terminate the currently running ollama.exe process. In your PowerShell window, run the following command. You might need to run PowerShell as Administrator if the command fails, but usually taskkill is fine without it for your own processes. taskkill /PID 27296 /F You should see a success message like: "SUCCESS: The process with PID 27296 has been terminated." Step 2: Start ollama serve manually. After confirming the process is terminated, immediately run: ollama serve This time, it must start successfully without the "bind: Only one usage..." error. You should see logs indicating it's listening on 127.0.0.1:11434. Keep this PowerShell window open. The ollama serve command needs to run continuously for continue.dev to connect to it. Step 3: Proceed with VS Code. Now that the Ollama server is definitely running under your control: Open VS Code. Ensure "Continue" is installed. (If you uninstalled it as part of the deep clean, reinstall it now). Perform a "Developer: Reload Window" in VS Code (Ctrl+Shift+P or Cmd+Shift+P -> "Reload Window"). This will force VS Code to re-initialize all extensions, including Continue. Go to View -> Output. Click the dropdown menu. You must now see "Continue" as an option. Select it. Observe the logs in the "Continue" output channel. Look for messages indicating it's loading your config.yaml and connecting to Ollama. Check the continue.dev sidebar (the AI icon). Your "Llama 3.1 8B Local (Ollama)" model should finally appear in the "Select model" dropdown. This is it! Successfully getting ollama serve to run without error, combined with the clean install/reload of continue.dev, should resolve everything.