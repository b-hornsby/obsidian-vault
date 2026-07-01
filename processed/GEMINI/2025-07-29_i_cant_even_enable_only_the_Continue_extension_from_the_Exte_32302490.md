---
category: ai-tools
date: 2025-07-29
id: 770550
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble enabling the Continue extension in VS Code, hindering
  his troubleshooting efforts.
tags:
- vscode-extension-troubleshooting
- continue-dev-extension
- debugging
- development-environment
---
# i can't even enable only the "Continue" extension from the Extensions view to troubleshoot this 

### USER
i can't even enable only the "Continue" extension from the Extensions view to troubleshoot this 

### GEMINI
Thank you for the new screenshot. This is a critical piece of information! The screenshot of the Extensions view shows the "Continue - open-source AI code assistant" extension, and right under its title, it says: "This extension is disabled by the environment." And at the bottom right corner of VS Code, there's a blue bar that says: "All installed extensions are temporarily disabled. Reload to Enable Extensions" This is the root cause of all your problems! The "Continue" extension (and likely all your other extensions) is completely disabled in your current VS Code session. This explains: Why the model isn't showing up (the extension isn't running). Why "Continue" isn't an option in the Output dropdown (the extension isn't registering its output channel because it's disabled). Solution: You need to enable your extensions. The blue bar at the bottom right tells you exactly how: Click the "Reload to Enable Extensions" button in the blue bar at the bottom right of your VS Code window. If you don't see the blue bar, simply restart VS Code completely, or use the Command Palette (Ctrl+Shift+P or Cmd+Shift+P), type Reload Window, and select "Developer: Reload Window". Once VS Code reloads with extensions enabled, the "Continue" extension should now start properly. After reloading and enabling extensions: Confirm ollama serve is still running in your PowerShell terminal. (It needs to be continuously running). Go to the VS Code Output tab. Select "Continue" from the dropdown. You should now see it as an option. Observe the logs in the "Continue" output channel. They should show the extension loading and hopefully connecting to Ollama and finding your model. Check the continue.dev sidebar. Your "Llama 3.1 8B Local (Ollama)" model should finally appear in the "Select model" dropdown. This is almost certainly the solution. Let me know once you've clicked that "Reload to Enable Extensions" button and restarted VS Code!
