---
category: ai-tools
date: 2025-07-29
id: 500922
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that the continue.dev extension still doesn't show his
  Ollama model in the VS Code dropdown menu after multiple attempts.
tags:
- continue.dev
- vs-code
- ollama
- model-not-appearing
---
# continue still doesn't pop up in that drop down menu after all of that 

### USER
continue still doesn't pop up in that drop down menu after all of that 

### GEMINI
This is truly an unusual and persistent issue. If "Continue" is showing as activated in the "Extension Host" logs, but its own output channel never appears in the dropdown, and the model isn't loading, we're dealing with something beyond typical configuration or installation problems. Given this, the most likely culprit is now some form of corruption in your VS Code installation or its cached extension data that a normal uninstall doesn't fully clear. Here's a more aggressive, but often effective, approach. This involves manually clearing VS Code's cached data for extensions. Important: Before you start, backup your config.yaml file to a safe location (e.g., your Desktop or Documents folder), as we will be clearing some VS Code user data. Step-by-Step for a "Deep Clean" of VS Code Extension Data: Close all VS Code windows completely. Ensure no VS Code processes are running in Task Manager. Manually delete the "Continue" extension folder: Navigate to your VS Code extensions directory: On Windows: C:\Users\YourUsername\.vscode\extensions Replace YourUsername with your actual Windows username. Look for a folder named continue.continue-x.x.x (where x.x.x is the version number, e.g., continue.continue-0.9.9). Delete this entire folder. Clear VS Code's cached user data (this is the key deeper clean): Navigate to the VS Code user data directory: On Windows: C:\Users\YourUsername\AppData\Roaming\Code (for stable VS Code) (If you use VS Code Insiders, it would be C:\Users\YourUsername\AppData\Roaming\Code - Insiders) Inside this Code (or Code - Insiders) folder, you will see several folders. The most relevant ones for extension data are often: CachedData Local Storage User (specifically workspaceStorage which can sometimes cache extension states per workspace) Safest approach: Delete the CachedData and Local Storage folders. More aggressive (if previous fails): Delete the entire Code (or Code - Insiders) folder. Warning: This will reset almost all your VS Code settings, themes, and remove all installed extensions. This is a last resort if nothing else works. Restart your computer. This ensures any lingering processes or file locks are cleared. After restarting, open VS Code. Reinstall the "Continue" extension from the Marketplace. Go to the Extensions view (Ctrl+Shift+X). Search for "Continue" and click "Install". Perform a "Developer: Reload Window." Verify Ollama is running: Open your PowerShell and ensure ollama serve is still active. Check the VS Code Output tab: Go to View -> Output. Click the dropdown. Now, "Continue" must appear as an option. If it still doesn't after this deep clean, there's a highly unusual system-level interaction preventing it, or a very specific bug with this version of Continue/VS Code on your system. If "Continue" appears, select it and check its logs. Check the Continue sidebar for your model. If, after ALL of this, "Continue" still doesn't appear in the Output dropdown: Consider filing an issue on the continue.dev GitHub repository. Provide them with all the troubleshooting steps you've tried, your VS Code version, and your operating system details. The fact that the extension says it activates but never registers its output channel is a unique symptom they might be able to diagnose. Try VS Code Insiders: As a test, download and install VS Code Insiders (the preview version). It's a completely separate installation. Install continue.dev there and see if it behaves differently. This helps isolate if the issue is with your stable VS Code installation or something broader. This deep clean is usually the solution for stubborn extension issues. Let's hope it finally gets "Continue" working for you!
