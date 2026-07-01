---
category: coding
date: 2025-04-29
id: 212070
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- operation-immortal-agent
resolution: unresolved
sentiment: frustrated
source: GEMINI
summary: The user is debugging a Python market tracker script that is encountering
  HTTP errors (404 and 429) when trying to fetch data for various tokens/coins.
tags:
- python
- api-errors
- http-status-codes
- market-tracker
- rate-limiting
- 404-error
---
# i got a few errors. this is what it gave me: PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
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
│ SPX6900  │ spx      │ $502,745,040 │ -6.78%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Gigachad │ giga     │ $190,952,104 │ -9.44%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Mog Coin │ mog      │ $230,853,681 │ -6.66%       │ ❌                   │
╘══════════╧══════════╧══════════════╧══════════════╧═════════════════════╛
SOLANA (SOL)
Price: $145.43
Market Cap: $75,270,704,606
24h Change: -1.65% 🔴
PS C:\Users\Bryan> 

### USER
i got a few errors. this is what it gave me: PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
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
│ SPX6900  │ spx      │ $502,745,040 │ -6.78%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Gigachad │ giga     │ $190,952,104 │ -9.44%       │ ❌                   │
├──────────┼──────────┼──────────────┼──────────────┼─────────────────────┤
│ Mog Coin │ mog      │ $230,853,681 │ -6.66%       │ ❌                   │
╘══════════╧══════════╧══════════════╧══════════════╧═════════════════════╛
SOLANA (SOL)
Price: $145.43
Market Cap: $75,270,704,606
24h Change: -1.65% 🔴
PS C:\Users\Bryan> 

### GEMINI
Okay, I see what's happening. You're getting a mix of status codes: 404 Not Found: This for "apu-apustaja" means that the CoinGecko API couldn't find a coin with that specific ID. It's possible the ID is incorrect or the coin is no longer listed under that ID. 429 Too Many Requests: This is happening for "popcat", "harrypotterobamasonic10inu-eth", "retardio", "lock-in", "mini", and "american-coin". This error indicates that your script is making too many requests to the CoinGecko API in a short period. Most public APIs have rate limits to prevent abuse and ensure fair usage. Here's how we can address these issues: Investigate the 404 Error: Double-check the CoinGecko ID for "apu-apustaja". It's possible there's a typo or the ID has changed. You might want to search on the CoinGecko website to confirm the correct ID. If the coin is no longer listed under that ID, you might need to remove it from your coins dictionary. Handle the 429 Too Many Requests Error (Rate Limiting): Implement a Delay: The most common way to handle rate limiting is to introduce a small delay between your API requests. This gives the CoinGecko server time to process each request and prevents you from hitting the limit too quickly. You can use the time.sleep() function in Python for this. Here's the updated code incorporating a delay to address the rate limiting. I've also added a placeholder comment for you to investigate the "apu-apustaja" ID: import requests from tabulate import tabulate import time def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None coins = { "solana": "solana", "spx6900": "spx6900", "gigachad": "gigachad-2", "mog": "mog-coin", "apu": "apu-apustaja", # Check this ID! "popcat": "popcat", "harrypotter": "harrypotterobamasonic10inu-eth", "retardio": "retardio", "lockin": "lock-in", "mini": "mini", "usa": "american-coin" } sol_data = get_coin_data("solana") if sol_data: sol_change = sol_data['change_24h'] results = [] for key, coin_id in coins.items(): if coin_id == "solana": continue time.sleep(0.15) # Add a delay of 0.15 seconds between requests coin_data = get_coin_data(coin_id) if coin_data: outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌" results.append([ coin_data["name"], coin_data["symbol"], f"${coin_data['market_cap']:,.0f}", f"{coin_data['change_24h']:.2f}%", outperforming ]) headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})") print(f"Price: ${sol_data['price']:,.2f}") print(f"Market Cap: ${sol_data['market_cap']:,.0f}") if sol_data['change_24h'] is not None: indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴" print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}") else: print("24h change: data not available ⚠️") else: print("Failed to fetch Solana data, so comparison cannot be made.") Explanation of the Change: import time: We import the time module. time.sleep(0.15): Inside the loop that fetches data for each coin, we've added a time.sleep(0.15). This pauses the script for 0.15 seconds after each API request. You might need to adjust this value. A good starting point is between 0.1 and 0.3 seconds, but you might need to experiment based on CoinGecko's specific rate limits. Next Steps for You: Run the updated code. The 429 errors should hopefully disappear or at least become much less frequent. Investigate the "apu-apustaja" ID. Check if it's correct on CoinGecko's website. If not, update it in your coins dictionary or remove it if the coin is no longer relevant to you. Let me know how it goes after you make these changes! 😊