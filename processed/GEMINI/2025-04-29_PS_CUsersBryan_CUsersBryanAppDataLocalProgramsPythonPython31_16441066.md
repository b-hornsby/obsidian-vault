---
category: coding
date: 2025-04-29
id: 998320
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered an IndentationError in their Python script 'murad_market_tracker'
  and was trying to run it but got stuck due to a syntax issue on line 63.
tags:
- python
- indentation-error
- debugging
- script-execution
- syntax-fix
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 63
    print(f"24h Change: {change_24h:.2f}% {indicator}")
IndentationError: unexpected indent
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 63
    print(f"24h Change: {change_24h:.2f}% {indicator}")
IndentationError: unexpected indent
PS C:\Users\Bryan>

### GEMINI
You've got a keen eye for these indentation errors! The latest one is on line 63: print(f"24h Change: {change_24h:.2f}% {indicator}") Just like the previous one, this line seems to be indented one level too far. It's inside the if change_24h is not None: block, which is correct, but the print statement itself shouldn't have that extra indentation. Here's the corrected section: print(f"Market Cap: ${market_cap:,.0f}") if change_24h is not None: indicator = "🟢" if change_24h >= 0 else "🔴" print(f"24h Change: {change_24h:.2f}% {indicator}") else: print("24h change: data not available ⚠️") I've removed the extra indentation from the print(f"24h Change...") line. Make sure the lines within the if block are indented consistently. Let's run it again and see if we've tamed all the indentation gremlins for now! 😊