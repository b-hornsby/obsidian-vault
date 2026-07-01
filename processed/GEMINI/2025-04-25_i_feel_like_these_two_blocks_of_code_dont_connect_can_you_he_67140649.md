---
category: coding
date: 2025-04-25
id: 215342
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan felt that two blocks of his Python code weren't properly connected
  and asked for help integrating them.
tags:
- python-code-integration
- code-structure
- debugging
---
# i feel like these two blocks of code don't connect can you help me 

### USER
i feel like these two blocks of code don't connect can you help me 

### GEMINI
You're right, just looking at those two isolated blocks, it's not immediately clear how they fit together. To help you connect them, I need a bit more context. Could you provide the following: The code for the get_price() function: This is being called within the get_murad_prices() function, so understanding how it works and what it returns is crucial. How coin_dict is being defined or populated: What kind of data does this dictionary hold? What are its keys and values? Where and how get_murad_prices() is being called: How are you using the output of this function? Is it being passed to another function or being printed? Once I see the surrounding code and understand the flow of data, I can definitely help you understand how these two blocks connect (or identify if there's a logical gap). For example, it seems like get_murad_prices() is designed to fetch prices for a list of coins provided in coin_dict. The keys in coin_dict are likely the coin_id values that get_price() expects, and the values in coin_dict are the display names for those coins. The get_murad_prices() function then returns a dictionary where the keys are the display names and the values are the fetched prices. But to confirm this and see how it fits into your larger program, please share more of your code. Let's piece this puzzle together!
