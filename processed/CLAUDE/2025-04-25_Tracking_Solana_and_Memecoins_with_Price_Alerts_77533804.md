---
id: 697229
source: CLAUDE
date: 2025-04-25
tags: ['solana-price-tracking', 'memecoin-analysis', 'python-coding-help', 'price-alerts', 'coingecko-api']
category: crypto-web3
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan is building a Python script to track Solana and memecoin prices with alerts, seeking line-by-line tutoring and assistance with integrating a memecoin list.
---
# Tracking Solana and Memecoins with Price Alerts

### HUMAN
you are a python experrt with 7+ years of experience and a specialty in tutoring complete beginners in the language with no prior knowledge. I'm working on a project that compares the price of Solana to the price of Murad Mahmudov's list of memecoins that he believes in. I also want it to have alerts too. I already started on the solana tracking part so can i send over my code and can you help me pull this all together?

### ASSISTANT
I'd be happy to help you with your project comparing Solana and memecoins with price alerts! As a Python tutor for beginners, I can definitely help build on your existing code. Please go ahead and share what you've created so far, and I'll help you integrate the memecoin tracking and alert functionality.

### HUMAN
import requests

import csv

from datetime import datetime



#live SOL price

def get_price (coin_id='solana', currency='usd'):

    url =  f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"

    response = requests.get(url)

    data = response.json()

    return data[coin_id][currency]



#logging SOL price

def log_price(price):

    with open("sol_price_log.csv", mode="a",newline="") as file:

        writer = csv.writer(file)

        writer.writerow([datetime.now(),price])



#output SOL price

if __name__ == "__main__":

    price = get_price()

    log_price(price)

    print(f"Logged SOL price: ${price}")

### ASSISTANT
Your code is a great start! It's getting the current Solana price from CoinGecko's API and logging it to a CSV file. Let's build on this foundation to add memecoin tracking and price alerts.

Here's what we'll do:
1. Create a list of Murad Mahmudov's recommended memecoins
2. Fetch prices for all those coins 
3. Add price alert functionality
4. Generate a comparison report

Let's enhance your code:

<antArtifact identifier="crypto-tracker" type="application/vnd.ant.code" language="python" title="Solana and Memecoin Price Tracker with Alerts">
import requests
import csv
import time
from datetime import datetime
import os

# List of Murad Mahmudov's recommended memecoins (replace with actual list)
MURAD_MEMECOINS = {
    'dogecoin': 'DOGE',
    'shiba-inu': 'SHIB',
    'pepe': 'PEPE',
    'bonk': 'BONK',
    'book-of-meme': 'BOME'
    # Add more as needed
}

# Dictionary to store previous prices for alerting
previous_prices = {}

# Get price for any coin from CoinGecko
def get_price(coin_id='solana', currency='usd'):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
        response = requests.get(url)
        data = response.json()
        return data[coin_id][currency]
    except Exception as e:
        print(f"Error fetching price for {coin_id}: {e}")
        return None

# Get prices for all tracked coins
def get_all_prices():
    prices = {}
    # Get Solana price
    sol_price = get_price('solana')
    prices['solana'] = sol_price
    
    # Get memecoin prices
    for coin_id in MURAD_MEMECOINS.keys():
        price = get_price(coin_id)
        prices[coin_id] = price
        
    return prices

# Log prices to CSV
def log_prices(prices):
    timestamp = datetime.now()
    
    # Ensure main log directory exists
    if not os.path.exists('price_logs'):
        os.makedirs('price_logs')
    
    # Log Solana price
    sol_log_path = "price_logs/sol_price_log.csv"
    if not os.path.exists(sol_log_path):
        with open(sol_log_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Price (USD)"])
    
    with open(sol_log_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, prices['solana']])
    
    # Log memecoin prices
    meme_log_path = "price_logs/memecoin_price_log.csv"
    if not os.path.exists(meme_log_path):
        with open(meme_log_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            header = ["Timestamp"] + list(MURAD_MEMECOINS.values())
            writer.writerow(header)
    
    with open(meme_log_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        row = [timestamp] + [prices[coin_id] for coin_id in MURAD_MEMECOINS.keys()]
        writer.writerow(row)

# Check for price alerts
def check_alerts(current_prices, alert_threshold=0.05):
    alerts = []
    
    for coin_id, price in current_prices.items():
        if price is None:
            continue
            
        # Get display name
        display_name = MURAD_MEMECOINS.get(coin_id, coin_id.upper())
        if coin_id == 'solana':
            display_name = 'SOL'
            
        # If we have a previous price, check for significant changes
        if coin_id in previous_prices and previous_prices[coin_id] is not None:
            prev_price = previous_prices[coin_id]
            percent_change = (price - prev_price) / prev_price
            
            if abs(percent_change) >= alert_threshold:
                direction = "increased" if percent_change > 0 else "decreased"
                alerts.append(
                    f"{display_name} price {direction} by {abs(percent_change)*100:.2f}%: "
                    f"${prev_price:.6f} → ${price:.6f}"
                )
    
    # Update previous prices for next comparison
    previous_prices.update(current_prices)
    
    return alerts

# Generate comparison report
def generate_report(prices):
    if prices['solana'] is None:
        return "Unable to generate report: Solana price unavailable"
        
    report = f"PRICE REPORT ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n"
    report += "-" * 50 + "\n"
    report += f"SOL: ${prices['solana']:.4f}\n\n"
    
    report += "MEMECOINS:\n"
    for coin_id, symbol in MURAD_MEMECOINS.items():
        if prices[coin_id] is not None:
            # Calculate price ratio to SOL (how many memecoins per 1 SOL)
            if prices[coin_id] > 0:
                ratio = prices['solana'] / prices[coin_id]
                report += f"{symbol}: ${prices[coin_id]:.6f} ({ratio:.2f} {symbol} per SOL)\n"
            else:
                report += f"{symbol}: ${prices[coin_id]:.6f}\n"
        else:
            report += f"{symbol}: Price unavailable\n"
    
    return report

# Main function
def main(check_interval=3600):  # Default: check every hour
    print("Starting Solana and Memecoin Price Tracker")
    print(f"Tracking: SOL and {', '.join(MURAD_MEMECOINS.values())}")
    print(f"Checking prices every {check_interval} seconds")
    print("-" * 50)
    
    try:
        while True:
            # Get current prices
            current_prices = get_all_prices()
            
            # Log prices
            log_prices(current_prices)
            
            # Check for alerts
            alerts = check_alerts(current_prices)
            
            # Generate and display report
            report = generate_report(current_prices)
            print(report)
            
            # Display any alerts
            if alerts:
                print("\nALERTS:")
                for alert in alerts:
                    print(f"⚠️ {alert}")
                print()
            
            # Wait for next check
            print(f"Next check in {check_interval} seconds...\n")
            time.sleep(check_interval)
            
    except KeyboardInterrupt:
        print("\nExiting price tracker. Goodbye!")

# Run as standalone script
if __name__ == "__main__":
    # For testing, check every 60 seconds
    # For production use, consider a longer interval like 3600 (hourly)
    main(check_interval=60)
</antArtifact>

This enhanced script builds on your original code with several key improvements:

1. **Memecoin Tracking**: It now tracks a list of memecoins (currently populated with examples - you should replace with Murad Mahmudov's actual recommendations).

2. **Organized Logging**: Creates a separate CSV file for memecoins alongside your Solana log.

3. **Price Alerts**: Compares current prices with previous values and alerts you when price changes exceed a threshold (default 5%).

4. **Price Comparison Report**: Shows the current prices and calculates how many of each memecoin you could get for 1 SOL.

5. **Continuous Monitoring**: Runs on a configurable interval (default is set to 60 seconds for testing, but you can increase it for production).

To use this script:

1. First, update the `MURAD_MEMECOINS` dictionary with the actual list of memecoins he recommends.
2. Adjust the `alert_threshold` if you want to be notified at a different percentage change.
3. Set an appropriate `check_interval` for how often you want prices checked.

Would you like me to explain any specific part of the code in more detail?

### HUMAN
okay two things I wanted to add. You are crazy at code generation by the way but I want to understand the language so can you explain line by line what each function means as i type along with your instruction? I want to have a deep understanding so I don't want to just copy/paste your code. I'll also send you a screenshot of his list so you have reference when including those

### ASSISTANT
I appreciate your approach to learning Python deeply rather than just copying code. That's exactly how you'll develop a strong foundation in the language. Let's go through the code together line by line, and I'll explain each component as you type along.

Once you share that screenshot of Murad's list, we can incorporate those specific memecoins. Let's start with the fundamentals and work our way through:

### Basic Import Statements

```python
import requests  # Library for making HTTP requests (to fetch cryptocurrency prices)
import csv  # Library for reading/writing CSV files (to log price data)
import time  # Library for adding delays and working with time
from datetime import datetime  # For getting and formatting current time
import os  # For working with files and directories
```

These imports bring in the essential tools we'll need:
- `requests`: Lets us make API calls to CoinGecko to get cryptocurrency prices
- `csv`: Allows us to save price data in CSV format
- `time`: We'll use this to pause between price checks
- `datetime`: For timestamping our price logs
- `os`: For creating directories and checking if files exist

### Setting Up Constants

```python
# List of Murad Mahmudov's recommended memecoins (replace with actual list)
MURAD_MEMECOINS = {
    'dogecoin': 'DOGE',
    'shiba-inu': 'SHIB',
    'pepe': 'PEPE',
    'bonk': 'BONK',
    'book-of-meme': 'BOME'
    # Add more as needed
}
```

This is a dictionary where:
- Keys are the coin IDs used by CoinGecko API (like 'dogecoin')
- Values are the ticker symbols (like 'DOGE') for display purposes
- We'll replace these with Murad's actual recommendations once you share the screenshot

```python
# Dictionary to store previous prices for alerting
previous_prices = {}
```

This empty dictionary will keep track of the last recorded price for each coin, allowing us to calculate percentage changes for alerts.

### Price Fetching Function

```python
# Get price for any coin from CoinGecko
def get_price(coin_id='solana', currency='usd'):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
        response = requests.get(url)
        data = response.json()
        return data[coin_id][currency]
    except Exception as e:
        print(f"Error fetching price for {coin_id}: {e}")
        return None
```

This function:
1. Takes a `coin_id` (defaulting to 'solana') and currency (defaulting to 'usd')
2. Constructs a URL to query CoinGecko's API
3. Makes the HTTP request and converts the response to JSON
4. Extracts the price from the response data
5. Has error handling to prevent crashes if the API call fails

### Function to Get All Prices

```python
# Get prices for all tracked coins
def get_all_prices():
    prices = {}
    # Get Solana price
    sol_price = get_price('solana')
    prices['solana'] = sol_price
    
    # Get memecoin prices
    for coin_id in MURAD_MEMECOINS.keys():
        price = get_price(coin_id)
        prices[coin_id] = price
        
    return prices
```

This function:
1. Creates an empty dictionary to store all prices
2. Gets the Solana price and adds it to the dictionary
3. Loops through each memecoin in our list
4. Gets the price for each memecoin and adds it to the dictionary
5. Returns the complete dictionary of prices

### Price Logging Function

```python
# Log prices to CSV
def log_prices(prices):
    timestamp = datetime.now()
    
    # Ensure main log directory exists
    if not os.path.exists('price_logs'):
        os.makedirs('price_logs')
```

This function starts by:
1. Recording the current timestamp
2. Creating a 'price_logs' directory if it doesn't already exist

```python    
    # Log Solana price
    sol_log_path = "price_logs/sol_price_log.csv"
    if not os.path.exists(sol_log_path):
        with open(sol_log_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Price (USD)"])
    
    with open(sol_log_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, prices['solana']])
```

This section:
1. Defines the path for the Solana price log
2. Checks if the file exists, and if not, creates it with headers
3. Opens the file in append mode ('a')
4. Adds a new row with the current timestamp and Solana price

```python
    # Log memecoin prices
    meme_log_path = "price_logs/memecoin_price_log.csv"
    if not os.path.exists(meme_log_path):
        with open(meme_log_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            header = ["Timestamp"] + list(MURAD_MEMECOINS.values())
            writer.writerow(header)
    
    with open(meme_log_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        row = [timestamp] + [prices[coin_id] for coin_id in MURAD_MEMECOINS.keys()]
        writer.writerow(row)
```

Similarly, this section:
1. Defines the path for the memecoin price log
2. Creates the file with headers if it doesn't exist
3. Adds a new row with timestamp and prices for all memecoins

Let me know when you've finished typing this part, and I'll continue with the explanation of the remaining functions.

### HUMAN
can i add the list after the output for solana price instead?

### ASSISTANT
Absolutely! We can modify the code structure to add Murad's list of memecoins after you've successfully fetched the Solana price. This is a great approach that builds on your existing code more incrementally.

Let's adjust the design so that we maintain your original code for fetching the Solana price, and then extend it to handle the memecoins. Here's how we can organize it:

```python
import requests
import csv
from datetime import datetime
import time
import os

# Your original function for getting SOL price
def get_price(coin_id='solana', currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    return data[coin_id][currency]

# Your original function for logging SOL price
def log_price(price):
    with open("sol_price_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), price])
```

Then after that, we can add the memecoin tracking functionality:

```python
# Murad's list of memecoins will go here
MURAD_MEMECOINS = {
    # We'll add these from the screenshot you'll send
}

# New function to get memecoin prices
def get_memecoin_prices():
    prices = {}
    for coin_id in MURAD_MEMECOINS.keys():
        try:
            price = get_price(coin_id)
            prices[coin_id] = price
        except Exception as e:
            print(f"Error getting price for {coin_id}: {e}")
            prices[coin_id] = None
    return prices

# New function to log memecoin prices
def log_memecoin_prices(prices):
    # Create the file with headers if it doesn't exist
    if not os.path.exists("memecoin_prices.csv"):
        with open("memecoin_prices.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            header = ["Timestamp"] + list(MURAD_MEMECOINS.values())
            writer.writerow(header)
    
    # Append the current prices
    with open("memecoin_prices.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        timestamp = datetime.now()
        row = [timestamp] + [prices[coin_id] for coin_id in MURAD_MEMECOINS.keys()]
        writer.writerow(row)
```

And finally we can update the main execution block to incorporate both:

```python
if __name__ == "__main__":
    # Get and log SOL price (your original code)
    sol_price = get_price()
    log_price(sol_price)
    print(f"Logged SOL price: ${sol_price}")
    
    # Now get and log memecoin prices
    print("\nFetching Murad's recommended memecoin prices...")
    memecoin_prices = get_memecoin_prices()
    log_memecoin_prices(memecoin_prices)
    
    # Display results
    print("\nCurrent prices:")
    print(f"SOL: ${sol_price}")
    for coin_id, symbol in MURAD_MEMECOINS.items():
        if coin_id in memecoin_prices and memecoin_prices[coin_id] is not None:
            print(f"{symbol}: ${memecoin_prices[coin_id]}")
        else:
            print(f"{symbol}: Price unavailable")
```

This approach keeps your original code intact and adds the memecoin functionality afterward. When you share Murad's list, we'll populate the `MURAD_MEMECOINS` dictionary with the actual coins he recommends.

### HUMAN
okay so to kind of reel it in im going to send you a screenshot of coins that he believes in. don't pay any attention to the market cap or anything like that moreso just the ticker name. after that i'll send you the lines of python that i have so far and i need you to help tutor me on implementing the next steps to bring my idea to life. still need the line by line instruction as well

### ASSISTANT
I'll be happy to help you implement your idea step-by-step once you send over both the screenshot of Murad's coin list and your existing Python code. 

When I see the coin tickers in the screenshot, I'll focus just on those names rather than any market cap data or other details. Then once I can see your current code, I'll provide detailed line-by-line guidance to implement the memecoin tracking and alert system.

Looking forward to seeing the screenshot and your code so we can continue building your project together!

### HUMAN
this is that list. i will send you my code next

### ASSISTANT
I see the list of Murad's recommended coins with their tickers. Perfect! I've captured the following coin tickers from the screenshot:

1. SPX6900
2. BITCOIN (not BTC)
3. MOG
4. APU
5. FARTCOIN
6. PEPE
7. GIGA
8. POPCAT
9. FWOG
10. WIF
11. RETARDIO
12. SIGMA
13. MICHI
14. LOCKIN
15. ZEREBRO
16. MINI
17. GOAT

I'll use these tickers when implementing the memecoin tracking functionality in your code. Looking forward to seeing your current code so I can help you build on it!

### HUMAN
import requests

import csv

from datetime import datetime

import os 



#live SOL price

def get_price (coin_id='solana', currency='usd'):

    url =  f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"

    response = requests.get(url)

    data = response.json()

    return data[coin_id][currency]



#logging SOL price

def log_price(price):

    with open("sol_price_log.csv", mode="a",newline="") as file:

        writer = csv.writer(file)

        writer.writerow([datetime.now(),price])



#output SOL price

if __name__ == "__main__":

    price = get_price()

    log_price(price)

    print(f"Logged SOL price: ${price}")

### ASSISTANT
Great! Now I can see your current code. It's a good foundation that gets the SOL price from CoinGecko and logs it to a CSV file. Let's build on this to incorporate the list of memecoins and add the alert functionality.

I'll guide you through implementing this step by step, with explanations for each line:

### Step 1: Add Constants for Murad's Memecoins

First, let's add the list of memecoins right after your imports:

```python
# List of Murad Mahmudov's recommended memecoins
# The keys are CoinGecko API IDs, values are display tickers
MURAD_MEMECOINS = {
    'spx6900': 'SPX6900',
    'bitcoin-bep2': 'BITCOIN',  # Using BEP2 token as placeholder
    'mogwai': 'MOG',
    'aptos': 'APU',  # Using Aptos as placeholder
    'fart': 'FARTCOIN',
    'pepe': 'PEPE',
    'giga-finance': 'GIGA',
    'popcat': 'POPCAT',
    'frog': 'FWOG',  # Using 'frog' as placeholder
    'wif-token': 'WIF',
    'retardio': 'RETARDIO',
    'sigmacoin': 'SIGMA',  # Using placeholder
    'michi': 'MICHI',
    'lockin': 'LOCKIN',
    'zerebro': 'ZEREBRO',
    'mini': 'MINI',
    'goat-token': 'GOAT'  # Using placeholder
}
```

Let me explain:
- This creates a dictionary where the keys are the CoinGecko API IDs and the values are the ticker symbols you want to display
- I've had to make educated guesses for some coins because CoinGecko might use different IDs than the ticker names
- We'll need to test and adjust these IDs later to match what CoinGecko actually uses

### Step 2: Create a Dictionary to Store Previous Prices for Alerts

```python
# Dictionary to store previous prices for alerting
previous_prices = {}
```

This will store the last fetched price for each coin, allowing us to compare and generate alerts.

### Step 3: Add a Function to Get Memecoin Prices

```python
# Get prices for all memecoins
def get_memecoin_prices():
    prices = {}
    for coin_id, ticker in MURAD_MEMECOINS.items():
        try:
            price = get_price(coin_id)
            prices[coin_id] = price
            print(f"Successfully fetched {ticker} price: ${price}")
        except Exception as e:
            print(f"Error fetching {ticker} price: {e}")
            prices[coin_id] = None
    return prices
```

Explanation:
- This function loops through each memecoin in our list
- For each coin, it tries to fetch the price using your existing `get_price` function
- If successful, it stores the price in the `prices` dictionary
- If there's an error (which might happen if CoinGecko doesn't recognize our coin ID), it prints an error message and stores `None` for that coin
- Finally, it returns the dictionary of prices

### Step 4: Add Function to Log Memecoin Prices

```python
# Log memecoin prices to CSV
def log_memecoin_prices(prices):
    # Make sure we have a directory for logs
    if not os.path.exists("price_logs"):
        os.makedirs("price_logs")
    
    # File path for memecoin log
    memecoin_log_path = "price_logs/memecoin_prices.csv"
    
    # Create file with headers if it doesn't exist
    if not os.path.exists(memecoin_log_path):
        with open(memecoin_log_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            header = ["Timestamp"] + list(MURAD_MEMECOINS.values())
            writer.writerow(header)
    
    # Append the current prices
    with open(memecoin_log_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        timestamp = datetime.now()
        row = [timestamp]
        
        # Add each memecoin's price to the row
        for coin_id in MURAD_MEMECOINS.keys():
            row.append(prices.get(coin_id, "N/A"))
        
        writer.writerow(row)
```

Explanation:
- First, we ensure we have a directory for logs
- We define the path for our memecoin price log file
- If the file doesn't exist yet, we create it with appropriate headers
- We open the file in append mode to add a new row
- We create a row starting with the current timestamp
- We add each memecoin's price to the row
- Finally, we write the row to the CSV file

### Step 5: Create Alert Function

```python
# Check for significant price changes and generate alerts
def check_price_alerts(new_prices, threshold=0.05):
    alerts = []
    
    # Compare with previous prices (if any)
    for coin_id, price in new_prices.items():
        if price is None:
            continue
            
        # Get display ticker for this coin
        ticker = MURAD_MEMECOINS.get(coin_id, coin_id.upper())
        
        # If we have a previous price for comparison
        if coin_id in previous_prices and previous_prices[coin_id] is not None:
            prev_price = previous_prices[coin_id]
            
            # Calculate percentage change
            if prev_price > 0:  # Avoid division by zero
                percent_change = (price - prev_price) / prev_price
                
                # If change exceeds threshold, generate alert
                if abs(percent_change) >= threshold:
                    direction = "increased" if percent_change > 0 else "decreased"
                    alert_msg = f"{ticker} has {direction} by {abs(percent_change)*100:.2f}%: ${prev_price:.6f} → ${price:.6f}"
                    alerts.append(alert_msg)
    
    # Update previous prices for next comparison
    previous_prices.update(new_prices)
    
    return alerts
```

Explanation:
- This function takes a dictionary of new prices and a threshold percentage (default 5%)
- It creates an empty list to store alerts
- For each coin with a valid price:
  - It gets the display ticker for the coin
  - If we have a previous price to compare with, it calculates the percentage change
  - If the change exceeds our threshold, it creates an alert message
  - The alert includes the direction of change, percentage, and both old and new prices
- After checking all coins, it updates our `previous_prices` dictionary
- Finally, it returns the list of alerts

### Step 6: Update the Main Function

```python
# Modified main function
if __name__ == "__main__":
    try:
        # Get and log SOL price (your original code)
        sol_price = get_price()
        log_price(sol_price)
        print(f"Logged SOL price: ${sol_price}")
        
        # Get memecoin prices
        print("\nFetching Murad's memecoin prices...")
        memecoin_prices = get_memecoin_prices()
        
        # Log memecoin prices
        log_memecoin_prices(memecoin_prices)
        print("Logged memecoin prices to 'price_logs/memecoin_prices.csv'")
        
        # Check for alerts (none on first run)
        alerts = check_price_alerts(memecoin_prices)
        
        # Display alerts if any
        if alerts:
            print("\nALERTS:")
            for alert in alerts:
                print(f"⚠️ {alert}")
                
        print("\nAll prices fetched and logged successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

Explanation:
- This replaces your original main function
- It starts by getting and logging the SOL price (your original code)
- Then it fetches memecoin prices
- It logs those prices to a CSV file
- It checks for price alerts (though there won't be any on the first run)
- If there are any alerts, it displays them
- Finally, it confirms that everything was fetched and logged
- The whole thing is wrapped in a try-except block to handle any unexpected errors

Would you like to implement these functions one by one, or would you prefer to see how they all work together in the complete program?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/crypto-web3|Crypto Web3]]
