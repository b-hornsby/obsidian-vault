---
category: coding
date: 2025-04-29
id: 550331
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: User encountered a Python syntax error in their market tracker script and
  was trying to run it from the command line.
tags:
- python
- syntax-error
- debugging
- script-execution
- market-tracker
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 16
    else: 
    ^^^^
SyntaxError: invalid syntax
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 16
    else: 
    ^^^^
SyntaxError: invalid syntax
PS C:\Users\Bryan>

### GEMINI
You're right, another SyntaxError! This time, it's pointing to the else: statement right after your return None in the get_coin_data function. else: print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None The issue here is that the return None statement already exits the if block. You don't need an else after a return in this context. The code will naturally proceed after the if block if the condition (response.status_code == 200) is false. Here's the corrected part of the get_coin_data function: def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None I've removed the else: block. The print statement and return None will now execute if the if condition is false. Give this a shot! We're getting closer! 😊