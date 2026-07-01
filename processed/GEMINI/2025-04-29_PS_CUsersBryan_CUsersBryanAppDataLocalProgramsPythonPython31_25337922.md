---
category: crypto-web3
date: 2025-04-29
id: 28988
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- murad_market_tracker
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: The user is running a Python script to track meme coin market data but encountering
  HTTP errors including 404 and 429 status codes when fetching data for various tokens.
tags:
- market-tracker
- api-errors
- rate-limiting
- data-fetching
- python-script
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
failed to fetch data for apu-apustaja. status code: 404
failed to fetch data for popcat. status code: 429
failed to fetch data for harrypotterobamasonic10inu-eth. status code: 429
failed to fetch data for retardio. status code: 429
failed to fetch data for lock-in. status code: 429
failed to fetch data for mini. status code: 429
failed to fetch data for american-coin. status code: 429
╒══════════╤══════════╤══════════════╤══════════════╤═════════════════════╕
│ Name     │ Symbol   │ Market Cap   │ 24h Change   │ Outperforming SOL   │
╞══════════╪══════════╪══════════════╪══════════════╪═════════════════════╡
│ SPX6900  │ spx      │ $503,566,164 │ -6.20%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Gigachad │ giga     │ $190,479,672 │ -9.96%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Mog Coin │ mog      │ $230,897,770 │ -6.45%       │ ❌                   │
╘══════════╧══════════╧══════════════╧══════════════╧═════════════════════╛
SOLANA (SOL)
Price: $145.42
Market Cap: $75,267,628,239
24h Change: -1.64% 🔴
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
failed to fetch data for apu-apustaja. status code: 404
failed to fetch data for popcat. status code: 429
failed to fetch data for harrypotterobamasonic10inu-eth. status code: 429
failed to fetch data for retardio. status code: 429
failed to fetch data for lock-in. status code: 429
failed to fetch data for mini. status code: 429
failed to fetch data for american-coin. status code: 429
╒══════════╤══════════╤══════════════╤══════════════╤═════════════════════╕
│ Name     │ Symbol   │ Market Cap   │ 24h Change   │ Outperforming SOL   │
╞══════════╪══════════╪══════════════╪══════════════╪═════════════════════╡
│ SPX6900  │ spx      │ $503,566,164 │ -6.20%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Gigachad │ giga     │ $190,479,672 │ -9.96%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Mog Coin │ mog      │ $230,897,770 │ -6.45%       │ ❌                   │
╘══════════╧══════════╧══════════════╧══════════════╧═════════════════════╛
SOLANA (SOL)
Price: $145.42
Market Cap: $75,267,628,239
24h Change: -1.64% 🔴
PS C:\Users\Bryan>

### GEMINI
Okay, that's progress! We're now successfully fetching the data for Solana, which means the initial delay helped with the immediate rate limiting issue. However, we're still seeing the 429 Too Many Requests errors for most of the other coins. This tells us that even with a 1-second delay between those requests, we're still hitting the rate limit. Here's what we need to do now: Increase the delay within the loop significantly: Let's try increasing the delay between each coin data fetch to 2 seconds. Here's the updated code with the increased delay in the loop: import requests from tabulate import tabulate import time # Add a delay before the first API call time.sleep(5) def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None coins = { "solana": "solana", "spx6900": "spx6900", "gigachad": "gigachad-2", "mog": "mog-coin", "apu": "apu-apustaja", # Check this ID! "popcat": "popcat", "harrypotter": "harrypotterobamasonic10inu-eth", "retardio": "retardio", "lockin": "lock-in", "mini": "mini", "usa": "american-coin" } sol_data = get_coin_data("solana") if sol_data: sol_change = sol_data['change_24h'] results = [] for key, coin_id in coins.items(): if coin_id == "solana": continue time.sleep(2) # Increased delay within the loop to 2 seconds coin_data = get_coin_data(coin_id) if coin_data: outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌" results.append([ coin_data["name"], coin_data["symbol"], f"${coin_data['market_cap']:,.0f}", f"{coin_data['change_24h']:.2f}%", outperforming ]) headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})") print(f"Price: ${sol_data['price']:,.2f}") print(f"Market Cap: ${sol_data['market_cap']:,.0f}") if sol_data['change_24h'] is not None: indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴" print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}") else: print("24h change: data not available ⚠️") else: print("Failed to fetch Solana data, so comparison cannot be made.") What to Expect Now: The script will now pause for 5 seconds initially, and then for 2 seconds before fetching the data for each of the other coins. This significantly reduces the rate at which we're making requests to the API. If you still encounter 429 errors after this change, the CoinGecko API might have a very strict rate limit in place at the moment, or there might be other factors at play. In that case, you might need to consider: Increasing the delay further (e.g., 3 or 4 seconds). Reducing the number of coins you are tracking. Checking CoinGecko's API documentation for any specific rate limit information. Please run this updated code and let me know if the 429 errors persist for the other coins. We're getting closer! Also, don't forget to look into the "apu-apustaja" 404 error when you have a moment.