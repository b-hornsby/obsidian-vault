---
id: 998071
source: CLAUDE
date: 2025-03-31
tags: ['python-fundamentals', 'beginner-python', 'python-tutorial']
category: coding
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is requesting a Python tutorial to learn the fundamentals of the language.
---
# Python Fundamentals for Beginners

### HUMAN
Teach me Python.

### ASSISTANT
# Introduction to Python

Python is one of the most popular and versatile programming languages today. Let's start with the basics and gradually build up your skills.

## Getting Started

Python has a clean, readable syntax that makes it excellent for beginners. Here's a simple "Hello World" program:

```python
print("Hello, World!")
```

## Variables and Data Types

Python uses dynamic typing, which means you don't need to declare variable types:

```python
# Numbers
age = 25             # integer
price = 19.99        # float

# Strings
name = "Alice"
message = 'Python is fun!'

# Booleans
is_active = True
has_completed = False

# Lists (ordered, mutable collections)
fruits = ["apple", "banana", "cherry"]

# Dictionaries (key-value pairs)
person = {"name": "John", "age": 30, "city": "New York"}
```

## Control Flow

### Conditional Statements

```python
x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x equals 5")
else:
    print("x is less than 5")
```

### Loops

```python
# For loop
for fruit in fruits:
    print(fruit)

# Range-based for loop
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions

```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Python Learner")
print(message)
```

## Would you like to dive deeper into any specific area or try some exercises to practice what you've learned so far?
