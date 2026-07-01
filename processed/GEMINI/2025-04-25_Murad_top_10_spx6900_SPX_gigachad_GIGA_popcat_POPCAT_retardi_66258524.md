---
category: crypto-web3
date: 2025-04-25
id: 359978
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan was building a Python dictionary of Murad's top 10 meme coins and writing
  a function to fetch their prices from CoinGecko API.
tags:
- crypto-portfolio
- meme-coins
- murad-top-10
- coingecko-api
- python-dictionaries
---
# Murad_top_10 = {
    'spx6900': "SPX",
    'gigachad': "GIGA",
    'popcat' : "POPCAT",
    'retardio' : "RETARDIO",
    'mog-coin' : "MOG",  
    'apu-apustaja' : "APU",
    'harrypotterobamasonic10inu-eth' : "BITCOIN",
    'minimini' : "MINI",
    'lock-in' : "LOCKIN",
    'american-coin' : "USA"
}

#fetching list prices
def get_murad_prices(coin_dict, currency= 'usd'):
    prices = {}
    for coin_id, display_name in coin_dict.items():
        try:
            price = get_price(coin_id, currency)
            prices[display_name] = price 
        except KeyError:
                print (f"Could not fetch price for: {display_name} ({coin_id})")

### USER
Murad_top_10 = {
    'spx6900': "SPX",
    'gigachad': "GIGA",
    'popcat' : "POPCAT",
    'retardio' : "RETARDIO",
    'mog-coin' : "MOG",  
    'apu-apustaja' : "APU",
    'harrypotterobamasonic10inu-eth' : "BITCOIN",
    'minimini' : "MINI",
    'lock-in' : "LOCKIN",
    'american-coin' : "USA"
}

#fetching list prices
def get_murad_prices(coin_dict, currency= 'usd'):
    prices = {}
    for coin_id, display_name in coin_dict.items():
        try:
            price = get_price(coin_id, currency)
            prices[display_name] = price 
        except KeyError:
                print (f"Could not fetch price for: {display_name} ({coin_id})")

### GEMINI
Okay, this gives us a much clearer picture! Now we can see how Murad_top_10 and get_murad_prices are intended to work together. Here's how these two blocks of code connect: Murad_top_10 Dictionary: This dictionary, Murad_top_10, acts as the input for the get_murad_prices function. The keys in this dictionary (e.g., 'spx6900', 'gigachad', 'popcat', etc.) are the coin_id values that the get_price() function (which you shared earlier in a different context for 'solana') likely expects to fetch price data from an API (like CoinGecko). The values in this dictionary (e.g., "SPX", "GIGA", "POPCAT", etc.) are the user-friendly display names that you want to use as keys in the resulting prices dictionary. get_murad_prices Function: This function takes Murad_top_10 (or any dictionary with a similar structure) as its coin_dict argument. It iterates through each key-value pair in the coin_dict using coin_dict.items(). In each iteration: coin_id will hold the API identifier of the coin (e.g., 'spx6900'). display_name will hold the user-friendly name (e.g., "SPX"). Inside the try block, it calls the get_price() function (which we saw earlier was designed to fetch the price for a given coin_id and currency). It passes the current coin_id and the default currency ('usd') to get_price(). It assumes that get_price() will return the price of the coin. This price is then stored in the prices dictionary with the display_name as the key. So, for example, you might get prices['SPX'] = 123.45. The except KeyError: block is there to gracefully handle situations where the get_price() function might not find price data for a given coin_id (perhaps the API doesn't recognize that ID). If a KeyError occurs within get_price(), it will print a message indicating which coin's price couldn't be fetched. Finally, the function returns the prices dictionary, which will contain the display names of the coins as keys and their corresponding fetched prices as values (for all the coins for which the price retrieval was successful). How they connect in a typical workflow: You would likely first define your Murad_top_10 dictionary. Then, you would call the get_murad_prices() function, passing Murad_top_10 as the argument: prices = get_murad_prices(Murad_top_10) print(prices) The prices variable would then hold a dictionary containing the fetched prices for the coins in Murad_top_10, using the display names as keys. For example, the output might look something like: {'SPX': 4800.50, 'GIGA': 0.00005, 'POPCAT': 0.03, 'RETARDIO': 0.002, 'MOG': 0.0008, 'APU': 0.0015, 'BITCOIN': 65000.20, 'MINI': 1e-07, 'LOCKIN': 0.1, 'USA': 0.05} (Note: These are just example prices and might not be accurate.) So, Murad_top_10 provides the list of coins you're interested in, and get_murad_prices uses this list to fetch their prices and organize them into a more user-friendly dictionary. The connection is through the coin_dict parameter of the function. Do you have any specific questions about how they connect or what you're trying to achieve with this? Knowing your goal might help me provide even more relevant insights.
