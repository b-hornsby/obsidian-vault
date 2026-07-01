---
category: coding
date: 2025-04-25
id: 515939
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- solana_logger
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered a SyntaxError in their Python script tracker.py related
  to a misplaced except block, indicating a structural issue with their error handling
  code.
tags:
- Python
- SyntaxError
- Solana
- Debugging
- Script Execution
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/solana_logger/tracker.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 26
    except KeyError:
    ^^^^^^
SyntaxError: invalid syntax

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/solana_logger/tracker.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 26
    except KeyError:
    ^^^^^^
SyntaxError: invalid syntax

### GEMINI
Okay, another SyntaxError. This time, it's pointing to the except KeyError: line, specifically the except keyword. This kind of error often arises when there's an issue with the preceding try block. Looking back at the code snippet you shared earlier: for coin_id, display_name in coin_dict.items(): try: price = get_price(coin_id, currency) prices[display_name] = price except KeyError: print(f"Could not fetch price for: {display_name} ({coin_id})") return prices The structure looks correct. A try block should always be immediately followed by at least one except block or a finally block. However, the traceback indicates the error is on line 26. Let's consider the possibility of some invisible characters or indentation issues that might not be obvious. Could you please share the exact code block around lines 23 to 27 of your tracker.py file? Copy and paste it directly. This will help me see if there's anything subtle going on with the indentation or if there's another issue in the lines leading up to the except statement. Sometimes, even a seemingly correct structure can have hidden problems like mixed tabs and spaces for indentation, which Python can be sensitive to. Let's take a closer look at that specific section of your code.