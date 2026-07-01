---
category: coding
date: 2025-04-29
id: 371663
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- murad_market_tracker
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: User encountered a Python syntax error while running a market tracker script
  and is seeking help to fix the invalid syntax issue on line 70.
tags:
- python
- syntax-error
- debugging
- beginner-coding
- script-execution
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 70
    else:
    ^^^^
SyntaxError: invalid syntax
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 70
    else:
    ^^^^
SyntaxError: invalid syntax
PS C:\Users\Bryan>

### GEMINI
You're doing a fantastic job of pinpointing these errors! This SyntaxError: invalid syntax on line 70: else: indicates an issue with the else block. Looking at the code around it: if change_24h is not None: indicator = "🟢" if change_24h >= 0 else "🔴" print(f"24h Change: {change_24h:.2f}% {indicator}") else: print("24h change: data not available ⚠️") The else block here is correctly associated with the if change_24h is not None: statement. The indentation within both the if and else blocks also looks correct in this snippet. The problem might be due to inconsistent indentation before this if/else block. Double-check the indentation of the lines leading up to if change_24h is not None:. If the if statement itself has incorrect indentation (e.g., it's inside a loop or another block unintentionally), that could cause the else to be seen as out of place. Could you share the few lines of code immediately preceding this if/else block? That will help me understand the context and identify the root cause of this SyntaxError. 😊