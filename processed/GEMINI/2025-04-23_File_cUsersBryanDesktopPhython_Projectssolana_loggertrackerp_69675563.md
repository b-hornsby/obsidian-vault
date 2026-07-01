---
category: crypto-web3
date: 2025-04-23
id: 951291
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- solana_logger
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered a KeyError when trying to fetch Solana price data in
  their Python tracker script, indicating the API response doesn't contain the expected
  'solana' key.
tags:
- solana
- python
- api-error
- debugging
- keyerror
---
#   File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 18, in <module>
    price = get_price()
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 9, in get_price
    return data[coin_id][currency]
           ~~~~^^^^^^^^^
KeyError: 'solana'
PS C:\Users\Bryan\Desktop\Phython Projects\solana_logger> 

### USER
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 18, in <module>
    price = get_price()
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 9, in get_price
    return data[coin_id][currency]
           ~~~~^^^^^^^^^
KeyError: 'solana'
PS C:\Users\Bryan\Desktop\Phython Projects\solana_logger> 

### GEMINI
Ah, a classic KeyError! It looks like the dictionary data doesn't have a key named 'solana' at the point where you're trying to access it in the get_price() function. To help you pinpoint the exact cause, could you share the code for your tracker.py file? Specifically, I'd like to see: How the data dictionary is being populated or where it's coming from. The complete get_price() function. Once I see that, I can give you more targeted advice on how to fix this KeyError. It could be a simple typo, an issue with the data source, or a logical error in how you're handling the data. Let's take a look!