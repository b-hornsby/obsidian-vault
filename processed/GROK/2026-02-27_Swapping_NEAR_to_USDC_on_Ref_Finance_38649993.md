---
id: 842702
source: GROK
date: 2026-02-27
tags: ['near', 'usdc', 'ref-finance', 'ledger-live', 'token-swap', 'solana']
category: crypto-web3
sentiment: stuck
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was trying to swap NEAR to USDC on Ref Finance and also swap ICP to USDC on Solana, encountering issues with Ledger Live's swap functionality.
---
# Swapping NEAR to USDC on Ref Finance

### HUMAN
How do I cash out my $near? I want to swap to usdc but it won’t let me

### ASSISTANT
To swap your **$NEAR** (NEAR tokens) to **USDC** on the NEAR blockchain, the most common issue people run into when it "won't let" them is trying to do the swap directly in a basic wallet interface (like MyNearWallet or similar) without enough liquidity, incorrect token selection, high slippage, insufficient gas (NEAR for fees), or using a wallet/DEX that doesn't support the pair well.

USDC exists natively on NEAR (thanks to Circle integration since 2023), and the standard way to swap is via a **decentralized exchange (DEX)** on the NEAR network.

### Recommended Steps to Swap NEAR → USDC on NEAR
1. **Use a NEAR-compatible wallet** — Popular options include:
   - MyNearWallet (app.mynearwallet.com)
   - Meteor Wallet
   - HERE Wallet
   - Or MetaMask (with NEAR snap/support added if needed)

   Make sure your NEAR tokens are in this wallet (not locked in staking without unstaking first, if applicable).

2. **Go to a reliable NEAR DEX** — The most popular and reliable one for this pair is **Ref Finance** (ref.finance). It's the go-to DEX on NEAR for swapping NEAR to USDC (or other tokens).

   - Connect your wallet to ref.finance.
   - Select NEAR as the "from" token.
   - Select USDC as the "to" token (it should show as native USDC on NEAR; avoid any bridged versions like USDC.e if possible).
   - Enter the amount of NEAR you want to swap.
   - Adjust **slippage tolerance** if needed (start with 0.5–1%; increase to 2–3% if it fails due to price impact or low liquidity).
   - Ensure you have a tiny bit of extra NEAR (~0.01–0.1 NEAR) in your wallet for transaction fees/gas.
   - Review the route (it may route through pools like NEAR → wNEAR → USDC or direct if available), confirm, and approve/sign the transactions.

3. **If Ref Finance doesn't work or shows errors** (e.g., "unable to swap," no route, high price impact):
   - Try increasing slippage.
   - Swap in smaller amounts first to test.
   - Use an alternative NEAR DEX like Spin.fi, RHEA Finance (dex.rhea.finance), or Veax.
   - Check liquidity on NEAR explorer (nearblocks.io) for the NEAR/USDC pool to see if it's deep enough for your size.

Once you have USDC on NEAR, that's your "cash out" step partially done (stablecoin, low volatility). If you want to go further (e.g., to fiat USD in a bank):

- **Bridge or transfer USDC** to another chain/exchange: Use native USDC tools (via Circle) to move to Ethereum, Base, or others without bridge fees in many cases, then deposit to a centralized exchange (CEX) like Kraken, Coinbase, Binance, etc.
- **On a CEX**: Deposit NEAR directly (if supported) → swap to USDC/USDT → sell for fiat → withdraw to bank. Kraken has direct NEAR/USDC trading pairs and easy fiat off-ramps.
- **Other quick options**: Aggregators like SimpleSwap, ChangeNOW, or Changelly let you swap NEAR → USDC (often on Ethereum/Base) without a wallet connect, just send NEAR to their address.

### Common Reasons It Won't Let You Swap
- Not enough NEAR for fees.
- Slippage too low (market volatility).
- Low liquidity in the pool for large amounts → break into smaller swaps.
- Wallet/DEX glitch → refresh, reconnect, or try a different browser/device.
- Token confusion (e.g., trying bridged USDC instead of native).

If none of this works, reply with more details: Which wallet are you using? What exact error/message do you see? How much NEAR are you trying to swap? Screenshot if possible (but don't share private keys/seed). That'll help narrow it down.

Stay safe—double-check URLs (official ref.finance), never share your seed phrase, and use small test amounts first.

### HUMAN
I’m using ledger live if that helps

### ASSISTANT
Thanks for the extra detail—that you're using **Ledger Live** (with your Ledger hardware wallet) helps a lot. Ledger Live has added support for NEAR over time, including some swap options, but **direct NEAR → USDC swaps inside Ledger Live** can be limited or not always available for on-chain NEAR DEX-style swaps due to how NEAR works (it's not EVM-compatible like Ethereum, so integrations differ).

From recent Ledger support info (as of 2026), here's the current picture:

- Ledger Live supports **NEAR Protocol** for sending/receiving/staking, and you can connect your Ledger to NEAR wallets like MyNearWallet or Sender Wallet for full control.
- For swaps, Ledger Live uses providers like **Changelly** (centralized/custodial swaps), **1inch**, **THORChain**, **NEAR Intents** (via SwapKit for non-custodial cross-chain), and others.
- **NEAR Intents** is specifically integrated for cross-chain/non-custodial swaps involving NEAR (e.g., NEAR to assets on Ethereum, Solana, Bitcoin, etc.), and it can include stablecoins like USDC.
- However, if you're trying to swap **native NEAR to native USDC on the NEAR chain** (on-chain DEX style), Ledger Live's built-in Swap tab may not support it directly or route it properly—especially if the pair isn't listed, liquidity is low, or the provider doesn't cover intra-NEAR swaps well. That's a common reason it "won't let you" (e.g., no quote appears, error, or grayed out).

### Quick Fixes and Steps in Ledger Live
1. **Update Ledger Live** — Make sure you're on the latest version (check for updates in the app; recent releases improved swap integrations).
2. **Open the Swap tab**:
   - Connect/unlock your Ledger device.
   - Go to the left sidebar → **Swap**.
   - Select **NEAR** as the "from" asset (ensure your NEAR account is added and visible in Ledger Live).
   - Search/select **USDC** as the "to" asset (it may show as USDC on NEAR or bridged/cross-chain).
   - Enter amount → see if quotes load from providers (including NEAR Intents if available for your pair).
   - If quotes appear → pick the best one, review fees/rates, confirm on your Ledger device.
3. **If no quotes or it fails**:
   - Try different providers if selectable (e.g., switch to NEAR Intents explicitly if shown).
   - Check for errors like "insufficient funds" (need extra NEAR for gas fees, ~0.01–0.1 NEAR), network issues, or VPN interference (disable VPN if using one).
   - Clear cache: Settings → Help → Clear Cache (often fixes sync/swap glitches).
   - If still no luck, the direct on-NEAR swap isn't routed well in Ledger Live.

### Best Workaround: Connect Ledger to a NEAR DEX (Recommended for On-Chain NEAR → USDC)
Since you have a Ledger, you can keep full security while using a proper NEAR DEX:

1. Go to **Ref Finance** (official: https://app.ref.finance) — the top DEX on NEAR with good NEAR/USDC liquidity.
2. Click **Connect Wallet** → choose **Ledger** (or "Hardware Wallet" option; it uses WalletConnect or direct integration via MyNearWallet).
3. Follow prompts to connect your Ledger (install/open the NEAR app on your device if not already).
4. Once connected:
   - Select NEAR → USDC (native USDC on NEAR should appear).
   - Enter amount, adjust slippage (try 1–3% if volatile).
   - Approve/sign transactions on your Ledger (you'll see details on-device for security).
5. Confirm → swap executes on-chain, USDC lands in your NEAR address (still secured by Ledger).

This is non-custodial, direct on NEAR, and usually works when Ledger Live's built-in swap doesn't.

Alternatives if Ref doesn't connect smoothly:
- **MyNearWallet** (app.mynearwallet.com) → Connect Ledger → access Ref Finance or built-in swap from there.
- **Sender Wallet** — another Ledger-compatible NEAR wallet with DEX integrations.

### After You Have USDC on NEAR
- To "cash out" to fiat: Bridge USDC to Ethereum/Base/etc. (low/no fees via native Circle tools if supported), or send to a CEX like Coinbase/Kraken (they support NEAR/USDC deposits → sell → bank withdraw).
- Or swap NEAR directly on a CEX if you prefer: Withdraw NEAR from Ledger to Kraken/Coinbase → trade to USDC/USDT → fiat.

If you share the **exact error message** in Ledger Live (or a screenshot description), which provider it's trying to use, or how much you're swapping, I can troubleshoot more precisely. Also confirm if your NEAR is in a Ledger-managed account or already connected elsewhere. Stay safe—always double-check URLs and never enter your seed phrase!

### HUMAN
I made the swap from zec to usdc on solana and it went through but its taking forever?

### ASSISTANT
Solana transactions, including swaps like ZEC → USDC (likely bridged or wrapped via a cross-chain service, then swapped on Solana DEX/Jupiter/etc.), are normally **very fast**—often confirming in **1-5 seconds**, with full finality around **12-15 seconds** under normal conditions. This is one of Solana's big selling points compared to slower chains.

If your swap "went through" (meaning the transaction was broadcast and accepted/submitted successfully) but is taking forever to show the USDC in your wallet or finalize, here are the most common reasons and what to do:

### 1. Network Congestion (Most Likely Right Now)
Solana has had periodic congestion issues in recent months/years, especially during high activity (memecoins, DeFi spikes, or stablecoin volume surges—USDC transfers on Solana have been massive lately). Even if the official status page shows "operational" with no major outages (which it does as of today—no incidents reported in February 2026), **subtle congestion** can still cause:
- Transactions to queue up.
- Slower confirmations (minutes to hours in bad cases).
- "Pending" or stuck status in wallets/explorers.
- Higher failure/drop rates if priority fees were low.

From recent reports, this happens even without full downtime—success rates dip, and swaps/DeFi actions lag. Your ZEC → USDC swap might have hit a busy period.

**What to check/do:**
- Paste your transaction signature (TX ID) into a Solana explorer like:
  - https://solscan.io/
  - https://solana.fm/
  - https://explorer.solana.com/
- Look at the status: "Processed/Confirmed"? "Finalized"? Or still "Pending/Signature"?
- If it's confirmed but balance not updated → wallet sync delay (refresh, restart app, or switch RPC in wallet settings—try a fast one like Helius or QuickNode if your wallet allows).
- If pending/stuck long-term (hours+): It might drop/expire eventually (Solana TXs expire after ~60-90 seconds if not landed, but some wallets retry). In rare cases, resubmit if your wallet supports it.

### 2. Wallet or DEX-Specific Delays
- If you used Jupiter Aggregator, Raydium, or another DEX for the USDC part: These can route through multiple steps (e.g., bridge + swap), adding time during congestion.
- Wallet refresh lag: Phantom, Backpack, Solflare, etc., sometimes don't update instantly—force refresh or check balance directly on explorer.
- Cross-chain aspect (ZEC is on its own chain): If this was via a bridge (e.g., Allbridge, Mayan, or Wormhole), the inbound to Solana can take extra time (minutes normally, longer if congested).

### 3. Priority Fees Too Low
Solana lets you add priority fees for faster inclusion. If you (or the swap tool) used minimal/default, it gets deprioritized in busy times.

**Fix for future swaps:** In Jupiter or your DEX/wallet, bump priority fee (e.g., set to "High" or add 0.001-0.01 SOL extra).

### Next Steps Right Now
- **Monitor the TX** on an explorer (share the TX ID here if you want me to help check specifics—don't share private info).
- Wait a bit more—many "forever" cases resolve in 5-60 minutes once load eases.
- If it's been hours and still pending: Contact your wallet's support (e.g., Phantom help) or the swap service (if via a specific app/bridge). Funds aren't lost if the TX was broadcast—worst case, it fails and reverts (ZEC side might need reclaim).
- Check real-time status: status.solana.com (currently good, but doesn't catch mild congestion) or https://solanabeach.io/ for more metrics.

Solana usually bounces back quick—it's resilient lately with upgrades. If it's still stuck after checking the explorer, drop more details (wallet used, approx time of swap, or TX hash description), and I'll guide further. Hang tight!

### HUMAN
It does say that the transaction isn’t confirmed but it def went through

### ASSISTANT
The screenshot shows a classic **pending/unconfirmed** outgoing transaction in your wallet (likely **Ledger Live** or a similar app integrated with Ledger for Zcash, based on prior context). It deducted **-0.321 ZEC** (~$72.70) from your balance, but the status is "**Not confirmed** (2)" with a clock icon, meaning the transaction was **broadcast** to the Zcash network (so it "went through" from your end—your wallet signed and sent it), but it hasn't been included in a block yet by miners.

This is normal for Zcash (similar to Bitcoin)—transactions aren't instant; they sit in the **mempool** (network queue) until confirmed (usually 1-10+ confirmations needed for safety, depending on the recipient/exchange). "Def went through" means it was submitted successfully, but confirmation is separate.

### Why It's Taking Forever (Common Reasons Right Now)
From recent reports (including Zcash forums, GitHub issues, and community threads up to early 2026):
- **Low transaction fee**: Zcash uses a fee market like Bitcoin. If the fee was minimal (auto-set or low during setup), miners prioritize higher-fee TXs first. During any network activity or miner competition (Zcash mining difficulty hit all-time highs in early Feb 2026), low-fee TXs can lag or stay stuck for hours/days.
- **Mempool congestion or propagation issues**: Zcash has had periodic mempool backups (old GitHub issues from 2017 still relevant; recent forum posts mention pending TXs in wallets like Zashi). No major outages reported as of late Feb 2026 (network looks stable, no widespread alerts), but subtle delays happen.
- **Wallet-specific quirks**: In Ledger Live or Ledger-integrated Zcash support, there are known issues with certain UTXOs (e.g., older pre-NU5 shielded/transparent funds), leading to broadcast failures or pending states. Recent threads note "pending" screens in apps like Zashi during sends/swaps.
- **Swap/bridge context**: Since this is part of your ZEC → USDC on Solana flow (likely via a cross-chain swap like Near Intents, Mayan, or a service in Zashi/Zcash wallet), the ZEC send might be to a bridge/deposit address. If the bridge side is waiting or delayed, it compounds the wait. Some swaps show "pending" until the inbound chain confirms.

Zcash blocks come ~every 75 seconds, so normal confirmations are quick (minutes), but stuck ones can take hours+ or eventually drop (expire from mempool, usually after days/weeks, returning funds to your wallet automatically—no action needed).

### What to Do Right Now
1. **Check the transaction status on a Zcash explorer** (this is key—don't just trust the wallet):
   - Go to https://blockchair.com/zcash or https://explorer.zcha.in/ (or https://zcashblockexplorer.com/).
   - Search by your **wallet address** (the sending transparent or shielded address) or—if your wallet shows a TX ID/hash—use that.
   - If it appears: Look at confirmations (0 = still pending/unconfirmed). Note the fee and size.
   - If not visible: It may not have propagated fully (rare, but retry broadcast via wallet if possible) or dropped already (funds should return soon).
   
   Share the TX hash/ID or your sending address (public only!) if you want me to help look it up specifically.

2. **Wait it out** — Many pending ZEC TXs resolve in 1-24 hours once a miner picks it up or congestion clears. Check back in a few hours.

3. **If stuck too long (e.g., 24+ hours)**:
   - In Ledger Live: Go to your Zcash account → transaction history → find this one → see if there's a "speed up" or "cancel" option (some wallets allow RBF—replace-by-fee—to rebroadcast with higher fee, but Zcash/Ledger support for this is spotty).
   - Restart/sync the wallet or Ledger app.
   - If using a third-party wallet (e.g., Zashi for swaps): Check their status or retry the swap step if it failed partially.
   - Worst case: Funds aren't lost. If it expires/drops from mempool (after ~2 weeks max in many cases), your ZEC returns to your wallet automatically (balance reappears). Then retry the swap with higher fee or smaller amount.

4. **Prevent for next time**:
   - Use higher/custom fees when sending (if the wallet allows).
   - For swaps to Solana USDC: Try smaller test amounts first, or use aggregators like ChangeNOW/Changelly (they handle bridging/swaps with retries).
   - Monitor network health via Zcash forums or explorer for real-time mempool size.

Your funds are safe as long as the TX isn't confirmed (no double-spend risk yet). If it's been stuck since around 8:33 (your screenshot time, likely AM EST today), give it more time—Zcash isn't as congested as Solana often is. Drop the TX details or how long it's been pending exactly, and I can narrow it down more! Hang in there.

### HUMAN
What about icp? It only lets me send and receive but I can’t swap?

### ASSISTANT
Yes, **ICP** (Internet Computer token) support in **Ledger Live** is limited compared to chains like Ethereum, Solana, or NEAR. Ledger added ICP accounts a while back (around 2022–2023, with updates into 2026), so you can securely **send** and **receive** ICP tokens directly in Ledger Live—your hardware wallet signs the transactions offline for max security. However, **swapping ICP** (e.g., ICP → USDC or other tokens) isn't available in the built-in Swap tab.

### Why Swap Isn't Supported for ICP in Ledger Live
From Ledger's own support docs and user reports (including Reddit threads and official announcements):
- ICP isn't integrated with Ledger's swap providers (like Changelly, 1inch, or others they use for most assets).
- It's explicitly noted that swap pairs involving ICP (buying or selling to/from it) often don't appear because providers don't support it yet.
- Staking ICP is also not built-in—you need the separate **Network Nervous System (NNS)** dApp for that, which can connect to your Ledger for secure neuron management.
- Ledger Live focuses on basic send/receive for ICP, with no on-chain DEX routing or direct swap functionality like it has for EVM chains.

This matches what you've seen: only send/receive works, swap is grayed out or missing for ICP.

### How to Swap Your ICP (e.g., to USDC) Securely
Since you're using Ledger, the best way is to **connect it to an ICP-compatible wallet/dApp** that supports swaps while keeping your keys on the hardware device. ICP has its own ecosystem (canisters, NNS), and native DEXes exist.

1. **Use the Official ICP DEX or Aggregators** (Recommended for On-Chain Swaps):
   - Go to **ICPSwap** (icpswap.com) or **Sonic DEX** / other ICP-native DEXes—these are the go-to for swapping ICP to ckUSDC (the wrapped/canister version of USDC on ICP) or bridged USDC.
   - Connect your Ledger: Many ICP wallets/dApps support Ledger integration via the NNS or Plug wallet style (install the ICP app on your Ledger device first via Ledger Live → Manager).
   - Steps:
     - Open the dApp in a browser (e.g., Chrome).
     - Choose "Connect Wallet" → select Ledger/hardware option.
     - Approve on your Ledger device (you'll see transaction details).
     - Select ICP → USDC (or ckUSDC), enter amount, set slippage if needed, and confirm.
   - Liquidity on ICP DEXes has improved a lot—check pool depth on the site before big swaps.

2. **Alternative: Non-Custodial or Easy Swaps (No Direct Ledger Connect Needed)**:
   - **Withdraw ICP from Ledger Live** to a temporary ICP wallet (e.g., Plug Wallet, Bitfinity, or even a CEX like Kraken/Coinbase that supports ICP deposits).
   - Then swap there:
     - On Kraken: Direct ICP/USDC or ICP/USDT pairs → swap → withdraw USDC to Solana/Ethereum if needed.
     - Instant swap services like **SimpleSwap**, **ChangeNOW**, or **Changelly**: Send ICP from your Ledger address → get USDC (on Ethereum, Solana, etc.) to your preferred chain. No KYC for small amounts, privacy-focused, and they handle the conversion.
   - This is often faster for cross-chain to USDC on Solana (tying back to your earlier swap).

3. **If You Want to Cash Out to Fiat**:
   - Send ICP to Kraken, Coinbase, or Binance (they list ICP) → sell to USDC/USDT → fiat withdraw to bank.
   - Or bridge ICP to another chain first if needed (ICP has cross-chain tools via ckBTC/ckETH, but for USDC it's usually via centralized or aggregator routes).

Double-check everything:
- Use official sites (ledger.com for app installs, internetcomputer.org for NNS/dApps).
- Start with a small test swap to confirm.
- Never share your seed phrase—Ledger signs everything on-device.

If the swap is for a specific amount or you're hitting an error when trying to connect Ledger to an ICP dApp, share more details (e.g., which dApp you tried or screenshot of the limitation), and I can refine the steps. This should get you swapping without much hassle!

### HUMAN
What is the path of least resistance? I just want to swap it for usdc on solana

### ASSISTANT
The **path of least resistance** for swapping your ICP (from your Ledger-secured account) directly to **USDC on Solana**—without dealing with complex bridges, ICP-native DEX connections, or extra steps—is to use a **non-custodial instant swap service**. These handle the cross-chain conversion automatically: you send ICP from your Ledger address, and they deliver USDC straight to your Solana wallet address.

This avoids:
- Connecting Ledger to ICP dApps (which can be finicky).
- Manual bridging (no direct simple ICP → Solana bridge exists widely).
- CEX deposits/withdrawals (which require accounts, potential KYC for larger amounts, and extra transfers).

### Easiest Options (Ranked by Simplicity & Reliability)
1. **SimpleSwap (simpleswap.io)** — Top pick for least hassle right now.
   - No registration or KYC required (for most swaps; they may flag very large/risky ones rarely).
   - Supports **ICP → USDC** directly (they route to the chain you specify—select USDC on Solana if available in the dropdown; if not explicit, it often defaults or lets you paste a Solana address).
   - Steps:
     1. Go to simpleswap.io.
     2. Select "You send": ICP (Internet Computer).
     3. Select "You get": USDC (specify Solana network if prompted; or just paste your Solana USDC address below).
     4. Enter the amount of ICP → see the quote (includes fees, estimated USDC received).
     5. Provide your Solana wallet address (e.g., from Phantom, Backpack, or Ledger-connected Solana account).
     6. Copy the generated ICP deposit address → send your ICP from Ledger Live (use the Send tab for your ICP account; confirm on-device).
     7. Wait 5–30 minutes (usually fast; track on their site).
   - Pros: Super simple UI, no account needed, privacy-focused.
   - Cons: Fees ~0.5–1% + network costs; rates are market-based.

2. **ChangeNOW (changenow.io)** — Very close second, often slightly better rates or more options.
   - Also no mandatory KYC/registration for standard swaps.
   - Explicitly supports ICP swaps (including to Solana assets via their multichain bridge).
   - Steps are almost identical: Pick ICP → USDC (select Solana USDC if shown), enter amount, paste Solana address, send ICP to their temp address.
   - They handle the routing (ICP → intermediate → Solana USDC).
   - Good for larger amounts if SimpleSwap limits kick in.

Both are reliable in 2026 for this pair—no major complaints in recent checks, and they process cross-chain like this routinely.

### Quick Tips for Your Setup
- **From Ledger Live**: In your ICP account, hit Send → paste the deposit address from the swap site → set a reasonable fee (ICP fees are low anyway) → confirm on your Ledger device.
- **Solana Wallet**: Use Phantom or Solflare (easy to set up if you don't have one). Make sure it's a fresh address or one you control for receiving USDC.
- **Test First**: Swap a tiny amount (e.g., 1–5 ICP) to confirm it lands as USDC on Solana before doing the full amount.
- **Fees & Time**: Expect 0.5–2% total cost (swap fee + networks), 10–60 min processing. Solana side is instant once received.
- **If You Prefer a CEX Route** (slightly more steps but potentially cheaper/better rates):
  - Send ICP from Ledger to Kraken (supports ICP deposits, has ICP/USDC pair) → swap to USDC → withdraw USDC to Solana (Kraken supports Solana withdrawals for USDC). This adds KYC if not already verified, but it's straightforward.

This method keeps things minimal—no extra wallets to connect, no on-chain DEX fiddling on ICP. If you run into an issue (e.g., USDC network not listed), just paste your Solana address anyway—most services detect it and route correctly. Let me know how much you're swapping or if you hit a snag, and I can tweak! Stay safe—double-check addresses and use official sites.
