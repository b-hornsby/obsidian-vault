---
category: coding
date: 2025-04-21
id: 312331
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan was progressing through a Python lesson and wanted to know what topic
  to learn next.
tags:
- python-learning
- beginner-progression
- programming-tutorial
---
# Yeah so far so good what’s next?

### USER
Yeah so far so good what’s next?

### GEMINI
Fantastic! I'm glad you're finding it easy to follow. Let's dive into the concept of variables. Variables: Giving Names to Values Think of a variable as a container or a labeled box where you can store a value. Instead of having to remember the actual value every time you want to use it, you can just refer to the label (the variable name). Creating Variables (Assignment) In Python, you create a variable and assign a value to it using the equals sign (=). The general form is: variable_name = value Let's try some examples in the Python interpreter: age = 30 name = "Alice" pi = 3.14159 is_student = False In these lines of code, we've created four variables: age now holds the integer value 30. name now holds the string value "Alice". pi now holds the floating-point value 3.14159. is_student now holds the boolean value False. Notice that when you type these lines into the interpreter and press Enter, nothing seems to happen. That's because Python has stored these values in the variables in its memory. To see the values, you can simply type the variable name and press Enter: age You should see 30. name You should see 'Alice'. pi You should see 3.14159. is_student You should see False. You can also use the print() function to display the value of a variable: print(age) print(name) print(pi) print(is_student) This will print each value on a separate line. Using Variables in Calculations The real power of variables comes when you start using them in operations: year_born = 1995 current_year = 2025 my_age = current_year - year_born print(my_age) Here, we stored the birth year and the current year in variables. Then, we calculated the age by subtracting year_born from current_year and stored the result in a new variable called my_age. Finally, we printed the value of my_age, which should be 30. radius = 5 area = 3.14159 * radius ** 2 print(area) In this example, we used the variable radius in a calculation to find the area of a circle. Rules for Naming Variables When you choose names for your variables, there are a few rules you need to follow: Must start with a letter or an underscore (_). They cannot start with a number. my_variable (valid) _count (valid) variable1 (valid) 1st_variable (invalid) Can contain letters, numbers, and underscores. Spaces are not allowed. user_name (valid) total_count (valid) user name (invalid - contains a space) Variable names are case-sensitive. This means that myVariable and myvariable are treated as two different variables. Avoid using Python's reserved keywords. These are special words that have a specific meaning in Python (like print, if, for, etc.). You'll learn more about these later. Good Variable Names While the rules above dictate what's allowed, it's also important to choose good, descriptive variable names. This makes your code easier to read and understand. For example, using age is much clearer than using a, and user_name is better than un. Let's Practice! Try creating a few variables yourself in the Python interpreter: Create a variable named city and assign it the string value "Akron". Create a variable named temperature and assign it a floating-point value like 72.5. Create a variable named is_raining and assign it a boolean value. Perform a calculation using these variables (even a simple one like printing them with a message). Once you've done that, let me know, and we'll move on to the next fundamental concept: data structures, which allow you to work with collections of data. How does that sound?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
