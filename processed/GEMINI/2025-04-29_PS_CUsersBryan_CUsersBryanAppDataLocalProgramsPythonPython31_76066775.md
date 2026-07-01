---
category: coding
date: 2025-04-29
id: 511341
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered a SyntaxError in their Python market tracker project
  due to incorrect dictionary key access syntax (missing dot notation), and the issue
  was not yet fixed in the provided excerpt.
tags:
- python
- syntax-error
- debugging
- dictionary-access
- beginner-mistake
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 10
    'name': data ['name']
            ^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 10
    'name': data ['name']
            ^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
PS C:\Users\Bryan>

### GEMINI
Ah, the dreaded SyntaxError: invalid syntax! It looks like Python is pointing to this line in your get_coin_data function: 'name': data ['name'] The error message "Perhaps you forgot a comma?" is spot on. When you define a dictionary in Python, each key-value pair needs to be separated by a comma. Here's the corrected get_coin_data function: def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } else: print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None I've added commas after each key-value pair within the dictionary. Give this a try, and that syntax error should disappear! Let me know if you run into any other issues. 😊