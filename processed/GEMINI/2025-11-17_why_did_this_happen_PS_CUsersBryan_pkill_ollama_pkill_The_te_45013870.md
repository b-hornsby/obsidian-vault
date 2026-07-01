---
id: 840020
source: GEMINI
date: 2025-11-17
tags: ['homelab', 'ollama', 'ai', 'gemini', 'dex', 'go', 'shell', 'script']
category: homelab
sentiment: frustrated
resolution: abandoned
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
---
# why did this happen?: PS C:\Users\Bryan> pkill ollama
pkill : The term 'pkill' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ pkill ollama
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (pkill:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\Bryan>

### USER
why did this happen?: PS C:\Users\Bryan> pkill ollama
pkill : The term 'pkill' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ pkill ollama
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (pkill:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\Bryan>

### GEMINI
This happened because the command pkill is not a native command in Windows PowerShell (PS), which is the environment you were using. 💻 Command Recognition pkill is a standard utility command used on Linux and macOS (Unix-like systems) to send a signal (by default, termination) to processes based on their name. PowerShell (the shell in Windows) does not have a built-in command named pkill. This is why the error message says: "The term 'pkill' is not recognized as the name of a cmdlet, function, script file, or operable program." 🛠️ The Windows Equivalent To achieve the same goal—killing a process by its name—in Windows PowerShell, you should use the following common cmdlets: Find the process: Use Get-Process (or its alias, gps) to find the process named 'ollama'. Stop the process: Pipe the result to Stop-Process (or its alias, kill). The correct command to stop the 'ollama' process in PowerShell is: Get-Process -Name ollama | Stop-Process Alternative using taskkill (a legacy Windows command) You could also use the older command-line utility taskkill, though the PowerShell-native method above is generally preferred: taskkill /IM ollama.exe /F /IM: Specifies the Image Mame (the process name). /F: Forces the termination of the process. Would you like me to run the correct PowerShell command to stop a process by name?