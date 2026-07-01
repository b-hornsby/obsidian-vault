---
category: coding
date: 2025-06-24
id: 879068
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
resolution: resolved
sentiment: frustrated
source: GEMINI
summary: TEST
tags:
- coding
- gemini
- model
- cursor
- text-generation
- python
- rust
- go
---
# (venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat debug_server_output.log
  File "/home/bryan_/text-generation-webui/server.py", line 339
    print("DEBUG: Calling create_interface()")
    ^
IndentationError: expected an indented block after 'try' statement on line 337
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$'

### USER
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cat debug_server_output.log
  File "/home/bryan_/text-generation-webui/server.py", line 339
    print("DEBUG: Calling create_interface()")
    ^
IndentationError: expected an indented block after 'try' statement on line 337
(venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$'

### GEMINI
I understand this is incredibly frustrating. The IndentationError: expected an indented block after 'try' statement means that, no matter how many times we try, the line directly after your try: statement (which is print("DEBUG: Calling create_interface()")) is still not being read by Python as properly indented within the try block. This usually points to a very subtle issue: Invisible characters: Sometimes copy-pasting can introduce invisible characters. Mixed tabs and spaces: If nano or your shell is set to insert tabs when you press tab, and you're manually adding spaces, Python gets confused. Not enough spaces: You might still not be putting exactly 4 spaces (which is standard) for each indentation level. The Most Robust Fix: Replace the Entire Block To eliminate any hidden characters or inconsistent spacing, let's try replacing the entire else: block where this code resides. This ensures all the indentation is consistent from a known good source. Open server.py in nano: nano server.py Locate the else: block: Find the line that says else: that precedes the code you've been working on. This else: itself might be indented depending on what's before it (e.g., if shared.args.api: ... else:). Delete the ENTIRE content of that else: block. Place your cursor on the line immediately after else:. Select all lines within that else: block, down to (but not including) any code that comes after the while True: loop. Delete the selected lines. Carefully paste the following code into the else: block. IMPORTANT: Ensure the try: line and the while True: line are indented to the exact same level as the else: line itself was. All lines within the try/except and while loops should be consistently indented 4 spaces further. # Find the line that says 'else:' (it will have its own indentation) # Then replace everything INSIDE that 'else:' block with this code: # Launch the web UI # The 'try:' below should be at the same indentation level as the original 'create_interface()' was, # or the same level as the 'else:' above if that's where it starts. # It must be consistently 4 spaces from the 'else:'. try: print("DEBUG: Calling create_interface()") create_interface() print("DEBUG: create_interface() returned successfully.") except Exception as e: print(f"DEBUG ERROR: Exception during create_interface(): {e}") import traceback, sys traceback.print_exc() sys.exit(1) # The 'while True:' below should be at the same indentation level as the 'try:' while True: time.sleep(0.5) if shared.need_restart: shared.need_restart = False time.sleep(0.5) shared.gradio['interface'].close() time.sleep(0.5) try: # This 'try' should be indented 4 spaces from the 'if' print("DEBUG: Calling create_interface() for restart.") create_interface() print("DEBUG: create_interface() for restart returned successfully.") except Exception as e: # This 'except' MUST align with the 'try' above it print(f"DEBUG ERROR: Exception during create_interface() on restart: {e}") import traceback, sys traceback.print_exc() sys.exit(1) Save the file and exit nano: (Ctrl + X, then Y, then Enter). Final Attempt to Get the Real Error: Run the server: python3 server.py --listen --listen-port 7862 --model-menu --verbose &> debug_server_output.log Check the log file: cat debug_server_output.log Please, please, please paste the entire content of debug_server_output.log here. If this doesn't fix the indentation, there might be a very unusual nano configuration or shell setting at play.