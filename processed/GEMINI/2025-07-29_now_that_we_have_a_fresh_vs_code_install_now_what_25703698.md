---
id: 709450
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ollama', 'ai', 'gemini', 'model', 'defi', 'go', 'shell']
category: coding
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
---
# now that we have a fresh vs code install, now what?

### USER
now that we have a fresh vs code install, now what?

### GEMINI
Okay, excellent! With a fresh VS Code install, we're effectively starting from a clean slate, which should resolve any underlying corruption or conflicts that might have been interfering with the continue.dev extension. Now, let's go through the steps to get continue.dev and Ollama set up correctly in your fresh VS Code environment. Phase 1: Confirm Ollama Status Verify Ollama Server is Running: Open your PowerShell window. Run ollama serve. You should see it start successfully, indicating it's "listening on 127.0.0.1:11434". Keep this PowerShell window open. The Ollama server needs to run continuously for continue.dev to connect to it. Confirm Ollama is NOT in Startup Apps: Just to be absolutely sure, open Task Manager (Ctrl + Shift + Esc), go to the "Startup apps" tab, and ensure "ollama" is still disabled. This prevents it from automatically occupying the port. Phase 2: Set up continue.dev in Fresh VS Code Open your freshly installed VS Code. Install the "Continue - open-source AI code assistant" extension: Go to the Extensions view (Ctrl + Shift + X). Search for "Continue". Click the "Install" button. Restore your config.yaml: Copy your backed-up config.yaml file from your safe location (e.g., Desktop) back to its original path: C:\Users\Bryan\.continue\config.yaml. (If the .continue folder doesn't exist in C:\Users\Bryan\, create it, then place config.yaml inside it). Reload VS Code: Open the Command Palette (Ctrl + Shift + P). Type Reload Window and select "Developer: Reload Window". This ensures all new extensions and configurations are loaded properly. Phase 3: Verify continue.dev Functionality Check the VS Code Output Tab for "Continue": Go to View -> Output. Click the dropdown menu on the right (where it might currently say "Tasks" or "Extension Host"). Crucially, you should now see "Continue" as an option. Select it. Observe the logs in this panel. You should see messages indicating that continue.dev is initializing, reading your config.yaml, and attempting to connect to Ollama. Check the continue.dev Sidebar: Click on the "Continue" icon in the VS Code sidebar (the AI brain icon). Look at the "Select model" dropdown. Your "Llama 3.1 8B Local (Ollama)" model, as defined in your config.yaml, should now appear here. If "Continue" appears in the Output dropdown and your model shows up in the sidebar, then the complete reinstall of VS Code has successfully cleared whatever underlying issue was preventing its proper initialization!