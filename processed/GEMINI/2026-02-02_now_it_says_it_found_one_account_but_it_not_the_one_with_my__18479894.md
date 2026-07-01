---
category: crypto-web3
date: 2026-02-02
id: 997458
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was trying to recover a crypto wallet account but the tool found a
  different account than the one containing his funds.
tags:
- crypto-wallet
- account-recovery
- funds-access
---
# now it says it found one account but it not the one with my funds?

### USER
now it says it found one account but it not the one with my funds?

### GEMINI
Finding "one account" that is empty means you have the right words, but you're looking at the wrong branch of the tree. A single recovery phrase can generate thousands of different addresses (accounts). If the one you see isn't yours, it’s because Phantom is defaulting to the first address it finds, whereas your funds are likely on a secondary account or a different "derivation path." 1. The "Add Account" Loop (Most Likely) Phantom only automatically displays accounts that have a transaction history. If it missed yours for some reason, you have to manually "force" it to find the others. The Fix: Click your Account Name/Avatar at the top left → Add/Connect Wallet → Create New Account. The Logic: Even though it says "Create," it actually just looks for the next address associated with your phrase. If you had three accounts before, you might need to do this 2 or 3 times until your funded address pops up. 2. The Derivation Path Conflict If you originally created this wallet in a different app (like Trust Wallet, Exodus, or Solflare) and then moved to Phantom, they might be using a different mathematical "map" to find your address. The Fix: When you are at the "Select Accounts" screen during import, look for a small "Advanced" or "Derivation Path" dropdown. The Options: Try switching between: m/44'/501'/0'/0' (Phantom Default) m/44'/501'/0' (Solflare/Legacy) m/501'/0'/0/0 (Other/Older wallets) The Blind Spot: If you use the wrong path, you will get a valid, empty wallet every single time. You must match the path used by the original app where you made the wallet. 3. The "Wrong Phrase" Hard Truth If you have cycled through 10 "New Accounts" and tried every derivation path, and they are all empty, you are likely using a recovery phrase for a different wallet you made a long time ago. Objective Check: Do you have more than one 12-word list written down? Action: If you still have the old device or app where the funds are visible, go into those settings and "View Private Key" for that specific address. Importing a Private Key is surgical—it bypasses the "path" issue entirely and takes you directly to the money. Step-by-step for right now: Go to Add Account > Create New Account and do it five times in a row. Does the balance change or do any of the addresses look familiar?
