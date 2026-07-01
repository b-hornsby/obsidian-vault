---
category: homelab
date: 2025-06-24
id: 164244
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- private-ai-consulting
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user was trying to run the Text Generation WebUI with Gradio but encountered
  a connection issue and a security warning about exposing the interface without authentication,
  indicating they are setting up a local AI tool in their homelab environment.
tags:
- text-generation-webui
- gradio-auth
- local-ai
- network-security
- server-configuration
---
# running the url didn't connect to the webui. the thing i got was: (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --listen --model-menu
15:28:17-944390 INFO     Starting Text generation web UI
15:28:17-946589 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:28:17-951042 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
running the url didn't connect to the webui. the thing i got was: (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ python3 server.py --listen --model-menu
15:28:17-944390 INFO     Starting Text generation web UI
15:28:17-946589 WARNING
                         You are potentially exposing the web UI to the entire internet without any access password.
                         You can create one with the "--gradio-auth" flag like this:

                         --gradio-auth username:password

                         Make sure to replace username:password with your own.
15:28:17-951042 ERROR    No models are available! Please download at least one.
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You're right to point that out. My apologies for the assumption. The output you provided doesn't explicitly show the Running on local URL: line, which is what we need to see. It's very likely that it scrolled off the screen, just like the "Successfully installed" message from the pip command. The server is definitely starting (as indicated by "Starting Text generation web UI"), but we need to confirm the exact address. Let's try running it again, but this time with a --verbose flag to ensure all output is shown, and we can specifically look for the URL. Please stop the current running server in your WSL terminal (if it's still running) by pressing Ctrl + C. You should get your prompt back. Then, run this command: python3 server.py --listen --model-menu --verbose Please paste the entire output you get from this command. I'll be looking for a line that starts with something like: Running on local URL: http://127.0.0.1:7860 Or Running on public URL: https://[some-random-gradio-url] (if it tries to use Gradio's public share, which it shouldn't with --listen unless a firewall blocks local access). The key is that Running on local URL: line. That's the address you'll put into your web browser.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]