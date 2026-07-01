---
id: 719737
source: GEMINI
date: 2025-11-17
tags: ['homelab', 'ollama', 'ai', 'gemini', 'model', 'go', 'shell', 'code']
category: homelab
sentiment: frustrated
resolution: abandoned
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
---
# ran these commands and ollama wont serve?: Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\Bryan> ollama list
NAME                                 ID              SIZE      MODIFIED
qwen2.5-coder:14b-instruct-q4_K_M    9ec8897f747e    9.0 GB    22 minutes ago
PS C:\Users\Bryan> ollama serve
Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
PS C:\Users\Bryan>

### USER
ran these commands and ollama wont serve?: Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\Bryan> ollama list
NAME                                 ID              SIZE      MODIFIED
qwen2.5-coder:14b-instruct-q4_K_M    9ec8897f747e    9.0 GB    22 minutes ago
PS C:\Users\Bryan> ollama serve
Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
PS C:\Users\Bryan>

### GEMINI
It looks like you're running into a common issue when trying to start the Ollama server: the port is already in use. The error message Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted. means that another process is already using the network address (127.0.0.1) and port (11434) that Ollama tries to use by default. 💡 Why Ollama Won't Serve This usually happens because Ollama is already running in the background as a service or a separate process. On Windows, when you install Ollama, it often starts automatically and keeps running so it's ready to use. When you run ollama serve manually, it attempts to start a second instance of the server, which fails because the port is occupied by the first one. ✅ Steps to Fix the Issue You generally do not need to run ollama serve manually unless you've explicitly stopped the background service. Since you've already pulled a model (qwen2.5-coder), you should be able to interact with it directly. 1. Try Running a Model Directly Since the server is likely already running, you should be able to use the ollama run command immediately. Command to Try: ollama run qwen2.5-coder:14b-instruct-q4_K_M This command will connect to the existing, running server and start an interactive chat session with your downloaded model. 2. Verify and Stop the Existing Server (If needed) If you must run ollama serve in your current PowerShell window (e.g., for troubleshooting or specific environment setups), you first need to stop the background process. Find the process using the port: netstat -ano | findstr :11434 This command will show you the process ID (PID) using port 11434. Stop the process: Once you have the PID (e.g., if the PID is 1234), you can terminate it. Stop-Process -Id 1234 -Force Replace 1234 with the actual PID you found. After stopping the original process, you should be able to run ollama serve without the error. Would you like to try running the model directly with ollama run now, or would you like to check for the background process?