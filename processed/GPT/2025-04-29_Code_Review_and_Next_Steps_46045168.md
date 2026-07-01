---
source: GPT
date: 2025-04-29
category: crypto-web3
id: 46045168
linked_nodes: ['nodes/people/bryan.md']
---
# Code Review and Next Steps

### USER
{'asset_pointer': 'file-service://file-PBJtKg4YF8va7mtcT3ZruD', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1100, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 463549, 'width': 924}

### ASSISTANT
Excellent idea — including **market cap** alongside **24h performance** will give a clearer picture, especially since many of these behave like low-float microcaps. So here’s what we’ll do in the next version of your script:

### ✅ Plan for Code Upgrade
1. **Fetch Solana’s 24h change + market cap** (already done ✅)
2. **Loop through the 10 meme coins**:
   - Get market cap
   - Get 24h % change
   - Compare to Solana’s % change
   - Store results
3. **Display everything in a table** using `tabulate` for clarity

**Quick notes:**  
- Some names might not match *CoinGecko's IDs* exactly. We'll probably need to slightly adjust or map them when we actually pull API data (e.g., "PEPE" is likely `pepe` on CoinGecko).
- There's also a "BITCOIN" listed, but that's the real Bitcoin (BTC), right? Or is this some meme version of "BITCOIN" in Murad's meme coin list?

> Should we pull *live prices, market caps, and 24h % changes* for each of these from CoinGecko and then compare them vs Solana?  
>   
> ✅ Yes = I'll show you how we can *batch fetch* them to save API calls and speed things up.  
> ❓ No = We can pick a few manually if you want it lighter first.

What are you thinking?

### ASSISTANT
Thanks! Based on the updated image, here’s Murad’s **Top 10 Meme Coins** with more precise tickers and chains — which we’ll need for accurate CoinGecko lookups:

| Name                    | Ticker     | Chain     |
|
---
-
---
-
---
-
---
-
---
-
---
--|
---
-
---
-
---
-|
---
-
---
-
---
|
| SPX6900                 | SPX        | Ethereum  |
| GigaChad                | GIGA       | Solana    |
| Mog Coin                | MOG        | Ethereum  |
| Apu Apustaja            | APU        | Ethereum  |
| Popcat                  | POPCAT     | Solana    |
| HarryPotterObamaSonic10Inu | BITCOIN  | Ethereum  |
| Retardio                | RETARDIO   | Solana    |
| Lock In                 | LOCKIN     | Solana    |
| Mini                    | MINI       | Solana    |
| American Coin           | USA        | Solana    |

## 🧩 Your Current Code Recap (simplified)

You already have:
```python
import requests

url = "https://api.coingecko.com/api/v3/coins/solana"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    name = data ['name']
    symbol = data['symbol']
    price = data['market_data']['current_price']['usd']
    market_cap = data['market_data']['market_cap']['usd']
    change_24h = data['market_data']['price_change_percentage_24h']
    # Print stuff...
```

### 2. Under that, replace your hardcoded `url = ...` and `response = ...` block with this new **helper function** (reuseable and cleaner):

```python
def get_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        symbol = data["symbol"].upper()
        market_cap = data["market_data"]["market_cap"]["usd"]
        change_24h = data["market_data"]["price_change_percentage_24h"]
        return {
            "name": name,
            "symbol": symbol,
            "market_cap": market_cap,
            "change_24h": change_24h
        }
    else:
        print(f"Error fetching {coin_id}: {response.status_code}")
        return None
```

This replaces your Solana-only block and makes the same logic available for **any coin** by ID.

### 4. Now fetch Solana data as the baseline:

```python
sol_data = get_coin_data(coins["solana"])
sol_change = sol_data["change_24h"]
```

### 6. Finally, display it all in a table:

```python
headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"]
print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
```

Would you like me to walk you through testing a section of this live to verify your data is printing correctly before continuing?

### ASSISTANT
That’s *exactly* the right mindset — you don’t need to memorize everything, but you **should understand the moving parts well enough to know what to Google and why**. I’ll guide you line by line with real reasoning behind each step, so you’re learning *how to build this kind of tool* — not just copying syntax.

## 🧱 Step-by-Step (and why)

### 1. **Import your tools**
```python
import requests
from tabulate import tabulate
```
- `requests`: makes web calls to CoinGecko’s API.
- `tabulate`: helps print a clean, aligned table in the terminal. (You can `pip install tabulate` if needed.)

### 3. **Create a helper function to fetch coin data**
We’ll write one reusable function to fetch:
- Name
- Symbol
- Market Cap (USD)
- 24h Change %

```python
def get_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        symbol = data["symbol"].upper()
        market_cap = data["market_data"]["market_cap"]["usd"]
        change_24h = data["market_data"]["price_change_percentage_24h"]
        return {
            "name": name,
            "symbol": symbol,
            "market_cap": market_cap,
            "change_24h": change_24h
        }
    else:
        print(f"Error fetching {coin_id}: {response.status_code}")
        return None
```

**What this does:**
- Fetches JSON data from the CoinGecko API.
- Pulls out only the info we care about.
- Returns it in a Python `dict`.

### 5. **Loop through memecoins and build a results list**
```python
results = []
for key, coin_id in coins.items():
    if coin_id == "solana":
        continue  # already handled

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
```

**Why this works:**
- Loops through all coins except Solana.
- Grabs their data.
- Compares each coin’s 24h change to Solana.
- Adds a row to a `results` list to be displayed in a table.

## 🧩 Final Result

After we build this together, you’ll be able to:
- Expand to **weekly/monthly % change**
- Add **alerts** (email, sound, or Telegram)
- Sort by performance or market cap

### ✅ CoinGecko API IDs for Murad’s Top 10 Meme Coins

| Coin Name                      | Ticker   | CoinGecko ID                          |
|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-|
---
-
---
---|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
|
| SPX6900                        | SPX      | `spx6900`                             |
| Gigachad                       | GIGA     | `gigachad-2`                          |
| Mog Coin                       | MOG      | `mog-coin`                            |
| Apu Apustaja                   | APU      | `apu-apustaja`                        |
| Popcat                         | POPCAT   | `popcat`                              |
| HarryPotterObamaSonic10Inu     | BITCOIN  | `harrypotterobamasonic10inu-eth`      |
| Retardio                       | RETARDIO | `retardio`                            |
| Lock In                        | LOCKIN   | `lock-in`                             |
| Mini                           | MINI     | `mini`                                |
| American Coin                  | USA      | `american-coin`                       |

**So to move forward**, the idea is:  
- Grab **Solana**'s price change % (we already do)  
- Grab each of these **memecoins' price change %** (using CoinGecko API)  
- **Compare** their 24h % change to Solana's  
- **Alert** if any coin is *outperforming* SOL
---

**Quick thing:**  
Some of these names (like `BITCOIN` and `PEPE`) might pull weird results if we don’t use their *correct IDs* from CoinGecko.  
Example:  
- Bitcoin is the main Bitcoin (btc) — not a meme.  
- PEPE is an ETH coin, might have multiple listings.  
- SPX6900, FARTCOIN, FWOG, etc. might need *specific IDs*.  

👉 Would you like me to quickly help **lookup their correct CoinGecko IDs** first, just to be sure the comparisons are accurate?  
(Should only take a sec.)  
If yes, we can **make a clean ID list** to pull their real data! 🚀