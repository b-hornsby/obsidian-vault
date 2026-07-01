---
id: 761198
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ollama', 'ai', 'gemini', 'model', 'rust', 'go', 'shell']
category: coding
sentiment: curious
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# it says the workspace isn't trusted when i launched vs code again?  

### USER
it says the workspace isn't trusted when i launched vs code again?  

### GEMINI
You've hit another crucial piece of information! The message "This extension has been disabled because the current workspace is not trusted" (visible in image_a52da4.png under the "Continue" extension details) is the most likely reason why continue.dev is not fully initializing and why you don't see its output channel or models. VS Code has a "Workspace Trust" feature for security. If a workspace (the folder you have open in VS Code) is not trusted, extensions can be disabled or operate with limited functionality to prevent malicious code execution. Even if you don't have a specific "folder" open, if VS Code opens to a default starting point that isn't trusted, or if the ~/.continue folder itself is somehow considered part of an untrusted "workspace," it can disable the extension. Here's the immediate action plan: Trust the Workspace (or the User folder): When you open VS Code, if you see a banner at the top asking if you trust the workspace/folder, click "Trust Folder" or "Trust Workspace". If you don't see a banner, try this: Go to File > Preferences > Settings (or Ctrl+,). Search for "Workspace Trust". Under "Security > Workspace: Trust Enabled", ensure it's checked. Click "Workspace Trust: Manage Workspace Trust". In the dialog that appears, you might see "Untrusted Folders". If your user home directory (e.g., C:\Users\Bryan) or the specific folder you open in VS Code is listed as untrusted, add it to the trusted list. The simplest approach is often to "Trust all files in the current directory" or simply open your C:\Users\Bryan folder in VS Code and mark that as trusted. Verify continue.dev is enabled globally: Go to the Extensions view (Ctrl+Shift+X). Search for "Continue". Ensure the "This extension has been disabled because the current workspace is not trusted" message is GONE. Also, make sure the "Uninstall" button is visible and not "Enable" or "Disable (Workspace)". If it says "Enable (Workspace)", click it. Reload VS Code: Ctrl+Shift+P -> "Developer: Reload Window". Confirm Ollama Server is Running: Make sure your PowerShell with ollama serve is still active. Check the VS Code Output Tab for "Continue": This is the moment of truth! If the workspace trust was the culprit, "Continue" should now appear in the dropdown. Check the continue.dev Sidebar for your model: Your llama3.1:8b-instruct-q4_K_M model should be listed. This "workspace not trusted" message is a very common reason for extensions to not function, and it perfectly explains all the symptoms you've been seeing! Let's hope this is finally the fix.