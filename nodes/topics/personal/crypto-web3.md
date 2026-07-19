---
type: topic
tags: [topic, moc, q2-2026]
aliases: [crypto, web3, defi, trading]
---

# Crypto/Web3

*194 conversations about leverage, liquidation, wallet management, and the slow process of learning how DeFi actually works by building something real.*

---

## The honest truth

I understand the mechanics — leverage, perps, stop-losses, DEX aggregators, wallet management. I can explain these concepts to others. But the gap is in consistent strategy execution. I know the vocabulary but not the language.

I'm not a trader. I'm a builder who's learning about finance by building a trading bot on Solana.

---

## The journey

### Getting started
I asked the basics: *"Do either have the ability to hold ondo? And how do I buy ondo?"* I was figuring out which wallets support which tokens, how to move funds, and what the actual mechanics of buying crypto were.

I've asked about moving USDC to a Coinbase card: *"I don't want to keep it on the exchange I want it directly on the card."* I've helped my aunt buy crypto through Coinbase and send it to Phantom.

### The trading bot
I'm building a Solana trading bot. I've tested the quoting stage, set up Phantom wallets, and worked through Jupiter Perps integrations. I've asked: *"so now that this is in my plan.md what do i tell claude to get this started?"*

I created a new Phantom wallet using email signup and had to figure out: *"how do i see what email is attached to my current wallet?"*

### Leverage and liquidation
I've asked about liquidation more than once: *"If my trade for troll doesn't show up anymore does that mean I got liquidated?"* I've tried to understand why adding collateral reduced my leverage: *"Why did my leverage go down when I added more collateral on Jupiter perps? I had $10 in at 10x and I added $10 more and now it's 4.97x?"*

This is the kind of thing you only learn by doing — and by losing money.

### The AI agent strategy
I've received detailed reviews of my AI agent strategy covering success metrics, funding models, and the relationship between DeFi yield and API costs. This is the Operation Immortal Agent concept — an agent that earns enough from DeFi to pay for its own API costs.

---

## What I've learned

**Leverage is counterintuitive.** Adding collateral doesn't always increase leverage. The math is more complex than it seems, and you have to understand how the platform calculates position size vs collateral.

**Wallet management matters.** I've set up multiple wallets, moved funds between exchanges and wallets, and learned that you should never have wallet addresses in GitHub repos (even private ones).

**Security is paramount.** Moving wallet addresses and keys out of GitHub and into Docker environment variables. Using .env files. Not trusting exchanges with large amounts.

**The funding problem is real.** Generating enough yield to sustain an AI agent is harder than it looks. The math is optimistic, and the risks are real.

---

## Current knowledge

- **Solana ecosystem** — Jupiter, Meteora DLMM, Kamino staking
- **Wallet management** — Phantom, Coinbase, wallet security
- **DeFi mechanics** — leverage, perps, liquidation, collateral, yield
- **Trading bot development** — quoting, transaction building, signing
- **Security practices** — .env files, Docker environment variables, GitHub hygiene

---

## What I'm working on

- **Solana trading bot** — testing quoting stages, integrating with Jupiter Perps
- **Phantom wallet management** — understanding email-based wallet recovery
- **Leverage optimization** — understanding how to maintain desired leverage levels
- **Operation Immortal Agent** — the long-term vision of a self-sustaining AI agent

---

## Key Conversations

- [[processed/GPT/2025-09-19_Liquidation_confirmation_steps_27490454.md|Liquidation check]] — "If my trade for troll doesn't show up anymore does that mean I got liquidated?"
- [[processed/GROK/2026-03-11_Jupiter_Perps_Adding_Collateral_Reduces_Leverage_36073302.md|Leverage confusion]] — "Why did my leverage go down when I added more collateral?"
- [[processed/GEMINI/2025-04-08_Do_either_have_the_ability_to_hold_ondo_And_how_do_I_buy_ond_55160168.md|Wallet basics]] — "Do either have the ability to hold ondo?"
- [[processed/GEMINI/2026-02-26_how_do_i_see_what_email_is_attached_to_my_current_wallet_55408844.md|Wallet recovery]] — "how do i see what email is attached to my current wallet?"

---

## Related

- [[nodes/people/bryan.md|Bryan]] — the person learning DeFi
- [[nodes/projects/operation-immortal-agent.md|Operation Immortal Agent]] — the self-sustaining agent concept
- [[nodes/topics/tech/ai-tools.md|AI Tools]] — the tools the agent would use
- [[nodes/topics/tech/homelab.md|Homelab]] — the infrastructure it would run on
- [[nodes/topics/career.md|Career]] — the financial pressure that makes this appealing
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — why the funding problem is hard
