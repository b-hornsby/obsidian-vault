---
category: coding
date: 2025-06-24
id: 749842
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- text-generation-webui
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered an IndentationError in the text-generation-webui server.py
  file where a print statement was not properly indented after a try block, and is
  seeking help debugging the Python syntax issue in their homelab setup.
tags:
- python-debugging
- indentation-error
- text-generation-webui
- server-setup
- syntax-error
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat debug_server_output.log
  File "/home/bryan_/text-generation-webui/server.py", line 338
    print("DEBUG: Calling create_interface()")
IndentationError: expected an indented block after 'try' statement on line 337
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat debug_server_output.log
  File "/home/bryan_/text-generation-webui/server.py", line 338
    print("DEBUG: Calling create_interface()")
IndentationError: expected an indented block after 'try' statement on line 337
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You're very persistent, and we're getting closer! This is still an indentation error, but it's a different one, which is progress. IndentationError: expected an indented block after 'try' statement on line 337 This error means that Python expects the line immediately following a try: statement (which is print("DEBUG: Calling create_interface()") on line 338) to be indented. It's telling you that either: Line 338 is not indented at all, or not enough, relative to line 337 (try:). There's still an inconsistent mix of spaces and tabs, causing Python to misinterpret the indentation level. Action: Precise Indentation Fix (Again!) This is the trickiest part of manual Python editing. Let's be extremely precise this time. Open server.py again in nano: nano server.py Go directly to line 337. (Use Alt + G or Ctrl + _ and type 337, then Enter). Focus on the try: line and the lines immediately after it: # ... code before ... else: # Launch the web UI try: # <
--- THIS IS LINE 337 # This next line (print) MUST be indented EXACTLY 4 spaces from the 'try:' print("DEBUG: Calling create_interface()") # <
--- THIS IS LINE 338 create_interface() print("DEBUG: create_interface() returned successfully.") except Exception as e: # <
--- THIS 'except' MUST ALIGN PERFECTLY WITH ITS 'try' print(f"DEBUG ERROR: Exception during create_interface(): {e}") import traceback, sys traceback.print_exc() sys.exit(1) # ... rest of your code ... How to fix line 338 (and the others in the try block): Place your cursor at the very beginning of the print("DEBUG: Calling create_interface()") line. Press the Backspace key repeatedly until the p of print is at the very first column (no leading spaces or tabs at all). Now, press the Spacebar exactly 4 times. This should correctly indent it under the try: statement. Do the same for the create_interface() line and the print("DEBUG: create_interface() returned successfully.") line. Make sure they also start with exactly 4 spaces. Also, double-check that the except Exception as e: line has the same number of leading spaces as the try: line. And all the lines inside the except block should be indented 4 spaces from the except line. This precise correction is key for Python to understand the code structure. Save the file and exit nano: (Ctrl + X, then Y, then Enter). Step 7: The Moment of Truth (Run and Check Log) Run the server one more time: python3 server.py --listen --listen-port 7862 --model-menu --verbose &> debug_server_output.log Check the log file: cat debug_server_output.log Please paste the entire content of debug_server_output.log here. If we've conquered the indentation, this should finally give us the real error message from the UI creation!