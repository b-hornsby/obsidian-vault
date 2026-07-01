---
category: coding
date: 2025-04-29
id: 165119
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- murad_market_tracker
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered an IndentationError while running a Python script for
  a market tracker project and was seeking help to resolve the issue.
tags:
- python
- indentation-error
- debugging
- syntax-error
- script-execution
---
# PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 34
    if sol_data:
IndentationError: unexpected indent
PS C:\Users\Bryan>

### USER
PS C:\Users\Bryan> & C:/Users/Bryan/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Bryan/Desktop/Phython Projects/murad_market_tracker/main.py"
  File "c:\Users\Bryan\Desktop\Phython Projects\murad_market_tracker\main.py", line 34
    if sol_data:
IndentationError: unexpected indent
PS C:\Users\Bryan>

### GEMINI
Aha, the infamous IndentationError! Python is very sensitive to indentation, as it uses it to define code blocks. This error on line 34: if sol_data: means that this line has an unexpected extra level of indentation. It looks like it's indented one level too far to the right. To fix this, you need to dedent that line so it aligns with the code around it. Here's the corrected section: coins = { "solana": "solana", "spx6900": "spx6900", "gigachad": "gigachad-2", "mog": "mog-coin", "apu": "apu-apustaja", "popcat": "popcat", "harrypotter": "harrypotterobamasonic10inu-eth", "retardio": "retardio", "lockin": "lock-in", "mini": "mini", "usa": "american-coin" } sol_data = get_coin_data("solana") if sol_data: sol_change = sol_data['change_24h'] results = [] for key, coin_id in coins.items(): if coin_id == "solana": continue coin_data = get_coin_data(coin_id) if coin_data: outperforming = "✅" if coin_data["change_24h"] > sol_change else "❌" results.append([ coin_data["name"], coin_data["symbol"], f"${coin_data['market_cap']:,.0f}", f"{coin_data['change_24h']:.2f}%", outperforming ]) headers = ["Name", "Symbol", "Market Cap", "24h Change", "Outperforming SOL"] print(tabulate(results, headers=headers, tablefmt="fancy_grid")) print(f"{name.upper()} ({symbol.upper()})") print(f"Price: ${price:,.2f}") print(f"Market Cap: ${market_cap:,.0f}") if change_24h is not None: indicator = "🟢" if change_24h >= 0 else "🔴" print(f"24h Change: {change_24h:.2f}% {indicator}") else: print("24h change: data not available ⚠️") Notice that I've moved if sol_data: one level to the left. Make sure the lines within that if block are indented correctly relative to it. Keep going, you're doing great at identifying these errors from the traceback! Let me know what happens after this fix. 😊