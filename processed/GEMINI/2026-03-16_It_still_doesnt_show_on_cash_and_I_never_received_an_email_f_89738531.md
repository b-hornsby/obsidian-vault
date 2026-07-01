---
category: crypto-web3
date: 2026-03-16
id: 455801
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting an issue with a USDC transfer from Coinbase to Apple Pay,
  where the transaction isn't showing up and he hasn't received a confirmation email.
tags:
- coinbase
- apple-pay
- usdc-transfer
- transaction-issue
---
# It still doesn’t show on cash and I never received an email from Coinbase saying hey you got sent something from Apple Pay

### USER
It still doesn’t show on cash and I never received an email from Coinbase saying hey you got sent something from Apple Pay

### GEMINI
Look, the fact that you haven't received an email from Coinbase yet confirms one thing: The money hasn't officially cleared their ledger. When you do an "Instant Transfer" to a debit card, it isn't like sending a text; it’s a request sent through the Visa/Mastercard network. Since it is currently 8:09 AM and your transfer was at 7:59 AM, you are only 10 minutes into the wait. Here is the "brutally honest" reality of why it’s not showing: 1. The 30-Minute Rule Even though Apple says "Cleared," Coinbase uses a third-party processor (usually Green Dot Bank or Marqeta) to handle card deposits. They almost always have a 30-minute delay for security scrubbing before they notify the main Coinbase app to update your balance. If it’s not there by 8:30 AM, then you can start getting annoyed. 2. The Email Sync Coinbase only triggers that "Hey, you got money" email after the funds are fully settled in your account. If the money is still in the "Authorized" state (the banking void), Coinbase doesn't technically "see" it yet, so no email will be sent. 3. Verification & Safety Holds If you haven't done this specific "loop" (Coinbase -> Apple Pay -> Coinbase) before, or if you don't do it often, their system might have flagged the "round-trip" as suspicious activity. The Opportunity Cost: By moving the money back and forth, you’ve basically triggered a fraud alert. Coinbase might hold this for 24 hours just to make sure the Apple Pay side doesn't try to "claw back" the funds. The "No-BS" Action Plan: Step 1: The App Refresh. Don't just look at the home screen. Go to Assets -> US Dollar (Not USDC). Tap the "History" or "Transactions" section inside the US Dollar asset. Often, the transaction will show up as "Pending" in that specific list before it ever shows in your total balance. Step 2: Check the "Add Cash" Screen. Go like you are going to buy more USDC. When it asks for a payment method, look at your USD Balance. Does it show the $88.47 there? Sometimes the buying interface updates faster than the portfolio UI. Step 3: The 2-Hour Limit. If the money isn't in your USD balance by 10:00 AM, it means one of two things: Rejection: The deposit was rejected by the card issuer, and the money is being sent back to Apple Cash (this can take 1–3 days). Shadow Hold: Coinbase has it, but they are keeping it "invisible" until they verify the source. Stop checking it every 60 seconds. If you don't see it in your "US Dollar" history by 8:30 AM, it's a settlement delay. Do you want me to give you the direct link to the Coinbase "Live Chat" so you can have it ready if it hasn't landed by 10 AM?
