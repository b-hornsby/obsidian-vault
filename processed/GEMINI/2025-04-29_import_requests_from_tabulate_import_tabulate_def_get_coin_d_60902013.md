---
category: crypto-web3
date: 2025-04-29
id: 314105
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan shared an updated version of his crypto comparison script with syntax
  errors to get help debugging.
tags:
- crypto-comparison
- coingecko-api
- tabulate
- solana-benchmark
- code-debugging
---
# import requests
from tabulate import tabulate

def get_coin_data(coin_id):
    url = "https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data ['name'],
            'symbol': data['symbol'],
            'price': data['market_data']['current_price']['usd'],
            'market_cap': data['market_data']['market_cap']['usd'],
            'change_24h': data['market_data']['price_change_percentage_24h']
    }
 
    print(f"failed to fetch data for {coin_id}. status code: {response.status_code}")
    return None

    coins = {
    "solana": "solana",
    "spx6900": "spx6900",
    "gigachad": "gigachad-2",
    "mog": "mog-coin",
    "apu": "apu-apustaja",
    "popcat": "popcat",
    "harrypotter": "harrypotterobamasonic10inu-eth",
    "retardio": "retardio",
    "lockin": "lock-in",
    "mini": "mini",
    "usa": "american-coin"
    }

    if sol_data:
        sol_change = sol_data['change_24h']

    results = []
    for key, coin_id in coins.items():
        if coin_id == "solana":
            continue

    coin_data = get_coin_data(coin_id)
    if coin_data:
        outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌"
        results.append([
            coin_data["name"],
            coin_data["symbol"],
            f"${coin_data['market_cap']:,.0f}",
            f"{coin_data['change_24h']:.2f}%",
            outperforming
        ])

headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"]
print(tabulate(results, headers=headers, tablefmt="fancy_grid"))


print(f"{name.upper()} ({symbol.upper()})")
print(f"Price: ${price:,.2f}")
print(f"Market Cap: ${market_cap:,.0f}")
    
if change_24h is not None:
    indicator = "🟢" if change_24h >= 0 else "🔴"
    print(f"24h Change: {change_24h:.2f}% {indicator}")
else:
    print("24h change: data not available ⚠️")




else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

### USER
import requests
from tabulate import tabulate

def get_coin_data(coin_id):
    url = "https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data ['name'],
            'symbol': data['symbol'],
            'price': data['market_data']['current_price']['usd'],
            'market_cap': data['market_data']['market_cap']['usd'],
            'change_24h': data['market_data']['price_change_percentage_24h']
    }
 
    print(f"failed to fetch data for {coin_id}. status code: {response.status_code}")
    return None

    coins = {
    "solana": "solana",
    "spx6900": "spx6900",
    "gigachad": "gigachad-2",
    "mog": "mog-coin",
    "apu": "apu-apustaja",
    "popcat": "popcat",
    "harrypotter": "harrypotterobamasonic10inu-eth",
    "retardio": "retardio",
    "lockin": "lock-in",
    "mini": "mini",
    "usa": "american-coin"
    }

    if sol_data:
        sol_change = sol_data['change_24h']

    results = []
    for key, coin_id in coins.items():
        if coin_id == "solana":
            continue

    coin_data = get_coin_data(coin_id)
    if coin_data:
        outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌"
        results.append([
            coin_data["name"],
            coin_data["symbol"],
            f"${coin_data['market_cap']:,.0f}",
            f"{coin_data['change_24h']:.2f}%",
            outperforming
        ])

headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"]
print(tabulate(results, headers=headers, tablefmt="fancy_grid"))


print(f"{name.upper()} ({symbol.upper()})")
print(f"Price: ${price:,.2f}")
print(f"Market Cap: ${market_cap:,.0f}")
    
if change_24h is not None:
    indicator = "🟢" if change_24h >= 0 else "🔴"
    print(f"24h Change: {change_24h:.2f}% {indicator}")
else:
    print("24h change: data not available ⚠️")




else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

### GEMINI
Thanks! I see a few things that might be causing you trouble. Let's break it down: Indentation in get_coin_data: The print statement for the failed fetch and the return None are indented inside the if response.status_code == 200: block. This means they will only execute if the request was successful, which isn't the desired behavior for error handling. They should be outside this if block. coins Dictionary Placement: The coins dictionary is defined inside the get_coin_data function. This means it's only accessible within that function and won't be used in the main part of your script. It should be moved outside the function definition, at the top level of your script. sol_data Not Defined: You're trying to access sol_data['change_24h'] before sol_data has been defined. You need to call get_coin_data("solana") to fetch the Solana data and assign it to sol_data before you can access its elements. name, symbol, price, market_cap, change_24h Not Defined in the Final Print Statements: The variables name, symbol, price, market_cap, and change_24h are only defined within the get_coin_data function. They are not accessible in the final print statements outside the loop. It seems like you might have intended to print the data for Solana specifically here, but those variables weren't assigned values in the main part of the script. Here's the corrected code with these issues addressed: import requests from tabulate import tabulate def get_coin_data(coin_id): url = f"https://api.coingecko.com/api/v3/coins/{coin_id}" response = requests.get(url) if response.status_code == 200: data = response.json() return { 'name': data['name'], 'symbol': data['symbol'], 'price': data['market_data']['current_price']['usd'], 'market_cap': data['market_data']['market_cap']['usd'], 'change_24h': data['market_data']['price_change_percentage_24h'] } print(f"failed to fetch data for {coin_id}. status code: {response.status_code}") return None coins = { "solana": "solana", "spx6900": "spx6900", "gigachad": "gigachad-2", "mog": "mog-coin", "apu": "apu-apustaja", "popcat": "popcat", "harrypotter": "harrypotterobamasonic10inu-eth", "retardio": "retardio", "lockin": "lock-in", "mini": "mini", "usa": "american-coin" } sol_data = get_coin_data("solana") if sol_data: sol_change = sol_data['change_24h'] results = [] for key, coin_id in coins.items(): if coin_id == "solana": continue coin_data = get_coin_data(coin_id) if coin_data: outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌" results.append([ coin_data["name"], coin_data["symbol"], f"${coin_data['market_cap']:,.0f}", f"{coin_data['change_24h']:.2f}%", outperforming ]) headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})") print(f"Price: ${sol_data['price']:,.2f}") print(f"Market Cap: ${sol_data['market_cap']:,.0f}") if sol_data['change_24h'] is not None: indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴" print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}") else: print("24h change: data not available ⚠️") else: print("Failed to fetch Solana data, so comparison cannot be made.") Let me know if you're still seeing any issues or have other questions! 😊

### GEMINI
File "/tmp/sandbox0/workspace/main.py", line 10 'name': data ['name'], ^ SyntaxError: invalid syntax
