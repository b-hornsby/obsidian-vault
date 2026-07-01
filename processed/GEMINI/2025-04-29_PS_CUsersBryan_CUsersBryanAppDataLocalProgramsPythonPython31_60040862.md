---
category: coding
date: 2025-04-29
id: 695819
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- murad_market_tracker
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user was running a Python market tracker script that fetches Solana data
  but encountered a 429 rate limit error, causing the script to fail to retrieve data
  and complete its comparison task.
tags:
- API rate limiting
- Python scripting
- cryptocurrency data fetching
- error handling
- market tracker
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
failed to fetch data for solana. status code: 429
Failed to fetch Solana data, so comparison cannot be made.
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
failed to fetch data for solana. status code: 429
Failed to fetch Solana data, so comparison cannot be made.
PS C:\Users\Bryan>

### GEMINI
That's incredibly frustrating that even with a 5-second initial delay, we're still hitting the rate limit on the very first request for Solana. This strongly suggests that CoinGecko's rate limiting is either extremely strict at the moment, or there might be some other factor at play. Given this, here are the next steps we should consider: Increase the initial delay even further: Let's try a more substantial initial delay. Change the time.sleep() at the beginning to 10 seconds. import requests from tabulate import tabulate import time # Add a significant delay before the first API call time.sleep(10) # ... rest of your code ... Reduce the number of initial requests: For now, let's comment out the loop that fetches data for the other coins. This will help us isolate whether the issue is with the very first request or with the subsequent requests even with the delay. import requests from tabulate import tabulate import time # Add a significant delay before the first API call time.sleep(10) def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None coins = { "solana": "solana", "spx6900": "spx6900", "gigachad": "gigachad-2", "mog": "mog-coin", "apu": "apu-apustaja", # Check this ID! "popcat": "popcat", "harrypotter": "harrypotterobamasonic10inu-eth", "retardio": "retardio", "lockin": "lock-in", "mini": "mini", "usa": "american-coin" } sol_data = get_coin_data("solana") if sol_data: sol_change = sol_data['change_24h'] results = [] # Comment out the loop for now # for key, coin_id in coins.items(): # if coin_id == "solana": # continue # # time.sleep(2) # Increased delay within the loop to 2 seconds # coin_data = get_coin_data(coin_id) # if coin_data: # outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌" # results.append([ # coin_data["name"], # coin_data["symbol"], # f"${coin_data['market_cap']:,.0f}", # f"{coin_data['change_24h']:.2f}%", # outperforming # ]) # # headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] # print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})") print(f"Price: ${sol_data['price']:,.2f}") print(f"Market Cap: ${sol_data['market_cap']:,.0f}") if sol_data['change_24h'] is not None: indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴" print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}") else: print("24h change: data not available ⚠️") else: print("Failed to fetch Solana data, so comparison cannot be made.") What we're trying to achieve with these changes: More aggressive initial delay: To ensure we're not immediately hitting a very short-term rate limit. Isolating the first request: By commenting out the loop, we'll see if we can at least successfully fetch the Solana data. After making these changes, please run the script and let me know if you still get the 429 error for Solana. If even with a 10-second delay and only requesting Solana data, you're still getting a 429, it might indicate a temporary issue on CoinGecko's end, or a very strict rate limit is in place for your IP address at this moment due to previous requests. In such a scenario, you might need to wait a bit longer before trying again, or consider if there are any other applications on your network making frequent requests to CoinGecko.