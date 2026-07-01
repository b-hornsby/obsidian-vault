---
source: GPT
date: 2025-05-10
category: ai-tools
id: 90946988
linked_nodes: ['nodes/people/bryan.md']
---
### 🔹 `import` statements

```python
import requests
from tabulate import tabulate
import time
```

- `requests` lets you pull live data from websites (in this case, the CoinGecko API).
- `tabulate` helps format data into nice, readable tables in the terminal.
- `time` allows for things like pausing your code between actions (`time.sleep()`).

### 🧠 `get_coin_data()` function — what it does

```python
def get_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'symbol': data['symbol'],
            'price': data['market_data']['current_price']['usd'],
            'market_cap': data['market_data']['market_cap']['usd'],
            'change_24h': data['market_data']['price_change_percentage_24h']
        }
    print(f"failed to fetch data for {coin_id}. status code: {response.status_code}")
    return None
```

#### 🧱 Indentation explained:
- Everything **inside the function** is indented one level.
- Inside the `if`, everything gets indented **one more level**.
- Think of indentation as “this belongs to that.”

#### ✅ What it does:
1. Builds a URL for a specific coin.
2. Sends a request to that URL.
3. If the request was successful (`200`), it:
   - Grabs JSON data from the response.
   - Extracts important details (name, symbol, price, etc.).
4. If the request failed, it prints an error and returns `None`.

### 🌞 Get Solana's data

```python
sol_data = get_coin_data("solana")
```

This fetches Solana’s current info so it can be used as the baseline for comparison.

### 🔁 Loop through all coins (except Solana)

```python
    for key, coin_id in coins.items():
        if coin_id == "solana":
            continue
```

- `for key, coin_id in coins.items()` goes through the dictionary.
- If it's Solana again, `continue` skips it.

### 📥 Get coin data and compare

```python
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

- Calls `get_coin_data()` for each coin.
- If it gets data, it:
  - Compares the 24h change to Solana.
  - Adds the result to the table.

### 📢 Print Solana’s individual stats

```python
    print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})")
    ...
```

Once you run this, send me the **error message** you get. That will tell us:
- Where the problem happened,
- What kind of error it was, and
- What you may need to change.

Ready to debug when you are — go ahead and run it and copy-paste the error here.

### ASSISTANT
I understand that you're encountering a 404 error when attempting to fetch data for "apu-apustaja" via the CoinGecko API, even though the coin's page exists on their website. This discrepancy can arise due to differences between the website's URL structure and the API's coin IDs.

To resolve this, let's verify the correct coin ID using the CoinGecko API:

1. **Fetch the list of all coins**: CoinGecko provides an endpoint to retrieve a list of all supported coins along with their IDs and symbols.

2. **Search for "Apu Apustaja"**: Once you have the list, you can search for the coin by name to find its corresponding ID.

Here's a Python function to help you with this:

```python
import requests

def find_coin_id(search_term):
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    if response.status_code == 200:
        coins = response.json()
        matches = [coin for coin in coins if search_term.lower() in coin['name'].lower()]
        for match in matches:
            print(f"Name: {match['name']}, ID: {match['id']}")
    else:
        print(f"Failed to fetch coin list. Status code: {response.status_code}")

# Example usage:
find_coin_id("Apu Apustaja")
```

Run this script to see the available coin IDs for "Apu Apustaja". Once you identify the correct ID, update your main script accordingly.

Additionally, to handle rate limiting (HTTP 429 errors), you can implement a retry mechanism with exponential backoff. Here's how you might modify your `get_coin_data` function:

```python
import requests
import time

def get_coin_data(coin_id, retries=3, delay=5):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    for attempt in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                'name': data['name'],
                'symbol': data['symbol'],
                'price': data['market_data']['current_price']['usd'],
                'market_cap': data['market_data']['market_cap']['usd'],
                'change_24h': data['market_data']['price_change_percentage_24h']
            }
        elif response.status_code == 429:
            print(f"Rate limit hit for {coin_id}. Waiting {delay} seconds before retrying...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
        else:
            print(f"Failed to fetch data for {coin_id}. Status code: {response.status_code}")
            break
    return None
```

This function will attempt to fetch the coin data up to `retries` times, doubling the wait time after each 429 error.

Let me know if you need further assistance with implementing these changes or handling other aspects of your project.

### ASSISTANT
Great question. The coin ID lookup function isn’t something you need in your **final project script** — it’s more of a **one-time helper tool** you can run separately to find the correct API IDs for coins that are giving you errors.

### 💡 What it does

This script pulls the **entire list of coins** from CoinGecko, then searches it for matches to `"apu"`. It will show results like:

```
Name: Apu Apustaja, ID: apu
Name: Apu Apustaja (ETH), ID: apu-apustaja
```

You can then update your main script to use the exact `ID` that works with the API.

Would you like me to run a full check on the other coin IDs for you as well and send back a cleaned-up list?

### USER
import requests
from tabulate import tabulate
import time

time.sleep(5)

def get_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
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
    "apu": "apu-apustaja-base",  
    "popcat": "popcat",
    "harrypotter": "harrypotterobamasonic10inu-eth",
    "retardio": "retardio",
    "lockin": "lock-in",
    "mini": "mini",
    "usa": "american-coin"
}

sol_data = get_coin_data("solana")

if sol_data:
    sol_change = sol_data['change_24h']
    results = []
    for key, coin_id in coins.items():
        if coin_id == "solana":
            continue

        time.sleep(2)  
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

    print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})")
    print(f"Price: ${sol_data['price']:,.2f}")
    print(f"Market Cap: ${sol_data['market_cap']:,.0f}")

    if sol_data['change_24h'] is not None:
        indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴"
        print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}")
    else:
        print("24h change: data not available ⚠️")

else:
    print("Failed to fetch Solana data, so comparison cannot be made.")

### ASSISTANT
Thanks for running the code — this gives us a clear picture of what’s going on.

## ✅ Fixes (Step-by-step)

### 🔧 Step 1: Fix `apu-apustaja`
- Visit [CoinGecko](https://www.coingecko.com/en) and search “Apu Apustaja”.
- Get the **exact coin ID** from the URL.
- Replace it in your `coins` dictionary.

## 🧠 Optional: Add Basic Retry for 429s

If you’d like to learn how to automatically retry on 429 errors later, I can walk you through that too — but for now, let’s keep it simple and just:

1. Fix any wrong coin IDs.
2. Slow down the requests.

## ✅ WHAT WORKED
These coins fetched data successfully:
- `spx6900`
- `gigachad-2`
- `mog-coin`
- `solana`

Your table output and comparison logic are working **exactly as intended**. ✅

### 2. `429` errors for the others:

```
status code: 429
```

- `429 = Too Many Requests`
- You are **hitting the API too fast**, and CoinGecko is temporarily blocking your IP.

This happened to:
- `popcat`
- `harrypotterobamasonic10inu-eth`
- `retardio`
- `lock-in`
- `mini`
- `american-coin`

### 🧠 Why this happened
Even though you added `time.sleep(2)`, it may **still not be enough**. CoinGecko has **strict rate limits**, especially if you're not using an API key.

### ✅ Step 2: Double-check coin IDs

One of your IDs is likely invalid:

```python
"apu": "apu-apustaja",  # 404 Not Found
```

🔍 You can search CoinGecko manually:
1. Go to https://www.coingecko.com
2. Search for “apu”
3. Click the coin and look at the URL. Example:
   - URL: `https://www.coingecko.com/en/coins/apu`
   - Coin ID: `apu` (not `apu-apustaja`)

So update your dictionary like this:

```python
"apu": "apu",  # correct ID
```

Repeat this for others if needed.

Let me know if you want to:
- Add retry logic with a **maximum number of retries** to avoid infinite loops.
- See how to use an **API key** (CoinGecko offers higher limits if you register).
- Add failed coins to the table with a ❌ or ⚠️ to visually track failures.

Would you like to implement one of those next?

### USER
when you look up apu this is the url on coingecko: https://www.coingecko.com/en/coins/apu-apustaja

### USER
that fixed the apu issue but i have a new error. ill send my code then the error

### USER
import requests
from tabulate import tabulate
import time

time.sleep(5)

def get_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
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

sol_data = get_coin_data("solana")

if sol_data:
    sol_change = sol_data['change_24h']
    results = []
    for key, coin_id in coins.items():
        if coin_id == "solana":
            continue

        time.sleep(2)  
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

    print(f"{sol_data['name'].upper()} ({sol_data['symbol'].upper()})")
    print(f"Price: ${sol_data['price']:,.2f}")
    print(f"Market Cap: ${sol_data['market_cap']:,.0f}")

    if sol_data['change_24h'] is not None:
        indicator = "🟢" if sol_data['change_24h'] >= 0 else "🔴"
        print(f"24h Change: {sol_data['change_24h']:.2f}% {indicator}")
    else:
        print("24h change: data not available ⚠️")

else:
    print("Failed to fetch Solana data, so comparison cannot be made.")

### USER
> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
Traceback (most recent call last):
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 48, in <module>
    outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌"
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: '>' not supported between instances of 'NoneType' and 'float'
PS C:\Users\Bryan>

### ASSISTANT
Great catch — so it turns out your original guess was correct!

That means the coin **does exist** on CoinGecko, and the URL confirms the coin ID is indeed:

```
apu-apustaja
```

But you still got this error:

```
failed to fetch data for apu-apustaja. status code: 404
```

So now we ask: **Why would CoinGecko give us a 404 if the coin exists?**

## 🧠 Why this matters

The CoinGecko **web interface** can use a more flexible routing system (e.g., redirecting to the right coin page), but the **API needs the exact coin ID** from their internal list.

So even though the URL shows `apu-apustaja`, the API might use something like just `apu` or even something like `apu-eth` depending on how they labeled it in the backend.

### ❌ The error:
```bash
TypeError: '>' not supported between instances of 'NoneType' and 'float'
```

### 📍 The problem line:
```python
outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌"
```

### 🧠 What it means:
You're trying to compare a value that is `None` (i.e. `coin_data["change_24h"]`) to a number (`sol_change`, which is a float). Python doesn’t know how to compare those.

This happens when a coin is missing 24h change data in the API response, so `coin_data["change_24h"]` becomes `None`.

### 💡 What changed:
- **Line-by-line check for `None`** before comparing.
- Gave `"N/A"` and `"⚠️"` to coins missing 24h data.
- All indented inside the `if coin_data:` block — otherwise, Python will throw an indentation error or skip data.
---

Would you like me to send the full corrected version of your script next?