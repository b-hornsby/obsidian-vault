---
id: 686840
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ollama', 'ai', 'gemini', 'model', 'long', 'go', 'shell']
category: coding
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# PS C:\Users\Bryan> taskkill /PID 27296 /F
ERROR: The process "27296" not found.
PS C:\Users\Bryan>
\

### USER
PS C:\Users\Bryan> taskkill /PID 27296 /F
ERROR: The process "27296" not found.
PS C:\Users\Bryan>
\

### GEMINI
Got it. "ERROR: The process '27296' not found." means that the process you tried to kill (ollama.exe PID 27296) was no longer running when you executed the taskkill command. This is a good sign that the previous taskkill (or some other event) did successfully terminate it, but then something else immediately grabbed the port before you could start your ollama serve. This strongly, strongly points to Ollama running as a Windows Service that automatically restarts very quickly. This is the most common reason for this behavior. We need to confirm and stop that Ollama Windows Service. Here's how to do it again, very carefully: Open Windows Services: Press Windows Key + R (to open the Run dialog). Type services.msc and press Enter. Locate the Ollama Service: In the "Services" window that opens, scroll down alphabetically and look for an entry named: Ollama ollama Or anything that clearly says "Ollama" in the "Name" or "Description" column. Stop and Disable (or set to Manual) the Ollama Service: Once you find it, right-click on the service. Select "Stop". (If it's greyed out, it means it's not running, which would be unusual). Right-click on the service again and select "Properties". In the "General" tab, look for "Startup type". Change it from "Automatic" to "Manual". This will prevent it from automatically restarting with Windows. Click "Apply", then "OK". Confirm the Port is Free (immediately after stopping the service): Go back to your PowerShell window. Run netstat -ano | findstr :11434 Expected result: This command should now return nothing, indicating that port 11434 is free. If it still shows a process, something is seriously wrong with your system, but it's unlikely if you successfully stopped the service. Start Ollama manually: If netstat shows no process, immediately run: ollama serve This must work now. It should start logging messages and say "listening on 127.0.0.1:11434". Keep this PowerShell window open. Proceed with VS Code: With ollama serve running, go back to VS Code. Perform a "Developer: Reload Window" (Ctrl+Shift+P -> "Reload Window"). Check the VS Code Output tab dropdown for "Continue". Check the continue.dev sidebar for your model. The service is almost certainly the culprit. Let me know if you found and stopped the Ollama service!