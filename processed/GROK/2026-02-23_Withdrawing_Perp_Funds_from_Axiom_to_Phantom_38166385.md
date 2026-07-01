---
id: 675565
source: GROK
date: 2026-02-23
tags: ['axiom', 'phantom-wallet', 'perp-withdrawal', 'sol-fees', 'funds-transfer']
category: crypto-web3
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was trying to withdraw funds from his perpetual wallet on Axiom back to his Phantom wallet and encountering issues with the confirm button and insufficient SOL for fees.
---
# Withdrawing Perp Funds from Axiom to Phantom

### HUMAN
How do I get my money out of my perp wallet on axiom and get it back in my phantom?

### ASSISTANT
Axiom (axiom.trade) integrates with **Hyperliquid** for perpetuals trading on Solana. Your "perp wallet" likely refers to the collateral balance (usually in USDC) used for perps trading on Hyperliquid via Axiom.

Funds in perps are held on Hyperliquid (bridged from Solana), so withdrawing involves converting back to native Solana assets (often SOL) and then transferring to your Phantom wallet.

### Step-by-Step Guide to Withdraw

1. **Log in to Axiom** at https://axiom.trade/ (ensure you're connected with the wallet/account you used for perps).

2. **Navigate to your balances** — Look for the wallet icon or balance display in the top right (it shows SOL and USDC balances).

3. **Convert USDC to SOL if needed** (perp collateral is typically USDC on Hyperliquid):
   - Click the **SOL - USDC** button (or similar swap/convert button) in the top right.
   - Select **Swap** or **Convert**.
   - Enter the amount of USDC to convert to SOL.
   - Confirm the conversion. This processes on-chain (may take ~5 minutes), and you'll receive SOL in your Axiom/Solana balance.

   *Note*: Some guides mention this swap bridges back from Hyperliquid to native Solana USDC/SOL.

4. **Withdraw to Phantom**:
   - Click the **wallet icon** or balance area, then select **Withdraw**.
   - Choose the asset (SOL or USDC, depending on what you have after conversion).
   - Enter the withdrawal amount.
   - Paste your **Phantom wallet address** (open Phantom, go to your SOL or USDC token, click "Receive" or "Deposit" to copy the address).
   - Ensure the network is **Solana** (SPL for tokens like USDC).
   - Double-check the address (Solana addresses are case-sensitive; paste carefully to avoid loss of funds).
   - Confirm the transaction (pay any small Solana network fee).

5. **Check Phantom** — Once processed (usually quick on Solana), the funds (as SOL or USDC) appear in your Phantom wallet.

### Tips & Warnings
- Always start with a small test withdrawal if unsure.
- There may be small fees (Solana network gas + possible bridge/swap fees; no major platform withdrawal fee mentioned).
- Axiom is non-custodial — your funds are on-chain, but verify everything in your connected wallet.
- If your funds are stuck in open perp positions, close them first to free up collateral.
- For visual step-by-step, search YouTube for "How To Withdraw Solana From Axiom Pro" or "withdraw from Axiom to Phantom" — many 2025/2026 tutorials match this flow (e.g., clicking wallet icon > withdraw > paste Phantom address).
- If issues arise (e.g., conversion not showing), check Axiom's docs at https://docs.axiom.trade/perpetuals/withdraw or their support.

This should get your funds back safely! If something looks different in the UI, feel free to describe what you see for more tailored help.

### HUMAN
I’m on the mobile phantom app and logged in that way for axiom. Where do I go to do this?

### ASSISTANT
Since you're using the **mobile Phantom app** to log in to Axiom (axiom.trade), you're likely accessing the Axiom website through Phantom's built-in browser (by going to axiom.trade directly in Phantom or via a dApp connection link). The interface is the same as the desktop web version but optimized for mobile viewing—tap-friendly, with menus that may appear as icons or a hamburger menu (three lines) on smaller screens.

Axiom doesn't have a native standalone mobile app for trading (based on current info; it integrates with wallets like Phantom for mobile use). Here's how to handle the withdrawal process on mobile:

### 1. Ensure You're Logged In and Viewing Balances
- Open the **Phantom app** on your phone.
- If not already connected: Go to your browser tab in Phantom (or search/open axiom.trade), connect your wallet if prompted, and log in.
- Once on the main Axiom dashboard (trading/perps screen), look for your **balance display**—usually in the **top right corner** (it shows SOL and/or USDC amounts, possibly with a wallet icon or your address shortened).
  - On mobile, this might be a small icon (wallet/purse) or text like "Balance: X SOL / Y USDC". Tap it to expand if needed.

### 2. Convert Perp USDC Back (If Your Collateral Is in USDC on Hyperliquid)
Perps use bridged USDC (via Hyperliquid), so first bridge/convert it back to native Solana assets:
- Tap the **SOL - USDC** button or indicator in the **top right** (it may say "SOL/USDC" or show a swap icon next to balances).
- Select **Swap** or **Convert** (tap the button labeled as such).
- Choose to convert **USDC (Hyperliquid/perps) to SOL** or **USDC on Solana** (the exact label is often "Convert your USDC to USDC on SOL" or similar).
- Enter the amount of USDC to convert.
- Confirm the transaction (sign via Phantom popup—approve the tx).
- Wait ~5 minutes for processing (it bridges back on-chain). You'll see the SOL (or native USDC) appear in your Axiom/Solana balance.

If the button isn't obvious on mobile, try rotating your phone to landscape mode for better layout, or look for a "Convert" or "Bridge" section under balances.

### 3. Withdraw to Your Phantom Wallet
- After conversion, go back to the **top right balance/wallet icon** and tap it (or look for a **Withdraw** button nearby—sometimes it's directly under balances or in a menu).
- Select **Withdraw**.
- Choose the asset (SOL or USDC, whichever you now have).
- Enter the amount to withdraw.
- Paste your **Phantom receive address**:
  - In a separate step: Open Phantom app → Tap your main SOL balance (or USDC token if withdrawing that) → Tap **Receive** or **Deposit** → Copy the address shown.
  - Paste it carefully into the Axiom withdraw field (double-check—Solana addresses start with numbers/letters, case-sensitive).
- Confirm the network is **Solana** (it should default to this).
- Sign/approve the transaction in Phantom (small Solana fee applies).
- Funds should arrive in Phantom quickly (Solana is fast; check your Phantom balance or transaction history).

### Quick Mobile Tips
- If the UI feels cramped, zoom in/out or use landscape mode.
- Phantom may prompt for signatures multiple times (one for conversion/bridge, one for withdraw)—always review details.
- If stuck (e.g., no withdraw button visible), check for a **menu** (three lines or dots in top corner) → look under "Wallet", "Balances", or "Perps".
- Close any open perp positions first if collateral is locked.
- Test with a tiny amount first to confirm.

This matches the standard flow from Axiom's docs and user reports (e.g., top-right SOL-USDC swap for bridging back, then withdraw). If the screen looks different or you see an error, describe what buttons/icons you see (or screenshot if possible), and I can refine! For visuals, search YouTube in your browser for "withdraw from Axiom to Phantom mobile" — recent 2026 tutorials show the mobile browser flow. Stay safe!

### HUMAN
It won’t let me tap confirm when I go to convert

### ASSISTANT
The "confirm" button not responding (or being un-tappable/grayed out/disabled) during the convert step on Axiom (via Phantom's mobile browser) is a common hiccup, often tied to transaction requirements, UI glitches on mobile, or setup issues. Based on Axiom's official docs and user reports, here are the most likely causes and fixes—try them in order:

### 1. **Check for Open Perp Positions or Locked Collateral**
   - If any perpetual trades are open (long/short positions), your USDC collateral might be partially or fully locked/used as margin. You can't convert/withdraw locked funds.
   - **Fix**: Go to the **Perpetuals** tab (usually bottom or side menu on mobile). Close all open positions (tap position → close → confirm). This frees up the full USDC balance.
   - After closing, refresh the page (pull down or restart Phantom browser tab) and retry the convert.

### 2. **Insufficient SOL for Fees / Gas**
   - The convert/bridge process (USDC on Hyperliquid → native Solana USDC/SOL) requires a small amount of **SOL** in your connected wallet for transaction fees (typically 0.001–0.01 SOL, but can vary).
   - On mobile/Phantom, if your SOL balance is too low (or zero), the confirm button disables without clear error messaging.
   - **Fix**:
     - Check your top-right balance: Ensure you have at least ~0.02 SOL (extra buffer).
     - If low: Deposit a tiny amount of SOL from Phantom first (go to Phantom → SOL → Send → paste your Axiom-connected address from Axiom's wallet icon → send small test).
     - Or swap tiny SOL to cover fees if you have other assets.
   - Retry convert after topping up.

### 3. **Mobile/Phantom Browser UI Glitch or Permissions**
   - Phantom's in-app browser can be finicky with pop-ups, signatures, or taps on smaller screens—sometimes confirm doesn't register taps, or the button appears but is unresponsive until refreshed.
   - **Fixes to try**:
     - Rotate to **landscape mode** for better button visibility/layout.
     - **Force refresh**: Pull down on the page or close/reopen the axiom.trade tab in Phantom.
     - Clear Phantom cache: In Phantom app → Settings → Privacy/Security → Clear Cache (or similar; restart app after).
     - Ensure Phantom is updated (App Store/Google Play).
     - Try entering a slightly smaller amount (e.g., if converting max, try 99%—sometimes edge cases disable confirm).
     - If a Phantom signature popup appears but confirm still won't tap, approve any pending tx first.

### 4. **Amount or Input Issues**
   - If the amount field is empty, exceeds your available balance, or has invalid formatting, confirm disables.
   - **Fix**: Double-check:
     - Balance shown matches what you expect (after any open positions closed).
     - Enter exact amount manually (don't use "Max" if it's buggy).
     - Tap outside the field to "commit" the input.

### 5. **Next Steps if Still Stuck**
   - Wait 5–10 minutes and retry (occasional on-chain delays or bridge sync issues).
   - Check Axiom's Discord for support (docs link: join via https://docs.axiom.trade/support → verify → create ticket in #tickets channel). Describe: "Mobile Phantom, convert USDC button confirm not tappable, no error shown."
   - Search YouTube in your browser for "Axiom convert USDC mobile issue" or similar—videos from 2026 show exact taps (e.g., top-right SOL-USDC → Swap/Convert → enter amount → confirm).
   - As a last resort, if funds aren't huge, close positions → convert small test amount first to confirm flow works.

Most users resolve this by closing positions or adding tiny SOL for fees. Once convert succeeds (~5 min processing), you'll see native USDC/SOL in balances → then withdraw as before (wallet icon → Withdraw → paste Phantom address → confirm).

Describe exactly what you see (e.g., is button gray? Any error text? Balance amounts? Open positions?) or if one of these fixes it, and I'll narrow it further! Stay patient—Solana moves fast once fixed.

### HUMAN
I have .005 sol is that why?

### ASSISTANT
Yes, your **0.005 SOL** balance is very likely the reason the **Confirm** button won't tap/activate during the convert step.

Here's why and how to fix it:

### Why 0.005 SOL Is Too Low
- The convert process (bridging USDC from Hyperliquid back to native Solana USDC/SOL) involves on-chain transactions on Solana.
- Every Solana transaction requires a small fee paid in **SOL** (base fee is fixed at ~0.000005 SOL, but with prioritization fees, real-world costs for complex actions like bridging/swaps often hit **0.0001–0.001 SOL** or more per tx, especially if the network has any congestion).
- Some actions (e.g., if it creates/updates associated token accounts for USDC on Solana) can require a bit more upfront to cover "rent" or setup (~0.002 SOL in some cases).
- Many dApps/wallets (including Phantom integrations) disable the confirm button if your SOL balance is below a safe threshold (commonly warns at ~0.005 SOL minimum, but for reliable execution on bridges/swaps, users report needing **at least 0.01–0.02 SOL** buffer to avoid failures or grayed-out buttons).
- With only 0.005 SOL, you're right at or below the edge—Phantom/Axiom likely detects it as insufficient for the full tx (including any priority to ensure it lands quickly) → button stays un-tappable/no error popup, just unresponsive.

This matches common Solana/Phantom behaviors: swaps, bridges, or token ops often block if SOL is too low to cover fees safely.

### Quick Fix: Add a Bit More SOL
1. **From your main Phantom wallet** (or another source):
   - Open Phantom app.
   - Go to your SOL balance → Tap **Send**.
   - Paste your **Axiom-connected wallet address**:
     - In Axiom (via Phantom browser): Tap the top-right wallet icon/balance → it shows your shortened Solana address (or full one) — copy that.
   - Send **at least 0.02–0.05 SOL** (small test if you want; e.g., 0.03 SOL covers fees + buffer comfortably). This is cheap (~$5–10 at typical SOL prices).
   - Confirm/send (Phantom will deduct a tiny fee from the send amount).

2. **Once received** (usually instant):
   - Refresh the Axiom tab in Phantom browser (pull down or close/reopen).
   - Go back to the convert screen (top-right SOL-USDC → Swap/Convert → enter USDC amount).
   - The Confirm button should now be tappable/blue/active.
   - Proceed: Enter amount → Confirm (Phantom signature popup → approve).

After convert finishes (~5 min), you'll have native USDC/SOL in balances → then withdraw as before (wallet icon → Withdraw → paste Phantom address → confirm).

### Extra Tips
- Always leave ~0.01 SOL minimum in the connected wallet for future txs.
- If still no luck after adding SOL: Close any open perp positions first (frees collateral), or force-refresh + restart Phantom app.
- Test with a small USDC convert amount once unlocked.
- If the button remains dead even with more SOL, it could be a temporary UI glitch—try landscape mode, clear Phantom cache (Settings → Privacy → Clear), or check Axiom Discord for similar reports.

This should unblock you fast. Let me know your new SOL balance after adding or if the button changes!
