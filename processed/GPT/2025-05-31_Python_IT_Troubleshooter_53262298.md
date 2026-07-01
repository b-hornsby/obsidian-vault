---
id: 338307
source: GPT
date: 2025-05-31
tags: ['python', 'chatbot', 'it-troubleshooting', 'beginner-project']
category: coding
sentiment: building
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan was building a Python-based IT troubleshooting chatbot as a portfolio project and shared his initial code for the intro function.
---
# Python IT Troubleshooter

### ASSISTANT
Great start! You already have a clean intro with options and routing to different functions based on user input.

### To keep it manageable, let’s start by defining one of the help functions — say, `wifi_help()` — with a couple of questions and tips. Then we’ll build the others similarly.

Want me to help build the others? Or would you like me to help with input validation and looping next?

### ASSISTANT
Got it! Send over your current code whenever you’re ready, and we’ll pick up from there to build the next steps together. Looking forward to it!

### USER
🎯 Project Goal:

    Build a simple Python chatbot that helps users troubleshoot common IT problems (like slow computers, Wi-Fi issues, etc.) through a series of questions.

We'll do this using:

    Python functions (to organize each help topic)

    Conditional logic (if/else)

    User input (input() function)

    Basic print statements for interaction

### ASSISTANT
Great! Let’s build a simple Python chatbot step-by-step that helps users troubleshoot common IT problems. We’ll keep it simple and organized, using functions for each help topic, conditional logic to guide the flow, and user input to interact.

### Step 2: Write functions for each topic

Each function will ask some questions and give troubleshooting tips based on user answers.

### Here’s the full code with explanations inline:

```python
def troubleshoot_slow_computer():
    print("\nTroubleshooting Slow Computer...")
    response = input("Is your computer slow when starting up? (yes/no): ").lower()
    if response == "yes":
        print("Try disabling startup programs you don't need and run a virus scan.")
    else:
        response = input("Is your computer slow when running multiple programs? (yes/no): ").lower()
        if response == "yes":
            print("Try closing unused programs and consider upgrading your RAM.")
        else:
            print("Try restarting your computer or check for system updates.")

def troubleshoot_wifi():
    print("\nTroubleshooting Wi-Fi Issues...")
    response = input("Are you unable to connect to Wi-Fi? (yes/no): ").lower()
    if response == "yes":
        print("Try restarting your router and make sure the Wi-Fi password is correct.")
    else:
        response = input("Is your Wi-Fi connection slow? (yes/no): ").lower()
        if response == "yes":
            print("Try moving closer to the router or disconnect devices that use bandwidth.")
        else:
            print("Try resetting your network settings or contact your ISP.")

def troubleshoot_printer():
    print("\nTroubleshooting Printer Problems...")
    response = input("Is the printer not turning on? (yes/no): ").lower()
    if response == "yes":
        print("Check the power cable and power source. Make sure it's plugged in securely.")
    else:
        response = input("Is the printer not printing? (yes/no): ").lower()
        if response == "yes":
            print("Check if there is paper and ink, and ensure the printer is set as default.")
        else:
            print("Try restarting the printer and your computer.")

def chatbot():
    print("Welcome to IT Help Chatbot!")
    while True:
        print("\nWhat issue can I help you with?")
        print("1. Slow Computer")
        print("2. Wi-Fi Issues")
        print("3. Printer Problems")
        print("4. Exit")
        
        choice = input("Please enter the number of your choice: ").strip()
        
        if choice == "1":
            troubleshoot_slow_computer()
        elif choice == "2":
            troubleshoot_wifi()
        elif choice == "3":
            troubleshoot_printer()
        elif choice == "4":
            print("Thanks for using the IT Help Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    chatbot()
```

Want me to explain any part in more detail or add features like input validation or more topics?

### USER
no i was just explaining what we're working on. ill send my current code over and we'll work on building the next steps to build this project for real

### USER
def intro():
    print("welcome to my Self Service Troubleshooting Bot!")
    print("I'll help you fix common tech issues step by step")
    print("What problem are you experiencing?")
    print("1. I can't connect to Wifi")
    print("2. My pc is running super slow")
    print("3. It wont let me print")
    print("4. I can't hear sound")
    print("5. My screen is blank")

    choice = input("Please enter the option best associated with your issue")

    if choice == '1': 
        wifi_help()
    elif choice == '2':
        slow_computer()
    elif choice == '3':
        printer_help()
    elif choice == '4':
        sound_help()
    elif choice == '5':
        screen_help()
    else:
        print("Sorry, I didn't understand that. Please restart the tool and enter the option best associated with your issue")

intro()