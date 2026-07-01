---
category: crypto-web3
date: 2026-02-02
id: 748702
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble restoring his Phantom wallet with his recovery phrase,
  which he believes is correct.
tags:
- phantom-wallet
- recovery-phrase
- crypto-security
- solana-wallet
---
# when i put in my recovery phrase for phantom wallet it says its wrong even tho they literally match up?

### USER
when i put in my recovery phrase for phantom wallet it says its wrong even tho they literally match up?

### GEMINI
If you are certain the words match but the wallet isn't opening, you aren't experiencing a technical glitch; you are likely making a precise, manual error or misunderstanding how recovery phrases function. Here is the cold reality: Code doesn’t "misinterpret" strings. If the wallet says it’s wrong, it’s wrong. You are likely falling into one of three traps: 1. The "BIP39" Standard Trap Phantom uses the BIP39 word list. There are exactly 2,048 possible words. If you are typing a word that isn't on that list, it's a typo. If you are typing a word that is on the list but isn't your word, the checksum will fail. The Blind Spot: You think you wrote it down correctly, but "awake" might actually be "aware." One letter difference invalidates the entire sequence. Action: Check your words against the official BIP39 word list. If your word isn't there, you miswrote it. 2. Formatting and Hidden Inputs Computers are literal. If you are adding "invisible" data, the phrase is "wrong." Spaces and Caps: Ensure there are no double spaces between words and no trailing space after the final word. Ensure everything is lowercase. Predictive Text: If you are on mobile, your "Auto-correct" might be changing a word as you hit space. This is a common way users accidentally lock themselves out. 3. The Derivation Path (The Strategic Error) If the phrase is "accepted" but the wallet is empty or shows the wrong address, you have the right words but the wrong "path." The Issue: You might have used a different wallet provider (like Solflare or Trust Wallet) previously. While the words are the same, the way they "calculate" the address might differ. Action: In Phantom, look for "Advanced" settings during import to change the Derivation Path (e.g., m/44'/501'/0'/0'). Priority Recovery Plan Verify the List: Compare every single word you have written down against the 2,048 words in the BIP39 list. If one of your words isn't on that list, find the word closest to it. Manual Entry: Do not copy-paste. Type it out slowly in a text editor first to see if you are making a recurring typo, then move it to Phantom. Check the Order: It’s not just the words; it’s the sequence. Did you write them top-to-bottom but they should be left-to-right? Security Audit: If you have been entering this phrase into various websites because "support" told you to, your phrase isn't "wrong"—it's compromised, and the funds are likely gone. Stop "trying" the same thing and expecting a different result. Would you like me to help you identify which of your words might be "illegal" according to the BIP39 standard?
