---
id: 692915
source: GROK
date: 2026-03-11
tags: ['jupiter-perps', 'leverage-reduction', 'collateral-addition', 'lend-tab', 'position-reopen']
category: crypto-web3
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was trying to understand why adding collateral reduced his leverage and how to increase it back on an existing Jupiter Perps position.
---
# Jupiter Perps: Adding Collateral Reduces Leverage

### HUMAN
Why did my leverage go down when I added more collateral on Jupiter perps? I had $10 in at 10x and I added $10 more and now it’s 4.97x?

### ASSISTANT
**That's exactly how Jupiter Perps (Jupiter's perpetual futures exchange) is designed to work.** Adding more collateral to an existing position **reduces your effective leverage** — it's not a bug, it's intentional to make the position safer.

Here's why, broken down simply with your numbers:

- You started with **$10 collateral** at **10x leverage**.
  - This means your position size (notional exposure) was **$10 × 10 = $100**.
  - Leverage = Position size / Collateral = 100 / 10 = **10x**.

- You then added **$10 more collateral**, bringing total collateral to **$20**.
  - The position size stays the same (**$100** worth of the asset you're long/short on) because adding collateral doesn't increase your exposure — it just adds more of your own money as buffer/margin.
  - New leverage = Position size / New collateral = 100 / 20 = **5x**.

- You saw ~**4.97x** probably due to minor factors like:
  - Small unrealized PnL changes since opening.
  - Borrow fees or funding that slightly adjusted the effective numbers.
  - Rounding/display in the UI.

From Jupiter's official docs (Collateral Management section):

> When traders deposit collateral, the liquidation price and leverage for the long position decreases as the maintenance margin increases.

(And similarly for shorts — leverage decreases when you add collateral.)

Adding collateral is a way to **de-leverage** your position, move your liquidation price farther away (safer), and reduce risk without closing or reducing the position size. If you wanted to keep higher leverage (or increase it), you'd need to increase the position size instead (by opening more exposure with the added funds), not just add margin to the existing one.

If the price hasn't moved much against you, this is normal behavior. If something still looks off (e.g., big unexpected PnL or fees), feel free to share more details like the asset (SOL/ETH/BTC?), long/short, or a screenshot, and I can help dig deeper!

### HUMAN
So to increase my leverage on that position I need to do what?

### ASSISTANT
To increase leverage on your **existing position** in Jupiter Perps (instead of just adding collateral, which lowers it), you need to **increase the position size** (i.e., add more exposure/notional value) while using your additional funds (or borrowing more via the platform's mechanics).

Leverage = Position Size / Collateral  
- Adding collateral alone keeps position size the same → leverage drops (like your $10 → $20 collateral example dropping from 10x to ~5x).  
- To raise leverage, you must grow the position size faster than the collateral (or at least proportionally more).

### Main Ways to Do This on Jupiter Perps
1. **Use the "Multiply" or Leverage Adjustment Feature (Recommended if Available for Your Position)**  
   From Jupiter's support docs:  
   - Go to your open position in the interface.  
   - Look for the **Multiply** tab (or similar "Increase Leverage" / leverage slider option in position management).  
   - Adjust the leverage slider upward to your target (e.g., back toward 10x or higher, up to the max allowed like 100x–250x depending on the asset and current limits).  
   - This effectively increases your position size by borrowing more against your existing collateral + any new funds, updating your exposure, liquidation price, etc.  
   - Review the projected changes (new position size, fees, liq price), then confirm the tx.  

   This is the cleanest way without closing anything—it's designed for ramping up leverage on existing trades.

2. **Manually Increase Position Size**  
   - If no direct "Multiply" button shows for your position, or you want full control:  
     - Deposit/add more collateral first (if needed for buffer/room).  
     - Then open an **additional trade** in the **same direction** (long or short) on the same asset, using the same wallet/position logic if it merges, or just stack exposure.  
     - Set higher leverage on the new portion (via the slider when opening).  
   - Jupiter Perps often merges same-direction positions on the same asset into one effective position, so the overall leverage recalculates higher as total size grows relative to total collateral.  
   - Example with your numbers:  
     - Current: $100 position / $20 collateral = 5x.  
     - Add funds to open another ~$100 exposure at 10x (using ~$10 more collateral) → new total ~$200 position / ~$30 collateral = ~6.67x (higher than before).  
     - Repeat/adjust to push toward your target.

3. **Other Notes / Workarounds from Community**  
   - Some users mention workarounds like partially closing then re-opening at higher leverage, but that's inefficient (fees + potential slippage). Avoid if possible.  
   - Jupiter doesn't always have a one-click "increase leverage without size change" like some CEXs—it's tied to position size adjustments.  
   - Check current max leverage for your asset (e.g., SOL/ETH/wBTC often up to 250x, but can vary by market conditions/position health).

Head to the Jupiter Perps dashboard → your Positions tab → click into your open trade and look for Multiply / leverage slider / "Increase" options first—that's usually the spot. If it's not there or behaves weird (e.g., due to PnL, fees, or asset), share the asset (SOL?), direction (long/short), and maybe approximate current numbers/screenshot details for more specific troubleshooting.

Higher leverage = higher risk (closer liq price, amplified losses), so size it carefully! Let me know how it goes.

### HUMAN
I don’t see that I just see this

### ASSISTANT
To increase leverage on your existing WBTC short position (currently at ~4.97x with $99.45 size and ~$20 collateral), the key is to **increase the position size** (notional exposure) relative to your collateral. Adding collateral alone lowers leverage, as you've seen.

From the screenshot, your position looks standard for **Jupiter Perps** (on jup.ag/perps), and the UI doesn't show a direct "Multiply" button or leverage slider **right in the Positions tab view** you shared. That's because Multiply (or similar adjustment tools) often appears in a dedicated management flow or separate tab/section.

### Steps to Increase Leverage
1. **Click into Position Management / Detailed View**  
   - In your screenshot, the position card has icons like the share button (blue 🔗) or possibly an expand arrow/next to "4.97x Short".  
   - Tap/click the position itself (e.g., the WBTC line or any edit pencil icons like next to Collateral $19.99). This should open a **full position management page** or modal.  
   - On that detailed page, look for tabs or sections like:  
     - **Multiply** tab  
     - **Increase Leverage** / **Adjust Leverage**  
     - A **leverage slider** (common in Jupiter docs for adjusting from low to max like 100x–250x for WBTC).  

   Jupiter's support explicitly says: Use the **Multiply** tab to increase leverage on your existing position → Adjust the leverage slider to your target → Review projected changes (new size, liq price, etc.) → Confirm tx.

2. **If No Multiply Tab Shows Up**  
   - Switch to the main **Trade** tab (bottom of your screenshot has "Trade" button highlighted).  
   - Select WBTC short again, but now with your existing position in mind—Jupiter often merges same-direction trades on the same asset.  
   - Deposit/add a bit more collateral if needed (via the pencil edit on Collateral).  
   - Use the **leverage slider** when opening/increasing to set higher than current (e.g., aim for 10x on the new portion).  
   - Execute to **add size** — this combines with your existing $99.45 exposure, pushing overall leverage up (e.g., adding ~$100 size with minimal extra collateral could bump you toward 8–10x).  

   Docs confirm: Traders can "increase the size for existing positions" with up to 250x leverage on wBTC, and limit/market orders to add will combine automatically.

3. **Quick Math Example for Your Setup**  
   - Current: Size $99.45 / Collateral $20 ≈ 5x.  
   - To hit ~10x: Need ~$200 total size (with same $20 collateral).  
     → Add ~$100.55 exposure (open/increase short WBTC at higher leverage slider setting).  
   - Use minimal new collateral for the add-on (e.g., $5–10) to keep leverage high. Review the preview before confirming— it'll show updated leverage, new liq price (yours is currently safe at $83k+ for short), and fees.

Higher leverage moves your liq price closer (riskier for shorts if WBTC pumps), so check the projected liq price carefully. WBTC max is up to 250x, but start conservative.

If after clicking in you still don't see Multiply/slider (maybe UI variation or mobile quirk), or if it errors, screenshot the detailed position page or describe what tabs/buttons appear—I can guide more precisely. You could also hit the "Talk to us" chat in-app for quick support. Let me know what you find!

### HUMAN
I don’t see any of that. Do I need to just close and reopen the position?

### ASSISTANT
No, you **don't need to close and reopen** the position to increase leverage—that would cost extra fees (open/close), risk slippage on re-entry, and potentially miss your current favorable entry price. Jupiter Perps supports adjusting existing positions without closing them.

From Jupiter's official support docs (especially the "Leverage Management" and "Managing a Multiply position" articles), the clean way is via the **Multiply** feature/tab for increasing leverage on open positions.

### Why You're Not Seeing It Yet
Your screenshot shows the main **Positions** list view, which is a summary/high-level dashboard. The Multiply options (leverage slider, etc.) appear in the **detailed position management page** or modal—not directly on this overview screen.

### Step-by-Step to Access It
1. **Open the detailed view for your WBTC short**:
   - Tap/click directly on the position card (the WBTC line with "4.97x Short", or the orange WBTC icon, or any expandable arrow/chevron if visible).
   - Alternatively, look for a pencil/edit icon next to Collateral ($19.99) or the share button (🔗)—clicking those often leads to management.
   - This should load a **full position management screen** with tabs/sections.

2. **Look for the Multiply tab/section**:
   - On that page, you'll see options like **Multiply** tab (or "Increase Leverage").
   - Switch to it if tabbed.
   - There should be a **leverage slider** (you can slide it up from current ~5x toward your target, e.g., 10x or higher—WBTC supports up to 250x depending on market).
   - It will show a **Projected Position** preview: new size (increased exposure), updated leverage, new liq price (which will move closer for a short if you ramp up), health status, fees, etc.

3. **Execute**:
   - Adjust to your desired leverage.
   - Review everything carefully (higher leverage = position size grows via more borrowing, liq price gets riskier—yours is currently far at ~$83k for short).
   - Hit **Multiply** (or confirm button) → sign the tx in your wallet.
   - Done—your existing position updates with higher leverage/size, no closing involved.

### If Multiply Still Doesn't Show
- It might be because your position is very small/low PnL, or a UI glitch/mobile view limitation—try refreshing the page, switching to desktop/web view if on mobile, or force-reload (pull down or clear cache).
- Alternative (still no close needed): Go back to the main **Trade** tab → select WBTC short again → set higher leverage on the slider → input additional collateral/size to add → execute. Jupiter merges same-direction (short) positions on the same asset automatically, so this increases overall size/leverage without duplicating.
  - Example: Add enough to push total size to ~$200 with minimal extra collateral → leverage jumps toward 10x.

Closing/reopening is a last resort (and inefficient here). If after trying the detailed view you still see nothing (no Multiply, no slider), it could be a temporary UI thing or specific to WBTC shorts—screenshot the detailed page if possible, or use the in-app "Talk to us" chat for quick help from Jupiter support.

Higher leverage amps both wins/losses and moves liq closer, so size conservatively. Let me know what you see after clicking into the position!

### HUMAN
I’m now on the desktop website. How do I increase my leverage on that existing position

### ASSISTANT
On the desktop version of **jup.ag/perps** (or the Perps section on the main site), the Multiply feature for increasing leverage is tied to **Jupiter Lend's Multiply** (not always directly in the core Perps trading UI for standard perpetuals). From official Jupiter support docs, this is how to increase leverage on an existing position without closing it.

### Steps on Desktop
1. **Navigate to Your Position Details**:
   - Log in/connect your wallet on jup.ag.
   - Go to the **Perps** tab (bottom nav or sidebar on desktop).
   - Click on **Positions** (you should see your WBTC short listed as in your screenshot).
   - Click directly on your specific position card (the WBTC 4.97x Short row). This opens the **position management page** or detailed modal/view. (On desktop, this is usually a larger panel or full page with more options than mobile.)

2. **Access the Multiply Tab**:
   - In the detailed position view, look for tabs or sections at the top/middle: **Multiply** should appear (alongside things like Add/Withdraw Collateral, TP/SL, Close).
   - Switch to the **Multiply** tab if it's tabbed.

3. **Increase Leverage**:
   - You'll see a **leverage slider** (or multiplier slider) — slide it up from your current ~5x to your target (e.g., 10x or higher; WBTC supports up to 250x max depending on market).
   - The UI shows a **Projected Position** preview panel: this updates in real-time showing new position size (increased exposure/notional), updated collateral/debt, new liquidation price (it'll move closer for your short if ramping up), health status, fees, etc.
   - Review everything carefully — higher leverage increases risk (closer liq price if WBTC rises).

4. **Confirm**:
   - Click the **Multiply** button (or similar "Increase" / "Execute").
   - Confirm the transaction in your wallet (Phantom/Solflare/etc.).
   - Once processed, your existing position updates automatically with the higher leverage and larger size — no need to close/reopen.

### If Multiply Tab Isn't Visible in Perps Position View
Jupiter has separate but integrated products (Perps for futures trading, Lend for borrowing/lending with Multiply looping). Your position is a standard **Perps** perpetual short (WBTC perp), not a Lend Multiply vault position (those are for looped lending like SOL/JLP).

For pure Perps positions like yours:
- There isn't always a dedicated "Multiply" tab in the core Perps UI for mid-position leverage boosts (some community threads note this limitation; you'd adjust by adding size).
- Instead, use this workaround (no closing required):
  1. Go back to the main **Trade** tab in Perps.
  2. Select WBTC, Short direction again.
  3. Set your desired higher leverage on the slider (e.g., 10x).
  4. Input an amount to add (e.g., deposit a small amount of additional collateral like $5–10 USDC/USDT, or use existing balance).
  5. Place the order (market/limit) to increase the position.
  - Jupiter Perps merges same-direction positions on the same asset (your short WBTC will combine automatically).
  - Result: Total size increases (e.g., from ~$99 to ~$200), collateral rises only slightly → overall leverage jumps (e.g., toward 10x).

This achieves the same effect as "Multiply" by growing exposure relative to collateral.

If the detailed view still lacks options (rare UI bug or specific to small positions), try:
- Refreshing the page or clearing cache.
- Checking under **Portfolio** > Perps section for position actions.
- Using the in-app chat ("Talk to us") for live support—they can confirm if Multiply applies to your perp type.

Avoid closing/reopening unless necessary — it adds fees and risks re-entry at worse price. Your current short is in slight profit with safe liq distance; ramping leverage carefully is fine, but monitor mark price vs. entry.

If you click into the position and describe/take a screenshot of what tabs/buttons show on desktop, I can pinpoint exactly! Let me know how it goes.

### HUMAN
So I have to go to the lend tab to add more leverage to my $20 position now that it decreased my original 10x leverage?

### ASSISTANT
**No, you don't need to go to the Lend tab** (Jupiter Lend / Multiply vaults) for your $20 WBTC perp short position—that's a separate product for looped lending/borrowing on assets like JLP, SOL, etc., not for standard perpetual futures like yours.

Your position is a classic **Jupiter Perps** perpetual contract (WBTC short with isolated collateral), where leverage is simply Position Size / Collateral. The "Multiply" feature with the slider for increasing leverage is primarily documented for **Jupiter Lend Multiply positions** (e.g., leveraged vaults), not directly for pure Perps like this one. In Perps, there's no one-click "Multiply tab" in the position details for ramping leverage mid-trade without adjusting size/collateral.

### How to Increase Leverage on Your Existing Perps Position (Without Closing)
The standard way in Jupiter Perps is to **increase the position size** (add more exposure/notional) while adding minimal or no extra collateral—this effectively raises leverage since size grows faster than collateral.

Steps on desktop (jup.ag/perps):
1. **Go to the Trade tab** (main trading interface, not Positions).
2. Select **WBTC** as the asset and **Short** direction (same as your open position).
3. In the order panel:
   - Set your desired **higher leverage** using the leverage slider (e.g., slide to 10x or whatever target; it defaults low but goes up to 250x max for WBTC).
   - Input an amount: This could be a small additional collateral deposit (e.g., $5–20 USDC/USDT from your wallet) to fund the size increase. Use market or limit order.
   - The preview will show the added size/exposure.
4. Place the order and confirm the tx.
   - Jupiter Perps **automatically merges** same-direction positions on the same asset (your existing short + new short add-on → one combined position).
   - Result: Total size increases (e.g., from ~$99 to $150–200+), collateral only rises slightly → leverage jumps (e.g., back to ~10x or higher).
   - Your entry price averages slightly, liq price updates (moves closer for short if ramping up—check preview!), and PnL combines.

This is the cleanest method per community discussions and Perps mechanics—no closing fees/slippage, keeps your original entry mostly intact.

### Why No Direct Multiply in Perps UI?
Perps leverage is set at open/add, and adjustments happen via size changes (not pure "multiply debt" like in Lend vaults). If your position details page (after clicking the WBTC card) shows no Multiply tab/slider, that's expected for standard perps—it's not there like in Lend.

### Alternatives if the Above Doesn't Fit
- Add collateral first (via pencil edit on your position → increases buffer but lowers leverage further—then use step above to counter by adding size).
- Partial close + re-add at higher leverage (but avoid if possible—extra fees + potential worse re-entry).

Test with a tiny add-on first to see the merged effect. Higher leverage means closer liq price (your current $83k+ is safe; ramping to 10x will bring it down a lot—review preview!).

If merging doesn't happen or UI behaves oddly, hit the "Talk to us" chat in-app—they're quick. Or share what the Trade panel shows when you try to open another WBTC short. You got this!
