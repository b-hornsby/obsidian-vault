---
category: crypto-web3
date: 2025-04-29
id: 489013
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan was building a Python script to compare Murad's top 10 meme coins against
  Solana's 24h price performance using CoinGecko API and tabulate for display.
tags:
- crypto-comparison
- coingecko-api
- tabulate
- solana-benchmark
- meme-coins
---
# import requests
from tabulate import tabulate

def get_coin_data(coin_id):
    url = "https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data ['name']
            'symbol': data['symbol']
            'price': data['market_data']['current_price']['usd']
            'market_cap': data['market_data']['market_cap']['usd']
            'change_24h': data['market_data']['price_change_percentage_24h']
    }
else: 
    print(f"failed to fetch data for {coin_id}. status code: {response.status_code}"
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
    print(f"Failed to fetch data. Status code: {response.status_code}")\

### USER
import requests
from tabulate import tabulate

def get_coin_data(coin_id):
    url = "https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data ['name']
            'symbol': data['symbol']
            'price': data['market_data']['current_price']['usd']
            'market_cap': data['market_data']['market_cap']['usd']
            'change_24h': data['market_data']['price_change_percentage_24h']
    }
else: 
    print(f"failed to fetch data for {coin_id}. status code: {response.status_code}"
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
    print(f"Failed to fetch data. Status code: {response.status_code}")\

### GEMINI
File "/tmp/sandbox0/workspace/main.py", line 15 'name': data ['name'] ^ SyntaxError: invalid syntax
