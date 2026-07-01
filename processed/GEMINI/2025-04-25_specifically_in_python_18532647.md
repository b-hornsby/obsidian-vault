---
category: coding
date: 2025-04-25
id: 519124
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is clarifying that his question is specifically about Python.
tags:
- python
- coding-question
---
# specifically in python 

### USER
specifically in python 

### GEMINI
Ah, you want to focus specifically on Python! In that case, the answer is straightforward: functions and other code blocks in Python do NOT end in curly braces {}. Instead, Python uses indentation to define the scope and boundaries of code blocks. This applies to: Function definitions (def): The code that belongs to a function is indented under the def line. Conditional statements (if, elif, else): The code that executes based on the condition is indented under the respective keyword. Loops (for, while): The code that is executed repeatedly is indented under the loop statement. Class definitions (class): The attributes and methods of a class are indented under the class line. Context managers (with): The code that runs within the context is indented under the with statement. Exception handling (try, except, finally): The code within each of these blocks is indented. Here's an example to illustrate: def my_function(x): if x > 5: print("x is greater than 5") result = x * 2 else: print("x is not greater than 5") result = x + 2 return result for i in range(3): print(i) class MyClass: def __init__(self, name): self.name = name def greet(self): print(f"Hello, {self.name}!") Notice how the code that belongs to my_function, the if and else blocks, the for loop, and the MyClass definition is all indented. There are no curly braces used to mark the beginning or end of these blocks. Why does Python use indentation? Guido van Rossum, Python's creator, made this design choice to emphasize code readability. By making the visual structure of the code directly correspond to its logical structure, Python aims to be more human-friendly and less prone to errors caused by mismatched or misplaced braces (a common issue in languages that use them). So, in Python, you'll never see functions or other control flow structures ending with curly braces. The indentation is the key to defining code blocks. Consistent and correct indentation is crucial for Python code to run properly.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
