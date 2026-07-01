---
category: coding
date: 2025-04-25
id: 284405
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking a basic question about how empty dictionaries are represented
  in Python.
tags:
- python
- empty-dictionary
- coding-question
---
# so if its an empty dictionary it'll end in {}

### USER
so if its an empty dictionary it'll end in {}

### GEMINI
Yes, that's absolutely correct! In Python, an empty dictionary is indeed represented by a pair of curly braces with nothing inside: {}. When you initialize an empty dictionary, like in the line prices = {} in your previous example, you are essentially creating a dictionary that currently holds no key-value pairs. It's like an empty container ready to store data. As you add items to the dictionary (like prices[display_name] = price), it will start to contain key-value pairs within those curly braces, separated by colons, and the pairs themselves separated by commas. For example, after adding some prices, the prices dictionary might look something like this: {'Bitcoin': 40000.50, 'Ethereum': 3000.20, 'Solana': 150.75} But when it's initially created as empty, it's just {}. So, to directly answer your question: yes, an empty dictionary in Python is represented and ends (and begins!) with {}.
