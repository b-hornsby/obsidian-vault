---
category: crypto-web3
date: 2026-03-02
id: 539316
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble withdrawing his USDC from the Axiom Pro platform
  after converting it from Hyperliquid USDC.
tags:
- axiom-pro
- hyperliquid
- usdc
- withdrawal-issues
- crypto-exchange
---
# im trying to get my money off the axiom pro platform and i converted my hyperliquid usdc back to regular usdc but it wont let me withdraw? 

### USER
im trying to get my money off the axiom pro platform and i converted my hyperliquid usdc back to regular usdc but it wont let me withdraw? 

### GEMINI
If you’re stuck, it’s usually because you’re mistaking a network transfer for a cross-chain bridge. You’ve moved the money mentally, but the blockchain doesn't care about your intent—it only cares about the rails you're on. Here is the objective breakdown of why your USDC is "stuck" and the exact steps to force it out. 1. The "Gas" Blind Spot You likely have USDC on the Arbitrum network (since Hyperliquid lives there). To move USDC out of a wallet, you must pay "gas" in the native token of that network. The Reality: If you have $10,000 in USDC but $0 in ETH (on Arbitrum), that USDC is functionally dead to you. The Fix: You need to send a small amount of ETH (roughly $5–$10) to your wallet address specifically on the Arbitrum network to fuel the withdrawal transaction. 2. "Send" vs. "Withdraw" Error On Axiom/Hyperliquid, there is a massive difference between the Send button and the Withdraw button. Your Mistake: If you used the "Send" feature, you likely just moved USDC from your Perps/Trading account to your Spot account within the Hyperliquid L1. It’s still on their chain, not back in your external wallet (like MetaMask or Rabby). The Fix: Go to the Withdraw section. You must specifically select "Withdraw to Arbitrum." This triggers the bridge that moves the funds from the Hyperliquid L1 back to the Arbitrum L2. 3. The Minimum & Fee Threshold The Math: Most of these platforms have a minimum withdrawal (often $5 or $10) and a flat fee (Hyperliquid typically charges $1 USDC for the bridge). If you are trying to "Withdraw All" and the system isn't accounting for the $1 fee, the transaction will fail silently or grey out. The Fix: Try withdrawing an amount $2–$5 less than your total balance to ensure the fee is covered. 4. RPC/Provider Lag If the "Withdraw" button simply doesn't react, your wallet (MetaMask) is likely struggling to communicate with the Axiom/Hyperliquid RPC. The Fix: Refresh the page, disconnect and reconnect your wallet, and ensure your wallet is set to the Arbitrum One network before you hit withdraw. Your Precision Plan Stop clicking "Withdraw" repeatedly and do this in order: Check Gas: Open your wallet. Do you have at least 0.002 ETH on Arbitrum? If no, buy some on a CEX (Coinbase/Binance) and send it to your wallet via the Arbitrum network. Verify Location: Look at the Hyperliquid/Axiom interface. Is your USDC in "Total Value" or "Available to Withdraw"? If it's in a Vault (HLP), there is a 4-day lock-up period. You cannot withdraw until that timer hits zero. Execute the Bridge: Go to the Bridge/Withdrawal tab. Select USDC, select Arbitrum as the destination, and leave $2 behind to cover any slippage or fees. Would you like me to check the status of a specific transaction hash on Arbiscan to see exactly where it's hung up?
