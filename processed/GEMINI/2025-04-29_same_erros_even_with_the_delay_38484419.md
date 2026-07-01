---
category: crypto-web3
date: 2025-04-29
id: 109711
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was still getting the same errors from CoinGecko API even after adding
  delays between requests.
tags:
- coingecko-api
- rate-limiting
- 429-error
- api-throttling
---
# same erros even with the delay

### USER
same erros even with the delay

### GEMINI
That's unexpected! The 429 errors persisting even with the delay suggest that either the delay isn't long enough, or there might be a more aggressive rate limit in place at the moment. Let's try increasing the delay. Could you try changing the time.sleep() value to something a bit higher? Let's try 0.5 seconds and see if that makes a difference. import requests from tabulate import tabulate import time def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None coins = { "solana": "solana", "spx6900": "spx6900", "gigachad": "gigachad-2", "mog": "mog-coin", "apu": "apu-apustaja", # Check this ID! "popcat": "popcat", "harrypotter": "harrypotterobamasonic10inu-eth", "retardio": "retardio", "lockin": "lock-in", "mini": "mini", "usa": "american-coin" } sol_data = get_coin_data("solana") if sol_data: sol_change = sol_data['change_24h'] results = [] for key, coin_id in coins.items(): if coin_id == "solana": continue time.sleep(0.5) # Increased delay to 0.5 seconds coin_data = get_coin_data(coin_id) if coin_data: outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌" results.append([ coin_data["name"], coin_data["symbol"], f"${coin_data['market_cap']:,.0f}", f"{coin_data['change_24h']:.2f}%", outperforming ]) headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})") print(f"Price: ${sol_data['price']:,.2f}") print(f"Market Cap: ${sol_data['market_cap']:,.0f}") if sol_data['change_24h'] is not None: indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴" print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}") else: print("24h change: data not available ⚠️") else: print("Failed to fetch Solana data, so comparison cannot be made.") What else could be happening: Very Strict Rate Limiting: CoinGecko might have a very strict rate limit in place at this specific time due to high traffic. Multiple Requests Too Close Initially: Even with a delay in the loop, if your script executes very quickly initially (e.g., fetching Solana data and then immediately starting the loop), you might still trigger the rate limit. If increasing the delay to 0.5 seconds still results in 429 errors, we might need to consider even longer delays or look into more sophisticated rate limiting strategies (though for this simple script, a longer delay is the easiest approach). Also, did you have a chance to check the CoinGecko ID for "apu-apustaja"? The 404 error is a separate issue from the rate limiting. Let me know if increasing the delay helps!
