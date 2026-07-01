---
id: 631936
source: GEMINI
date: 2025-07-29
tags: ['homelab', 'ollama', 'ai', 'gemini', 'model', 'long', 'shell', 'code']
category: homelab
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
---
# what am i doing wrong?: >>> /bye
PS C:\Users\Bryan> ollama serve
Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
PS C:\Users\Bryan>

### USER
what am i doing wrong?: >>> /bye
PS C:\Users\Bryan> ollama serve
Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
PS C:\Users\Bryan>

### GEMINI
You're very close! The error message: Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted. This error means exactly what it says: something else is already using port 11434 on your computer. This is the default port that Ollama uses for its server. This usually happens because: Ollama Server is Already Running in the Background: You might have started ollama serve previously in another terminal, or it might have been configured to start automatically, and that instance is still running. Another Application is Using Port 11434: Less likely, but possible, another piece of software on your computer is coincidentally using the same port. What to do: You need to find the existing process that is using port 11434 and terminate it. Here's how you can do it on Windows (using PowerShell or Command Prompt): Find the Process ID (PID) using the port: Open a new PowerShell or Command Prompt window and run: netstat -ano | findstr :11434 This command lists all active network connections and listening ports, then filters for anything using port 11434. You'll get output similar to this (the PID is the last number on the line): TCP 127.0.0.1:11434 0.0.0.0:0 LISTENING 1234 In this example, 1234 would be the PID. Identify the application using the PID (Optional but Recommended): Once you have the PID, you can see which application it belongs to: tasklist /fi "PID eq 1234" (Replace 1234 with the actual PID you found). This will show you the image name (e.g., ollama.exe). Terminate the Process: Once you're confident it's the Ollama server (or if you can't find another obvious culprit), you can kill the process using its PID: taskkill /PID 1234 /F (Again, replace 1234 with your actual PID). /F forces the termination of the process. After terminating the old process: Try ollama serve again in your PowerShell window. It should now start successfully without the "bind" error. Keep that window open as the Ollama server needs to be running. Reload VS Code as before to pick up the model. This should resolve the issue and allow continue.dev to connect to your Ollama model.