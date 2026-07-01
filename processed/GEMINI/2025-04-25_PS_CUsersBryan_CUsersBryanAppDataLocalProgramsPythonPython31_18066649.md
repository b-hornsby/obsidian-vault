---
category: coding
date: 2025-04-25
id: 674993
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- solana_logger
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered a SyntaxError in their Python script while trying to
  run a Solana price tracker, indicating a missing underscore in a function call.
tags:
- python
- syntax-error
- solana
- debugging
- scripting
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/solana_logger/tracker.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 24
    price = get price(coin_id, currency)
                ^^^^^
SyntaxError: invalid syntax

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/solana_logger/tracker.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 24
    price = get price(coin_id, currency)
                ^^^^^
SyntaxError: invalid syntax

### GEMINI
Ah, a SyntaxError! Python is telling you that it doesn't understand something in the structure of your code. Looking at the traceback, it's pointing to line 24 of your tracker.py file: price = get price(coin_id, currency) The issue here is the space between get and price. In Python, when you want to call a function, you write the function name immediately followed by the parentheses containing the arguments. The space is causing Python to interpret get as something separate from price(coin_id, currency), leading to the invalid syntax. To fix this, you need to remove the space: price = get_price(coin_id, currency) Make sure there are no spaces between get and price. This should resolve the SyntaxError. Give it a try after making this correction! Let me know if you encounter any other snags. We're getting closer to a smoothly running logger!