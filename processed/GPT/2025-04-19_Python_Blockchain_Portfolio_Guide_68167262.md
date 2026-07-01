---
source: GPT
date: 2025-04-19
category: homelab
id: 68167262
linked_nodes: ['nodes/people/bryan.md']
---
# Python Blockchain Portfolio Guide

### ASSISTANT
Got you — let’s troubleshoot and get `requests` working in VS Code. This is super common for first-time setups, so you're not alone.

### ✅ Quick Fixes Based on Common Issues:

#### ✅ 2. Check which Python version VS Code is using

- Look in the **bottom-left or bottom-right** corner of VS Code.
- You should see something like: `Python 3.x.x (path/to/python)`
- Click it and choose the correct interpreter:
  - Usually it’s something like: `Python 3.x.x` or `python.exe`

This tells VS Code to use the right Python version (the one where `requests` is installed).

### 🔄 Final Test:

After doing the above, run this in the terminal:

```bash
python
```

Then type:

```python
import requests
```

If no error shows up, you’re good!

## 🛠️ Project 1: Crypto Price Tracker (CLI Tool)

### 🔧 Step 1: Install Python (if you haven't yet)

1. Go to [https://www.python.org/downloads](https://www.python.org/downloads)
2. Download and install the latest version (Windows, Mac, Linux — pick yours).
3. **IMPORTANT:** During install, make sure to check **"Add Python to PATH"**.

✅ Once installed, open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```bash
python --version
```

You should see something like:
```bash
Python 3.x.x
```

Let me know if that’s working, then we’ll move to writing your first code. Want me to wait while you install it, or are you good to go?

### USER
yes please

### ASSISTANT
Absolutely, I’ve got you. Since you’re starting from zero but want to end up in a solid place like a **Blockchain Data Analyst**, we’ll start small, build real projects, and make sure every step is clear. I’ll keep things bite-sized, practical, and explain what we’re doing and why it matters.

#### ✅ **Phase 1: Python Basics Through Real Use**
**Goal**: Get fluent with Python essentials by building small, focused projects.

##### 🛠️ Project 1: *Crypto Price Tracker (CLI Tool)*
**What it does**: Pulls the latest prices of Bitcoin, Ethereum, etc., and shows them in your terminal.

**Why it matters**: Teaches you:
- Basic syntax
- Working with APIs
- Printing & formatting data
- Running a script

#### ✅ **Phase 3: Blockchain Data Exploration**
**Goal**: Work with actual on-chain data.

##### 🛠️ Project 3: *Ethereum Wallet Tracker*
**What it does**: Enter a wallet address and it shows balance, recent transactions, and token holdings.

**Why it matters**:
- Learn how to use web3.py or Etherscan APIs
- Interact with smart contracts
- Parse JSON and blockchain data

### 🛣️ How We'll Do This:
For each project, I’ll give you:
- A *beginner-friendly explanation*
- The *goal* and *learning outcomes*
- A *step-by-step guide* (with no jargon)
- *Mini challenges* to help lock it in

## 🧰 Full Python Setup with a Text Editor (VS Code)

### ✅ Step 2: Install VS Code (Your Text Editor)

1. Go to: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download and install VS Code for your operating system.

### ✅ Step 4: Create Your First Project Folder

1. On your computer, create a folder anywhere you like — for example:
   ```
   Documents/PythonProjects/crypto-tracker
   ```
2. Open **VS Code**, then go to:
   ```
   File > Open Folder > Select the folder you just made
   ```

### ✅ Step 6: Run Python in VS Code

Inside your `tracker.py` file, type this to test your setup:

```python
print("Hello from Python!")
```

To run it:
1. Right-click anywhere in the file
2. Click **"Run Python File in Terminal"**

You should see:
```
Hello from Python!
```

## 🚀 Crypto Price Tracker (Beginner Project)

### ✅ Step 1: Install Required Python Package

We’ll use a library called `requests` to fetch data from a crypto API.

In your VS Code **terminal**, type:

```bash
pip install requests
```

This installs the `requests` package, which lets Python talk to websites.

### ✅ Step 3: Run Your Script

Right-click anywhere in the `tracker.py` file and select:

**➡️ Run Python File in Terminal**

You should see output like:

```
💰 Bitcoin: $64052
🪙 Ethereum: $3171
```

### 💡 Mini Challenge (Optional):
Try adding another crypto — like `dogecoin` — to the URL.

Hint: Update the URL like this:

```python
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd"
```

Then grab the price with:
```python
doge_price = data["dogecoin"]["usd"]
print(f"🐶 Dogecoin: ${doge_price}")
```

### 🏆 **Top Pick: VS Code (Visual Studio Code)**  
- ✅ **Most popular among Python developers**
- ✅ Tons of extensions (Python, Jupyter, GitHub, etc.)
- ✅ Free, lightweight, customizable
- ✅ Excellent for both beginners and pros  
- ✅ Works great with data science, blockchain dev, and web3 tools

🔧 Ideal for:
- Python scripting
- Jupyter notebooks
- Smart contract dev (with extensions like Solidity and web3 tools)

### 🧑‍💻 What Most Professionals Use Today:
- **VS Code** for almost everything — code, data analysis, smart contracts, scripts, even markdown docs.
- **Jupyter Notebooks** when doing exploratory data work or working with Pandas.
- **PyCharm** if they want a dedicated IDE and are deep into Python.
---
### 🔥 Verdict for You:
Since you're just starting out, **VS Code is the best choice**:
- It's easy to use
- You’ll grow into it as your skills improve
- Works great for both scripting and data work

Want to keep going with the tracker project now? We’re just about to write your first real Python code.