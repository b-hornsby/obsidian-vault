---
category: coding
date: 2025-04-25
id: 234594
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan shared code with a syntax error in the try-except block indentation
  for his Murad top 10 crypto price fetcher.
tags:
- python-syntax-error
- try-except-indentation
- crypto-price-fetcher
---
# #fetching list prices
def get_murad_prices(coin_dict, currency= 'usd'):
    prices = {}
    for coin_id, display_name in coin_dict.items():
        try:
            price = get_price(coin_id, currency)
            prices[display_name] = price 
            except KeyError:
                print (f"Could not fetch price for: {display_name} ({coin_id})")

### USER
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
Ah, I see the problem now! It's a subtle but crucial syntax error related to the indentation of your except block. In Python, the except keyword must be at the same indentation level as the try keyword it corresponds to. Looking at your code snippet: #fetching list prices def get_murad_prices(coin_dict, currency= 'usd'): prices = {} for coin_id, display_name in coin_dict.items(): try: price = get_price(coin_id, currency) prices[display_name] = price except KeyError: # Incorrect indentation print (f"Could not fetch price for: {display_name} ({coin_id})") The except KeyError: line is indented one level deeper than the try: line. This is causing the SyntaxError. Here's the corrected code with the proper indentation: #fetching list prices def get_murad_prices(coin_dict, currency= 'usd'): prices = {} for coin_id, display_name in coin_dict.items(): try: price = get_price(coin_id, currency) prices[display_name] = price except KeyError: # Correct indentation print (f"Could not fetch price for: {display_name} ({coin_id})") Key Change: I've moved the except KeyError: line to be at the same indentation level as the try: line above it. Python relies heavily on consistent indentation to define code blocks. Make sure that the try, except, and any finally blocks associated with a try statement all have the same level of indentation. Give this corrected code a run, and this SyntaxError should be resolved! Let me know if there's anything else. We're making good progress!
