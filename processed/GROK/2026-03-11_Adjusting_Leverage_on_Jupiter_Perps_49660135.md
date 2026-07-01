---
category: crypto-web3
date: 2026-03-11
id: 034902
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GROK
summary: Bryan was trying to restore his 10x leverage on a Jupiter Perps position
  after adding more collateral caused it to drop to 4.97x.
tags:
- jupiter-perps
- leverage-adjustment
- collateral-management
- position-management
---
# Adjusting Leverage on Jupiter Perps

### HUMAN
I had a $10 10x perp position placed and I decided to add $10 more to it making my position worth $20 of my own money. When I did that my 10x leverage went down to 4.97 and I want to fix it so it’s back to the original 10x. I’m currently using jup perps on desktop

### ASSISTANT
On Jupiter Perps (jup.ag/perps or the perps section on desktop), adding collateral to an existing position (what you did by adding another $10) increases your total margin without changing the position size. This **decreases** your effective leverage because leverage = position size / your total collateral.

In your case:
- Original: $10 collateral at 10x leverage → position size of ~$100 notional.
- After adding $10 more collateral: $20 total collateral → same ~$100 position size → leverage drops to ~5x (close to your 4.97x, minor difference likely from fees, funding, or rounding).

Jupiter Perps combines positions in the same direction (e.g., both long) into one averaged position, and the leverage shown is the blended/average leverage across the collateral used.

To get back to (or closer to) 10x leverage without closing the position entirely, you need to **increase the position size** relative to your current collateral. This effectively ramps up the leverage again.

Here's how to do it on the desktop interface:

1. Go to your open positions list (usually at the bottom or in the positions tab on the perps dashboard).
2. Find your position and click the **Edit** button (or pencil icon) next to it — this opens the position management panel.
3. Look for options like **Increase Size**, **Add to Position**, or the **Leverage Slider** in the adjustment view.
   - Use the leverage slider or input to target higher leverage (e.g., slide toward 10x or enter it manually).
   - This will calculate how much additional collateral (or borrow) is needed to increase the notional position size accordingly.
   - Review the preview: It should show the projected new position size, updated leverage, new liquidation price, etc.
4. Confirm the transaction in your wallet (it'll be a small Solana tx).

If the interface shows a **Multiply** tab or section in the position editor (mentioned in some Jupiter docs for increasing leverage), use that — adjust the slider to your target (like 10x), review the changes, and execute.

Note:
- Increasing leverage this way makes your liquidation price worse (closer to current price), so higher risk — make sure the market direction supports it.
- If the slider maxes out below 10x, it could be due to current market conditions, utilization, or position size limits (though SOL/ETH/wBTC go up to 250x normally).
- Withdrawing collateral would increase leverage further (but you just added, so that's the opposite of what you want right now).

If the Edit panel doesn't show a direct way to target higher leverage (some older forum posts suggest partial close/re-open workarounds), try increasing the position size manually by entering a larger amount in the "Increase Position" flow.

For the most accurate/current steps, check the official support page directly: https://support.jup.ag/hc/en-us/articles/18734981395356-Leverage-Management or the in-app tooltips on desktop. If it's still not clear or behaving differently, screenshot the position details and check Jupiter's Discord/support for real-time help. Be careful with leverage — higher means faster liqs on moves against you!

### HUMAN
Yeah none of that pops up for me I just see this

### ASSISTANT
From the screenshot, your WBTC short position shows:

- **Effective leverage**: 4.97x (blended after adding collateral)
- **Collateral**: ~$19.90 (likely ≈$20 total now)
- **Position value/size**: Around $99.45 notional (0.00142324 WBTC, at mark price ~$69,802)
- **Liq price**: $83,727.88 (for a short, liq happens if price rises to this level)
- **Current PnL**: Slightly positive +$0.27 (+1.34%)
- TP/SL set at $63,400 take profit and $71,000 stop loss (partial/full options visible)

Adding collateral reduced leverage because it increased your margin base while keeping the same position size (notional exposure). Leverage = position size / effective collateral, so more collateral → lower leverage.

Jupiter Perps doesn't have a direct "set leverage to X" button on existing positions like some platforms. The leverage slider is mainly for **opening new positions** or **increasing size**. For existing ones, the main ways to adjust leverage are:

### To Increase Leverage Back Toward 10x (Recommended Path)
Increase the position size (add to the short). This keeps your collateral roughly the same but ramps up the notional exposure, pushing leverage higher.

1. In the Positions tab (where you see this card), click the **pencil/edit icon** or the **View** / **+** button next to your WBTC short position (it might say "Edit" or show expand arrows).
2. This should open a panel with options like:
   - **Increase Size** or **Add to Position**
   - Possibly a **Multiply** tab/section (Jupiter has a "Multiply" feature for ramping exposure/leverage on existing positions in some views)
   - Leverage slider or input field to target higher leverage (e.g., slide to 10x or type it in)
3. If the slider appears:
   - Drag it toward 10x (or higher, up to limits for WBTC, which supports up to 250x but practical max depends on pool utilization/risk).
   - The UI will preview: new required borrow/additional size, updated liq price (it'll move closer to current mark price, worsening for a short), new notional, fees, etc.
   - Confirm the tx in your wallet — it'll increase the short size accordingly.
4. If no slider shows directly in edit:
   - Use the main trade panel (top of perps page) to open an **additional short** on WBTC with your desired higher leverage (e.g., set to 10x).
   - Jupiter auto-combines same-direction positions in the same market into one averaged entry/leverage.
   - This effectively blends to higher overall leverage without closing anything.

### Alternative: Withdraw Some Collateral (to Raise Leverage)
- In the same position edit panel, look for **Withdraw Collateral** or **Manage Margin** option.
- Withdraw a portion (e.g., pull out ~$10 to get back near original $10 collateral).
- This increases leverage (liq price moves closer for shorts) but reduces your buffer against adverse moves.
- From docs: Withdrawing collateral increases leverage and moves liq price (worse for shorts).

### Why You Might Not See Edit/Multiply Options
- UI can vary slightly by browser/resolution or if the position is small/low-liquidity.
- For shorts on wBTC, same rules apply as longs.
- If nothing editable shows, try:
  - Refreshing the page or switching to the full perps dashboard (jup.ag/perps).
  - Checking under "Open Orders" or "History" if it's glitched.
  - Using the main trade interface to "Increase" via new order as above.

This matches community/forum reports (e.g., on discuss.jup.ag): To raise leverage, add to position or withdraw collateral; no one-click "reset to 10x" without action.

**Risk note**: Pushing to 10x on this short (current mark ~$69,802, entry ~$68,874) makes liq price tighter (~closer to current price). Your current SL at $71k protects, but higher leverage amplifies losses if WBTC pumps. Monitor borrow fees too (shown in value).

If the edit panel still doesn't show increase/multiply/sliders after trying, screenshot that specific view or hop into Jupiter's Discord (discord.gg/jup) — support there is active for UI issues. Let me know what options appear when you click edit!

### HUMAN
It still won’t let me edit the leverage. Should I just close and reopen the position?

### ASSISTANT
Yes, closing and reopening the position at 10x leverage is a straightforward workaround if the edit options aren't appearing for you, and it's commonly used when the UI doesn't cooperate or limits adjustments on existing positions (especially smaller ones like your ~$20 collateral WBTC short).

From Jupiter's official support and community discussions:

- The primary way to **increase leverage** on an existing position is via the **Multiply** tab in the position management/edit panel. This uses a leverage slider to ramp up exposure (by effectively borrowing more and increasing size), updating your blended leverage without closing.
- Steps: Click the pencil/edit icon or "View" / expand on your position card → look for tabs like **Multiply** (for increasing leverage), **Unwind** (for reducing/closing), or direct **Increase Size** / slider options. Adjust to target 10x, preview the changes (new size, liq price, etc.), and confirm the tx.
- If that Multiply tab or slider simply isn't showing (which happens for some users based on position type, size, browser glitches, or UI variants), then **closing and reopening** is the reliable fallback. Jupiter combines same-direction positions automatically, but there's no one-click "reset leverage" button beyond Multiply.

### Quick Pros/Cons of Closing & Reopening
- **Pros**:
  - Gets you exactly back to 10x leverage cleanly.
  - You can set fresh TP/SL if needed (your current ones at $63,400 TP and $71,000 SL look solid for the short, with mark at ~$69,802 and liq at $83,728).
  - Minimal extra fees if done quickly (just open/close fees + any borrow/funding accrued).

- **Cons**:
  - You pay closing fees (~0.06-0.1% typically on Jupiter Perps) and reopening fees.
  - Realized any unrealized PnL (yours is small +$0.27/+1.34%, so almost nothing lost).
  - Slight slippage/risk during the close-open window (market could move against you briefly).
  - Your average entry might shift slightly if price changes between actions.

### How to Do It Safely
1. In the Positions tab, click **Close** (or the dropdown arrow → Close) on your WBTC short.
   - Choose **Market** close for speed, or limit if you want a specific price.
   - Confirm tx — you'll get your collateral back (~$19.90 USDC) + small PnL.
2. Immediately go to the main Perps trade panel (top section).
   - Select WBTC short again.
   - Set collateral to your desired amount (~$10 for original size, or $20 if keeping the added funds but wanting higher leverage).
   - Use the leverage slider to set **10x** (or type it in).
   - Review projected position, liq price (will be farther out than your current worsened one), fees.
   - Place the order (market or limit).
3. Re-set your TP/SL to match or improve (e.g., keep similar levels relative to new entry).

This should restore your original setup pretty closely. If you're worried about timing, do it during low volatility or set limit orders.

If you try the edit/Multiply one more time (refresh page, clear cache, or try mobile/desktop switch), and it still doesn't show, closing/reopening is fine—many users do it for similar issues. For persistent UI bugs, Jupiter Discord or support ticket is best.

Higher leverage means tighter risk management—your current 4.97x gives more buffer, so at 10x watch that liq price closely (it'll move closer to current mark on reopen). Good luck with the short! Let me know if anything changes when you try.
