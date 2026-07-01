---
id: 251472
source: GROK
date: 2025-11-18
tags: ['ngrok', 'chocolatey', 'uninstall', 'windows-cli']
category: coding
sentiment: stuck
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan needed help uninstalling ngrok from his Windows machine after installing it via Chocolatey.
---
# Uninstalling Ngrok via Chocolatey Steps

### HUMAN
how do i delete ngrok from my computer? i used chocolatey to install it

### ASSISTANT
To completely remove **ngrok** from your Windows computer when you installed it via **Chocolatey**, follow these steps. (This assumes you're on Windows, as Chocolatey is primarily for Windows.)

### Step 1: Uninstall via Chocolatey (Recommended)
The cleanest way is to use Chocolatey itself, as it will handle removing the package and any shims/shortcuts it created.

1. Open **Command Prompt** or **PowerShell** **as Administrator** (right-click > Run as administrator). This is required for most Chocolatey operations.

2. Run this command:
   ```
   choco uninstall ngrok -y
   ```
   - The `-y` flag automatically confirms the uninstall (otherwise it will prompt you).
   - If you installed a specific version and want to be sure, you can add `--all-versions`.

   Example output should look something like:
   ```
   Chocolatey vX.X.X
   Uninstalling the following packages:
   ngrok
   ...
   ngrok has been successfully uninstalled.
   ```

If you get an error saying the package isn't found, try `choco uninstall ngrok.portable -y` (older versions of the package used the `.portable` name).

### Step 2: Verify It's Gone
After uninstalling:
```
ngrok --version
```
If it says “'ngrok' is not recognized as an internal or external command”, it's removed from your PATH.

### Step 3: Optional Manual Cleanup (Usually Not Needed)
Chocolatey normally cleans everything up, but if you want to be thorough:

- Delete any leftover folder (rare):  
  `C:\ProgramData\chocolatey\lib\ngrok  
  (or ngrok.portable)

- If you ever manually added ngrok to your system PATH environment variable, remove that entry.

- Check Programs and Features (Add/Remove Programs) — ngrok shouldn't appear there unless you used a very old version.

That’s it! ngrok should now be completely removed from your system. If you run into any errors, paste the exact output here and I can help troubleshoot.
