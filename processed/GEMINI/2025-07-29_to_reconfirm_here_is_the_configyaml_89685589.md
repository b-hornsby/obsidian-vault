---
id: 986815
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ollama', 'ai', 'gemini', 'model', 'go', 'code', 'error']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# to reconfirm here is the config.yaml: 

### USER
to reconfirm here is the config.yaml: 

### GEMINI
Thanks for reconfirming the config.yaml. Based on the config.yaml you've provided and the fact that you now have ollama serve running successfully in your terminal, there's nothing visually incorrect with the config.yaml itself that would prevent continue.dev from picking it up. You've got: title: Llama 3.1 8B Local (Ollama) (This is what should appear in the dropdown) provider: ollama (Correct for Ollama) model: llama3.1:8b-instruct-q4_K_M (Matches your pulled model) apiBase: http://localhost:11434 (Matches the default Ollama server address) Given that ollama serve is running and your config.yaml looks correct, the final troubleshooting step is almost always a VS Code reload. Please confirm you've done this specific action after getting ollama serve running: Go to your VS Code window. Open the Command Palette: On Windows/Linux: Press Ctrl+Shift+P On macOS: Press Cmd+Shift+P Type Reload Window and select the "Developer: Reload Window" option. After VS Code reloads, give it a moment to initialize. Then, check the continue.dev sidebar again. The "Select model" dropdown should now show "Llama 3.1 8B Local (Ollama)". If it still doesn't show up after a reload, here are a few more things to check, but they are less common: Is config.yaml in the correct directory? For Windows, it should typically be C:\Users\Bryan\.continue\config.yaml. Sometimes users might inadvertently save it elsewhere. Any errors in the Continue Output channel in VS Code? In VS Code, go to View > Output. In the dropdown menu that appears in the Output panel, select Continue. Look for any error messages or warnings related to loading the configuration or connecting to Ollama. This can provide crucial clues. VS Code Permissions (less likely): In rare cases, if VS Code doesn't have proper read permissions to the .continue directory, it might fail to load the config. But truly, the reload is the most common fix when the server is running and the config is correct.