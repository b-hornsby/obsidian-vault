---
source: GPT
date: 2025-06-02
category: crypto-web3
id: 81614546
linked_nodes: ['nodes/people/bryan.md']
---
# Shorting Explained in Leverage

### ASSISTANT
Absolutely — let’s break it down **step-by-step** with a **realistic example**, using ox.fun to **set up a short position**.

## 🔁 What you're about to do:

You're going to open a **$1,000 short** position on ETH using only **$100** of your actual funds. You're betting ETH will go **down**, so you can profit from the price drop.

### 🧪 2. **Select Your Market**
- Click the dropdown next to the chart
- Choose **ETH-USD**

### ⚙️ 4. **Choose Your Leverage**
- You’ll see a slider or box to choose leverage
- Set it to **10x**
> This means for every $1 you put up, you’re controlling $10 worth of ETH.

### ⏱️ 6. **Choose Order Type**
You can pick:
- **Market Order** (Executes immediately at the current price)
- **Limit Order** (Executes only if ETH hits your chosen price)

> For this example, we’ll keep it simple: **Market Order**

### 📊 8. **Watch the PnL (Profit & Loss)**
- If ETH drops to **$2,900**, you’ve made ~$100 = 100% gain.
- If ETH rises to **$3,100**, you’ve **lost** $100 and are **liquidated**.

🔺 Use the platform’s **Take Profit** and **Stop Loss** options to automatically close positions at your targets.

### ⚠️ What If Price Went Up Instead?

- If ETH goes **up to $3,100**, your $1,000 position is now worth $1,033.
- You’ve **lost your $100 margin** and get **liquidated**.

Would you like me to walk you through an example with a **limit order**, or explain **liquidation price math** next?

### USER
Can you break it down more for me? Like give me an example and walk me through how to set up a short on that platform

### ASSISTANT
Ahhh — got it! You're asking:

> **“How do I actually secure the profits when shorting on ox.fun?”**

Totally fair — this part can feel abstract because **you don’t “buy back” anything manually.** ox.fun handles it under the hood. Let’s go through it in the context of **how ox.fun works** — step-by-step.

## ✅ How to *Secure* or *Take* Profit on ox.fun:

### 📍 Step 1: **Monitor Your Position**

Once you’ve opened a short, your trade shows up in the **"Open Positions"** panel below the chart.

Here you’ll see:
- Entry price
- Current price
- Unrealized PnL (profit & loss)
- Liquidation price

If the price is dropping and you’re short — your **unrealized PnL turns green**. That’s your floating profit.

### 📍 Optional: **Set a Take-Profit Target (Auto-close)**

To avoid watching the screen constantly:

1. Click the settings or "TP/SL" (Take Profit / Stop Loss) on your open position
2. Enter a **Take Profit price**  
   - For example, if ETH is $3,000 and you want to exit when it hits $2,900, set TP = $2,900
3. ox.fun will automatically **close your position** when price hits that level and **lock in your profit**.

## 💡 Quick Summary:

| Action                  | What it Does                                                 |
|
---
-
---
-
---
-
---
-
---
-
---
---|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
---|
| "Open Short"             | Sells ETH at high price (opens position betting price drops) |
| Price drops              | Unrealized profit increases                                   |
| "Close" Position         | Buys ETH back at lower price (automatically)                 |
| Profit is Secured        | ox.fun credits your wallet with the PnL                      |
| Optional: TP/SL          | Auto-closes trade at set prices                              |

Want me to walk you through **a simulated example** from opening to closing with screenshots or visuals? I can also explain **how to calculate and set TP/SL** based on your short’s entry and leverage.

### ASSISTANT
Exactly! ✅ You’ve *got it*!  
Let me just reword and reinforce it so it’s rock solid for you:

## 🔍 So yes — here's how it really works on ox.fun:

1. **You open a short position** (e.g., $1,000 short on ETH at $3,000)

2. If ETH drops (say to $2,900), your position shows a green **unrealized profit**

3. You have 2 options:
   - 🔘 **Manual**: Watch the chart, and **click “Close”** when you're happy with the profit  
   - 🎯 **Automatic**: Set a **Take Profit (TP)** at $2,900 and ox.fun will **close the position for you** when the price hits it

4. When the position is closed, ox.fun **does all the backend stuff** — it credits your PnL and settles everything automatically

## ✅ TL;DR Recap:

| Concept                     | What You Do                                                  |
|
---
-
---
-
---
-
---
-
---
-
---
-
---
--|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
|
| Shorting                    | You’re betting the price will go **down**                    |
| Making profit               | Happens **as the price drops** while your short is open      |
| Securing profit             | You **must close** the trade manually or with **Take Profit** |
| Selling actual coins?       | ❌ Nope — you don’t sell your own coins                       |
| ox.fun handles everything   | ✅ Automatically does borrowing/selling/buying logic for you   |

## 🧠 Key Idea:  
> When you **short**, you’re selling something now at a **higher price**, expecting to **buy it back later at a lower price**.  
> The difference between those prices = **your profit**.

### 📉 What happens behind the scenes:

1. **You "sell" $1,000 worth of ETH at $3,000.**
   - That’s **~0.3333 ETH** you’ve sold (1,000 ÷ 3,000).

2. ETH drops to **$2,900**.

3. Now you **"buy back" that same 0.3333 ETH** — but this time at $2,900.

4. What does that cost you?  
   - 0.3333 ETH × $2,900 = **$966.67**

## 🧮 Profit Formula (for shorting):

```text
Profit = (Entry Price – Exit Price) × Position Size ÷ Entry Price
```

### Using our numbers:

```text
Profit = ($3,000 – $2,900) × $1,000 ÷ $3,000
       = $100 × 0.3333
       = $33.33
```

## 🔁 Quick Analogy:

> Think of it like selling something you borrowed — like a used PS5 — for $500 now, expecting the price to drop. If you can buy it back later for $400, you made $100 profit.  
> But if the price goes up and it costs $600 to replace, you’re out $100.

## ⚖️ What’s a **Reasonable Leverage** on ox.fun?

> A reasonable leverage is **between 1x–5x** for most responsible traders.

That’s the sweet spot where:
- You get some **amplification of profit**
- But you’re **not one small move away from liquidation**

## 🧠 Why Lower Leverage = Smarter Starting Point:

1. **More breathing room** — you won’t get liquidated on small market moves
2. **Easier learning** — lets you build muscle memory without getting punished instantly
3. **Better for swing trading** — lets you hold positions overnight or during volatility

## ✅ Safe Beginner Strategy

If you’re just getting comfortable:

> Start with **3x–5x**, use small size (like $10–$50 per trade), and always set **stop-losses and take-profits**.

You can scale up later when you:
- Get faster at entries/exits
- Understand price action better
- Get comfortable managing risk

## 💬 TL;DR:

- Use **3x–5x leverage** if you want to trade responsibly
- Avoid 10x+ unless you’re scalping or using strict stops
- Set Take Profit and Stop Loss every time
- Trade small while you’re learning — think survival > moonshot

### 🔁 First, a quick recap: What is leverage trading?

Leverage allows you to **trade with more than you actually have**.

- If you have $100 and use **10x leverage**, you can open a **$1,000 position**.
- This magnifies **profits and losses**.

## 📉 Now, SHORTING: Betting the price will go **down**

### 🧠 Simple Concept:
> When you short, you're **borrowing an asset and selling it now**, expecting to **buy it back cheaper later** and **keep the difference**.

### 🧾 Example: Shorting ETH with 10x leverage

You have **$100** in your wallet.

1. **Open a 10x short on ETH at $3,000**, size: $1,000 (you’re risking $100).
2. ETH drops to **$2,900**.
3. You **profit $100** (3.33% move × 10x = 33.3% gain on your $100).

✅ You just made **+100%** return on your $100.

### 🔍 How to Short on ox.fun (Step-by-step)

1. **Connect wallet** (usually via MetaMask or Phantom).
2. Select the **trading pair** (e.g., ETH/USD).
3. Click **"Short"**.
4. Choose your **leverage** (1x–50x).
   - Higher leverage = higher risk/reward.
5. Set **order type**:
   - **Market order**: Enter immediately at current price.
   - **Limit order**: Enter at your chosen price.
6. Set **size** — this is the total position size, not how much you’re risking.
7. Confirm and submit the trade.
8. Watch the **unrealized PnL (profit/loss)** — if it goes against you too far, you may get liquidated.

### 🛡️ Risk Tips

- Always know your **liquidation price**.
- Use **stop-losses** and **take-profits**.
- Don’t go too high on leverage unless you’re scalping or managing risk tightly.
- Start small to build confidence.
---
### USER
What is a reasonable leverage to borrow on ox.fun to trade responsibly?

### USER
So how does the profit happen when shorting? I understand you open the order but I don’t get the profit part