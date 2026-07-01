---
category: homelab
date: 2025-06-24
id: 966652
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/topics/tech/homelab.md']
resolution: resolved
sentiment: frustrated
source: GEMINI
summary: TEST
tags:
- homelab
- ai
- gemini
- model
- text-generation
- python
- go
- error
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat server_output.log
15:32:07-681321 INFO     Starting Text generation web UI
15:32:07-683217 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:32:07-684577 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat server_output.log
15:32:07-681321 INFO     Starting Text generation web UI
15:32:07-683217 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:32:07-684577 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
The log file server_output.log shows the exact same output as before, without the "Running on local URL" line from Gradio. This means the issue isn't just a scrolling problem in your terminal. The fact that text-generation-webui reports INFO Starting Text generation web UI but Gradio itself doesn't print its usual URL suggests that Gradio isn't fully initializing its web server. This could be due to a few reasons: Port Conflict: Another program on your system (either in WSL or Windows) might be using port 7860. Firewall: The Windows firewall might be preventing WSL from exposing port 7860 to your Windows browser. Gradio/Dependencies Issue: Less likely since the pip install seemed to complete successfully, but there could be a subtle issue with Gradio's ability to bind to the network. Let's try changing the port text-generation-webui uses, as this often resolves connection issues. We'll try 7861 instead. Try a Different Port First, make sure the current text-generation-webui process is stopped. Go back to your WSL terminal and press Ctrl + C. You should get your prompt back. Now, run the server again, explicitly telling it to use port 7861: python3 server.py --listen --listen-port 7861 --model-menu --verbose Observe the output carefully. Look for a line like Running on local URL: http://127.0.0.1:7861 or similar. If it appears, use that URL in your Windows web browser. If you still don't see the URL, or if you continue to have trouble connecting even with a new port, please let me know the full output of the command.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]