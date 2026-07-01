---
category: coding
date: 2025-04-29
id: 547547
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: stuck
source: GEMINI
summary: The user is running a Python market tracker script and encountering an IndentationError
  due to improper indentation on line 57, indicating they need to fix the spacing/formatting
  of their print statement in the file structure.
tags:
- python debugging
- indentation error
- script execution
- syntax troubleshooting
- file path handling
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 57
    print(f"{name.upper()} ({symbol.upper()})")
IndentationError: unexpected indent

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 57
    print(f"{name.upper()} ({symbol.upper()})")
IndentationError: unexpected indent

### GEMINI
Another indentation issue! You're becoming quite the expert at spotting these in the traceback. The error is now on line 57: print(f"{name.upper()} ({symbol.upper()})") This line also has an unexpected indent. It looks like it should be at the same indentation level as the headers = [...] and print(tabulate(...)) lines above it. Here's the corrected section of your code: headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{name.upper()} ({symbol.upper()})") print(f"Price: ${price:,.2f}") print(f"Market Cap: ${market_cap:,.0f}") if change_24h is not None: indicator = "🟢" if change_24h >= 0 else "🔴" print(f"24h Change: {change_24h:.2f}% {indicator}") else: print("24h change: data not available ⚠️") I've dedented the print(f"{name.upper()}...") line and the subsequent print and if/else block. These lines appear to be outside the loop that processes the coins, so they should be at the top level of your script (after the loop). Give this adjustment a try! We're steadily making progress. 😊