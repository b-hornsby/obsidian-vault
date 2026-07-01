---
category: coding
date: 2025-04-23
id: 527363
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan shared his full Python code for a Solana price logger to get help debugging
  multiple issues including csv.write and string formatting errors.
tags:
- python-code-review
- coingecko-api
- csv-logging
- solana-tracker
---
# import requests
import csv
from datetime import datetime

def get_price (coin_id='solana', currency='usd'):
    url =  f"https://api.coingecko.com/api/v3/simple/price?ids= {coin_id}&vs_currencies= {currency}"
    response = requests.get(url)
    data = response.json()
    return data[coin_id][currency]

def log_price(price):
    with open("sol_price_log.csv", mode=a,newline="") as file:
        writer = csv.write(file)
        writer.writerow([datetime.now(),price])


if __name__ == "__main__":
    price = get_price()
    log_price(price)
    print(f"Logged SOL price: ${price}")

### USER
import requests
import csv
from datetime import datetime

def get_price (coin_id='solana', currency='usd'):
    url =  f"https://api.coingecko.com/api/v3/simple/price?ids= {coin_id}&vs_currencies= {currency}"
    response = requests.get(url)
    data = response.json()
    return data[coin_id][currency]

def log_price(price):
    with open("sol_price_log.csv", mode=a,newline="") as file:
        writer = csv.write(file)
        writer.writerow([datetime.now(),price])


if __name__ == "__main__":
    price = get_price()
    log_price(price)
    print(f"Logged SOL price: ${price}")

### GEMINI
Thanks for sharing your code! I see the issue now. The problem lies in how you're constructing the URL for the CoinGecko API. Notice the extra spaces you have within the f-string: url = f"https://api.coingecko.com/api/v3/simple/price?ids= {coin_id}&vs_currencies= {currency}" These spaces are causing the coin_id in the URL to be " solana" instead of "solana". When the API returns the JSON response, the key for the Solana price will likely be "solana" (without the leading space), hence the KeyError: 'solana'. Here's how to fix it: Remove the extra spaces in your URL: import requests import csv from datetime import datetime def get_price (coin_id='solana', currency='usd'): url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}" response = requests.get(url) data = response.json() return data[coin_id][currency] def log_price(price): with open("sol_price_log.csv", mode="a", newline="") as file: writer = csv.writer(file) # You were missing the module name here writer.writerow([datetime.now(), price]) if __name__ == "__main__": price = get_price() log_price(price) print(f"Logged SOL price: ${price}") Key changes: Removed the spaces around {coin_id} and {currency} in the url definition. Corrected csv.write to csv.writer in the log_price function. You need to call the writer function from the csv module to create a writer object. Give this updated code a try, and it should resolve the KeyError. Let me know if you run into any other issues!
