---
id: 094709
source: GEMINI
date: 2025-06-24
tags: ['coding', 'ai', 'gemini', 'model', 'text-generation', 'python', 'go', 'error']
category: coding
sentiment: curious
resolution: abandoned
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --listen --model-menu --verbose
15:30:58-137486 INFO     Starting Text generation web UI
15:30:58-139786 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:30:58-141220 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --listen --model-menu --verbose
15:30:58-137486 INFO     Starting Text generation web UI
15:30:58-139786 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:30:58-141220 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
It's quite peculiar that the URL isn't showing up, even with --verbose. The logs you're seeing (like "Starting Text generation web UI") are from text-generation-webui itself, but the actual URL is typically printed by Gradio, the underlying library that creates the web interface. If Gradio isn't printing a URL, it means it's not fully initializing its web server in a way that provides that direct access link. Let's try a more robust way to capture all the output, including anything that might scroll off the screen or is sent to a different output stream. We'll direct all the console output to a file. First, make sure the previous python3 server.py process is stopped. Press Ctrl + C in your WSL terminal to get your prompt back. Then, run the command like this: python3 server.py --listen --model-menu --verbose &> server_output.log This command will: Start text-generation-webui as before. The &> part redirects all output (both standard output and standard error) into a file named server_output.log. Because the output is redirected, you might not see much in your terminal. You'll get your prompt back very quickly, which means the process is running in the background and logging to the file. Once you get your prompt back, let's look at the contents of that log file to find the URL. cat server_output.log Please copy and paste the entire content of server_output.log here. I'll meticulously go through it to find the URL or any other errors that might explain why the connection isn't working.