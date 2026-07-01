---
category: coding
date: 2025-04-25
id: 991986
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was confirming the syntax difference between Python lists [] and dictionaries
  {}.
tags:
- python-data-structures
- list-vs-dictionary
- syntax
---
# so a list is [] and a dictionary is {}

### USER
so a list is [] and a dictionary is {}

### GEMINI
That's the core of it! You've got the fundamental syntax down for representing empty collections in Python: List: An empty list is represented by []. Dictionary: An empty dictionary is represented by {}. Keep in mind that when they contain elements, the syntax expands: List with elements: [item1, item2, item3] Dictionary with elements: {key1: value1, key2: value2, key3: value3} And as we briefly touched on earlier, an empty set is a bit of an exception. You can't use {} to create an empty set because that creates an empty dictionary. To create an empty set, you need to use the set() constructor: empty_set = set() However, once a set has elements, you represent it using curly braces, similar to a dictionary but without the colons: my_set = {1, 2, 3} So, to summarize your initial statement: yes, [] for an empty list and {} for an empty dictionary is correct! Just remember the special case for creating an empty set. You're doing great!
