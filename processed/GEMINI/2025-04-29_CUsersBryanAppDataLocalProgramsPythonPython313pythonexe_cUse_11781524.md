---
category: coding
date: 2025-04-29
id: 685969
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: The user is trying to run a Python script to track Solana market data but
  is encountering a 429 rate limit error from the API, preventing data retrieval.
tags:
- python
- api-rate-limiting
- solana
- market-tracker
- error-handling
---
#                  > & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
failed to fetch data for solana. status code: 429
Failed to fetch Solana data, so comparison cannot be made.
PS C:\Users\Bryan>

### USER
                 > & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
failed to fetch data for solana. status code: 429
Failed to fetch Solana data, so comparison cannot be made.
PS C:\Users\Bryan>

### GEMINI
Okay, that's a crucial piece of information. The script is now failing to fetch even the data for Solana with a 429 error right at the beginning. This strongly indicates that the rate limiting is being hit very quickly, possibly even on the first request. Since even the initial request for Solana is failing, the delay we added within the loop isn't being reached before the rate limit is triggered. Here's what we need to do: Implement a delay before the first API call: We need to put a time.sleep() right after the imports and before we even try to fetch the Solana data. Increase the initial delay significantly: Let's start with a delay of 5 seconds before the first API call to give the rate limiting mechanism a chance to reset. Here's the modified code: import requests from tabulate import tabulate import time # Add a delay before the first API call time.sleep(5) def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None coins = { "solana": "solana", "spx6900": "spx6900", "gigachad": "gigachad-2", "mog": "mog-coin", "apu": "apu-apustaja", # Check this ID! "popcat": "popcat", "harrypotter": "harrypotterobamasonic10inu-eth", "retardio": "retardio", "lockin": "lock-in", "mini": "mini", "usa": "american-coin" } sol_data = get_coin_data("solana") if sol_data: sol_change = sol_data['change_24h'] results = [] for key, coin_id in coins.items(): if coin_id == "solana": continue time.sleep(1) # Keep the 1-second delay within the loop coin_data = get_coin_data(coin_id) if coin_data: outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌" results.append([ coin_data["name"], coin_data["symbol"], f"${coin_data['market_cap']:,.0f}", f"{coin_data['change_24h']:.2f}%", outperforming ]) headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})") print(f"Price: ${sol_data['price']:,.2f}") print(f"Market Cap: ${sol_data['market_cap']:,.0f}") if sol_data['change_24h'] is not None: indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴" print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}") else: print("24h change: data not available ⚠️") else: print("Failed to fetch Solana data, so comparison cannot be made.") Key Change: time.sleep(5) has been added right at the beginning of the script. What to Expect: The script will now pause for 5 seconds before attempting to fetch any data. This should hopefully give the CoinGecko API enough time since your last request (if you were running it frequently) to allow the first request for Solana to succeed. After this initial delay, the 1-second delay within the loop for the other coins will still be in effect. Please run this updated code and let me know if you're still encountering the 429 error for Solana. If it works for Solana but you still get 429 errors later, we might need to increase the initial delay even further or consider reducing the number of coins you're tracking.