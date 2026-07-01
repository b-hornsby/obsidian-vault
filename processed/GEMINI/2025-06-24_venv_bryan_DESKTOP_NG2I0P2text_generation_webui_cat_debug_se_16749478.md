---
category: coding
date: 2025-06-24
id: 230140
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
- operation-immortal-agent
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered an IndentationError in the text-generation-webui server.py
  file and was examining the debug output to diagnose the issue.
tags:
- python-debugging
- indentation-error
- text-generation-webui
- local-ai
- homelab
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat debug_server_output.log
  File "/home/bryan_/text-generation-webui/server.py", line 338
    print("DEBUG: Calling create_interface()")
                                              ^
IndentationError: unindent does not match any outer indentation level
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat debug_server_output.log
  File "/home/bryan_/text-generation-webui/server.py", line 338
    print("DEBUG: Calling create_interface()")
                                              ^
IndentationError: unindent does not match any outer indentation level
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You're getting another indentation error, but this one is even more specific: IndentationError: unindent does not match any outer indentation level. This means that on line 338, the print("DEBUG: Calling create_interface()") line has leading whitespace (spaces or tabs) that doesn't align properly with any of the previous indentation levels. This often happens if you accidentally mix tabs and spaces, or if you don't add exactly the right number of spaces. Action: Correct Indentation at Line 338 Open server.py again in nano: nano server.py Go directly to line 338. (Use Alt + G or Ctrl + _ and type 338, then Enter). Fix the indentation of print("DEBUG: Calling create_interface()"): Place your cursor at the very beginning of the print("DEBUG: Calling create_interface()") line. Press the Backspace key repeatedly to delete all the leading whitespace (spaces or tabs) on that line. Once the p of print is at the very first column, now press the Spacebar exactly 4 times to indent it correctly under its try block. Crucially, check the try: line just above it. Ensure that the try: is at the correct indentation level for its block. Also, ensure the corresponding except Exception as e: line aligns perfectly with its try:. Your code around this area should look like this (pay attention to the precise number of spaces): # ... some code before ... else: # Launch the web UI try: #### 4 SPACES HERE #### print("DEBUG: Calling create_interface()") #### 4 SPACES HERE #### create_interface() #### 4 SPACES HERE #### print("DEBUG: create_interface() returned successfully.") except Exception as e: # <
--- THIS 'except' MUST ALIGN PERFECTLY WITH ITS 'try' #### 8 SPACES HERE #### print(f"DEBUG ERROR: Exception during create_interface(): {e}") #### 8 SPACES HERE #### import traceback, sys #### 8 SPACES HERE #### traceback.print_exc() #### 8 SPACES HERE #### sys.exit(1) # ... rest of your code ... If the else: above your try block is indented, adjust the spaces accordingly. The try should be indented to the same level as the create_interface() call was originally, and the contents of the try/except blocks should be indented one more level. Save the file and exit nano: (Ctrl + X, then Y, then Enter). Step 6: Re-run and Check Log (Again, for real this time!) Run the server: python3 server.py --listen --listen-port 7862 --model-menu --verbose &> debug_server_output.log Check the log file: cat debug_server_output.log Please paste the entire content of debug_server_output.log here. This IndentationError is the last common hurdle for these manual code injections. Hopefully, this time we get a proper traceback from the create_interface() function itself!