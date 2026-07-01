---
source: GEMINI
date: 2025-06-24
category: ai-tools
id: 36555040
linked_nodes: ['nodes/people/bryan.md']
---
-
---
-
  warnings.warn(
Attempting to launch Gradio demo...
Running on local URL:  http://0.0.0.0:7862

To create a public link, set `share=True` in `launch()`.
Keyboard interruption in main thread... closing server.
Gradio demo launch command executed.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/gradio_test.py", line 13, in <module>
    time.sleep(60) # Keep the script running for a bit to see if it eventually launches
    ^^^^^^^^^^^^^^
KeyboardInterrupt
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$
### USER
/home/bryan_/text-generation-webui/venv/lib/python3.12/site-packages/gradio/analytics.py:106: UserWarning: IMPORTANT: You are using gradio version 4.37.2, however version 4.44.1 is available, please upgrade.
-
---
-
---
  warnings.warn(
Attempting to launch Gradio demo...
Running on local URL:  http://0.0.0.0:7862

To create a public link, set `share=True` in `launch()`.
Keyboard interruption in main thread... closing server.
Gradio demo launch command executed.
Traceback (most recent call last):
  File "/home/bryan_/text-generation-webui/gradio_test.py", line 13, in <module>
    time.sleep(60) # Keep the script running for a bit to see if it eventually launches
    ^^^^^^^^^^^^^^
KeyboardInterrupt
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Excellent! This is a major breakthrough! The log output: Running on local URL: http://0.0.0.0:7862 This confirms that: Gradio IS successfully launching its web server and binding to a network interface. The reason your prompt didn't return immediately is because the time.sleep(60) was keeping the script alive for 60 seconds (or until you pressed Ctrl + C). So, the core problem is NOT Gradio failing to launch. It's likely one of these: You're trying to access the wrong URL or IP from Windows. While the server is listening on 0.0.0.0 (which means "all available interfaces"), you typically access it from your Windows browser using http://127.0.0.1:[port] or http://localhost:[port]. Windows Firewall is blocking the connection. Even though WSL is listening, Windows Firewall might be preventing your browser from connecting to that port. Critical Test: Access the Running Gradio Demo Let's test this directly. Run the gradio_test.py script again, but this time, DO NOT press Ctrl + C immediately. python3 gradio_test.py (You won't get your prompt back for 60 seconds, which is intended this time). While that script is running in the WSL terminal (before the 60 seconds pass), open your web browser on Windows. Go to this URL: http://127.0.0.1:7862 You should see a very simple Gradio interface with an input box and an output box (where you can type a name and it says "Hello [Name]!"). What to do next: If you successfully access http://127.0.0.1:7862 and see the Gradio "Hello" demo: This is fantastic! It means WSL's networking is working, and Windows can access applications running on ports in WSL. The problem then likely lies in text-generation-webui's own startup or a specific port it uses. We'll then re-run text-generation-webui and try to access its default port (7860 or 7861 if you used that last). If you cannot access http://127.0.0.1:7862 and get a "connection refused" or "site unreachable" error: This points strongly to a Windows Firewall issue. We'll need to create an inbound rule for the port. Please let me know if you can access http://127.0.0.1:7862 while the gradio_test.py script is running!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]