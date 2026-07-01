---
id: 245132
source: GPT
date: 2025-09-19
tags: ['liquidation', 'quanto-exchange', 'trade-history', 'troll-coin']
category: crypto-web3
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was trying to confirm whether he got liquidated on his Troll trade on Quanto and how to check trade history to verify what happened.
---
# Liquidation confirmation steps

### USER
If my trade for troll doesn’t show up anymore does that mean I got liquidated?

### USER
Yeah how do I check the trade history for quanto to see what happened?

### ASSISTANT
Most likely, yeah — if your **open position for Troll isn’t showing up in your exchange’s positions tab anymore**, there are a few possible reasons, but the main one is **liquidation**:  

- **Liquidated:** If the price moved against you and hit your liquidation threshold, the exchange will automatically close your position to cover losses. It usually disappears from your active positions once this happens.  
- **Manually closed:** If you accidentally closed it yourself (market or limit close), it would also disappear, but you’d see it reflected in your balance/history.  
- **Exchange glitch:** Sometimes positions temporarily don’t show up due to UI or API issues — checking your trade history tab or PnL history will confirm what happened.  

👉 Check:  
1. Your **trade history** — it’ll show whether the position was liquidated.  
2. Your **wallet balance** — if it suddenly dropped a lot, that’s a liquidation.  
3. Any **emails/notifications** from the exchange (most send a liquidation notice).  

Want me to walk you through how to confirm liquidation step-by-step depending on what platform you’re using?

### ASSISTANT
Got it — since you’re trading on **QuantoSwap (or Quanto Futures on another platform)**, here’s how you can confirm what happened to your Troll position:  

### 🔎 Step 1: Go to the “Orders” / “Trade History” Tab  
- On most exchanges (Bybit, Binance, MEXC, etc.), **“Trade History” or “Order History”** is separate from the **“Positions” tab**.  
- If you were liquidated, you won’t see it under *active positions* anymore, but it **will still show up in the history**.  

### 🔎 Step 2: Look for “Liquidation” or “Closed by System”  
- In the history, check the **Status** column.  
- Liquidated trades usually show something like:  
  - *“Liquidated”*  
  - *“ADL” (Auto-Deleveraging)*  
  - *“Closed by System”*  

### 🔎 Step 3: Check Your PnL  
- If you see a **100% loss of margin**, that means liquidation happened.  
- Example: If you put in $178 at 10x leverage, and it shows `-178 USDT` realized PnL, that confirms it.  

### 🔎 Step 4: Cross-Check Wallet Balance  
- Go to your **Futures/Derivatives Wallet** inside Quanto.  
- If your margin balance dropped sharply, it matches liquidation.  

👉 If you tell me which exchange you’re using Quanto on (Bybit? MEXC? Bitget? or something else?), I can give you the exact button clicks to check.  

Do you want me to break it down **step-by-step for your specific exchange’s interface**?
