---
id: 865473
source: GEMINI
date: 2025-07-29
tags: ['continue.dev', 'uninstall', 'vs-code', 'reinstall']
category: ai-tools
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan is asking what to do next after uninstalling continue.dev and wants to retry the setup process.
---
# okay so now that thats done and i uninstalled continue.dev now what? 

### USER
okay so now that thats done and i uninstalled continue.dev now what? 

### GEMINI
Okay, excellent! Finding AppData and uninstalling "Continue" was a crucial step for the deep clean. Now that the old "Continue" extension files are gone, and assuming you've also deleted the CachedData and Local Storage folders (and potentially the Code folder itself if you went with the most aggressive clean), it's time to reinstall. Here are the next steps to get continue.dev running correctly: Restart your computer (if you haven't already). This is important to clear any lingering processes or file locks. Open VS Code. Reinstall the "Continue - open-source AI code assistant" extension from the Marketplace: Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X). Search for "Continue". Click the "Install" button. Reload VS Code: VS Code should prompt you to reload after installing. If not, open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P), type Reload Window, and select "Developer: Reload Window". Verify Ollama Server is Running: Open your PowerShell window. Ensure ollama serve is actively running. If it's not, start it and keep that window open. Check the VS Code Output Tab for "Continue": Go to View -> Output. Click the dropdown menu on the right (where you previously saw "Tasks", "Extension Host", etc.). Crucially, you should now see "Continue" as an option. Select it. Observe the logs in this panel for any errors or messages about loading the configuration. Check the continue.dev Sidebar: Click on the "Continue" icon in the VS Code sidebar (the AI brain icon). Look at the "Select model" dropdown. Your "Llama 3.1 8B Local (Ollama)" model, as defined in your config.yaml, should now appear here. This complete reinstall after clearing the cached data is designed to resolve deep-seated issues where the extension wasn't properly initializing or registering its components. If it still doesn't work after this, we'll have to consider it a highly unusual system-specific problem. Let me know what happens, especially if "Continue" appears in the Output dropdown!
