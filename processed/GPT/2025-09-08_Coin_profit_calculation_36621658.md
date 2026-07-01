---
id: 213067
source: GPT
date: 2025-09-08
tags: ['quanto-exchange', 'pnl', 'coin-profit', 'troll-coin', 'withdrawal']
category: crypto-web3
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was trying to understand how his Troll coin count increased from 999 to 1500, why PnL showed a loss despite more coins, and how withdrawals work on Quanto.
---
# Coin profit calculation

### ASSISTANT
Ah, this is a **classic “paper PnL vs. coin amount” situation**—it can definitely be confusing. Let’s break it down clearly.  

1. **Coin balance vs. PnL (Profit & Loss)**  
   - Your **coin balance** (1500 troll coins) reflects **how many coins your position is currently worth** at the platform’s latest price.  
   - Your **PnL** shows **profit or loss in USD (or another reference currency) relative to your entry price**, not just coin count.  

2. **Why PnL can show “down” even if coins went up**  
   - If the **coin price in USD dropped** slightly after a recent high, your coin count might still be higher due to leverage and your entry point, but the PnL (in USD) might appear negative temporarily.  
   - Platforms often **update PnL in real time**, but it can lag slightly or fluctuate faster than your visible coin balance.  

3. **Other factors**  
   - **Funding fees or interest** for leverage positions can temporarily reduce PnL.  
   - **Price feed differences**: Some platforms calculate PnL using slightly different exchange rates than the one showing in your wallet.  

✅ **Bottom line:** Your coin count is what matters if you plan to withdraw or swap. PnL is just a real-time “snapshot” in terms of USD and can fluctuate independently.  

If you want, I can **show a concrete example with numbers** to illustrate how your PnL can go down even when your coins go up. Do you want me to do that?

### ASSISTANT
Got it! Let’s break it down carefully:  

1. **Starting coins:** 999 troll coins.  
2. **Current coins:** 1500 troll coins.  

This means your **profit** in coins is:  

\[
1500 - 999 = 501 \text{ troll coins}
\]

So you’ve made **501 coins in profit** so far.  

If you want, I can also explain **what that means in USD or in terms of leverage/profit percentage**, depending on whether you’re still holding or thinking of closing the position. Do you want me to do that?

### USER
Okay so I started off with 999 coins and so far I have 1500 troll coins

### USER
Yes please

### USER
How often does the PnL thing update? It says I’m down in PnL but my coinage went up

### ASSISTANT
Perfect, let’s clarify what this means while you’re still holding.  

1. **Your position is still open.**  
   - That 1500 coins includes both your **original 999 coins** and the **profit you’ve earned so far** (501 coins).  
   - These are *not “extra” coins yet*—they are part of your open position’s current value.  

2. **Leverage effect (if you used 10x like before):**  
   - Leverage magnifies gains and losses. A 10x leverage means a 1% move in the underlying coin’s price changes your position by 10%.  
   - The fact that you’re at 1500 coins means the underlying price movement has worked in your favor since you opened the trade.  

3. **Liquidation risk:**  
   - As long as the price doesn’t drop too far (toward your liquidation price), your position remains open.  
   - If it hits the liquidation price, the platform will close your position automatically, and you’d lose some or all of the coins you put up as collateral.  

4. **Closing the trade:**  
   - Only when you **close the position** do those 1500 coins become “real” in your wallet.  
   - At that point, you can withdraw or swap them.  

**In short:** You’ve made significant gains so far, but it’s paper profit until you close the trade. The 1500 coins is just your position’s current value.  

If you want, I can **estimate your current USD profit and potential risk** based on the 1500 coins. Do you want me to do that?

### ASSISTANT
Exactly! ✅  

- **Coin count:** Shows how many coins you actually own in your open position.  
- **Total value (coins × current price):** Shows what those coins are worth right now.  
- **PnL:** Just a real-time snapshot of profit or loss in USD (or reference currency), which can fluctuate independently of your actual coin count due to small price changes, funding fees, or leverage mechanics.  

So for a live position: **watch your coins and their total value**. PnL is more like a “mood indicator” than a true reflection of your holdings.  

If you want, I can also explain **why your coin count can exceed your original coins even if the price hasn’t gone crazy**—it’s a bit unintuitive but makes sense once you see the math. Do you want me to?

### USER
I still hold wondering what this means

### USER
So basically look at coin count and what your total is worth and not so much the PnL

### ASSISTANT
Ah, now we’re getting to the juicy part: this is **why leveraged trading (or Quanto-style trading) can make your coin count increase**, unlike normal spot trading. Let’s break it down carefully.  

### 2. How Quanto does it (simplified)
- You put in **999 troll coins** as collateral.  
- You open a **10x leveraged long**.  
- The platform calculates your **profit in real time** and **adds it to your position as “virtual coins”**, so your coin count grows.  

Example:  
- Entry: 999 coins.  
- Profit so far: 501 coins worth.  
- Displayed coin count: 999 + 501 = 1500 coins.  

💡 In reality, you didn’t “magically get more coins” in the network—this is **paper coins in your position** that represent your profit. Once you close the trade, you can **withdraw or swap the total 1500 coins**.  

If you want, I can make a **tiny visual example showing how 999 coins can become 1500 coins under 10x leverage**, step by step, so it’s super easy to see. Do you want me to do that?

### ASSISTANT
Perfect—let’s do a **step-by-step example** to make this crystal clear. We’ll use simple numbers:  

### 2. Price moves up:
- Coin price rises to **$0.22**.  
- Your **position in coins is leveraged**, say 10x, so the **coin count can grow on the platform**.  
- Let’s say this increases your “coins” to **1500 troll coins** (what you currently see).  

- Value in USD now:

\[
1500 \times 0.22 = 330 \text{ USD (paper value)}
\]

- At this moment, PnL should be **positive**, around:

\[
330 - 177.8 \approx +152.2 USD
\]

### 4. Key takeaway:
- **Coin count** can go up due to leverage mechanics and margin adjustments.  
- **PnL in USD** can fluctuate based on **current coin price**, **funding fees**, or slight price feed differences.  
- This is why you might see “down” in PnL while your **coin count seems higher than your starting amount**.  

### 1. Your position is still open
- Right now, the **1500 troll coins** is the platform’s way of showing your **current position including unrealized profit**.  
- It’s like a “paper coin count.”  

### 2. When you close the trade
- Closing the position converts your leveraged/virtual coins into **real coins in your wallet**.  
- Example: If the coin price hasn’t dropped significantly and your position is 1500 coins at closing → you can **withdraw all 1500 coins**.  
- If the coin price drops slightly before closing → the coin count might be a bit lower, because your unrealized profit shrinks.  

### 3. Key point
- **You only “lock in” your total coins when you close the trade.**  
- Until then, the coin count can fluctuate with price and platform calculations.  

✅ So basically: yes, you *can* have 1500 coins, but it’s not guaranteed until you actually close the position.  

I can also explain **the easiest way to safely lock in your profits without risking a big dip** if you want. Do you want me to?

### USER
So when I withdrawal I’ll really have that many coins?

### USER
And how did my coins increase? Normally when you spot trade they just stay the same as whatever it was when you bought them