---
id: 972542
source: GEMINI
date: 2025-07-29
tags: ['coding', 'ollama', 'ai', 'gemini', 'rust', 'go', 'shell', 'code']
category: coding
sentiment: frustrated
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# so i opened my termianl and did the ollama serve command and got this even though i just restarted my pc: PS C:\Users\Bryan> ollama serveError: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.PS C:\Users\Bryan>

### USER
so i opened my termianl and did the ollama serve command and got this even though i just restarted my pc: PS C:\Users\Bryan> ollama serveError: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.PS C:\Users\Bryan>

### GEMINI
Ah, good catch. It's frustrating when you restart and the port is still in use! This "bind: Only one usage of each socket address..." error means that something is still holding onto port 11434, even after a PC restart. This can happen if: Ollama is set to run as a background service: Sometimes, Ollama gets installed in a way that it automatically starts with Windows as a service. This means it's running before you even log in or open a terminal. A lingering process: While a restart usually clears everything, very occasionally a process can remain or a driver might hold onto a port. What we need to do is confirm if Ollama is running as a service, or find the process holding the port. Let's check for an Ollama service first: Method 1: Check Windows Services Press Windows Key + R to open the Run dialog. Type services.msc and press Enter. This will open the Services management console. In the Services window, look for a service named anything like "Ollama", "ollama.exe", or similar. If you find it: Select the service. Check its "Startup type." If it's "Automatic," that explains why it's always running. Right-click on the service and select "Stop." (Optional: You can change its "Startup type" to "Manual" if you only want to run it when you explicitly type ollama serve.) Method 2: Manually Find and Kill the Process (Again) If you don't find a service, or if stopping the service doesn't work, you'll have to find the process holding the port manually. This is the same set of commands we used before, but now we're expecting a different result since you just restarted. Open PowerShell or Command Prompt as Administrator. (Right-click on the PowerShell icon and select "Run as administrator"). Run the command to find the PID: netstat -ano | findstr :11434 Look for the LISTENING line and note the PID (the last number). Once you have the PID, try to find out what process it is: tasklist /fi "PID eq <YOUR_PID_HERE>" (Replace <YOUR_PID_HERE> with the actual PID you found). If it's ollama.exe: Then it confirms Ollama is indeed running, likely as a service. If it's something else: Note down the process name, as that's the unexpected culprit. Terminate the process: taskkill /PID <YOUR_PID_HERE> /F After you successfully stop the process holding port 11434: Go back to your PowerShell window and try ollama serve again. It should now start without the bind error. Keep that ollama serve window open. Proceed with reinstalling "Continue" in VS Code, reloading VS Code, and checking the Output dropdown and sidebar. It's highly probable that Ollama is starting as a service for you, which is why it's always occupying the port.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]