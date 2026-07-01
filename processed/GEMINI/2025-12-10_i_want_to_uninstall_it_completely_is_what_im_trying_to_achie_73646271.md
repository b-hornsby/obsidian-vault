---
category: general
date: 2025-12-10
id: 256747
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble completely uninstalling a piece of software.
tags:
- software-uninstall
- persistent-software
- windows-troubleshooting
- application-removal
---
# i want to uninstall it completely is what i'm trying to achieve but its sticky for some reason 

### USER
i want to uninstall it completely is what i'm trying to achieve but its sticky for some reason 

### GEMINI
The desire for a clean break is valid, especially when a program doesn't behave as expected. You are not fooling yourself; Ollama does leave files behind, and the CLI being sticky is annoying. Here is the precise, prioritized plan for a complete uninstallation of Ollama on Windows, focusing on the steps needed to kill all residual processes and delete the data folders that hold the massive model files. 🛑 Prioritized Uninstallation Plan (Windows) Step 1: Terminate the Server and Uninstall the Program You must stop the running service/app first, or the uninstaller will fail. Stop the Server (Crucial): Find the Ollama icon in your Windows System Tray (near the clock). Right-click it and select Exit or Quit. If you cannot find this icon, move to the task manager step. Verify/Force Stop via Task Manager: Press Ctrl + Shift + Esc to open Task Manager. Look for any process named ollama.exe. If found, Right-click it and select End task. Run the Standard Uninstall: Open Windows Settings and go to Apps (or Add or remove programs). Find Ollama in the list. Click it and select Uninstall. Step 2: Delete Residual Files (The "Sticky" Part) The uninstaller does not always remove the large model files, which is likely why you feel it's "sticky" and still on your system. These are in a hidden folder in your user profile. Delete the Main Data/Model Folder: This is where the downloaded models (potentially many GBs) and configuration are stored. Open File Explorer. In the address bar, type: %USERPROFILE%\.ollama Press Enter. Delete the entire .ollama folder. (The path is usually C:\Users\YourUsername\.ollama) Delete Program Files: The core application files might linger. In the address bar, type: %LOCALAPPDATA%\Programs\Ollama Press Enter. Delete the entire Ollama folder if it exists. Step 3: Remove the CLI Path (The PowerShell Fix) The reason the command ollama still works in PowerShell, even if the program is gone, is because your system's PATH variable was updated. Open Environment Variables: Search the Start Menu for "environment variables" and click Edit the system environment variables. Click the Environment Variables... button. In the top pane (User variables for [Your Username]), look for a variable named Path. Clean the Path: Select Path and click Edit.... Look for any entry that contains Ollama (it often points to a folder like %LOCALAPPDATA%\Programs\Ollama\). Select that entry and click Delete. Click OK to close all windows. Step 4: Final Cleanup Restart PowerShell: You must close any currently open PowerShell windows and open a new one for the PATH changes to take effect. Test: In the new PowerShell window, type ollama and press Enter. It should now respond with: ollama : The term 'ollama' is not recognized... or a similar "command not found" error. This confirms the complete removal. You now have a clean system. What is your next strategic focus that you've freed up time and disk space for?
