---
category: coding
date: 2025-04-23
id: 557476
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- solana_logger
resolution: unresolved
sentiment: curious
source: GEMINI
summary: The user encountered an AttributeError while trying to write to a CSV file
  in their Solana price tracker project, specifically using `csv.write(file)` instead
  of `csv.writer(file)`, indicating a typo in the csv module usage.
tags:
- python
- csv-module-error
- solana-price-tracker
- debugging
- attribute-error
---
# PS C:\Users\Bryan\Desktop\Phython Projects\solana_logger> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/solana_logger/tracker.py"
Traceback (most recent call last):
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 19, in <module>
    log_price(price)
    ~~~~~~~~~^^^^^^^
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 13, in log_price
    writer = csv.write(file)
             ^^^^^^^^^
AttributeError: module 'csv' has no attribute 'write'. Did you mean: 'writer'?

### USER
PS C:\Users\Bryan\Desktop\Phython Projects\solana_logger> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/solana_logger/tracker.py"
Traceback (most recent call last):
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 19, in <module>
    log_price(price)
    ~~~~~~~~~^^^^^^^
  File "c:\Users\Bryan\Desktop\Phython Projects\solana_logger\tracker.py", line 13, in log_price
    writer = csv.write(file)
             ^^^^^^^^^
AttributeError: module 'csv' has no attribute 'write'. Did you mean: 'writer'?

### GEMINI
It seems like the error message is exactly the same as the previous one. This suggests that the last correction I provided might not have been saved or executed. Could you please double-check your tracker.py file to ensure that the log_price function now looks like this: def log_price(price): with open("sol_price_log.csv", mode="a", newline="") as file: writer = csv.writer(file) writer.writerow([datetime.now(), price]) Specifically, make sure that you've changed csv.write(file) to csv.writer(file). After you've confirmed the change, please try running the script again. If you still get the same error, there might be an issue with how the file is being saved or how the Python interpreter is picking up the changes. Let me know what you find! We'll get to the bottom of this.

### GEMINI
You're absolutely right! My apologies for that slip-up in the previous correction. The error message is spot on: the csv module doesn't have a function called write. The correct function to create a writer object is indeed csv.writer(). Let's fix the log_price function again: def log_price(price): with open("sol_price_log.csv", mode="a", newline="") as file: writer = csv.writer(file) writer.writerow([datetime.now(), price]) Correction: Changed csv.write(file) to csv.writer(file). Thanks for catching that! It's easy to make small mistakes like that when you're focused on the logic. This correction should get you past this AttributeError. Give it a run now!