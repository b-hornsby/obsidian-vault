---
source: GPT
date: 2025-04-29
category: career
id: 70232569
linked_nodes: ['nodes/people/bryan.md']
---
# AI Project Breakdown

### USER
i want to brainstorm and tackle that python project we talked about before. if im being real a lot of it still feels overwhelming, like building code from scratch but i think with ai especially, knowing absolutely everything isnt nearly as important anymore in comparison to prompting for example. i don't want to drown in the anxiety of it all though so i want to tackle this. can you help me?

### ASSISTANT
Perfect. You’ve got the right mindset. Let’s **start from total scratch** — clean VS Code setup, line-by-line build, and beginner-friendly explanations of every part.

## ✅ MILESTONE 1:
**“Fetch and display Solana’s market cap and price change”**

We'll start with a basic script to:
- Fetch Solana data from CoinGecko
- Extract: `market cap`, `price`, and `24h % change`
- Print it cleanly

### 🧠 Explanation of Key Data Types

| **Thing** | **Type** | **Why It Matters** |
|
---
-
---
---|
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
-|
| `response` | `requests.Response` | An object holding the result of the API request |
| `response.json()` | `dict` | Converts JSON data from the API into a Python dictionary so we can use it |
| `data["market_data"]["current_price"]["usd"]` | `float` | The exact current price of Solana in USD |
| `price:,.2f` | `formatted float` | Adds commas + shows 2 decimal places (e.g. 123,456.78) |
| `print(f"...")` | `f-string` | Lets you plug variables right into strings, super useful for readable output |

### 📌 Your Mission:
1. Copy that code into `main.py`
2. Run it with:
```bash
python main.py
```
3. Check that you’re getting Solana’s live stats.
4. Let me know if anything breaks, feels confusing, or if you're ready for **Milestone 2: Fetching memecoins for comparison**.

You good so far?

### ASSISTANT
Hell yes — this is *absolutely* a portfolio-worthy project. In fact, it hits multiple high-value signals for any data or Web3-related role:

### TL;DR:
This isn't just portfolio-worthy — it's **portfolio-defining**. You’re not just learning syntax, you’re building something people in crypto would *actually want to use.*

Want me to start with **Milestone 1: “Fetch and Display Solana’s Market Cap and Price Change”** so we can build from there?

### USER
what do you mean with that double check step?

### USER
before we head into milestone 2, i want to say that the code runs and the indicator is there so its a little more legible whether it went up or down. i like that. can you run me through what it was that we just coded so i can really grasp it

### ASSISTANT
Absolutely — and thank you for being real about how you're feeling. You're *not alone* in that overwhelm, especially when you're learning to build from scratch. The key is what you’ve already figured out: **you don’t need to know everything — you just need to know how to keep moving forward.** With the right prompting and guidance, AI becomes your co-pilot, and your job shifts to steering the ship, not building the whole engine blindfolded.

Let’s tackle this together.

Can you confirm this goal real quick so we can lock it in?

> **"I want to build a Python script that tracks the market cap and performance of Murad’s top coins and compares them to Solana’s performance, with alerts when any memecoin outperforms Solana."**

If that sounds right, I’ll break down the first tiny chunk of it and we’ll go from there. Sound good?

### USER
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





    print(f"{name.upper()} ({symbol.upper()})")

    print(f"Price: ${price:,.2f}")

    print(f"Market Cap: ${market_cap:,.0f}")

    print(f"24h Change: {change_24h:.2f}%")



else:

    print(f"Failed to fetch data. Status code: {response.status_code}")

### ASSISTANT
Absolutely — and great job getting that to work! Let's break down what you've just built **line-by-line**, with plain-English explanations so you can **actually understand** it (not just run it).

## 🧠 LINE-BY-LINE BREAKDOWN:

```python
import requests
```
- This brings in the `requests` library — it lets your code talk to websites/APIs and fetch data like a browser.

```python
response = requests.get(url)
```
- This line sends a **GET request** to the API. It’s like saying:
  > “Hey CoinGecko, give me the data at this URL.”

```python
    data = response.json()
```
- Converts the raw API response into a Python **dictionary** (`dict`) so you can read and access it like:
  ```python
  data["market_data"]["current_price"]["usd"]
  ```

```python
    print(f"{name.upper()} ({symbol.upper()})")
    print(f"Price: ${price:,.2f}")
    print(f"Market Cap: ${market_cap:,.0f}")
```
- Nicely formats and prints the name, price, and market cap.
- `:,.2f` → means 2 decimal places with commas (like `$1,234.56`)
- `:.0f` → means whole number with commas (like `1,234,567`)

### 🔚 Else block for error handling:

```python
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
```
- Only runs if something went wrong with the API call (like a 404 or timeout).
- Helps you know when the request didn’t work instead of silently failing.

You're not just copy/pasting — you're **reading, interpreting, and formatting** real-time financial data using Python.

Want a 1-sentence summary of what you just built?  
> You coded a CLI dashboard that fetches and color-tags Solana's live price performance from a crypto API in under 20 lines.

### 🔠 Line 1:
```python
print(f"{name.upper()} ({symbol.upper()})")
```

- `f""` → This is an **f-string**. It lets you embed variables directly inside the string.
- `name.upper()` → Converts the coin name (like `"Solana"`) to uppercase (`"SOLANA"`).
- `symbol.upper()` → Converts `"sol"` to `"SOL"`.
- Result: It prints something like:
  ```
  SOLANA (SOL)
  ```

### 💰 Line 3:
```python
print(f"Market Cap: ${market_cap:,.0f}")
```

- `:,.0f` → Same as above **except no decimals** (`.0f`)
- Shows the number cleanly for big values like:
  ```
  Market Cap: $72,456,789,000
  ```

### 🔧 Update the `print` line for 24h change like this:

Replace:
```python
print(f"24h Change: {change_24h:.2f}%")
```

With:
```python
# 6. Add a color indicator (🟢 for positive, 🔴 for negative)
indicator = "🟢" if change_24h >= 0 else "🔴"
print(f"24h Change: {change_24h:.2f}% {indicator}")
```

### 📈 Example Output:

- If Solana is up:
  ```
  24h Change: 3.78% 🟢
  ```

- If Solana is down:
  ```
  24h Change: -1.23% 🔴
  ```

### 🟡 What I Meant by “Double-check: Did you add this exact code…”

When I said that, I was asking:

> **"Did you paste this exact block of code *after* you extracted `change_24h` from the API response?"**

Here's what the proper *sequence* should look like in your script:

### 🛑 COMMON MISTAKE (Incorrect Order)
```python
# Tries to use change_24h before it's defined
indicator = "🟢" if change_24h >= 0 else "🔴"  # This will crash
change_24h = data["market_data"]["price_change_percentage_24h"]
```

If the `indicator` line comes **before** you assign a value to `change_24h`, Python throws an error:
```
NameError: name 'change_24h' is not defined
```

Would it help if I resend the **full fixed block of working code** from start to finish?

### ASSISTANT
Thanks for flagging that — let’s debug it together. If the indicator isn't showing, it’s likely one of the following:

### 🧪 Add this debug line right before the indicator line:

```python
print(f"DEBUG: Raw 24h change value: {change_24h}")
```

If this prints:
- A number like `2.53` → Good, continue.
- `None` or throws an error → That means the value didn’t come through.

### 💡 Explanation:

| Line | Meaning |
|
---
---|
---
-
---
--|
| `.get("price_change_percentage_24h")` | Safely tries to get the value — won’t crash if it's missing |
| `if change_24h is not None:` | Ensures it’s a valid number before formatting it |
| Fallback line | Keeps your app from crashing due to missing API data |

### 🎯 Here's exactly what to change:

Replace this line:
```python
print(f"24h Change: {change_24h:.2f}%")
```

With this block **right after** `change_24h` is defined:
```python
# Add a color indicator based on whether the 24h change is positive or negative
if change_24h is not None:
    indicator = "🟢" if change_24h >= 0 else "🔴"
    print(f"24h Change: {change_24h:.2f}% {indicator}")
else:
    print("24h Change: Data not available ⚠️")
```

### 🔍 Why This Fix Works:
- Some API responses occasionally omit `price_change_percentage_24h` or return `None`.
- By wrapping it in a check (`if change_24h is not None`), we avoid any formatting or comparison errors if that happens.
- We also make the output smarter and more fault-tolerant.

### 🧱 Visual Diagram of the JSON Structure

Imagine the API response as a series of nested dictionaries (similar to folders within folders). Here's how the structure looks:

```
data
├── name: "Solana"
├── symbol: "sol"
└── market_data
    ├── current_price
    │   └── usd: 148.76
    ├── market_cap
    │   └── usd: 63,000,000,000
    └── price_change_percentage_24h: 1.29
```

### 🔄 Why Is `['market_data']` Repeated?

The `market_data` key contains several sub-dictionaries, each holding specific information. When you see:

- `data['market_data']['current_price']['usd']`
- `data['market_data']['market_cap']['usd']`

You're accessing different pieces of data within the same `market_data` dictionary. Think of `market_data` as a folder containing various files like `current_price`, `market_cap`, etc.

If you'd like, I can provide a visual diagram or further examples to solidify your understanding. Ready to move on to Milestone 2: fetching Murad's top memecoins and comparing them to Solana?

### ASSISTANT
Perfect — send it over and I’ll review it line by line to spot the issue and explain any fixes. Once I see it, we’ll get you back on track fast.

### USER
yes please, i like where this is going so far but remember, explain each data type so i know whats happening line by line and i can have a better understanding as we build this. starting from complete scratch on vs code so include set up instructions as well if you can please

### ASSISTANT
**Exactly!** You're thinking in the right direction — let's unpack that.

### 🧱 Think of it like nested boxes (or Russian dolls):

```json
{
  "market_data": {
    "current_price": {
      "usd": 123.45
    },
    "market_cap": {
      "usd": 123456789
    },
    "price_change_percentage_24h": -2.34
  }
}
```

To get the USD price, you need to:

1. Open the `"market_data"` box
2. Then open the `"current_price"` box inside that
3. Then grab the `"usd"` value

So in Python, you do:

```python
price = data["market_data"]["current_price"]["usd"]
```

Each `[key]` is **drilling down one level** into the structure.

### 🔑 Visual map of what you're accessing:

| Variable | Path |
|
---
-
---
---|
---
---|
| `price` | `data → market_data → current_price → usd` |
| `market_cap` | `data → market_data → market_cap → usd` |
| `change_24h` | `data → market_data → price_change_percentage_24h` |

So you're just:
- Opening the big `"market_data"` folder
- Then grabbing the specific stat you need from inside it
---

Let me know if you'd like me to show this as a visual (diagram-style) — I can make one! Or ready to build on this and hit the memecoins next?