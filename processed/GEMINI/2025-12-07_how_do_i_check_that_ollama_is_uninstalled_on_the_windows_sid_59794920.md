---
category: ai-tools
date: 2025-12-07
id: 5405
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to verify that Ollama is completely uninstalled from
  Windows.
tags:
- ollama
- uninstall
- windows-11
- local-llm
---
# how do i check that ollama is uninstalled on the windows side of things? 

### USER
how do i check that ollama is uninstalled on the windows side of things? 

### GEMINI
That's a crucial checkpoint. You want verification that the destruction process was absolute, not just a successful app uninstall. Ollama, on Windows, typically leaves three major categories of artifacts behind: the running process/service, the application binary/entry, and the massive model data. Here is the prioritized checklist and the precise commands/steps you need to run to confirm the full removal on the Windows side. 🔬 Ollama Deletion Verification Checklist 1. The Running Service/Process (The Most Important Check) If the service is running, it means the core engine is still active. Task Manager Check: Press Ctrl + Shift + Esc to open Task Manager. Go to the Details tab. Look for any process named ollama.exe. Verification of Removal: If you do not see it, the process is stopped. PowerShell Check (More Definitive): Open PowerShell (no need for Admin rights). Run the command: Get-Process -Name "ollama" -ErrorAction SilentlyContinue Verification of Removal: If the command returns nothing (no red errors, no output), the main process is confirmed as dead. API Port Check (The Final Seal): Ollama defaults to port 11434. Check if anything is listening there. Run the command: curl http://localhost:11434 Verification of Removal: You should receive an error like "Connection refused" or "Failed to connect to localhost port 11434." If you get the response "Ollama is running," you have a ghost process you missed. 2. Application and Files (The Space Wasters) These confirm the installer is gone and the large model data is eliminated. App List Check: Go to Settings > Apps > Installed apps (or Apps & features). Search the list for "Ollama". Verification of Removal: You should not find an entry for Ollama. Model Data Check: Open File Explorer. Navigate to your user profile directory. You can use this shortcut: %USERPROFILE% Look for a hidden folder named .ollama. Verification of Removal: The folder .ollama should be deleted. This is where the multi-gigabyte models are stored. If it's still there, delete it manually. 3. Command Line Artifacts (The Path Cleaner) This ensures you can't accidentally invoke the old command. Command Verification: Open Command Prompt or PowerShell. Type the main command: ollama Verification of Removal: You should get an error message like "'ollama' is not recognized as an internal or external command, operable program or batch file." If it returns the Ollama usage instructions, the executable is still in your system's PATH. Execute these three categories of checks, starting with the running process. If all checks pass, your deletion was complete.
