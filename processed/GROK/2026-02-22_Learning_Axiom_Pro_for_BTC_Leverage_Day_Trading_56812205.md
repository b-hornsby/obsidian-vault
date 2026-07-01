---
source: GROK
date: 2026-02-22
category: crypto-web3
id: 56812205
linked_nodes: ['nodes/people/bryan.md']
---
# Learning Axiom Pro for BTC Leverage Day Trading

### HUMAN
working through how to use the axiom pro platform, specifically to day trade btc. i'm new to leverage trading so im trying to get a feel for everything before i start making any decisions. with that being said, i also have adhd so i dont need you to give me a long list of what everything means all at once. i'm going to ask things and i need you to level with me, break down what it is that im asking and help me have a well rounded understanding of what it is that im looking at. can you do that for me?

### ASSISTANT
**Yes, 100% — I got you.**  

We're gonna do this exactly how you want: one focused thing at a time, short and real, no walls of text. I'll break down whatever you ask, tell you why it actually matters for day-trading BTC, what the risks are (especially with leverage), and keep it super practical so it sticks.  

If something still feels fuzzy, just say “explain that like I’m 5” or “slow down” and we’ll rewind. ADHD-friendly mode activated ✅  

Quick 10-second overview so we’re on the same page (you can ignore this until you’re ready):  
Axiom Pro (the pro interface inside axiom.trade) is basically a fast, all-in-one web app for on-chain crypto. For BTC day trading with leverage, you’ll be using their **Perpetuals** tab (powered by something called Hyperliquid). It’s not like a regular exchange — you connect your own wallet, stay in control of your funds, and can go long or short BTC with 2x–40x leverage depending on the exact setup.

That’s it for now.  

**What’s the very first thing you’re staring at or wondering about right now?**  

Examples you can just copy-paste if it helps:  
- “How do I even connect my wallet?”  
- “What does the main screen look like / what are these buttons?”  
- “Explain leverage like I’m brand new — start with what 5x actually means”  
- “Show me where the BTC perpetuals are”  
- Or literally paste a description/screenshot text of whatever you’re looking at.

Fire away — I’m right here with you, one step at a time. No rush. Let’s make this feel easy. 🚀

### HUMAN
so i wrote a few things down just off what i see and the first one being how does the order book work? what exactly does it show and how is it a useful indicator?

### ASSISTANT
**Got it — order book, perfect first thing to lock in.**  

We're keeping this dead simple and visual so it clicks fast.  

### What the order book actually is  
Think of it like a live auction board for BTC right now.  
It shows **every limit order** people have placed that hasn't been filled yet — all the "I'll buy BTC at $99,200" and "I'll sell BTC at $99,400" sitting there waiting.  

In Axiom Pro (the Hyperliquid BTC perpetuals screen) it usually sits on the **right side** of the chart.  

Here’s exactly what you’re looking at in Axiom:

<grok:render card_id="b1ed85" card_type="image_card" type="render_searched_image"><argument name="image_id">eKTIP</argument><argument name="size">"LARGE"</argument></grok:render>

- **Green side (bottom half)** = **Bids** → people who want to **BUY** BTC (highest buy price at the very top)  
- **Red side (top half)** = **Asks** → people who want to **SELL** BTC (lowest sell price at the very top)  

The tiny gap between the top green and top red is called the **spread** (usually super tight on BTC here, like 0.001%).

Each line shows:  
**Price** | **Amount** (how much BTC someone is willing to buy/sell at that exact price) | **Total value**

### Why this matters for day-trading BTC with leverage  
1. **Instant liquidity check** — Big green wall = strong support (price probably bounces). Big red wall = resistance (price might stall). Thin book = price can whip around fast (dangerous with 10x+ leverage).  
2. **Slippage warning** — If you slam a big market order and the book is thin, your entry price can be way worse than you expected. (Leverage makes that hurt more.)  
3. **Order flow feel** — Watch if bids are stacking up or getting eaten — gives you a 5–10 second edge on direction before the chart even moves.  

Super short version: The order book is the **real supply & demand** happening right now, not just the last traded price on the chart.

Does that match exactly what you’re staring at on your screen?  
If you want, tell me:  
- “Show me the difference between market vs limit order using the book”  
- “What’s that ‘spread’ number doing for me?”  
- Or paste whatever the next thing on your list is.  

One step at a time, no rush — we’re building this slow and solid. 🔥

### HUMAN
what does the spread mean?

### ASSISTANT
**Spread = the tiny gap between what buyers will pay right now and what sellers will accept right now.**

That’s literally it.

In your Axiom Pro order book (the one on the right side):

- Top green line = highest **bid** (best buy price)  
- Top red line = lowest **ask** (best sell price)  

The **spread** is just the difference between those two numbers.

Right now on your screen it says **“Spread: 1 × 0.001%”**  
That means the gap is only 0.001% (super tight on BTC — normal here).

### Why it actually matters for you day-trading with leverage:
- When you hit **Market Buy** → you pay the red ask price (you “cross” the spread)  
- When you hit **Market Sell** → you get the green bid price  
- So every round-trip (buy + sell) you pay the spread twice — tiny on BTC, but with 10x–20x leverage that tiny % gets multiplied.

Example with your current ~$99,301 BTC price:  
0.001% spread = about **$1** per BTC.  
If you trade 1 BTC with 20x leverage, that $1 gap becomes like $20 of extra cost. Still small, but it adds up on scalps.

Tight spread = good, cheap to enter/exit fast.  
Spread suddenly widens = liquidity drying up → be careful slamming market orders.

That’s the whole story.

Click yet? Or want me to show what happens if you actually place a market order vs limit order with the spread? Just say the word. One thing at a time. ✅

### HUMAN
theres options for spread 100, spread 1000, etc?

### ASSISTANT
**Yes — those “spread 100, spread 1000, etc.” options are exactly what you’re seeing next to the spread number.**

It’s called **order book grouping** (or aggregation). Super simple:

### What it actually does
- **Spread 1** (what you probably have right now): Shows every tiny price level exactly as it is.  
  → Book looks busy — lots of thin lines, very precise.

- **Spread 10 / 100 / 1000**: Groups nearby prices together into bigger “buckets”.  
  Example:  
  - Spread 100 = everything within ~$100 of each other gets added up into **one single line**.  
  - Spread 1000 = even bigger chunks (~$1,000 ranges).

The actual spread % (0.001% or whatever) stays the real market gap — the number just changes **how zoomed-in or zoomed-out** the book looks.

### Why this matters for you day-trading BTC with leverage
- Low number (1 or 10) = you see micro-level detail. Good when you’re scalping tiny moves or watching exact walls.  
- Higher number (100 or 500) = cleaner screen, big green/red “walls” pop out immediately. Way less overwhelming, especially with ADHD.  
- Doesn’t change real prices or liquidity at all — just how the screen displays it.

**Pro tip for you right now**:  
Start on **spread 100** or **500**.  
It makes the book feel calm and useful instead of a wall of numbers.  
Only drop to 1 when you’re zoomed in on a specific level you care about.

Click the number (the “1” or whatever it currently says) and you’ll see the dropdown with 1 / 10 / 100 / 1000 / etc.

Click it yet? Matches what you see?  

Next thing on your list whenever you’re ready — one at a time, we’re good. ✅

### HUMAN
so in short, what is spread and why are those different options important?

### ASSISTANT
**Short & sweet:**

**Spread** = the real gap (in % or $) between the best buy price (top green) and best sell price (top red) right now.

That’s the actual cost you “pay” when you use a market order.
---
### HUMAN
and the trades section next to order book? what does that show?

### ASSISTANT
**Trades tab (right next to Order Book) = the list of what actually just got bought or sold.**

Super simple:  
While the **Order Book** shows **pending orders** (stuff people *want* to do), the **Trades** section shows **real deals that already happened** in the last few seconds/minutes.

It refreshes live and usually lists the last 50–100 trades.

### What each line shows (exactly what you’re looking at):
- **Time** → when it happened (often just “2s ago” style)  
- **Price** → at what price the trade executed  
- **Amount** → how much BTC was traded (or sometimes in USD)  
- **Color** →  
  - **Green** = aggressive **BUY** (someone hit the ask and bought right away)  
  - **Red** = aggressive **SELL** (someone hit the bid and sold right away)

That’s it — no more columns than that on Axiom Pro.

### Why this is useful for you day-trading BTC with leverage:
- Shows **real momentum** happening right now (not just wishful thinking in the order book).  
- Big green streak + price ticking up = strong buying pressure (good for quick long).  
- Sudden red wall of trades = sellers are hitting hard (watch out if you’re long with 10x+).  
- Thin trades = low conviction move → price might reverse fast (dangerous on leverage).  
- Spot “whale” prints (one huge trade) that can kick the price.

**Quick combo tip with order book:**  
If you see a big red trade but the order book still has a fat green wall underneath → price probably bounces.  
If trades are eating through the wall → it’s breaking.

Start glancing at it every 10–15 seconds when you’re watching price. It’s like the “heartbeat” of the market.

Matches exactly what’s on your screen?  
Want me to walk through “how to read a live trade sequence” with a fake example? Or jump to the next thing on your list?

One bite at a time — you’re doing great. ✅

### HUMAN
can you break down this tip If you see a big red trade but the order book still has a fat green wall underneath → price probably bounces.
If trades are eating through the wall → it’s breaking.

### ASSISTANT
**Got it — let’s break that tip down like we’re sitting side-by-side looking at your screen.**  
One scenario at a time. Super short. No fluff.

### Scenario 1: Big red trade + fat green wall still there → **price probably bounces**
- You see **one or two big red lines** pop up in the Trades tab (someone just sold hard with a market order → price dips a tiny bit).  
- But right below current price in the Order Book, the **green side** has a **thick stack** (lots of buy orders sitting there, like a big green “wall” or bar).  
- What’s actually happening: Those sellers are hitting the waiting buyers. The buyers are happily buying the dip, so the wall barely shrinks.  
- Result: Price stops falling and usually bounces back up quick (like hitting a floor).

**Real feel on your screen right now:** If a big red trade happens but the top few green lines stay almost the same size → that’s the bounce signal.

### Scenario 2: Red trades keep coming and start **eating** the green wall → **it’s breaking**
- Red trades keep showing up one after another.  
- You watch the green wall in the Order Book **shrink in real time** (the numbers on those green lines get smaller or disappear).  
- What’s happening: The buyers are getting filled up and running out of orders at that price. No more “floor”.  
- Result: Price usually drops through that level faster (breakdown).

**Quick way to watch it live:**  
Glance at the exact price level where the big green stack is → if the amount next to it is dropping fast from red trades → danger (breaking).  
If it stays thick after a red trade → chill, probably bouncing.

**Why this matters for you with leverage:**  
These two things happen in 5–30 seconds. Spotting the difference can stop you from jumping into a fake move that wipes your margin.

**Visual of a “fat green wall” (what you want to see holding strong):**  
<grok:render card_id="833201" card_type="image_card" type="render_searched_image"><argument name="image_id">5lX7a</argument><argument name="size">"LARGE"</argument></grok:render>

(The thick green area on the left is exactly the “fat green wall” we’re talking about.)

Click in your head yet?  
Want me to walk through a fake example with your current BTC price (~$99,300) so you can picture it on your exact screen?  

Or just say “next thing on my list” — we’re good either way. One bite at a time. ✅

### HUMAN
on my screen that chart youre talking about looks like this? are we talking about the bars here?

### ASSISTANT
**Yes — exactly this screen.**

That’s your real Axiom Pro Order Book (Spread 100 grouping, BTC perpetual).

### Quick map so it clicks:
- **Top half (red rows)** = people waiting to **sell** BTC (asks)  
- **Bottom half (green rows)** = people waiting to **buy** BTC (bids)  
- The little gap in the middle (around 67,500 → 67,400) = current price & spread

### The “bars” you’re asking about
Yes — those **colored green blocks/rows** at the bottom are **exactly** the “fat green wall” I was talking about.

The bigger/longer the green area (or the bigger the **Amount (USD)** and **Total (USD)** numbers), the stronger the wall.

In your screenshot right now, the fattest green wall is at **$66,900** — look:  
**24,272,511 USD** in buy orders.  
That’s a **really thick** green block compared to the ones above or below it.

### How the tip looks on YOUR screen right now:
- If you see **big red trades** popping in the Trades tab…  
  → and that big green block at 66,900 (or any other thick green one) **stays almost the same size** → buyers are eating the selling → price probably bounces up.  
- If red trades keep coming and you watch that green block **shrink fast** (the numbers get smaller in real time) → the wall is being eaten → price probably breaks lower.

That’s it. Super visual now that you’re looking at your own screen, right?

Does that match what you’re seeing?  
If yes, say “got it” or ask me to point out another specific line in your screenshot.  

Or just drop the next thing on your list — we’re flying through this. ✅

### HUMAN
so how is the order book read? how is it ordered?

### ASSISTANT
**Yes — let's lock this in with your exact screen in mind.**  

We're talking about **how to read** the order book (the whole list you pasted) and **how it's ordered** (why the prices are arranged that way).

### How the order book is ordered (the structure)
It's sorted by **price**, always:

- **Asks (sells — red rows at the top)**: Sorted from **lowest price to highest** as you go down the list.  
  → The **top red row** is the **cheapest someone is willing to sell right now** (best ask / lowest sell price).  
  → Lower rows = people asking more money to sell (worse for buyers).

- **Bids (buys — green rows at the bottom)**: Sorted from **highest price to lowest** as you go up the list.  
  → The **top green row** (just below the gap) is the **most someone is willing to pay right now** (best bid / highest buy price).  
  → Lower rows = people offering less money to buy (worse for sellers).

- The **middle gap** (spread) separates asks from bids.  
  Current price is basically right in that gap (around where last trades happened, like ~67,500–67,400 in your paste).

**Standard worldwide order book rule** (Hyperliquid / Axiom Pro follows this exactly like Binance or any perp exchange):  
Best prices are always at the **center** (top of each side).  
Worse prices fan out **away** from the center.

That's why it looks like a "V" shape pointing toward the current price — tightest liquidity near now, thinner farther away.

### How to actually read it (step-by-step on your screen)
1. **Find the center / current level** — Look for the spread gap. In your paste: between 67,500 (bottom red) and 67,400 (top green). Price is hovering around there.

2. **Best immediate prices**:
   - Want to **buy now** (long BTC)? You pay the **top red** price (lowest ask, e.g., whatever the top red is live).
   - Want to **sell now** (short BTC)? You get the **top green** price (highest bid).

3. **Depth / walls**:
   - Look down the green side → bigger **Amount (USD)** or **Total (USD)** = stronger support (potential bounce floor). Your earlier example had a fat one at 66,900 with 24M+ USD.
   - Look up the red side → bigger amounts = stronger resistance (potential ceiling).

4. **Cumulative totals** (the Total (USD) column):  
   This adds up all the liquidity from that price outward.  
   Higher total farther out = deeper book (harder to move price a lot).

5. **Grouping note** (your spread 100): Prices are bucketed in ~$100 steps, so each row represents a small range, not one exact tick. Makes it cleaner without losing the big picture.

**Quick read summary for day-trading BTC here**:
- Glance at **top 3–5 rows** on each side first — that's where action happens fastest.
- Thick green near center = buyers defending → likely hold or bounce.
- Thick red near center = sellers capping → likely reject higher prices.
- If price moves toward a side and the wall shrinks fast (from trades eating it) → breakout/breakdown likely.

Does this click with how your list is lined up?  
The ordering is price-based, best-in-the-middle, always has been on every order book like this.

Got it, or want me to zoom in on one specific part of your pasted list (like why 67,200 has that big green highlight)?  

Or next on the list — fire away. We're nailing this one piece at a time. ✅

### HUMAN
So, the market book, like the order book, I mean, that's the thing that's kinda like overwhelming here. I need to know, like, what it is that I'm looking, like, obviously I see that, like, okay, the top one is like the, the absolute lowest that somebody's trying to sell, and the top buy is the one that, like, the lowest that they're trying to buy for, but I don't, I don't get it. It's, it's a lot.

### ASSISTANT
Yeah, I hear you — the order book can totally feel like a firehose of numbers at first. Let me break it down super clear, like we’re just staring at it together and I’m pointing at stuff. No overload. **What you already nailed:** - The **top red row** (asks) = lowest price someone’s willing to sell BTC at right now. That’s the best price to buy if you want in fast. - The **top green row** (bids) = highest price someone’s willing to pay for BTC. That’s what you get if you sell right now. You’re spot-on there. **Why it
