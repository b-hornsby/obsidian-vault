---
category: crypto-web3
date: 2026-03-01
id: 459802
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: frustrated
source: GROK
summary: Bryan was trying to withdraw funds from Axiom Perps but the Phantom wallet
  browser extension wouldn't confirm the signing transaction.
tags:
- axiom-perps
- phantom-wallet
- withdrawal-issue
- transaction-signing
---
# Axiom Perps Withdrawal Phantom Signing Issue

### HUMAN
How come when I try and withdraw my perp account money from axiom it won’t let me confirm it in phantom even though I’m using the browser within phantom to sign in?

### ASSISTANT
Axiom (axiom.trade) is a non-custodial Solana-based trading platform that integrates spot trading, meme coin tools, yield, and perpetuals (perps) trading, often via integrations like Hyperliquid for perps and Marginfi for lending/yield. Your "perp account" likely refers to the perpetual futures balance (e.g., in USDC), separate from your main spot/token balance.

When withdrawing from Axiom (especially perps or perp-related funds), the process typically involves:

- For perps balances: You may first need to transfer/bridge from perps back to tokens/USDC/SOL within the platform (e.g., via a "Tokens ↔ Perps" or similar conversion step if using something like Phantom Terminal features, though Axiom has its own interface).
- Then initiate withdrawal to your connected wallet (Phantom in this case), which triggers a transaction signature request.

Since you're using the in-app browser within Phantom (Phantom's built-in browser for dApps), but the confirmation isn't going through, here are the most common reasons and fixes based on how these Solana dApps + Phantom work:

1. **Signature pop-up not appearing or failing silently** — Phantom's in-app browser sometimes has glitches with transaction requests, especially if the site (Axiom) is trying to request multiple signatures or if there's a connection hiccup. Try these:
   - Close the Phantom browser tab completely, refresh Axiom, and reconnect your wallet.
   - Use Phantom's browser extension in a regular Chrome/Brave/etc. browser instead of Phantom's internal one. Go to axiom.trade in a standard browser where Phantom extension is installed — this often resolves signing issues because the extension handles prompts more reliably than the in-app version.
   - In Phantom settings, check for any pending/queued transactions or clear cache if available.

2. **Insufficient SOL for fees** — Solana transactions (including signing withdrawals) require a tiny amount of SOL (~0.000005–0.001 SOL per tx, but more if account setup or priority fees apply). Even if your perp balance shows funds, the connected wallet needs SOL for gas. Check your Phantom wallet's SOL balance and add a little if it's under ~0.01 SOL.

3. **Account setup/initialization fees or pending actions** — Axiom sometimes requires one-time setup fees (e.g., ~0.016 SOL for Marginfi account or ~0.02 SOL for Hyperliquid perps account). If not paid earlier, withdrawal might block until resolved. Also ensure any perp position is closed or transferred to tokens first.

4. **Wrong address or formatting issue** — When pasting your Phantom address into Axiom for withdrawal, double-check no extra spaces (people report "invalid address" if there's a leading space — backspace and re-paste).

5. **Browser/wallet conflicts** — Disable any ad blockers, VPNs, or extensions that might interfere. Restart Phantom and your device. Ensure Phantom is updated.

6. **Platform-specific quirks** — Some users report needing to withdraw SOL/USDC directly (not other tokens without conversion). If your perp funds are in USDC, confirm the withdrawal flow handles that.

If none of that works:
- Visit axiom.trade directly and check their FAQ/docs or support section for withdrawal guides.
- Reach out to Axiom support (likely via Discord/Twitter/X or in-app chat if available).
- Or check Phantom help for dApp connection issues: help.phantom.com (search "transaction not signing" or "dApp connection").

This is usually fixable with the extension-in-normal-browser switch or adding SOL for fees — many Solana users hit similar snags with in-app browsers. Let me know more details (e.g., exact error message if any shows up) for better troubleshooting!
